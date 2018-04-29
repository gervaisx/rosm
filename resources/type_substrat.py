from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.type_substrat import TypeSubstratModel

class TypeSubstrat(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('type_substrat',
                        type=str,
                        required=False
                        )

    @jwt_required()
    def get(self):

        try:

            data = {}
            type_substrats = {}

            type_substrat = TypeSubstratModel.query.all()

            for substrat in type_substrat :
                type_substrats[substrat.id] = substrat.name

            data['types_substrat'] = type_substrats

            return data, 200

        except:

            return {'message': 'Could not retreive the substratum'}, 404

    @jwt_required()
    def post(self):

        data = TypeSubstrat.parser.parse_args()

        try:

            type_substrat = TypeSubstratModel(name = data['type_substrat'])

            type_substrat.save_to_db()

            return {'message': 'Substratum successfully added'}, 201

        except:

            return {'message': 'An error occurred adding the substratum.'}, 500