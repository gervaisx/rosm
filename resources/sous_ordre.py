from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.sous_ordre import SousOrdreModel
from models.ordre import OrdreModel

class SousOrdre(Resource):

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
    parser.add_argument('ordre',
                        type=int,
                        required=False
                        )

    @jwt_required()
    def get(self):

        try:

            data = {}
            list_sous_ordres = {}

            sous_ordres = SousOrdreModel.query.all()

            for sous_ordre in sous_ordres :
                list_sous_ordres[sous_ordre.id] = [sous_ordre.nom_commun, sous_ordre.nom_latin, sous_ordre.nom_commun_en, sous_ordre.descript]

            data['sous_ordres'] = list_sous_ordres

            return data, 200

        except:

            return {'message': 'Could not retreive the sous-ordre'}, 404

    @jwt_required()
    def post(self):

        data = SousOrdre.parser.parse_args()

        try:

            ordre = OrdreModel.query.filter_by(id = data['ordre']).first()

            sous_ordre = SousOrdreModel(nom_commun = data['nom_commun'],
                                    nom_latin = data['nom_latin'],
                                    nom_commun_en = data['nom_en'],
                                    descript = data['details'],
                                    ordre = ordre
                                    )

            sous_ordre.save_to_db()

            return {'message': 'Sous-ordre successfully added'}, 201

        except:

            return {'message': 'An error occurred adding the sous-ordre.'}, 500