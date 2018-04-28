import credentials

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister


# App Config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@server/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = credentials.secret_key['password']
api = Api(app)


# Authentification & Resources
jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(UserRegister, '/register')


# Init & Launch
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
