from db import db

class ObservationModel(db.Model):

    __tablename__ = 'observation'

    # Basic attributes
    id = db.Column(db.Integer, primary_key=True)
    cofidential = db.Column(db.Integer)
    active = db.Column(db.Integer)

    # Relations
    point_observation_id = db.Column(db.Integer, db.ForeignKey('point_observation.id'))
    espece_id = db.Column(db.Integer, db.ForeignKey('espece.id'))
    statut_observation_id = db.Column(db.Integer, db.ForeignKey('statut_observation.id'))
    sous_espece_id = db.Column(db.Integer, db.ForeignKey('sous_espece.id'))

    photo_observation = db.relationship('PhotoObservationModel', backref='photo_observation')
