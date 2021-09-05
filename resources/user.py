from flask import request, current_app
from flask_restful import Resource, marshal_with,abort
from werkzeug.security import generate_password_hash, check_password_hash
from database import db
from schema.request_schema import user_create_request_schema, session_header_request
from schema.response_schema import user_response_schema
from models.user import User
from middleware import token_required
import uuid
import jwt
import datetime


class UserOperations(Resource):
    @marshal_with(user_response_schema)
    @token_required
    def get(self, current_user):
        users = User.query.all()
        return users

    @token_required
    def post(self, current_user):
        id = str(uuid.uuid4())
        args = user_create_request_schema.parse_args()
        password = generate_password_hash(args['password'], method='sha256')
        user = User(id = id, username= args['username'], password= password)
        db.session.add(user)
        db.session.commit()
        return {"id": id}, 201

class UserById(Resource):
    @marshal_with(user_response_schema)
    @token_required
    def get(self, current_user, id):
        user = User.query.filter_by(id = id).first()
        return user, 200

    @token_required
    def delete(self, current_user, id):
        user = User.query.filter_by(id = id).first()
        db.session.delete(user)
        db.session.commit()
        return {}, 200


class GenerateJWTToken(Resource):
        def get(self):
            auth = request.authorization
            if not auth or not auth.username or not auth.password:
                abort(403, message='Request Unauthorized')
            user = User.query.filter_by(username = auth.username).first()
            if not user:
                abort(403, message='Invalid User')
            if check_password_hash(user.password, auth.password):
                print(current_app.config['SECRET_KEY'])
                token = jwt.encode({'id': user.id, 'username': user.username, 'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=30)}, current_app.config['SECRET_KEY'], algorithm="HS256")
                return {"token": token}, 201
            abort(403, message='Username or Password is Wrong')