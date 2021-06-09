import connexion
import json

from flask import Response
from swagger_server.models.organization_user import OrganizationUser  # noqa: E501
from swagger_server.models.user import User
from swagger_server.models.media import Media as MediaModels
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
    response = Response(status=HTTPStatus.NOT_FOUND.value)
    database.connect()
    try:
        retrieveOrganizationtUser = Organizacion.get(Organizacion.usuariocorreo == user_id)
        organizationUser = OrganizationUser()
        organizationUser.name = retrieveOrganizationtUser.nombre
        organizationUser.work_sector = retrieveOrganizationtUser.sector
        organizationUser.web_site = retrieveOrganizationtUser.sitioweb
        organizationUser.contact_name = retrieveOrganizationtUser.nombrecontact
        organizationUser.contact_email = retrieveOrganizationtUser.emailcontacto
        organizationUser.contact_phone = retrieveOrganizationtUser.telefonocontacto
        organizationUser.about = retrieveOrganizationtUser.acercade
        organizationUser.zip_code = retrieveOrganizationtUser.codigopostal

        retrieveGeneralUser = Usuario.get_by_id(retrieveOrganizationtUser.Usuariocorreo)
        generalUser = User()
        generalUser.city = retrieveGeneralUser.ciudad
        generalUser.email = retrieveGeneralUser.correo
        generalUser.country = retrieveGeneralUser.pais
        generalUser.user_id = retrieveGeneralUser.usuariocorreo

        retrievedPerfilPhoto = Media.get_by_id(retrieveGeneralUser.fotoperfil)
        profilePhoto = MediaModels()
        profilePhoto.file = retrievedPerfilPhoto.file
        generalUser.profile_photo = profilePhoto
        organizationUser.user = generalUser
    except DoesNotExist:
        response = Response(status=HTTPStatus.NOT_FOUND.value)
    finally:
        database.close()
        organizationUser_json = OrganizationUser.to_dict(organizationUser)
        response = Response(json.dumps(organizationUser_json),status=HTTPStatus.OK.value,mimetype="application/json")
    return response


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
