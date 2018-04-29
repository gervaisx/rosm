from db import db

class StatutObservationModel(db.Model):

    __tablename__ = 'statut_observation'

    # Basic attributes
    id = db.Column(db.Integer, primary_key=True)
    statut_observation = db.Column(db.String(128))

    # Relations
    statut_observation = db.relationship('ObservationModel', backref='statut_observation')