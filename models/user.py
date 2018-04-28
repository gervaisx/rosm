from db import db

class UserModel(db.Model):

    __tablename__ = 'user'

    # Basic attributes
    id = db.Column(db.Integer, primary_key=True)
    courriel = db.Column(db.String(128), unique=True, nullable=False)
    pw = db.Column(db.String(32), nullable=False)

    # Relations


    def __init__(self, username, password):
        self.courriel = username
        self.pw = password

    def save_to_db(self):

        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):

        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_username(cls, username):

        return cls.query.filter_by(courriel=username).first()