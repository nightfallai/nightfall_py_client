# coding: utf-8

"""
    Methods

    This API exposes detectors for sensitive data in arbitrary string payloads.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.scan_v1_api import ScanV1Api  # noqa: E501
from openapi_client.rest import ApiException


class TestScanV1Api(unittest.TestCase):
    """ScanV1Api unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.scan_v1_api.ScanV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_scan_payload_v1(self):
        """Test case for scan_payload_v1

        Scan for sensitive information in your data  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()