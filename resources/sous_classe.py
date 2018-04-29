from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.sous_classe import SousClasseModel
from models.classe import ClasseModel

class SousClasse(Resource):

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
    parser.add_argument('classe',
                        type=int,
                        required=False
                        )

    @jwt_required()
    def get(self):

        try:

            data = {}
            list_sous_classes = {}

            sous_classes = SousClasseModel.query.all()

            for sous_classe in sous_classes :
                list_sous_classes[sous_classe.id] = [sous_classe.nom_commun, sous_classe.nom_latin, sous_classe.nom_commun_en, sous_classe.descript]

            data['sous_classes'] = list_sous_classes

            return data, 200

        except:

            return {'message': 'Could not retreive the sous-classe'}, 404

    @jwt_required()
    def post(self):

        data = SousClasse.parser.parse_args()

        try:

            classe = ClasseModel.query.filter_by(id = data['classe']).first()

            sous_classe = SousClasseModel(nom_commun = data['nom_commun'],
                                    nom_latin = data['nom_latin'],
                                    nom_commun_en = data['nom_en'],
                                    descript = data['details'],
                                    classe = classe
                                    )

            sous_classe.save_to_db()

            return {'message': 'Sous-classe successfully added'}, 201

        except:

            return {'message': 'An error occurred adding the sous-classe.'}, 500