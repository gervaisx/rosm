from db import db

class SousClasseModel(db.Model):

    __tablename__ = 'sous_classe'

    # Basic attributes
    id = db.Column(db.Integer, primary_key=True)
    nom_commun = db.Column(db.String(128))
    nom_latin = db.Column(db.String(128))
    nom_commun_en = db.Column(db.String(128))
    descript = db.Column(db.String(256))

    # Relations
    classe_id = db.Column(db.Integer, db.ForeignKey('classe.id'))

    sous_classe = db.relationship('ClasseModel', backref='sous_classe')