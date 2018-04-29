from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.statut_espece import StatutEspeceModel

class StatutEspece(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('statut_espece',
                        type=str,
                        required=False
                        )

    @jwt_required()
    def get(self):

        try:

            data = {}
            list_statut = {}

            statuts_espece = StatutEspeceModel.query.all()

            for statut in statuts_espece :
                list_statut[statut.id] = statut.name

            data['statuts_espece'] = list_statut

            return data, 200

        except:

            return {'message': 'Could not retreive the status'}, 404

    @jwt_required()
    def post(self):

        data = StatutEspece.parser.parse_args()

        try:

            statut_espece = StatutEspeceModel(name = data['statut_espece'])

            statut_espece.save_to_db()

            return {'message': 'Status successfully added'}, 201

        except:

            return {'message': 'An error occurred adding the status.'}, 500