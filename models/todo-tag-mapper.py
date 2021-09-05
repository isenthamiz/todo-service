from database import db


todo_tag_mapper = db.Table(
    'todotagmapper',
    db.Model.metadata,
    db.Column('tag_id', db.ForeignKey('tag.id'), primary_key=True),
    db.Column('todo_id', db.ForeignKey('todo.id'), primary_key=True)
)