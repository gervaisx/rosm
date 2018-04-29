from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.embranchement import EmbranchementModel
from models.regne import RegneModel

class Embranchement(Resource):

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
    parser.add_argument('regne',
                        type=int,
                        required=False
                        )

    @jwt_required()
    def get(self):

        try:

            data = {}
            list_embranchements = {}

            embranchements = EmbranchementModel.query.all()

            for embranchement in embranchements :
                list_embranchements[embranchement.id] = [embranchement.nom_commun, embranchement.nom_latin, embranchement.nom_commun_en, embranchement.descript]

            data['embranchements'] = list_embranchements

            return data, 200

        except:

            return {'message': 'Could not retreive the embranchements'}, 404

    @jwt_required()
    def post(self):

        data = Embranchement.parser.parse_args()

        try:

            regne = RegneModel.query.filter_by(id = data['regne']).first()

            embranchement = EmbranchementModel(nom_commun = data['nom_commun'],
                                       nom_latin = data['nom_latin'],
                                       nom_commun_en = data['nom_en'],
                                       descript = data['details'],
                                       regne = regne
                                       )

            embranchement.save_to_db()

            return {'message': 'Embranchement successfully added'}, 201

        except:

            return {'message': 'An error occurred adding the embranchements.'}, 500