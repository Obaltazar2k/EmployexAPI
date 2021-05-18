# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.independient_user import IndependientUser  # noqa: E501
from swagger_server.models.organization_user import OrganizationUser  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOrganizationUserController(BaseTestCase):
    """OrganizationUserController integration test stubs"""

    def test_get_organization_user_by_id(self):
        """Test case for get_organization_user_by_id

        Get user by user id
        """
        response = self.client.open(
            '/ricardorzan/Employex/1.0.0/users/organization_user/{userId}'.format(user_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_register_organization_user(self):
        """Test case for register_organization_user

        Register organization user
        """
        body = OrganizationUser()
        response = self.client.open(
            '/ricardorzan/Employex/1.0.0/users/organization_user',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
