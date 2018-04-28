from db import db

class ProfilePictureModel(db.Model):

    __tablename__ = 'profile_picture'

    # Basic attributes
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(128))
    insert_at = db.Column(db.String(45))
    update_at = db.Column(db.String(45))

    # Relations
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))