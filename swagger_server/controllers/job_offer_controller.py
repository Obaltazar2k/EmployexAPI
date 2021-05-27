import json
from typing import final
import connexion
import six

from swagger_server.models.job_offer import JobOffer  # noqa: E501
from swagger_server import util
from flask import Response
from swagger_server.data.DBConnection import DBConnection
from http import HTTPStatus
from flask_jwt_extended import jwt_required
from swagger_server.data.db import Ofertadetrabajo, database
from peewee import DoesNotExist


def add_aplication_to_job_offer(user_id, job_offer_id):  # noqa: E501
    """Adds an aplication to a specified job offer

    Adds an aplication to a specified job offer # noqa: E501

    :param user_id: Unique identifier of the user
    :type user_id: int
    :param job_offer_id: Unique identifier of the job offer
    :type job_offer_id: int

    :rtype: None
    """
    return 'do some magic!'


def add_job_offer(body):  # noqa: E501
    """Add a new job offer to the catalog

     # noqa: E501

    :param body: Job offer object that needs to be added to the catalog
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = JobOffer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

@jwt_required()
def get_job_offers(page):  # noqa: E501
    """Returns a list of job offers

    A list of the last ten job offers published by the others users # noqa: E501

    :param page: Pagination
    :type page: int

    :rtype: List[JobOffer]
    """
    response = Response(status=HTTPStatus.NOT_FOUND.value)
    database.connect()
    try:
        list_joboffers = Ofertadetrabajo.select().paginate(page, 10)
    except DoesNotExist:
        response = Response(status=HTTPStatus.NOT_FOUND.value)
    finally:
        database.close()
    job_offer_objects = []
    for job_offer in list_joboffers:
        job_offer_aux = JobOffer()
        job_offer_aux.description = job_offer.descripcion
        job_offer_aux.job = job_offer.cargo
        job_offer_aux.job_category = job_offer.tipoempleo
        job_offer_aux.job_offer_id = job_offer.ofertadetrabajo_id
        job_offer_aux.location = job_offer.ubicacion
        job_offer_objects.append(job_offer_aux)
    if job_offer_objects:
        job_offer_json = []
        for job_offer_object in job_offer_objects:
            job_offer_json.append(JobOffer.to_dict(job_offer_object))
        for elem in job_offer_json:
            elem['jobCategory'] = elem.pop('job_category')
            elem['jobOfferId'] = elem.pop('job_offer_id')
        response = Response(json.dumps(job_offer_json),status=HTTPStatus.OK.value,mimetype="application/json")
    else:
        response = Response(status=HTTPStatus.NOT_FOUND.value)
    return response

def get_job_offers_aplications(user_id, job_offer_id):  # noqa: E501
    """Returns a list of aplications in a specified job offer published by the user

    A list of aplications in the job offer specified published by the user # noqa: E501

    :param user_id: Unique identifier of the user
    :type user_id: int
    :param job_offer_id: Unique identifier of the job offer
    :type job_offer_id: int

    :rtype: List[Aplication]
    """
    return 'do some magic!'


def get_job_offers_published_by_the_user(user_id):  # noqa: E501
    """Returns a list of job offers published by the user

    A list of the job offers published by the user # noqa: E501

    :param user_id: Unique identifier of the user
    :type user_id: int

    :rtype: List[JobOffer]
    """
    return 'do some magic!'
