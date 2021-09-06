from flask_restful import Resource, abort
from flask_apispec import marshal_with
from database import db
from datetime import datetime
from schema.response_schema import TodoResponseSchema
from schema.request_schema import todo_query_param, todo_request_schema, todo_update_request_schema
from models.todo import Todo
import uuid


def todo_update_helper(todo, payload):
    if payload['title']:
        todo.title = payload['title']
    if payload['description']:
        todo.description = payload['description']
    if payload['date']:
        todo.date = payload['date']
    if not payload['active'] == None:
        print(payload['active'])
        todo.active = payload['active']
    return todo


def get_active_or_inactive_todos(is_active):
    if not is_active in ['true', 'false']:
        abort(400, message="Invalid Parameter Value")
    if is_active == 'true':
        return Todo.query.filter_by(active=True).all()
    else:
        return Todo.query.filter_by(active=False).all()


class TodoOperationsWithId(Resource):
    @marshal_with(TodoResponseSchema)
    def get(self, id):
        response = Todo.query.filter_by(id = id).first()
        if not response:
            abort(404, message="Todo Not Found")
        return response

    @marshal_with(TodoResponseSchema)
    def put(self, id):
        try:
            response = Todo.query.filter_by(id=id).first()
            if not response:
                abort(404, message="Todo Not Found")
            args = todo_update_request_schema.parse_args()
            response = todo_update_helper(response, args)
            db.session.commit()
            return response, 202
        except:
            abort(500, message="Error While Updating Data")


class TodoOperations(Resource):
    @marshal_with(TodoResponseSchema)
    def get(self):
        args = todo_query_param.parse_args()
        active = args['active']
        if not active is None:
            return get_active_or_inactive_todos(active)
        else:
            return Todo.query.all()

    def post(self):
        args = todo_request_schema.parse_args()
        id = str(uuid.uuid4())
        args['date'] = str(datetime.now())
        args['active'] = True
        todo = Todo(id = id, title=args['title'], description=args['description'], date=args['date'], active=args['active'])
        db.session.add(todo)
        db.session.commit()
        return {"id": id}, 201