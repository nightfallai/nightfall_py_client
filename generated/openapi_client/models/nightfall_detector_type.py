# coding: utf-8

"""
    Methods

    This API exposes detectors for sensitive data in arbitrary string payloads.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class NightfallDetectorType(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    API_KEY = "API_KEY"
    RANDOMLY_GENERATED_TOKEN = "RANDOMLY_GENERATED_TOKEN"
    CRYPTOGRAPHIC_KEY = "CRYPTOGRAPHIC_KEY"
    CREDIT_CARD_NUMBER = "CREDIT_CARD_NUMBER"
    US_SOCIAL_SECURITY_NUMBER = "US_SOCIAL_SECURITY_NUMBER"
    AMERICAN_BANKERS_CUSIP_ID = "AMERICAN_BANKERS_CUSIP_ID"
    US_BANK_ROUTING_MICR = "US_BANK_ROUTING_MICR"
    ICD9_CODE = "ICD9_CODE"
    ICD10_CODE = "ICD10_CODE"
    US_DRIVERS_LICENSE_NUMBER = "US_DRIVERS_LICENSE_NUMBER"
    US_PASSPORT = "US_PASSPORT"
    PHONE_NUMBER = "PHONE_NUMBER"
    IP_ADDRESS = "IP_ADDRESS"
    EMAIL_ADDRESS = "EMAIL_ADDRESS"

    allowable_values = [API_KEY, RANDOMLY_GENERATED_TOKEN, CRYPTOGRAPHIC_KEY, CREDIT_CARD_NUMBER, US_SOCIAL_SECURITY_NUMBER, AMERICAN_BANKERS_CUSIP_ID, US_BANK_ROUTING_MICR, ICD9_CODE, ICD10_CODE, US_DRIVERS_LICENSE_NUMBER, US_PASSPORT, PHONE_NUMBER, IP_ADDRESS, EMAIL_ADDRESS]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """NightfallDetectorType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NightfallDetectorType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NightfallDetectorType):
            return True

        return self.to_dict() != other.to_dict()
