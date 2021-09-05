from flask_restful import fields


todo_response_schema = {
    'id': fields.String,
    'title': fields.String,
    'description': fields.String,
    'date': fields.String,
    'active': fields.Boolean
}

user_response_schema = {
    'id': fields.String,
    'username': fields.String,
    'password': fields.String
}