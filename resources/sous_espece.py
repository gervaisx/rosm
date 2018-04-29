from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.sous_espece import SousEspeceModel
from models.espece import EspeceModel

class SousEspeces(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('nom_commun',
                        type=str,
                        required=False
                        )
    parser.add_argument('nom_latin',
                        type=str,
                        required=False
                        )
    parser.add_argument('nom_en',
                        type=str,
                        required=False
                        )
    parser.add_argument('details',
                        type=str,
                        required=False
                        )
    parser.add_argument('espece',
                        type=int,
                        required=False
                        )

    @jwt_required()
    def get(self):

        try:

            data = {}
            list_sous_especes = {}

            sous_especes = SousEspeceModel.query.all()

            for sous_espece in sous_especes :
                list_sous_especes[sous_espece.id] = [sous_espece.nom_commun,sous_espece.nom_latin,sous_espece.nom_commun_en,sous_espece.descript]

            data['sous_especes'] = list_sous_especes

            return data, 200

        except:

            return {'message': 'Could not retreive the species'}, 404

    @jwt_required()
    def post(self):

        data = SousEspeces.parser.parse_args()

        try:

            espece = EspeceModel.query.filter_by(id = data['genre'])

            sous_espece = SousEspeceModel(nom_commun = data['nom_commun'],
                                 nom_latin = data['nom_latin'],
                                 nom_commun_en = data['nom_en'],
                                 descript = data['details'],
                                 espece = espece
            )

            sous_espece.save_to_db()

            return {'message': 'Specie successfully added'}, 201

        except:

            return {'message': 'An error occurred adding the specie.'}, 500