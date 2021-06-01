from swagger_server.models.user import User
import connexion
import json

from flask import Response
from swagger_server.models.independient_user import IndependientUser  # noqa: E501
from swagger_server.models.media import Media as MediaModels
from swagger_server.data.DBConnection import DBConnection
from http import HTTPStatus
from swagger_server.data.db import Media, Independiente, Usuario, database
from peewee import DoesNotExist


def get_independint_user_by_id(user_id):  # noqa: E501
    """Get user by user id

     # noqa: E501

    :param user_id: Unique identifier of the user
    :type user_id: int

    :rtype: IndependientUser
    """
    response = Response(status=HTTPStatus.NOT_FOUND.value)
    database.connect()
    try:
        retrieveIndependientUser = Independiente.get(Independiente.usuariocorreo == user_id)
        independientUser = IndependientUser()
        independientUser.surnames = retrieveIndependientUser.apellidos
        independientUser.persoanl_description = retrieveIndependientUser.descripcionpersonal
        independientUser.name = retrieveIndependientUser.nombre
        independientUser.ocupation = retrieveIndependientUser.ocupacion

        retrieveGeneralUser = Usuario.get_by_id(retrieveIndependientUser.Usuariocorreo)
        generalUser = User()
        generalUser.city = retrieveGeneralUser.ciudad
        generalUser.email = retrieveGeneralUser.correo
        generalUser.country = retrieveGeneralUser.pais
        generalUser.user_id = retrieveGeneralUser.usuariocorreo

        retrievedPerfilPhoto = Media.get_by_id(retrieveGeneralUser.fotoperfil)
        profilePhoto = MediaModels()
        profilePhoto.file = retrievedPerfilPhoto.file
        generalUser.profile_photo = profilePhoto
        independientUser.user = generalUser
    except DoesNotExist:
        response = Response(status=HTTPStatus.NOT_FOUND.value)
    finally:
        database.close()
        independientUser_json = IndependientUser.to_dict(independientUser)
        response = Response(json.dumps(independientUser_json),status=HTTPStatus.OK.value,mimetype="application/json")
    return response


def register_indpendient_user(body):  # noqa: E501
    """Register independient user

     # noqa: E501

    :param body: Independient user object to register
    :type body: dict | bytes

    :rtype: None
    """
    response = Response(status=HTTPStatus.UNAUTHORIZED.value)
    if connexion.request.is_json:
        body = IndependientUser.from_dict(connexion.request.get_json())  # noqa: E501
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
        
            Independiente.create(apellidos = body.surnames, aptitud = 'Creatividad', descripcionpersonal = body.persoanl_description,
            nombre = body.name, ocupacion = body.ocupation, usuariocorreo = body.user.email)

            response = Response(status=HTTPStatus.OK.value)
    return response