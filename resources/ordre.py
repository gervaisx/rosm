from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.ordre import OrdreModel
from models.sous_classe import SousClasseModel

class Ordre(Resource):

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
    parser.add_argument('sous_classe',
                        type=int,
                        required=False
                        )

    @jwt_required()
    def get(self):

        try:

            data = {}
            list_ordres = {}

            ordres = OrdreModel.query.all()

            for ordre in ordres :
                list_ordres[ordre.id] = [ordre.nom_commun, ordre.nom_latin, ordre.nom_commun_en, ordre.descript]

            data['ordres'] = list_ordres

            return data, 200

        except:

            return {'message': 'Could not retreive the ordre'}, 404

    @jwt_required()
    def post(self):

        data = Ordre.parser.parse_args()

        try:

            sous_classe = SousClasseModel.query.filter_by(id = data['sous_classe']).first()

            ordre = OrdreModel(nom_commun = data['nom_commun'],
                                    nom_latin = data['nom_latin'],
                                    nom_commun_en = data['nom_en'],
                                    descript = data['details'],
                                    sous_classe = sous_classe
                                    )

            ordre.save_to_db()

            return {'message': 'Ordre successfully added'}, 201

        except:

            return {'message': 'An error occurred adding the ordre.'}, 500