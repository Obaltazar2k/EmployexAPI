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
from flask_jwt_extended import jwt_required
from swagger_server.controllers.general_user_controller import send_validationToken_email, tokenGenerator

@jwt_required()
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

        try:
            retrievedPerfilPhoto = Media.get_by_id(retrieveGeneralUser.fotoperfil)
            profilePhoto = MediaModels()
            profilePhoto.file = retrievedPerfilPhoto.file
            generalUser.profile_photo = profilePhoto
        except DoesNotExist:
            generalUser.profile_photo = None
        organizationUser.user = generalUser

        organizationUser_json = OrganizationUser.to_dict(organizationUser)
        response = Response(json.dumps(organizationUser_json),status=HTTPStatus.OK.value,mimetype="application/json")
    except DoesNotExist:
        response = Response(status=HTTPStatus.NOT_FOUND.value)
    finally:
        database.close()      
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
            token = tokenGenerator()
            postedUser = Usuario.create(ciudad = body.user.city, contrasenia = body.user.password, correo = body.user.email,
            pais = body.user.country, usuariocorreo = body.user.email, validationtoken = token, validated = 0)

            postedMedia = Media()
            postedMedia.file = body.user.profile_photo.file
            postedMedia.usuariocorreo = body.user.email
            postedMedia.save()

            postedUser.fotoperfil = postedMedia.media_id
            postedUser.save()

            Organizacion.create(acercade = body.about, codigopostal = body.zip_code, emailcontacto = body.contact_email, nombre = body.name,
            nombrecontact = body.contact_name, sector = body.work_sector, sitioweb = body.web_site, telefonocontacto = body.contact_phone, usuariocorreo = body.user.email)
            send_validationToken_email(body.user.email, body.name, token)

            response = Response(status=HTTPStatus.OK.value)
    return response

@jwt_required()
def patch_organization_user_by_id(body, user_id):  # noqa: E501
    """Patch organization user

     # noqa: E501

    :param body: Organization user object to register
    :type body: dict | bytes
    :param user_id: Unique identifier of the user
    :type user_id: str

    :rtype: None
    """
    response = Response(status=HTTPStatus.NOT_FOUND.value)
    database.connect()
    if connexion.request.is_json:
        body = OrganizationUser.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            retrieveOrganizationUser = Organizacion.get(Organizacion.usuariocorreo == user_id)
            retrieveGeneralUser = Usuario.get_by_id(user_id)
            retrieveMedia = Media.get((Media.usuariocorreo == user_id) & (Media.seccion.is_null(True)) & (Media.ofertadetrabajo.is_null(True)))
            retrieveGeneralUser.ciudad = body.user.city
            retrieveGeneralUser.pais = body.user.country
            retrieveOrganizationUser.nombre = body.name
            retrieveOrganizationUser.acercade = body.about
            retrieveOrganizationUser.codigopostal = body.zip_code
            retrieveOrganizationUser.emailcontacto = body.contact_email
            retrieveOrganizationUser.nombrecontact = body.contact_name
            retrieveOrganizationUser.sector = body.work_sector
            retrieveOrganizationUser.sitioweb = body.web_site
            retrieveOrganizationUser.telefonocontacto = body.contact_phone
            retrieveMedia.file = body.user.profile_photo.file
            retrieveOrganizationUser.save()
            retrieveGeneralUser.save()
            retrieveMedia.save()
            response = Response(status=HTTPStatus.OK.value)
        except DoesNotExist:
            response = Response(status=HTTPStatus.NOT_FOUND.value)
        finally:
            database.close()
    return response
