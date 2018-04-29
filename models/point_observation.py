from db import db

class PointObservationModel(db.Model):

    __tablename__ = 'point_observation'

    # Basic attributes
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.String(45))
    lon = db.Column(db.String(45))
    temperature = (db.Integer)
    insert_at = db.Column(db.String(45))
    datetime = db.Column(db.String(45))
    active = (db.Integer)
    notes = db.Column(db.String(256))

    # Relations
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    type_substrat_id = db.Column(db.Integer, db.ForeignKey('type_substrat.id'))
    type_milieu_id = db.Column(db.Integer, db.ForeignKey('type_milieu.id'))
    categorie_profondeur_id = db.Column(db.Integer, db.ForeignKey('categorie_profondeur.id'))

    point_observation = db.relationship('ObservationModel', backref='point_observation')