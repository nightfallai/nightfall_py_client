# coding: utf-8

"""
    api_platform

    This API exposes detectors for sensitive data in arbitrary string payloads.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class ScanRequestV2(object):
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
        'config': 'ScanRequestV2Config',
        'payload': 'list[str]'
    }

    attribute_map = {
        'config': 'config',
        'payload': 'payload'
    }

    def __init__(self, config=None, payload=None, local_vars_configuration=None):  # noqa: E501
        """ScanRequestV2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._config = None
        self._payload = None
        self.discriminator = None

        if config is not None:
            self.config = config
        if payload is not None:
            self.payload = payload

    @property
    def config(self):
        """Gets the config of this ScanRequestV2.  # noqa: E501


        :return: The config of this ScanRequestV2.  # noqa: E501
        :rtype: ScanRequestV2Config
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this ScanRequestV2.


        :param config: The config of this ScanRequestV2.  # noqa: E501
        :type: ScanRequestV2Config
        """

        self._config = config

    @property
    def payload(self):
        """Gets the payload of this ScanRequestV2.  # noqa: E501

        The text sample(s) you wish to scan. This data is passed as a string list, so you may choose to segment your text into multiple items for better granularity. The aggregate size of your text (summed across all items in the list) must not exceed 500 KB for any individual request, and the number of items in that list may not exceed 50,000.  # noqa: E501

        :return: The payload of this ScanRequestV2.  # noqa: E501
        :rtype: list[str]
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this ScanRequestV2.

        The text sample(s) you wish to scan. This data is passed as a string list, so you may choose to segment your text into multiple items for better granularity. The aggregate size of your text (summed across all items in the list) must not exceed 500 KB for any individual request, and the number of items in that list may not exceed 50,000.  # noqa: E501

        :param payload: The payload of this ScanRequestV2.  # noqa: E501
        :type: list[str]
        """

        self._payload = payload

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
        if not isinstance(other, ScanRequestV2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScanRequestV2):
            return True

        return self.to_dict() != other.to_dict()
