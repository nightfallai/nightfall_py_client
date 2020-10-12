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


class ScanResponseV2(object):
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
        'fragment': 'str',
        'detector_name': 'str',
        'confidence': 'Confidence',
        'location': 'ScanResponseLocation'
    }

    attribute_map = {
        'fragment': 'fragment',
        'detector_name': 'detectorName',
        'confidence': 'confidence',
        'location': 'location'
    }

    def __init__(self, fragment=None, detector_name=None, confidence=None, location=None, local_vars_configuration=None):  # noqa: E501
        """ScanResponseV2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._fragment = None
        self._detector_name = None
        self._confidence = None
        self._location = None
        self.discriminator = None

        if fragment is not None:
            self.fragment = fragment
        if detector_name is not None:
            self.detector_name = detector_name
        if confidence is not None:
            self.confidence = confidence
        if location is not None:
            self.location = location

    @property
    def fragment(self):
        """Gets the fragment of this ScanResponseV2.  # noqa: E501

        The text sample that was flagged.  # noqa: E501

        :return: The fragment of this ScanResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._fragment

    @fragment.setter
    def fragment(self, fragment):
        """Sets the fragment of this ScanResponseV2.

        The text sample that was flagged.  # noqa: E501

        :param fragment: The fragment of this ScanResponseV2.  # noqa: E501
        :type: str
        """

        self._fragment = fragment

    @property
    def detector_name(self):
        """Gets the detector_name of this ScanResponseV2.  # noqa: E501

        The data type flagged in the text fragment.  # noqa: E501

        :return: The detector_name of this ScanResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._detector_name

    @detector_name.setter
    def detector_name(self, detector_name):
        """Sets the detector_name of this ScanResponseV2.

        The data type flagged in the text fragment.  # noqa: E501

        :param detector_name: The detector_name of this ScanResponseV2.  # noqa: E501
        :type: str
        """

        self._detector_name = detector_name

    @property
    def confidence(self):
        """Gets the confidence of this ScanResponseV2.  # noqa: E501


        :return: The confidence of this ScanResponseV2.  # noqa: E501
        :rtype: Confidence
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this ScanResponseV2.


        :param confidence: The confidence of this ScanResponseV2.  # noqa: E501
        :type: Confidence
        """

        self._confidence = confidence

    @property
    def location(self):
        """Gets the location of this ScanResponseV2.  # noqa: E501


        :return: The location of this ScanResponseV2.  # noqa: E501
        :rtype: ScanResponseLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this ScanResponseV2.


        :param location: The location of this ScanResponseV2.  # noqa: E501
        :type: ScanResponseLocation
        """

        self._location = location

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
        if not isinstance(other, ScanResponseV2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScanResponseV2):
            return True

        return self.to_dict() != other.to_dict()