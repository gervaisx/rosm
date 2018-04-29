from flask_restful import Resource, reqparse
from models.user import UserModel
from models.famille import FamilleModel
from models.genre import GenreModel
from models.level_admin import LevelAdminModel
from models.ordre import OrdreModel
from models.point_observation import PointObservationModel
from models.profile_picture import ProfilePictureModel
from models.sous_ordre import SousOrdreModel
from models.photo_observation import PhotoObservationModel
from models.statut_observation import StatutObservationModel
from models.observation import ObservationModel


class UserRegister(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201
