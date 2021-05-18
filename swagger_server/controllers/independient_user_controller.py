import connexion
import six

from swagger_server.models.independient_user import IndependientUser  # noqa: E501
from swagger_server import util


def get_independint_user_by_id(user_id):  # noqa: E501
    """Get user by user id

     # noqa: E501

    :param user_id: Unique identifier of the user
    :type user_id: int

    :rtype: IndependientUser
    """
    return 'do some magic!'


def register_indpendient_user(body):  # noqa: E501
    """Register independient user

     # noqa: E501

    :param body: Independient user object to register
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = IndependientUser.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
