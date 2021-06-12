import json
from typing import final
import connexion
import six

from swagger_server.models.job_offer import JobOffer  # noqa: E501
from swagger_server.models.media import Media as MediaModels
from swagger_server import util
from flask import Response
from swagger_server.data.DBConnection import DBConnection
from http import HTTPStatus
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from swagger_server.data.db import Independiente, Ofertadetrabajo, Usuario, database, Media, Aplicacion
from peewee import DoesNotExist
from datetime import date

@jwt_required()
def add_aplication_to_job_offer(user_id, job_offer_id):  # noqa: E501
    """Adds an aplication to a specified job offer

    Adds an aplication to a specified job offer # noqa: E501

    :param user_id: Unique identifier of the user
    :type user_id: int
    :param job_offer_id: Unique identifier of the job offer
    :type job_offer_id: int

    :rtype: None
    """
    current_user = get_jwt_identity()
    if current_user == user_id:
        response = Response(status=HTTPStatus.NOT_ACCEPTABLE.value)
    else:
        response = Response(status=HTTPStatus.NOT_FOUND.value)
        database.connect()
        aplication = None
        try:
            aplication = Aplicacion.select().where(
                Aplicacion.independiente == Independiente.get(Independiente.usuariocorreo == current_user)).where(
                Aplicacion.ofertadetrabajo == Ofertadetrabajo.get_by_id(job_offer_id)).get()
            response = Response(status=HTTPStatus.CONFLICT.value)
            print(aplication)
            return response
        except DoesNotExist:
            response = Response(status=HTTPStatus.NOT_FOUND.value)
        try:
            if aplication:
                response = response(status=HTTPStatus.CONFLICT.value)
            else:
                aplication = Aplicacion.create(
                    aprobado = False,
                    fecha = date.today().strftime("%y-%m-%d"),
                    independiente = Independiente.get(Independiente.usuariocorreo == current_user),
                    ofertadetrabajo = Ofertadetrabajo.get_by_id(job_offer_id)
                )
                response = Response(status=HTTPStatus.CREATED.value)
        except DoesNotExist:
            response = Response(status=HTTPStatus.NOT_FOUND.value)      
        finally:
            database.close()
    return response

@jwt_required()
def add_job_offer(body):  # noqa: E501
    """Add a new job offer to the catalog

     # noqa: E501

    :param body: Job offer object that needs to be added to the catalog
    :type body: dict | bytes

    :rtype: None
    """
    current_user = get_jwt_identity()
    response = Response(status=HTTPStatus.NOT_FOUND.value)
    if connexion.request.is_json:
        body = JobOffer.from_dict(connexion.request.get_json())  # noqa: E501
    database.connect()
    job_offer = Ofertadetrabajo.create(
        descripcion=body.description,
        cargo = body.job,
        tipoempleo=body.job_category,
        ubicacion=body.location,
        Usuariocorreo=current_user)
    for media in body.media:
        Media.create(
            file=media.file,
            ofertadetrabajo=job_offer)
    database.close()
    if job_offer:
        response = Response(status=HTTPStatus.CREATED.value)
    return response

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
        job_offer_objects = []  
        for job_offer in list_joboffers:
            job_offer_aux = JobOffer()
            job_offer_aux.description = job_offer.descripcion
            job_offer_aux.job = job_offer.cargo
            job_offer_aux.job_category = job_offer.tipoempleo
            job_offer_aux.job_offer_id = job_offer.ofertadetrabajo_id
            job_offer_aux.location = job_offer.ubicacion
            job_offer_aux.username = str(job_offer.usuariocorreo)
            list_media = Media.select().where(Media.ofertadetrabajo == job_offer)
            media_list = []
            for media in list_media:
                media_aux = MediaModels()
                media_aux.media_id = media.media_id
                media_aux.file = media.file
                media_list.append(media_aux)
            job_offer_aux.media = media_list
            job_offer_objects.append(job_offer_aux)
    except DoesNotExist:
        response = Response(status=HTTPStatus.NOT_FOUND.value)
    finally:
        database.close()
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

@jwt_required()
def get_job_offers_published_by_the_user(user_id):  # noqa: E501
    """Returns a list of job offers published by the user

    A list of the job offers published by the user # noqa: E501

    :param user_id: Unique identifier of the user
    :type user_id: int

    :rtype: List[JobOffer]
    """
    current_user = get_jwt_identity()
    response = Response(status=HTTPStatus.NOT_FOUND.value)
    database.connect()
    try:
        list_joboffers = Ofertadetrabajo.select().where(Ofertadetrabajo.usuariocorreo == current_user)
        job_offer_objects = []  
        for job_offer in list_joboffers:
            job_offer_aux = JobOffer()
            job_offer_aux.description = job_offer.descripcion
            job_offer_aux.job = job_offer.cargo
            job_offer_aux.job_category = job_offer.tipoempleo
            job_offer_aux.job_offer_id = job_offer.ofertadetrabajo_id
            job_offer_aux.location = job_offer.ubicacion
            job_offer_aux.username = str(job_offer.usuariocorreo)
            list_media = Media.select().where(Media.ofertadetrabajo == job_offer)
            media_list = []
            for media in list_media:
                media_aux = MediaModels()
                media_aux.media_id = media.media_id
                media_aux.file = media.file
                media_list.append(media_aux)
            job_offer_aux.media = media_list
            job_offer_objects.append(job_offer_aux)
    except DoesNotExist:
        response = Response(status=HTTPStatus.NOT_FOUND.value)
    finally:
        database.close()
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
