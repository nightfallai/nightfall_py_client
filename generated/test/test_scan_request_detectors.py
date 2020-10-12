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
from openapi_client.models.scan_request_detectors import ScanRequestDetectors  # noqa: E501
from openapi_client.rest import ApiException

class TestScanRequestDetectors(unittest.TestCase):
    """ScanRequestDetectors unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ScanRequestDetectors
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.scan_request_detectors.ScanRequestDetectors()  # noqa: E501
        if include_optional :
            return ScanRequestDetectors(
                name = 'API_KEY'
            )
        else :
            return ScanRequestDetectors(
        )

    def testScanRequestDetectors(self):
        """Test ScanRequestDetectors"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()