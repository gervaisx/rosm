from db import db

class GenreModel(db.Model):

    __tablename__ = 'genre'

    # Basic attributes
    id = db.Column(db.Integer, primary_key=True)
    nom_commun = db.Column(db.String(128))
    nom_latin = db.Column(db.String(128))
    nom_commun_en = db.Column(db.String(128))
    descript = db.Column(db.String(256))

    # Relations
    famille_id = db.Column(db.Integer, db.ForeignKey('famille.id'))

    genre = db.relationship('EspeceModel', backref='genre')

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()