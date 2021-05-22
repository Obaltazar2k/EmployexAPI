import connexion
import six, json

from swagger_server import util
from flask import Blueprint, request, Response, session

from swagger_server.models.user import User
from swagger_server.controllers.auth import Auth
from swagger_server.models.responses_rest import ResponsesREST
from swagger_server.data.DBConnection import DBConnection

login = Blueprint("Login", __name__)

def login_user(username, password):  # noqa: E501
    """Logs user into the system

     # noqa: E501

    :param username: The user name for login
    :type username: str
    :param password: The password for login in clear text
    :type password: str

    :rtype: str
    """
    #json_values = request.json
    #values_required = {"username", "password"}
    response = Response(status=ResponsesREST.INVALID_INPUT.value)
    #if all(key in json_values for key in values_required):
    account_login = User()
    account_login.username = username #json_values["username"]
    account_login.password = password #json_values["password"]
        
    query = "SELECT Usuariocorreo FROM Usuario WHERE Usuariocorreo = %s AND Contrasenia = %s"
    param = [account_login.username, account_login.password]
    connection = DBConnection()
    list_accounts = connection.select(query, param)
    account = False
    if list_accounts:
        account = True
    if account:
        token = Auth.generate_token(account_login, 1)
        #session.permanent = True
        #session["token"] = token
        response = Response(json.dumps({"token": token}), status=ResponsesREST.SUCCESSFUL.value, mimetype="application/json")
    else:
        response = Response(status=account)
    return response


def logout_user():  # noqa: E501
    """Logs out current logged in user session

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'
