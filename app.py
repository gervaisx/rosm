import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_cors import CORS, cross_origin

from security import authenticate, identity
from resources.user import UserRegister
from resources.level_admin import LevelAdmin
from resources.profile_picture import ProfilePicture
from resources.type_milieu import TypeMilieu
from resources.type_eau import TypeEau
from resources.type_substrat import TypeSubstrat
from resources.categorie_profondeur import CategorieProfondeur
from resources.statut_espece import StatutEspece
from resources.photo_sous_espece import PhotoSousEspece
from resources.regne import Regne
from resources.embranchement import Embranchement
from resources.classe import Classe
from resources.sous_classe import SousClasse
from resources.ordre import Ordre
from resources.sous_ordre import SousOrdre
from resources.famille import Famille
from resources.genre import Genre
from resources.espece import Especes
from resources.sous_espece import SousEspeces


# App Config
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.environ.get('SECRET_KEY', 'Under-Dev')
api = Api(app)
CORS(app)

@app.route("/")
@cross_origin(origin='*')
def helloWorld():
    return "Hello, cross-origin-world!"


# Authentification & Resources
jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(UserRegister, '/register')
api.add_resource(LevelAdmin, '/level-administrator')
api.add_resource(ProfilePicture, '/profile-picture')
api.add_resource(TypeMilieu, '/type-milieu')
api.add_resource(TypeEau, '/type-eau')
api.add_resource(TypeSubstrat, '/type-substrat')
api.add_resource(CategorieProfondeur, '/profondeur')
api.add_resource(StatutEspece, '/statut-espece')
api.add_resource(PhotoSousEspece, '/photo-sous-espece')
api.add_resource(Regne, '/regnes')
api.add_resource(Embranchement, '/embranchements')
api.add_resource(Classe, '/classes')
api.add_resource(SousClasse, '/sous-classes')
api.add_resource(Ordre, '/ordres')
api.add_resource(SousOrdre, '/sous-ordres')
api.add_resource(Famille, '/familles')
api.add_resource(Genre, '/genres')
api.add_resource(Especes, '/especes')
api.add_resource(SousEspeces, '/sous-especes')


# Init & Launch
if __name__ == '__main__':
    from db import db
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)
