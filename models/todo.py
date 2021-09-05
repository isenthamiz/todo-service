from database import db


class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.String(40), primary_key=True)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    user_id = db.Column(db.String(50))
    date = db.Column(db.String(50), nullable=False)
    active = db.Column(db.Boolean, nullable=False)

    def __str__(self):
        return self.title
