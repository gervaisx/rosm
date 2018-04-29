from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.famille import FamilleModel
from models.sous_ordre import SousOrdreModel

class Famille(Resource):

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
    parser.add_argument('sous_ordre',
                        type=int,
                        required=False
                        )

    @jwt_required()
    def get(self):

        try:

            data = {}
            list_familles = {}

            familles = FamilleModel.query.all()

            for famille in familles :
                list_familles[famille.id] = [famille.nom_commun, famille.nom_latin, famille.nom_commun_en, famille.descript]

            data['familles'] = list_familles

            return data, 200

        except:

            return {'message': 'Could not retreive the familles'}, 404

    @jwt_required()
    def post(self):

        data = Famille.parser.parse_args()

        try:

            sous_ordre = SousOrdreModel.query.filter_by(id = data['sous_ordre']).first()

            famille = FamilleModel(nom_commun = data['nom_commun'],
                                    nom_latin = data['nom_latin'],
                                    nom_commun_en = data['nom_en'],
                                    descript = data['details'],
                                    sous_ordre = sous_ordre
                                    )

            famille.save_to_db()

            return {'message': 'Famille successfully added'}, 201

        except:

            return {'message': 'An error occurred adding the famille.'}, 500