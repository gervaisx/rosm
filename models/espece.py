from db import db

class EspeceModel(db.Model):

    __tablename__ = 'espece'

    # Basic attributes
    id = db.Column(db.Integer, primary_key=True)
    nom_commun = db.Column(db.String(128))
    nom_latin = db.Column(db.String(128))
    nom_commun_en = db.Column(db.String(128))
    descript = db.Column(db.String(256))

    # Relations
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))

    espece = db.relationship('GenreModel', backref='espece')
    espece_observation = db.relationship('ObservationModel', backref='espece_observation')