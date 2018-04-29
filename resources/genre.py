from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.genre import GenreModel
from models.famille import FamilleModel

class Genre(Resource):

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
    parser.add_argument('famille',
                        type=int,
                        required=False
                        )

    @jwt_required()
    def get(self):

        try:

            data = {}
            list_genres = {}

            genres = GenreModel.query.all()

            for genre in genres :
                list_genres[genre.id] = [genre.nom_commun, genre.nom_latin, genre.nom_commun_en, genre.descript]

            data['genres'] = list_genres

            return data, 200

        except:

            return {'message': 'Could not retreive the genres'}, 404

    @jwt_required()
    def post(self):

        data = Genre.parser.parse_args()

        try:

            famille = FamilleModel.query.filter_by(id = data['famille']).first()

            genre = GenreModel(nom_commun = data['nom_commun'],
                                    nom_latin = data['nom_latin'],
                                    nom_commun_en = data['nom_en'],
                                    descript = data['details'],
                                    famille = famille
                                    )

            genre.save_to_db()

            return {'message': 'Genre successfully added'}, 201

        except:

            return {'message': 'An error occurred adding the genre.'}, 500