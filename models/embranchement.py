from db import db

class EmbranchementModel(db.Model):

    __tablename__ = 'embranchement'

    # Basic attributes
    id = db.Column(db.Integer, primary_key=True)
    nom_commun = db.Column(db.String(128))
    nom_latin = db.Column(db.String(128))
    nom_commun_en = db.Column(db.String(128))
    descript = db.Column(db.String(256))

    # Relations
    regne_id = db.Column(db.Integer, db.ForeignKey('regne.id'))

    embranchement = db.relationship('ClasseModel', backref='embranchement')

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()