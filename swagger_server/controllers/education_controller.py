import connexion

from swagger_server.models.education import Education  # noqa: E501
from flask import Response
from http import HTTPStatus
from swagger_server.data.db import Educacion, Independiente
from peewee import DoesNotExist
from flask_jwt_extended import jwt_required

@jwt_required()
def add_education(body, user_id):  # noqa: E501
    """Adds education info to an independient user

     # noqa: E501

    :param body: Education object that needs to be added to the catalog
    :type body: dict | bytes
    :param user_id: Unique identifier of the user
    :type user_id: int

    :rtype: None
    """
    response = Response(status=HTTPStatus.NOT_ACCEPTABLE.value)
    if connexion.request.is_json:       
        try:
            body = Education.from_dict(connexion.request.get_json())  # noqa: E501
            postedEducation = Educacion()
            retrievedIndependientUser = Independiente.get(Independiente.usuariocorreo == user_id)

            postedEducation.titulo = body.title
            postedEducation.universidad = body.university
            postedEducation.promedio = body.average
            postedEducation.disciplina = body.discipline
            postedEducation.descripcion = body.description            
            postedEducation.independiente = retrievedIndependientUser.independiente_id
            postedEducation.fechainicio = body.start_date
            postedEducation.fechafin = body.end_date
            
            postedEducation.save()
            response = Response(status=HTTPStatus.CREATED.value)
        except DoesNotExist:
            response = Response(status=HTTPStatus.NOT_FOUND.value)
    return response
