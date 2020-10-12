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
from openapi_client.models.scan_request_v2_config import ScanRequestV2Config  # noqa: E501
from openapi_client.rest import ApiException

class TestScanRequestV2Config(unittest.TestCase):
    """ScanRequestV2Config unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ScanRequestV2Config
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.scan_request_v2_config.ScanRequestV2Config()  # noqa: E501
        if include_optional :
            return ScanRequestV2Config(
                condition_set_uuid = '0', 
                condition_set = openapi_client.models.scan_request_v2_config_condition_set.ScanRequestV2_config_conditionSet(
                    conditions = [
                        openapi_client.models.condition.Condition(
                            min_num_findings = 56, 
                            min_confidence = 'VERY_UNLIKELY', 
                            detector = openapi_client.models.detector.Detector(
                                display_name = '0', 
                                detector_type = 'NIGHTFALL_DETECTOR', 
                                nightfall_detector = 'API_KEY', 
                                regex = openapi_client.models.regex.Regex(
                                    pattern = '0', 
                                    is_case_sensitive = True, ), 
                                word_list = openapi_client.models.word_list.WordList(
                                    values = [
                                        '0'
                                        ], 
                                    is_case_sensitive = True, ), 
                                context_rules = [
                                    openapi_client.models.context_rule.ContextRule(
                                        proximity = openapi_client.models.context_rule_proximity.ContextRule_proximity(
                                            window_before = 56, 
                                            window_after = 56, ), 
                                        confidence_adjustment = openapi_client.models.context_rule_confidence_adjustment.ContextRule_confidenceAdjustment(
                                            fixed_confidence = 'VERY_UNLIKELY', ), )
                                    ], 
                                exclusion_rules = [
                                    openapi_client.models.exclusion_rule.ExclusionRule(
                                        match_type = 'PARTIAL', 
                                        exclusion_type = 'REGEX', )
                                    ], ), )
                        ], )
            )
        else :
            return ScanRequestV2Config(
        )

    def testScanRequestV2Config(self):
        """Test ScanRequestV2Config"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()