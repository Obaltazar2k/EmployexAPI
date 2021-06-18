from typing import final
import connexion
import six

from swagger_server.models.aplication import Aplication  # noqa: E501
from swagger_server import util
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from flask import Response
from http import HTTPStatus
from swagger_server.data.db import Aplicacion, Ofertadetrabajo, database, Usuario
from datetime import date
from peewee import DoesNotExist


@jwt_required()
def add_aplication_to_job_offer(user_id, job_offer_id):  # noqa: E501
    """Adds an aplication to a specified job offer

    Adds an aplication to a specified job offer # noqa: E501

    :param user_id: Unique identifier of the user
    :type user_id: string
    :param job_offer_id: Unique identifier of the job offer
    :type job_offer_id: int

    :rtype: None
    """

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
