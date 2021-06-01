import connexion
import six

from swagger_server.models.certification import Certification  # noqa: E501
from swagger_server import util


def add_certification(body, user_id):  # noqa: E501
    """Adds certification info to an independient user

     # noqa: E501

    :param body: Certification object that needs to be added to the catalog
    :type body: dict | bytes
    :param user_id: Unique identifier of the user
    :type user_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Certification.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
