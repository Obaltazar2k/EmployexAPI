# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Media(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, media_id: str=None, file: str=None):  # noqa: E501
        """Media - a model defined in Swagger

        :param media_id: The media_id of this Media.  # noqa: E501
        :type media_id: str
        :param file: The file of this Media.  # noqa: E501
        :type file: str
        """
        self.swagger_types = {
            'media_id': str,
            'file': str
        }

        self.attribute_map = {
            'media_id': 'media_id',
            'file': 'file'
        }
        self._media_id = media_id
        self._file = file

    @classmethod
    def from_dict(cls, dikt) -> 'Media':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Media of this Media.  # noqa: E501
        :rtype: Media
        """
        return util.deserialize_model(dikt, cls)

    @property
    def media_id(self) -> str:
        """Gets the media_id of this Media.

        Binary data of the media file  # noqa: E501

        :return: The media_id of this Media.
        :rtype: str
        """
        return self._media_id

    @media_id.setter
    def media_id(self, media_id: str):
        """Sets the media_id of this Media.

        Binary data of the media file  # noqa: E501

        :param media_id: The media_id of this Media.
        :type media_id: str
        """

        self._media_id = media_id

    @property
    def file(self) -> str:
        """Gets the file of this Media.

        Binary data of the media file  # noqa: E501

        :return: The file of this Media.
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file: str):
        """Sets the file of this Media.

        Binary data of the media file  # noqa: E501

        :param file: The file of this Media.
        :type file: str
        """

        self._file = file