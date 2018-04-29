from db import db

class OrdreModel(db.Model):

    __tablename__ = 'ordre'

    # Basic attributes
    id = db.Column(db.Integer, primary_key=True)
    nom_commun = db.Column(db.String(128))
    nom_latin = db.Column(db.String(128))
    nom_commun_en = db.Column(db.String(128))
    descript = db.Column(db.String(256))

    # Relations
    sous_classe_id = db.Column(db.Integer, db.ForeignKey('sous_classe.id'))

    ordre = db.relationship('SousOrdreModel', backref='ordre')

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()