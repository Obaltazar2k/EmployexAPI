import connexion
import six

from swagger_server.models.aplication import Aplication  # noqa: E501
from swagger_server.models.body import Body  # noqa: E501
from swagger_server import util


def add_aplication_to_job_offer(user_id, job_offer_id, body=None):  # noqa: E501
    """Adds an aplication to a specified job offer

    Adds an aplication to a specified job offer # noqa: E501

    :param user_id: 
    :type user_id: int
    :param job_offer_id: 
    :type job_offer_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_job_offers_aplications(user_id, job_offer_id):  # noqa: E501
    """Returns a list of aplications in a specified job offer published by the user

    A list of aplications in the job offer specified published by the user # noqa: E501

    :param user_id: 
    :type user_id: int
    :param job_offer_id: 
    :type job_offer_id: int

    :rtype: List[Aplication]
    """
    return 'do some magic!'
