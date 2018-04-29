from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.espece import EspeceModel
from models.genre import GenreModel

class Especes(Resource):

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
    parser.add_argument('genre',
                        type=int,
                        required=False
                        )

    @jwt_required()
    def get(self):

        try:

            data = {}
            list_especes = {}

            especes = EspeceModel.query.all()

            for espece in especes :
                list_especes[espece.id] = [espece.nom_commun,espece.nom_latin,espece.nom_commun_en,espece.descript]

            data['especes'] = list_especes

            return data, 200

        except:

            return {'message': 'Could not retreive the species'}, 404

    @jwt_required()
    def post(self):

        data = Especes.parser.parse_args()

        try:

            genre = GenreModel.query.filter_by(id = data['genre'])

            espece = EspeceModel(nom_commun = data['nom_commun'],
                                 nom_latin = data['nom_latin'],
                                 nom_commun_en = data['nom_en'],
                                 descript = data['details'],
                                 genre = genre
            )

            espece.save_to_db()

            return {'message': 'Specie successfully added'}, 201

        except:

            return {'message': 'An error occurred adding the specie.'}, 500