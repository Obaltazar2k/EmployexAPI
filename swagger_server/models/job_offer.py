# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.job_category import JobCategory  # noqa: F401,E501
from swagger_server.models.media import Media  # noqa: F401,E501
from swagger_server.models.tag import Tag  # noqa: F401,E501
from swagger_server import util


class JobOffer(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, job_offer_id: str=None, job: str=None, description: str=None, job_category: JobCategory=None, location: str=None, tags: List[Tag]=None, media: List[Media]=None):  # noqa: E501
        """JobOffer - a model defined in Swagger

        :param job_offer_id: The job_offer_id of this JobOffer.  # noqa: E501
        :type job_offer_id: str
        :param job: The job of this JobOffer.  # noqa: E501
        :type job: str
        :param description: The description of this JobOffer.  # noqa: E501
        :type description: str
        :param job_category: The job_category of this JobOffer.  # noqa: E501
        :type job_category: JobCategory
        :param location: The location of this JobOffer.  # noqa: E501
        :type location: str
        :param tags: The tags of this JobOffer.  # noqa: E501
        :type tags: List[Tag]
        :param media: The media of this JobOffer.  # noqa: E501
        :type media: List[Media]
        """
        self.swagger_types = {
            'job_offer_id': str,
            'job': str,
            'description': str,
            'job_category': JobCategory,
            'location': str,
            'tags': List[Tag],
            'media': List[Media]
        }

        self.attribute_map = {
            'job_offer_id': 'job_offer_id',
            'job': 'job',
            'description': 'description',
            'job_category': 'job_category',
            'location': 'location',
            'tags': 'tags',
            'media': 'media'
        }
        self._job_offer_id = job_offer_id
        self._job = job
        self._description = description
        self._job_category = job_category
        self._location = location
        self._tags = tags
        self._media = media

    @classmethod
    def from_dict(cls, dikt) -> 'JobOffer':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The JobOffer of this JobOffer.  # noqa: E501
        :rtype: JobOffer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def job_offer_id(self) -> str:
        """Gets the job_offer_id of this JobOffer.

        Unique identifier of the job offer  # noqa: E501

        :return: The job_offer_id of this JobOffer.
        :rtype: str
        """
        return self._job_offer_id

    @job_offer_id.setter
    def job_offer_id(self, job_offer_id: str):
        """Sets the job_offer_id of this JobOffer.

        Unique identifier of the job offer  # noqa: E501

        :param job_offer_id: The job_offer_id of this JobOffer.
        :type job_offer_id: str
        """

        self._job_offer_id = job_offer_id

    @property
    def job(self) -> str:
        """Gets the job of this JobOffer.

        Title of the job  # noqa: E501

        :return: The job of this JobOffer.
        :rtype: str
        """
        return self._job

    @job.setter
    def job(self, job: str):
        """Sets the job of this JobOffer.

        Title of the job  # noqa: E501

        :param job: The job of this JobOffer.
        :type job: str
        """
        if job is None:
            raise ValueError("Invalid value for `job`, must not be `None`")  # noqa: E501

        self._job = job

    @property
    def description(self) -> str:
        """Gets the description of this JobOffer.

        Talk about what the job offer is about  # noqa: E501

        :return: The description of this JobOffer.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this JobOffer.

        Talk about what the job offer is about  # noqa: E501

        :param description: The description of this JobOffer.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def job_category(self) -> JobCategory:
        """Gets the job_category of this JobOffer.


        :return: The job_category of this JobOffer.
        :rtype: JobCategory
        """
        return self._job_category

    @job_category.setter
    def job_category(self, job_category: JobCategory):
        """Sets the job_category of this JobOffer.


        :param job_category: The job_category of this JobOffer.
        :type job_category: JobCategory
        """

        self._job_category = job_category

    @property
    def location(self) -> str:
        """Gets the location of this JobOffer.

        Location where the job offer is  # noqa: E501

        :return: The location of this JobOffer.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location: str):
        """Sets the location of this JobOffer.

        Location where the job offer is  # noqa: E501

        :param location: The location of this JobOffer.
        :type location: str
        """

        self._location = location

    @property
    def tags(self) -> List[Tag]:
        """Gets the tags of this JobOffer.

        Differents tags associated to the job offer  # noqa: E501

        :return: The tags of this JobOffer.
        :rtype: List[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags: List[Tag]):
        """Sets the tags of this JobOffer.

        Differents tags associated to the job offer  # noqa: E501

        :param tags: The tags of this JobOffer.
        :type tags: List[Tag]
        """

        self._tags = tags

    @property
    def media(self) -> List[Media]:
        """Gets the media of this JobOffer.

        Multimedia data related to the job offer  # noqa: E501

        :return: The media of this JobOffer.
        :rtype: List[Media]
        """
        return self._media

    @media.setter
    def media(self, media: List[Media]):
        """Sets the media of this JobOffer.

        Multimedia data related to the job offer  # noqa: E501

        :param media: The media of this JobOffer.
        :type media: List[Media]
        """

        self._media = media