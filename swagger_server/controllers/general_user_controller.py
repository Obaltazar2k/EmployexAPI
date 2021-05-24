import connexion
import six, json

from swagger_server import util
from flask import Blueprint, request, Response, session, Flask
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

from swagger_server.models.user import User
from swagger_server.controllers.auth import Auth
from swagger_server.models.responses_rest import ResponsesREST
from swagger_server.data.DBConnection import DBConnection
from swagger_server.data.extensions import jwt

login = Blueprint('Login_user', __name__)

#@jwt_required()
def login_user(username, password):  # noqa: E501
    """Logs user into the system

     # noqa: E501

    :param username: The user name for login
    :type username: str
    :param password: The password for login in clear text
    :type password: str

    :rtype: str
    """
    response = Response(status=ResponsesREST.INVALID_INPUT.value)
    account_login = User()
    account_login.username = username
    account_login.password = password
    query = "SELECT Usuariocorreo FROM Usuario WHERE Usuariocorreo = %s AND Contrasenia = %s"
    param = [account_login.username, account_login.password]
    connection = DBConnection()
    list_accounts = connection.select(query, param)
    if list_accounts:
        acces_token = create_access_token(identity=username)
        response = Response(json.dumps(acces_token), status=ResponsesREST.SUCCESSFUL.value, mimetype="application/json")
    else:
        response = Response(status=ResponsesREST.NOT_AUTHORIZED.value)
    return response

def logout_user():  # noqa: E501
    """Logs out current logged in user session

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'
