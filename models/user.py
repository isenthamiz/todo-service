from database import db


class User(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __repr__(self):
        return self.public_id