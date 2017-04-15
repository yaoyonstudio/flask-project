from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250),  unique=True, nullable=False)
    username = db.Column(db.String(250),  unique=True, nullable=False)
    password = db.Column(db.String(250))
    login_time = db.Column(db.Integer)

    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def __str__(self):
        return "Users(id='%s')" % self.id

    def getAll(self):
        return self.query.all()

    def get(self, id):
        return self.query.filter_by(id=id).first()

    def add(self, user):
        db.session.add(user)
        return session_commit()

    def update(self):
        return session_commit()

    def delete(self, id):
        self.query.filter_by(id=id).delete()
        return session_commit()


def session_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        reason = str(e)
        return reason
