from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.photo_sous_espece import PhotoSousEspeceModel
from models.sous_espece import SousEspeceModel

class PhotoSousEspece(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('photo',
                        type=str,
                        required=False
                        )
    parser.add_argument('sous_espece',
                        type=int,
                        required=False
                        )

    @jwt_required()
    def post(self):

        data = PhotoSousEspece.parser.parse_args()

        try:

            sous_espece = SousEspeceModel.query.filter_by(id = data['sous_espece'])

            photo = PhotoSousEspeceModel(url_photo = data['photo'],
                                         photo_sous_espece = sous_espece)

            photo.save_to_db()

            return {'message': 'Photo successfully added'}, 201

        except:

            return {'message': 'An error occurred adding the photo.'}, 500