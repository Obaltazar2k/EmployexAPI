# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.sector import Sector  # noqa: F401,E501
from swagger_server.models.user import User  # noqa: F401,E501
from swagger_server import util


class OrganizationUser(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, about: str=None, zip_code: int=None, contact_name: str=None, contact_phone: str=None, contact_email: str=None, web_site: str=None, work_sector: Sector=None, user: User=None):  # noqa: E501
        """OrganizationUser - a model defined in Swagger

        :param name: The name of this OrganizationUser.  # noqa: E501
        :type name: str
        :param about: The about of this OrganizationUser.  # noqa: E501
        :type about: str
        :param zip_code: The zip_code of this OrganizationUser.  # noqa: E501
        :type zip_code: int
        :param contact_name: The contact_name of this OrganizationUser.  # noqa: E501
        :type contact_name: str
        :param contact_phone: The contact_phone of this OrganizationUser.  # noqa: E501
        :type contact_phone: str
        :param contact_email: The contact_email of this OrganizationUser.  # noqa: E501
        :type contact_email: str
        :param web_site: The web_site of this OrganizationUser.  # noqa: E501
        :type web_site: str
        :param work_sector: The work_sector of this OrganizationUser.  # noqa: E501
        :type work_sector: Sector
        :param user: The user of this OrganizationUser.  # noqa: E501
        :type user: User
        """
        self.swagger_types = {
            'name': str,
            'about': str,
            'zip_code': int,
            'contact_name': str,
            'contact_phone': str,
            'contact_email': str,
            'web_site': str,
            'work_sector': Sector,
            'user': User
        }

        self.attribute_map = {
            'name': 'name',
            'about': 'about',
            'zip_code': 'zip_code',
            'contact_name': 'contact_name',
            'contact_phone': 'contact_phone',
            'contact_email': 'contact_email',
            'web_site': 'web_site',
            'work_sector': 'work_sector',
            'user': 'user'
        }
        self._name = name
        self._about = about
        self._zip_code = zip_code
        self._contact_name = contact_name
        self._contact_phone = contact_phone
        self._contact_email = contact_email
        self._web_site = web_site
        self._work_sector = work_sector
        self._user = user

    @classmethod
    def from_dict(cls, dikt) -> 'OrganizationUser':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OrganizationUser of this OrganizationUser.  # noqa: E501
        :rtype: OrganizationUser
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this OrganizationUser.

        Organization's name  # noqa: E501

        :return: The name of this OrganizationUser.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this OrganizationUser.

        Organization's name  # noqa: E501

        :param name: The name of this OrganizationUser.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def about(self) -> str:
        """Gets the about of this OrganizationUser.

        Organization overview  # noqa: E501

        :return: The about of this OrganizationUser.
        :rtype: str
        """
        return self._about

    @about.setter
    def about(self, about: str):
        """Sets the about of this OrganizationUser.

        Organization overview  # noqa: E501

        :param about: The about of this OrganizationUser.
        :type about: str
        """

        self._about = about

    @property
    def zip_code(self) -> int:
        """Gets the zip_code of this OrganizationUser.

        Zip code where the organization is located  # noqa: E501

        :return: The zip_code of this OrganizationUser.
        :rtype: int
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code: int):
        """Sets the zip_code of this OrganizationUser.

        Zip code where the organization is located  # noqa: E501

        :param zip_code: The zip_code of this OrganizationUser.
        :type zip_code: int
        """

        self._zip_code = zip_code

    @property
    def contact_name(self) -> str:
        """Gets the contact_name of this OrganizationUser.

        Contact person's name  # noqa: E501

        :return: The contact_name of this OrganizationUser.
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name: str):
        """Sets the contact_name of this OrganizationUser.

        Contact person's name  # noqa: E501

        :param contact_name: The contact_name of this OrganizationUser.
        :type contact_name: str
        """

        self._contact_name = contact_name

    @property
    def contact_phone(self) -> str:
        """Gets the contact_phone of this OrganizationUser.

        Contact person's phone  # noqa: E501

        :return: The contact_phone of this OrganizationUser.
        :rtype: str
        """
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, contact_phone: str):
        """Sets the contact_phone of this OrganizationUser.

        Contact person's phone  # noqa: E501

        :param contact_phone: The contact_phone of this OrganizationUser.
        :type contact_phone: str
        """

        self._contact_phone = contact_phone

    @property
    def contact_email(self) -> str:
        """Gets the contact_email of this OrganizationUser.

        Contact person's email  # noqa: E501

        :return: The contact_email of this OrganizationUser.
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email: str):
        """Sets the contact_email of this OrganizationUser.

        Contact person's email  # noqa: E501

        :param contact_email: The contact_email of this OrganizationUser.
        :type contact_email: str
        """
        if contact_email is None:
            raise ValueError("Invalid value for `contact_email`, must not be `None`")  # noqa: E501

        self._contact_email = contact_email

    @property
    def web_site(self) -> str:
        """Gets the web_site of this OrganizationUser.

        Organization's web site  # noqa: E501

        :return: The web_site of this OrganizationUser.
        :rtype: str
        """
        return self._web_site

    @web_site.setter
    def web_site(self, web_site: str):
        """Sets the web_site of this OrganizationUser.

        Organization's web site  # noqa: E501

        :param web_site: The web_site of this OrganizationUser.
        :type web_site: str
        """

        self._web_site = web_site

    @property
    def work_sector(self) -> Sector:
        """Gets the work_sector of this OrganizationUser.


        :return: The work_sector of this OrganizationUser.
        :rtype: Sector
        """
        return self._work_sector

    @work_sector.setter
    def work_sector(self, work_sector: Sector):
        """Sets the work_sector of this OrganizationUser.


        :param work_sector: The work_sector of this OrganizationUser.
        :type work_sector: Sector
        """

        self._work_sector = work_sector

    @property
    def user(self) -> User:
        """Gets the user of this OrganizationUser.


        :return: The user of this OrganizationUser.
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user: User):
        """Sets the user of this OrganizationUser.


        :param user: The user of this OrganizationUser.
        :type user: User
        """

        self._user = user
