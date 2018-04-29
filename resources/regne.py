from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.regne import RegneModel

class Regne(Resource):

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

    @jwt_required()
    def get(self):

        try:

            data = {}
            list_regnes = {}

            regnes = RegneModel.query.all()

            for regne in regnes :
                list_regnes[regne.id] = [regne.nom_commun, regne.nom_latin, regne.nom_commun_en, regne.descript]

            data['regnes'] = list_regnes

            return data, 200

        except:

            return {'message': 'Could not retreive the regne'}, 404

    @jwt_required()
    def post(self):

        data = Regne.parser.parse_args()

        try:

            regne = RegneModel(nom_commun = data['nom_commun'],
                               nom_latin = data['nom_latin'],
                               nom_commun_en = data['nom_en'],
                               descript = data['details']
                               )

            regne.save_to_db()

            return {'message': 'Regne successfully added'}, 201

        except:

            return {'message': 'An error occurred adding the regne.'}, 500