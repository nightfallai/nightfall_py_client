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


class ContextRule(object):
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
        'regex': 'Regex',
        'proximity': 'ContextRuleProximity',
        'confidence_adjustment': 'ContextRuleConfidenceAdjustment'
    }

    attribute_map = {
        'regex': 'regex',
        'proximity': 'proximity',
        'confidence_adjustment': 'confidenceAdjustment'
    }

    def __init__(self, regex=None, proximity=None, confidence_adjustment=None, local_vars_configuration=None):  # noqa: E501
        """ContextRule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._regex = None
        self._proximity = None
        self._confidence_adjustment = None
        self.discriminator = None

        if regex is not None:
            self.regex = regex
        if proximity is not None:
            self.proximity = proximity
        if confidence_adjustment is not None:
            self.confidence_adjustment = confidence_adjustment

    @property
    def regex(self):
        """Gets the regex of this ContextRule.  # noqa: E501


        :return: The regex of this ContextRule.  # noqa: E501
        :rtype: Regex
        """
        return self._regex

    @regex.setter
    def regex(self, regex):
        """Sets the regex of this ContextRule.


        :param regex: The regex of this ContextRule.  # noqa: E501
        :type: Regex
        """

        self._regex = regex

    @property
    def proximity(self):
        """Gets the proximity of this ContextRule.  # noqa: E501


        :return: The proximity of this ContextRule.  # noqa: E501
        :rtype: ContextRuleProximity
        """
        return self._proximity

    @proximity.setter
    def proximity(self, proximity):
        """Sets the proximity of this ContextRule.


        :param proximity: The proximity of this ContextRule.  # noqa: E501
        :type: ContextRuleProximity
        """

        self._proximity = proximity

    @property
    def confidence_adjustment(self):
        """Gets the confidence_adjustment of this ContextRule.  # noqa: E501


        :return: The confidence_adjustment of this ContextRule.  # noqa: E501
        :rtype: ContextRuleConfidenceAdjustment
        """
        return self._confidence_adjustment

    @confidence_adjustment.setter
    def confidence_adjustment(self, confidence_adjustment):
        """Sets the confidence_adjustment of this ContextRule.


        :param confidence_adjustment: The confidence_adjustment of this ContextRule.  # noqa: E501
        :type: ContextRuleConfidenceAdjustment
        """

        self._confidence_adjustment = confidence_adjustment

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
        if not isinstance(other, ContextRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContextRule):
            return True

        return self.to_dict() != other.to_dict()
