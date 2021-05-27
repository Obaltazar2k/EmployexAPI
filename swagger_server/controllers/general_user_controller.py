from swagger_server.models.base_model_ import T
import connexion
import six, json

from swagger_server import util
from flask import Blueprint, request, Response, session, Flask
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from swagger_server.app import limiter
from peewee import DoesNotExist

from swagger_server.models.user import User
from swagger_server.data.DBConnection import DBConnection
from http import HTTPStatus
from swagger_server.data.db import Usuario, database

login = Blueprint('Login_user', __name__)

#@jwt_required() Decorador para solicitar el token de acceso
#@limiter.limit("1/hour") Decorador para cambiar el limite por defecto de alguna transacción 
def login_user(username, password):  # noqa: E501
    """Logs user into the system

     # noqa: E501

    :param username: The user name for login
    :type username: str
    :param password: The password for login in clear text
    :type password: str

    :rtype: str
    """
    response = Response(status=HTTPStatus.NOT_FOUND.value)
    database.connect()
    try:
        user = Usuario.get_by_id(username)
        if (user.contrasenia == password):
            acces_token = create_access_token(identity=username)
            response = Response(acces_token, status=HTTPStatus.OK.value, mimetype="application/json")
        else:
            response = Response(status=HTTPStatus.UNAUTHORIZED.value)
    except DoesNotExist:
        response = Response(status=HTTPStatus.UNAUTHORIZED.value)
    finally:
        database.close()
    return response

def logout_user():  # noqa: E501
    """Logs out current logged in user session

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'
