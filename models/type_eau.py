from db import db

class TypeEauModel(db.Model):

    __tablename__ = 'type_eau'

    # Basic attributes
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    # Relations
    type_eau = db.relationship('TypeMilieuModel', backref='type_eau')

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()