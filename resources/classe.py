from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.classe import ClasseModel
from models.embranchement import EmbranchementModel

class Classe(Resource):

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
    parser.add_argument('embranchement',
                        type=int,
                        required=False
                        )

    @jwt_required()
    def get(self):

        try:

            data = {}
            list_classes = {}

            classes = ClasseModel.query.all()

            for classe in classes :
                list_classes[classe.id] = [classe.nom_commun, classe.nom_latin, classe.nom_commun_en, classe.descript]

            data['classes'] = list_classes

            return data, 200

        except:

            return {'message': 'Could not retreive the classe'}, 404

    @jwt_required()
    def post(self):

        data = Classe.parser.parse_args()

        try:

            embranchement = EmbranchementModel.query.filter_by(id = data['embranchement']).first()

            classe = ClasseModel(nom_commun = data['nom_commun'],
                                    nom_latin = data['nom_latin'],
                                    nom_commun_en = data['nom_en'],
                                    descript = data['details'],
                                    embranchement = embranchement
                                    )

            classe.save_to_db()

            return {'message': 'Classe successfully added'}, 201

        except:

            return {'message': 'An error occurred adding the classe.'}, 500