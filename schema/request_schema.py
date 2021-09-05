from flask_restful import reqparse
from datetime import datetime

todo_query_param = reqparse.RequestParser()
todo_query_param.add_argument('active', type=str, help='Bad Choice: It should be True or False')

todo_request_schema = reqparse.RequestParser()
todo_request_schema.add_argument('title', type=str, help='Title of todo item', required=True)
todo_request_schema.add_argument('description', type=str, help='Description of todo item')
todo_request_schema.add_argument('date', type=str, help='Date of todo item', nullable=False)
todo_request_schema.add_argument('tags', type=list, help='tag list for todo item')
todo_request_schema.add_argument('active', type=bool, help='Bad Choice: It should be True or False', nullable=False)


todo_update_request_schema = reqparse.RequestParser()
todo_update_request_schema.add_argument('title', type=str, help='Title of todo item')
todo_update_request_schema.add_argument('description', type=str, help='Description of todo item')
todo_update_request_schema.add_argument('date', type=str, help='Date of todo item')
todo_update_request_schema.add_argument('tags', type=list, help='tag list for todo item')
todo_update_request_schema.add_argument('active', type=bool, help='Bad Choice: It should be True or False')