from db import db

class PhotoSousEspeceModel(db.Model):

    __tablename__ = 'photo_sous_espece'

    # Basic attributes
    id = db.Column(db.Integer, primary_key=True)
    url_photo = db.Column(db.String(128))

    # Relations
    sous_espece_id = db.Column(db.Integer, db.ForeignKey('sous_espece.id'))