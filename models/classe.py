from db import db

class ClasseModel(db.Model):

    __tablename__ = 'classe'

    # Basic attributes
    id = db.Column(db.Integer, primary_key=True)
    nom_commun = db.Column(db.String(128))
    nom_latin = db.Column(db.String(128))
    nom_commun_en = db.Column(db.String(128))
    descript = db.Column(db.String(256))

    # Relations
    embranchement_id = db.Column(db.Integer, db.ForeignKey('embranchement.id'))

    classe = db.relationship('SousClasseModel', backref='classe')

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()