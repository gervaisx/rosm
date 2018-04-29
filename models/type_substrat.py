from db import db

class TypeSubstratModel(db.Model):

    __tablename__ = 'type_substrat'

    # Basic attributes
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    # Relations
    type_substrat = db.relationship('PointObservationModel', backref='type_substrat')