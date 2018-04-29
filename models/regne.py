from db import db

class RegneModel(db.Model):

    __tablename__ = 'regne'

    # Basic attributes
    id = db.Column(db.Integer, primary_key=True)
    nom_commun = db.Column(db.String(128))
    nom_latin = db.Column(db.String(128))
    nom_commun_en = db.Column(db.String(128))
    descript = db.Column(db.String(256))

    # Relations
    regne = db.relationship('EmbranchementModel', backref='regne')