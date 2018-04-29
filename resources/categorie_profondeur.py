from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.categorie_profondeur import CategorieProfondeurModel

class CategorieProfondeur(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('categorie_profondeur',
                        type=str,
                        required=False
                        )

    @jwt_required()
    def get(self):

        try:

            data = {}
            categeorie_profondeurs = {}

            categorie_profondeur = CategorieProfondeurModel.query.all()

            for profondeur in categorie_profondeur :
                categeorie_profondeurs[profondeur.id] = profondeur.name

            data['categories_profondeur'] = categeorie_profondeurs

            return data, 200

        except:

            return {'message': 'Could not retreive the depth'}, 404

    @jwt_required()
    def post(self):

        data = CategorieProfondeur.parser.parse_args()

        try:

            categorie_profondeur = CategorieProfondeurModel(name = data['categorie_profondeur'])

            categorie_profondeur.save_to_db()

            return {'message': 'Depth successfully added'}, 201

        except:

            return {'message': 'An error occurred adding the depth.'}, 500