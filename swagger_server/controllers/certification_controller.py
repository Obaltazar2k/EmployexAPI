import connexion

from swagger_server.models.certification import Certification  # noqa: E501
from flask import Response
from http import HTTPStatus
from swagger_server.data.db import Certificacion, Independiente
from peewee import DoesNotExist


def add_certification(body, user_id):  # noqa: E501
    """Adds certification info to an independient user

     # noqa: E501

    :param body: Certification object that needs to be added to the catalog
    :type body: dict | bytes
    :param user_id: Unique identifier of the user
    :type user_id: str

    :rtype: None
    """
    response = Response(status=HTTPStatus.NOT_ACCEPTABLE.value)
    if connexion.request.is_json:
        try:
            body = Certification.from_dict(connexion.request.get_json())  # noqa: E501
            postedCertification = Certificacion()
            retrievedIndependientUser = Independiente.get(Independiente.usuariocorreo == user_id)

            postedCertification.titulo = body.title
            postedCertification.empresaemisora = body.issuing_company
            postedCertification.credencialurl = body.credential_url        
            postedCertification.independiente = retrievedIndependientUser.independiente_id
            postedCertification.fechaexpedicion = body.expedition_date
            postedCertification.fechacaducidad = body.expiration_date
                       
            postedCertification.save()
            response = Response(status=HTTPStatus.OK.value)
        except DoesNotExist:
            response = Response(status=HTTPStatus.NOT_FOUND.value)
    return response
