# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.independient_user import IndependientUser  # noqa: E501
from swagger_server.test import BaseTestCase


class TestIndependientUserController(BaseTestCase):
    """IndependientUserController integration test stubs"""

    def test_get_independint_user_by_id(self):
        """Test case for get_independint_user_by_id

        Get user by user id
        """
        response = self.client.open(
            '/ricardorzan/Employex/1.0.0/users/independient_user/{userId}'.format(user_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_register_indpendient_user(self):
        """Test case for register_indpendient_user

        Register independient user
        """
        body = IndependientUser()
        response = self.client.open(
            '/ricardorzan/Employex/1.0.0/users/independient_user',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
