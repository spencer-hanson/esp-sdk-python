# coding: utf-8

"""
    ESP Documentation

    The Evident Security Platform API (version 2.0) is designed to allow users granular control over their Amazon Web Service security experience by allowing them to review alerts, monitor signatures, and create custom signatures.

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
from ..extensions.base_object import BaseObject
import re


class ExternalAccountAttributes(BaseObject):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, account=None, arn=None, created_at=None, external_id=None, name=None, updated_at=None, cloudtrail_name=None):
        """
        ExternalAccountAttributes - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'account': 'str',
            'arn': 'str',
            'created_at': 'str',
            'external_id': 'str',
            'name': 'str',
            'updated_at': 'str',
            'cloudtrail_name': 'str'
        }

        self.attribute_map = {
            'account': 'account',
            'arn': 'arn',
            'created_at': 'created_at',
            'external_id': 'external_id',
            'name': 'name',
            'updated_at': 'updated_at',
            'cloudtrail_name': 'cloudtrail_name'
        }

        self._account = account
        self._arn = arn
        self._created_at = created_at
        self._external_id = external_id
        self._name = name
        self._updated_at = updated_at
        self._cloudtrail_name = cloudtrail_name

    @property
    def account(self):
        """
        Gets the account of this ExternalAccountAttributes.
        The name of the account created

        :return: The account of this ExternalAccountAttributes.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this ExternalAccountAttributes.
        The name of the account created

        :param account: The account of this ExternalAccountAttributes.
        :type: str
        """
        if account is None:
            raise ValueError("Invalid value for `account`, must not be `None`")

        self._account = account

    @property
    def arn(self):
        """
        Gets the arn of this ExternalAccountAttributes.
        Amazon Resource Name for the IAM role

        :return: The arn of this ExternalAccountAttributes.
        :rtype: str
        """
        return self._arn

    @arn.setter
    def arn(self, arn):
        """
        Sets the arn of this ExternalAccountAttributes.
        Amazon Resource Name for the IAM role

        :param arn: The arn of this ExternalAccountAttributes.
        :type: str
        """
        if arn is None:
            raise ValueError("Invalid value for `arn`, must not be `None`")

        self._arn = arn

    @property
    def created_at(self):
        """
        Gets the created_at of this ExternalAccountAttributes.
        Created At

        :return: The created_at of this ExternalAccountAttributes.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this ExternalAccountAttributes.
        Created At

        :param created_at: The created_at of this ExternalAccountAttributes.
        :type: str
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")

        self._created_at = created_at

    @property
    def external_id(self):
        """
        Gets the external_id of this ExternalAccountAttributes.
        External Identifier set on the role

        :return: The external_id of this ExternalAccountAttributes.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this ExternalAccountAttributes.
        External Identifier set on the role

        :param external_id: The external_id of this ExternalAccountAttributes.
        :type: str
        """
        if external_id is None:
            raise ValueError("Invalid value for `external_id`, must not be `None`")

        self._external_id = external_id

    @property
    def name(self):
        """
        Gets the name of this ExternalAccountAttributes.
        Name

        :return: The name of this ExternalAccountAttributes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ExternalAccountAttributes.
        Name

        :param name: The name of this ExternalAccountAttributes.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def updated_at(self):
        """
        Gets the updated_at of this ExternalAccountAttributes.
        Updated At

        :return: The updated_at of this ExternalAccountAttributes.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this ExternalAccountAttributes.
        Updated At

        :param updated_at: The updated_at of this ExternalAccountAttributes.
        :type: str
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")

        self._updated_at = updated_at

    @property
    def cloudtrail_name(self):
        """
        Gets the cloudtrail_name of this ExternalAccountAttributes.
        Cloudtrail Name

        :return: The cloudtrail_name of this ExternalAccountAttributes.
        :rtype: str
        """
        return self._cloudtrail_name

    @cloudtrail_name.setter
    def cloudtrail_name(self, cloudtrail_name):
        """
        Sets the cloudtrail_name of this ExternalAccountAttributes.
        Cloudtrail Name

        :param cloudtrail_name: The cloudtrail_name of this ExternalAccountAttributes.
        :type: str
        """
        if cloudtrail_name is None:
            raise ValueError("Invalid value for `cloudtrail_name`, must not be `None`")

        self._cloudtrail_name = cloudtrail_name

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
        if not isinstance(other, ExternalAccountAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
