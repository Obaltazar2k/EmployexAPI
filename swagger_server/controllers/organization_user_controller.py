import connexion
import six

from flask import Blueprint, request, Response, session
from swagger_server.models.organization_user import OrganizationUser  # noqa: E501
from swagger_server import util
from swagger_server.data.DBConnection import DBConnection
from http import HTTPStatus


def get_organization_user_by_id(user_id):  # noqa: E501
    """Get user by user id

     # noqa: E501

    :param user_id: Unique identifier of the user
    :type user_id: int

    :rtype: IndependientUser
    """
    return 'do some magic!'


def register_organization_user(body):  # noqa: E501
    """Register organization user

     # noqa: E501

    :param body: Organization user object to register
    :type body: dict | bytes

    :rtype: None
    """
    response = Response(status=HTTPStatus.NOT_FOUND.value)
    if connexion.request.is_json:
        body = OrganizationUser.from_dict(connexion.request.get_json())  # noqa: E501
        query = "SELECT Usuariocorreo FROM Usuario WHERE Usuariocorreo = %s"
        param = [body.user.email]
        connection = DBConnection()
        list_accounts = connection.select(query, param)
        if list_accounts:
            return response
        else:
            query = "INSERT INTO Usuario VALUES (%s, %s,%s, null, %s, %s)"
            param = [body.user.city, body.user.password, body.user.email, body.user.country, body.user.email]
            connection.send_query(query, param)
            query = "INSERT INTO organizacion VALUES (%s,%s, %s, %s, %s, %s, %s, %s, null, %s)"
            param = [body.about, body.zip_code,  body.contact_email, body.name, body.contact_name, body.work_sector, body.web_site, body.contact_phone, body.user.email]
            connection.send_query(query, param)
            response = Response(status=HTTPStatus.OK.value)
    return response
