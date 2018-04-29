from db import db

class SousOrdreModel(db.Model):

    __tablename__ = 'sous_ordre'

    # Basic attributes
    id = db.Column(db.Integer, primary_key=True)
    nom_commun = db.Column(db.String(128))
    nom_latin = db.Column(db.String(128))
    nom_commun_en = db.Column(db.String(128))
    descript = db.Column(db.String(256))

    # Relations
    ordre_id = db.Column(db.Integer, db.ForeignKey('ordre.id'))

    sous_ordre = db.relationship('FamilleModel', backref='sous_ordre')

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()