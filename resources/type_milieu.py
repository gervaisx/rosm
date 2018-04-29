from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.type_milieu import TypeMilieuModel
from models.type_eau import TypeEauModel

class TypeMilieu(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('type_milieux',
                        type=str,
                        required=False
                        )
    parser.add_argument('type_eau',
                        type=int,
                        required=False
                        )

    @jwt_required()
    def get(self):

        try:

            data = {}
            milieux = {}

            type_milieux = TypeMilieuModel.query.all()

            for type_milieu in type_milieux :
                milieux[type_milieu.id] = [type_milieu.name, type_milieu.type_eau.name]

            data['types_milieux'] = milieux

            return data, 200

        except:

            return {'message': 'Could not retreive the milieu'}, 404

    @jwt_required()
    def post(self):

        data = TypeMilieu.parser.parse_args()

        try:

            type_eau = TypeEauModel.query.filter_by(id=data['type_eau']).first()

            type_milieu = TypeMilieuModel(name = data['type_milieux'],
                                          type_eau = type_eau)

            type_milieu.save_to_db()

            return {'message': 'Milieu successfully added'}, 201

        except:

            return {'message': 'An error occurred adding the milieu.'}, 500