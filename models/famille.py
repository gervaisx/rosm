from db import db

class FamilleModel(db.Model):

    __tablename__ = 'famille'

    # Basic attributes
    id = db.Column(db.Integer, primary_key=True)
    nom_commun = db.Column(db.String(128))
    nom_latin = db.Column(db.String(128))
    nom_commun_en = db.Column(db.String(128))
    descript = db.Column(db.String(256))

    # Relations
    sous_ordre_id = db.Column(db.Integer, db.ForeignKey('sous_ordre.id'))

    famille = db.relationship('SousOrdreModel', backref='famille')