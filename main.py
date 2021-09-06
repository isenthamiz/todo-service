from flask import Flask
from flask_restful import Api, abort
from database import db
from resources.todo import TodoOperations, TodoOperationsWithId
from resources.tag import TagOperations
from resources.user import UserOperations, UserById, GenerateJWTToken
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec


app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecret'
app.config['BUNDLE_ERRORS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5434/postgres'
app.config.update({
    'APISPEC_SPEC': APISpec('Todo Service', version='v1', openapi_version='2.0.0', plugins=[MarshmallowPlugin()]),
    'APISPEC_SWAGGER_URL': '/swagger/',
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'
})

api = Api(app, prefix='/api/todo-service')

api.add_resource(TodoOperations, '/todo')
api.add_resource(TodoOperationsWithId, '/todo/<string:id>')
api.add_resource(TagOperations, '/tag')
api.add_resource(UserOperations, '/user')
api.add_resource(UserById, '/user/<string:id>')
api.add_resource(GenerateJWTToken, '/authorize')

docs = FlaskApiSpec(app)
docs.register(GenerateJWTToken)
docs.register(UserOperations)
docs.register(UserById)

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)