from db import db

class TypeMilieuModel(db.Model):

    __tablename__ = 'type_milieu'

    # Basic attributes
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    # Relations
    type_eau_id = db.Column(db.Integer, db.ForeignKey('type_eau.id'))

    type_milieu = db.relationship('PointObservationModel', backref='type_milieu')

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()