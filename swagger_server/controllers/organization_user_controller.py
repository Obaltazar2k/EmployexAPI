import connexion
import six

from flask import Blueprint, request, Response, session
from swagger_server.models.organization_user import OrganizationUser  # noqa: E501
from swagger_server import util
from swagger_server.data.DBConnection import DBConnection
from http import HTTPStatus
from swagger_server.data.db import Media, Organizacion, Usuario, database
from peewee import DoesNotExist


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
            postedUser = Usuario.create(ciudad = body.user.city, contrasenia = body.user.password, correo = body.user.email,
            pais = body.user.country, usuariocorreo = body.user.email)

            postedMedia = Media()
            postedMedia.file = body.user.profile_photo.file
            postedMedia.usuariocorreo = body.user.email
            postedMedia.save()

            postedUser.fotoperfil = postedMedia.media_id
            postedUser.save()

            Organizacion.create(acercade = body.about, codigopostal = body.zip_code, emailcontacto = body.contact_email, nombre = body.name,
            nombrecontact = body.contact_name, sector = body.work_sector, sitioweb = body.web_site, telefonocontacto = body.contact_phone, usuariocorreo = body.user.email)
            response = Response(status=HTTPStatus.OK.value)
    return response
