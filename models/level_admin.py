from db import db

class LevelAdminModel(db.Model):

    __tablename__ = 'level_admin'

    # Basic attributes
    id = db.Column(db.Integer, primary_key=True)
    level_admin = db.Column(db.String(128))

    # Relations
    admin = db.relationship('UserModel', backref='admin')