from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
from models.user import UserModel


class UserRegister(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('email',
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

        if UserModel.find_by_username(data['email']):
            return {"message": "A user with that email already exists"}, 400

        user = UserModel(data['email'], data['password'])

        try:
            user.save_to_db()
        except:
            return {"message": "An error occurred creating the user."}, 500

        return {"message": "User created successfully."}, 201