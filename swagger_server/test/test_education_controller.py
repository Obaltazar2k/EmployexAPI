# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.education import Education  # noqa: E501
from swagger_server.test import BaseTestCase


class TestEducationController(BaseTestCase):
    """EducationController integration test stubs"""

    def test_add_education(self):
        """Test case for add_education

        Adds education info to an independient user
        """
        body = Education()
        response = self.client.open(
            '/ricardorzan/Employex/1.0.0/users/independient_user/{userId}/education'.format(user_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
