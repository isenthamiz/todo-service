from flask import Flask
from flask_restful import Api
from database import db
from resources.todo import TodoOperations, TodoOperationsWithId
from resources.tag import TagOperations

app = Flask(__name__)
app.config['BUNDLE_ERRORS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5434/postgres'

api = Api(app, prefix='/api/todo-service')

api.add_resource(TodoOperations, '/todo')
api.add_resource(TodoOperationsWithId, '/todo/<string:id>')
api.add_resource(TagOperations, '/tag')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)