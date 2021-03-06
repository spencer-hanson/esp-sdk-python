# coding: utf-8

"""
    ESP Documentation

    The Evident Security Platform API (version 2.0) is designed to allow users granular control over their Amazon Web Service security experience by allowing them to review alerts, monitor signatures, and create custom signatures.

    OpenAPI spec version: v2_sdk
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
from ..extensions.base_object import BaseObject
import re


class IntegrationSlack(BaseObject):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, url=None, created_at=None, updated_at=None, integration=None, integration_id=None):
        """
        IntegrationSlack - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'url': 'str',
            'created_at': 'datetime',
            'updated_at': 'datetime',
            'integration': 'Integration',
            'integration_id': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'url': 'url',
            'created_at': 'created_at',
            'updated_at': 'updated_at',
            'integration': 'integration',
            'integration_id': 'integration_id'
        }

        self._id = id
        self._url = url
        self._created_at = created_at
        self._updated_at = updated_at
        self._integration = integration
        self._integration_id = integration_id

    @property
    def id(self):
        """
        Gets the id of this IntegrationSlack.
        Unique ID

        :return: The id of this IntegrationSlack.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this IntegrationSlack.
        Unique ID

        :param id: The id of this IntegrationSlack.
        :type: int
        """

        self._id = id

    @property
    def url(self):
        """
        Gets the url of this IntegrationSlack.
        The URL for the Slack integration

        :return: The url of this IntegrationSlack.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this IntegrationSlack.
        The URL for the Slack integration

        :param url: The url of this IntegrationSlack.
        :type: str
        """

        self._url = url

    @property
    def created_at(self):
        """
        Gets the created_at of this IntegrationSlack.
        ISO 8601 timestamp when the resource was created

        :return: The created_at of this IntegrationSlack.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this IntegrationSlack.
        ISO 8601 timestamp when the resource was created

        :param created_at: The created_at of this IntegrationSlack.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this IntegrationSlack.
        ISO 8601 timestamp when the resource was updated

        :return: The updated_at of this IntegrationSlack.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this IntegrationSlack.
        ISO 8601 timestamp when the resource was updated

        :param updated_at: The updated_at of this IntegrationSlack.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def integration(self):
        """
        Gets the integration of this IntegrationSlack.
        Associated Integration

        :return: The integration of this IntegrationSlack.
        :rtype: Integration
        """
        return self._integration

    @integration.setter
    def integration(self, integration):
        """
        Sets the integration of this IntegrationSlack.
        Associated Integration

        :param integration: The integration of this IntegrationSlack.
        :type: Integration
        """

        self._integration = integration

    @property
    def integration_id(self):
        """
        Gets the integration_id of this IntegrationSlack.
        Associated Integration ID

        :return: The integration_id of this IntegrationSlack.
        :rtype: int
        """
        return self._integration_id

    @integration_id.setter
    def integration_id(self, integration_id):
        """
        Sets the integration_id of this IntegrationSlack.
        Associated Integration ID

        :param integration_id: The integration_id of this IntegrationSlack.
        :type: int
        """

        self._integration_id = integration_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, IntegrationSlack):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
