import connexion
import six

from swagger_server.models.section import Section  # noqa: E501
from swagger_server import util


def add_section(body, user_id):  # noqa: E501
    """Adds section info to an independient user

     # noqa: E501

    :param body: Section object that needs to be added to the catalog
    :type body: dict | bytes
    :param user_id: Unique identifier of the user
    :type user_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Section.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
