from marshmallow import Schema, fields


class TodoResponseSchema(Schema):
    id = fields.String()
    title = fields.String()
    description = fields.String()
    user_id = fields.String()
    date = fields.String()
    active = fields.Boolean


class UserResponseSchema(Schema):
    id = fields.String()
    username = fields.String()
    password = fields.String()