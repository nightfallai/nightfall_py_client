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


class ContextRuleConfidenceAdjustment(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'fixed_confidence': 'Confidence'
    }

    attribute_map = {
        'fixed_confidence': 'fixedConfidence'
    }

    def __init__(self, fixed_confidence=None, local_vars_configuration=None):  # noqa: E501
        """ContextRuleConfidenceAdjustment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._fixed_confidence = None
        self.discriminator = None

        if fixed_confidence is not None:
            self.fixed_confidence = fixed_confidence

    @property
    def fixed_confidence(self):
        """Gets the fixed_confidence of this ContextRuleConfidenceAdjustment.  # noqa: E501


        :return: The fixed_confidence of this ContextRuleConfidenceAdjustment.  # noqa: E501
        :rtype: Confidence
        """
        return self._fixed_confidence

    @fixed_confidence.setter
    def fixed_confidence(self, fixed_confidence):
        """Sets the fixed_confidence of this ContextRuleConfidenceAdjustment.


        :param fixed_confidence: The fixed_confidence of this ContextRuleConfidenceAdjustment.  # noqa: E501
        :type: Confidence
        """

        self._fixed_confidence = fixed_confidence

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
        if not isinstance(other, ContextRuleConfidenceAdjustment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContextRuleConfidenceAdjustment):
            return True

        return self.to_dict() != other.to_dict()
