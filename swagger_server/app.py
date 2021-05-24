#!/usr/bin/env python3
import datetime
import connexion

from flask import Flask

from swagger_server import encoder
from swagger_server.data.extensions import jwt
from swagger_server.controllers.general_user_controller import login

def create_app():
    app = connexion.FlaskApp(__name__, specification_dir='./swagger/')
    #app = Flask(__name__)

    app.app.secret_key = 'Blah!'
    app.app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)  
    #app.config['JWT_BLACKLIST_ENABLED'] = True
    #app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']

    jwt.init_app(app.app)

    app.app.register_blueprint(login)
    
    #app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Employex'}, pythonic_params=True)

    return app