from db import db

class PhotoObservationModel(db.Model):

    __tablename__ = 'photo_observation'

    # Basic attributes
    id = db.Column(db.Integer, primary_key=True)
    url_photo = db.Column(db.String(128))

    # Relations
    observation_id = db.Column(db.Integer, db.ForeignKey('observation.id'))