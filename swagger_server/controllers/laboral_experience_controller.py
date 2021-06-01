from operator import pos
import connexion

from swagger_server.models.laboral_experience import LaboralExperience  # noqa: E501
from flask import Response
from http import HTTPStatus
from swagger_server.data.db import Experiencialaboral, Independiente
from peewee import DoesNotExist


def add_laboral_experience(body, user_id):  # noqa: E501
    """Adds laboral experience info to an independient user

     # noqa: E501

    :param body: Laboral experience object that needs to be added to the catalog
    :type body: dict | bytes
    :param user_id: Unique identifier of the user
    :type user_id: int

    :rtype: None
    """
    response = Response(status=HTTPStatus.NOT_ACCEPTABLE.value)
    if connexion.request.is_json:
        print("Hola")
        try:
            body = LaboralExperience.from_dict(connexion.request.get_json())  # noqa: E501
            postedLaboralExperience = Experiencialaboral()
            retrievedIndependientUser = Independiente.get(Independiente.usuariocorreo == user_id)

            postedLaboralExperience.nombreempresa = body.company_name
            postedLaboralExperience.sector = body.sector
            postedLaboralExperience.tipoempleo = body.job_category
            postedLaboralExperience.titulo = body.job_title
            postedLaboralExperience.ubicacion = body.location
            postedLaboralExperience.independiente = retrievedIndependientUser.independiente_id
            postedLaboralExperience.fechainicio = body.start_date
            postedLaboralExperience.fechafin = body.end_date
            if body.current_job == True:
                postedLaboralExperience.cargoactual = True
            else:
                postedLaboralExperience.cargoactual = False
            postedLaboralExperience.save()
            response = Response(status=HTTPStatus.OK.value)
        except DoesNotExist:
            response = Response(status=HTTPStatus.NOT_FOUND.value)
    return response
