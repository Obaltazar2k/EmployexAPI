import connexion
import six

from swagger_server.models.education import Education  # noqa: E501
from swagger_server import util


def add_education(body, user_id):  # noqa: E501
    """Adds education info to an independient user

     # noqa: E501

    :param body: Education object that needs to be added to the catalog
    :type body: dict | bytes
    :param user_id: Unique identifier of the user
    :type user_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = Education.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
