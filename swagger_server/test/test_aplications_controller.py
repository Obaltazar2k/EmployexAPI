# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.aplication import Aplication  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAplicationsController(BaseTestCase):
    """AplicationsController integration test stubs"""

    def test_add_aplication_to_job_offer(self):
        """Test case for add_aplication_to_job_offer

        Adds an aplication to a specified job offer
        """
        response = self.client.open(
            '/ricardorzan/Employex/1.0.0/users/{user_id}/job_offers/{job_offer_id}/aplications'.format(user_id=56, job_offer_id=56),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_job_offers_aplications(self):
        """Test case for get_job_offers_aplications

        Returns a list of aplications in a specified job offer published by the user
        """
        response = self.client.open(
            '/ricardorzan/Employex/1.0.0/users/{user_id}/job_offer/{job_offer_id}/aplications'.format(user_id=56, job_offer_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
