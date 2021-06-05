import connexion

from swagger_server.models.section import Section  # noqa: E501
from flask import Response
from http import HTTPStatus
from swagger_server.data.db import Seccion, Media, Independiente
from peewee import DoesNotExist


def add_section(body, user_id):  # noqa: E501
    """Adds section info to an independient user

     # noqa: E501

    :param body: Section object that needs to be added to the catalog
    :type body: dict | bytes
    :param user_id: Unique identifier of the user
    :type user_id: str

    :rtype: None
    """
    response = Response(status=HTTPStatus.NOT_FOUND.value)
    if connexion.request.is_json:
        try:
            body = Section.from_dict(connexion.request.get_json())  # noqa: E501
            retrievedIndependientUser = Independiente.get(Independiente.usuariocorreo == user_id)
            
            '''postedSection = Seccion()
            postedSection.titulo = body.title
            postedSection.descripcion = body.description
            postedSection.independiente = retrievedIndependientUser.independiente_id                       
            postedSection.save()'''

            postedSection = Seccion.create(titulo = body.title, descripcion = body.description, independiente = retrievedIndependientUser.independiente_id)

            for media in body.media:
                Media.create(
                    file = media.file,
                    seccion = postedSection.seccion_id,
                    usuariocorreo = user_id)
            response = Response(status=HTTPStatus.OK.value)
        except DoesNotExist:
            response = Response(status=HTTPStatus.NOT_FOUND.value)
    return response
