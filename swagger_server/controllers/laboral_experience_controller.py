import connexion
import six

from swagger_server.models.laboral_experience import LaboralExperience  # noqa: E501
from swagger_server import util


def add_laboral_experience(body, user_id):  # noqa: E501
    """Adds laboral experience info to an independient user

     # noqa: E501

    :param body: Laboral experience object that needs to be added to the catalog
    :type body: dict | bytes
    :param user_id: Unique identifier of the user
    :type user_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = LaboralExperience.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
