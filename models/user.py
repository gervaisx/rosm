from db import db

class UserModel(db.Model):

    __tablename__ = 'user'

    # Basic attributes
    id = db.Column(db.Integer, primary_key=True)
    insert_at = db.Column(db.String(128))
    update_at = db.Column(db.String(128))
    prenom = db.Column(db.String(128))
    nom = db.Column(db.String(128))
    username = db.Column(db.String(128))
    password = db.Column(db.String(32))
    pseudo = db.Column(db.String(128))
    telephone = db.Column(db.String(128))
    active = db.Column(db.Integer)

    # Relations
    level_admin_id = db.Column(db.Integer, db.ForeignKey('level_admin.id'))

    user_picture = db.relationship('ProfilePictureModel', backref='user_picture')

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
