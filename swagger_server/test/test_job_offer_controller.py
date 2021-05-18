# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.aplication import Aplication  # noqa: E501
from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.job_offer import JobOffer  # noqa: E501
from swagger_server.test import BaseTestCase


class TestJobOfferController(BaseTestCase):
    """JobOfferController integration test stubs"""

    def test_add_aplication_to_job_offer(self):
        """Test case for add_aplication_to_job_offer

        Adds an aplication to a specified job offer
        """
        body = Body()
        response = self.client.open(
            '/ricardorzan/Employex/1.0.0/users/{userId}/job_offers/{jobOfferId}/aplications'.format(user_id=56, job_offer_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_job_offer(self):
        """Test case for add_job_offer

        Add a new job offer to the catalog
        """
        body = JobOffer()
        response = self.client.open(
            '/ricardorzan/Employex/1.0.0/job_offers',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_job_offers(self):
        """Test case for get_job_offers

        Returns a list of job offers
        """
        query_string = [('page', 56)]
        response = self.client.open(
            '/ricardorzan/Employex/1.0.0/job_offers',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_job_offers_aplications(self):
        """Test case for get_job_offers_aplications

        Returns a list of aplications in a specified job offer published by the user
        """
        response = self.client.open(
            '/ricardorzan/Employex/1.0.0/users/{userId}/job_offer/{jobOfferId}/aplications'.format(user_id=56, job_offer_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_job_offers_published_by_the_user(self):
        """Test case for get_job_offers_published_by_the_user

        Returns a list of job offers published by the user
        """
        response = self.client.open(
            '/ricardorzan/Employex/1.0.0/users/{userId}/job_offer'.format(user_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
