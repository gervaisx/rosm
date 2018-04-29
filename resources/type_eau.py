from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.type_eau import TypeEauModel

class TypeEau(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('type_eau',
                        type=str,
                        required=False
                        )

    @jwt_required()
    def get(self):

        try:

            data = {}
            type_eaux = {}

            type_eau = TypeEauModel.query.all()

            for eau in type_eau :
                type_eaux[eau.id] = eau.name

            data['types_eaux'] = type_eaux

            return data, 200

        except:

            return {'message': 'Could not retreive the milieu'}, 404

    @jwt_required()
    def post(self):

        data = TypeEau.parser.parse_args()

        try:

            type_eau = TypeEauModel(name = data['type_eau'])

            type_eau.save_to_db()

            return {'message': 'Water Type successfully added'}, 201

        except:

            return {'message': 'An error occurred adding the Water Type.'}, 500