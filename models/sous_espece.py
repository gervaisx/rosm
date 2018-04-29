from db import db

class SousEspeceModel(db.Model):

    __tablename__ = 'sous_espece'

    # Basic attributes
    id = db.Column(db.Integer, primary_key=True)
    nom_commun = db.Column(db.String(128))
    nom_latin = db.Column(db.String(128))
    nom_commun_en = db.Column(db.String(128))
    descript = db.Column(db.String(256))

    # Relations
    statut_espece_id = db.Column(db.Integer, db.ForeignKey('statut_espece.id'))
    espece_id = db.Column(db.Integer, db.ForeignKey('espece.id'))

    sous_espece = db.relationship('EspeceModel', backref='sous_espece')
    photo_sous_espece = db.relationship('PhotoSousEspeceModel', backref='photo_sous_espece')