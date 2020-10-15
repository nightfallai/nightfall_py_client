# coding: utf-8

"""
    Methods

    This API exposes detectors for sensitive data in arbitrary string payloads.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.confidence import Confidence  # noqa: E501
from openapi_client.rest import ApiException

class TestConfidence(unittest.TestCase):
    """Confidence unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Confidence
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.confidence.Confidence()  # noqa: E501
        if include_optional :
            return Confidence(
            )
        else :
            return Confidence(
        )

    def testConfidence(self):
        """Test Confidence"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
