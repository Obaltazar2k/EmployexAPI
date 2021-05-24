import json
import connexion
import six

from swagger_server.models.job_offer import JobOffer  # noqa: E501
from swagger_server import util
from flask import Response
from swagger_server.data.DBConnection import DBConnection
from http import HTTPStatus


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


def get_job_offers(page):  # noqa: E501
    """Returns a list of job offers

    A list of the last ten job offers published by the others users # noqa: E501

    :param page: Pagination
    :type page: int

    :rtype: List[JobOffer]
    """
    response = Response(status=HTTPStatus.NOT_FOUND.value)
    query = "SELECT ofertadetrabajo.OfertadetrabajoID as job_offer_id,  ofertadetrabajo.Cargo as job, ofertadetrabajo.Descripcion as description, ofertadetrabajo.Tipoempleo as job_category, ofertadetrabajo.Ubicacion as location FROM Ofertadetrabajo LIMIT %s, %s"
    param = [(page*10)-10, page*10]
    connection = DBConnection()
    list_joboffers = connection.select(query, param)
    job_offer_objects = []
    for job_offer in list_joboffers:
        job_offer_aux = JobOffer()
        job_offer_aux.description = job_offer['description']
        job_offer_aux.job = job_offer['job']
        job_offer_aux.job_category = job_offer['job_category']
        job_offer_aux.job_offer_id = job_offer['job_offer_id']
        job_offer_aux.location = job_offer['location']
        job_offer_objects.append(job_offer_aux)
    if job_offer_objects:
        job_offer_json = []
        for job_offer_object in job_offer_objects:
            job_offer_json.append(JobOffer.to_dict(job_offer_object))
        for elem in job_offer_json:
            elem['jobCategory'] = elem.pop('job_category')
            elem['jobOfferId'] = elem.pop('job_offer_id')
        response = Response(json.dumps(job_offer_json),status=HTTPStatus.CREATED.value,mimetype="application/json")
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
