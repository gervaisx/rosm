from db import db

class CategorieProfondeurModel(db.Model):

    __tablename__ = 'categorie_profondeur'

    # Basic attributes
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    # Relations
    categorie_profondeur = db.relationship('PointObservationModel', backref='categorie_profondeur')

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()