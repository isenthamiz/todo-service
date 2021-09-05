from flask import current_app
from flask_restful import abort
from functools import wraps
from schema.request_schema import session_header_request
import jwt
from models.user import User


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        args = session_header_request.parse_args()
        bearer_token = args['Authorization']
        if not bearer_token:
            abort(403, message="Token Missing")
        token = bearer_token.split(' ')[1]
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            user = User.query.filter_by(id=data['id']).first()
        except:
            abort(403, message="Invalid Token")
        return f(user, *args, **kwargs)
    return decorated