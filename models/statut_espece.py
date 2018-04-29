from db import db

class StatutEspeceModel(db.Model):

    __tablename__ = 'statut_espece'

    # Basic attributes
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    # Relations
    statut_espece = db.relationship('SousEspeceModel', backref='statut_espece')