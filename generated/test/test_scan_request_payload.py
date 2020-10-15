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
from openapi_client.models.scan_request_payload import ScanRequestPayload  # noqa: E501
from openapi_client.rest import ApiException

class TestScanRequestPayload(unittest.TestCase):
    """ScanRequestPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ScanRequestPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.scan_request_payload.ScanRequestPayload()  # noqa: E501
        if include_optional :
            return ScanRequestPayload(
                items = [
                    '0'
                    ]
            )
        else :
            return ScanRequestPayload(
        )

    def testScanRequestPayload(self):
        """Test ScanRequestPayload"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()