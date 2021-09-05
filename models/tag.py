from database import db


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.String(40), primary_key=True)
    name = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return self.name
