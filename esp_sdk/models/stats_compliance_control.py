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


class StatsComplianceControl(BaseObject):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, _pass=None, fail=None, compliance_control=None, compliance_control_id=None, stat=None, stat_id=None, errors=None):
        """
        StatsComplianceControl - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            '_pass': 'int',
            'fail': 'int',
            'compliance_control': 'ComplianceControl',
            'compliance_control_id': 'int',
            'stat': 'Stat',
            'stat_id': 'int',
            'errors': 'list[str]'
        }

        self.attribute_map = {
            'id': 'id',
            '_pass': 'pass',
            'fail': 'fail',
            'compliance_control': 'compliance_control',
            'compliance_control_id': 'compliance_control_id',
            'stat': 'stat',
            'stat_id': 'stat_id',
            'errors': 'errors'
        }

        self._id = id
        self.__pass = _pass
        self._fail = fail
        self._compliance_control = compliance_control
        self._compliance_control_id = compliance_control_id
        self._stat = stat
        self._stat_id = stat_id
        self._errors = errors

    @property
    def id(self):
        """
        Gets the id of this StatsComplianceControl.
        Unique ID

        :return: The id of this StatsComplianceControl.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this StatsComplianceControl.
        Unique ID

        :param id: The id of this StatsComplianceControl.
        :type: int
        """

        self._id = id

    @property
    def _pass(self):
        """
        Gets the _pass of this StatsComplianceControl.

        :return: The _pass of this StatsComplianceControl.
        :rtype: int
        """
        return self.__pass

    @_pass.setter
    def _pass(self, _pass):
        """
        Sets the _pass of this StatsComplianceControl.

        :param _pass: The _pass of this StatsComplianceControl.
        :type: int
        """

        self.__pass = _pass

    @property
    def fail(self):
        """
        Gets the fail of this StatsComplianceControl.

        :return: The fail of this StatsComplianceControl.
        :rtype: int
        """
        return self._fail

    @fail.setter
    def fail(self, fail):
        """
        Sets the fail of this StatsComplianceControl.

        :param fail: The fail of this StatsComplianceControl.
        :type: int
        """

        self._fail = fail

    @property
    def compliance_control(self):
        """
        Gets the compliance_control of this StatsComplianceControl.
        Associated Compliance Control

        :return: The compliance_control of this StatsComplianceControl.
        :rtype: ComplianceControl
        """
        return self._compliance_control

    @compliance_control.setter
    def compliance_control(self, compliance_control):
        """
        Sets the compliance_control of this StatsComplianceControl.
        Associated Compliance Control

        :param compliance_control: The compliance_control of this StatsComplianceControl.
        :type: ComplianceControl
        """

        self._compliance_control = compliance_control

    @property
    def compliance_control_id(self):
        """
        Gets the compliance_control_id of this StatsComplianceControl.
        Associated Compliance Control Id

        :return: The compliance_control_id of this StatsComplianceControl.
        :rtype: int
        """
        return self._compliance_control_id

    @compliance_control_id.setter
    def compliance_control_id(self, compliance_control_id):
        """
        Sets the compliance_control_id of this StatsComplianceControl.
        Associated Compliance Control Id

        :param compliance_control_id: The compliance_control_id of this StatsComplianceControl.
        :type: int
        """

        self._compliance_control_id = compliance_control_id

    @property
    def stat(self):
        """
        Gets the stat of this StatsComplianceControl.
        Associated Stat

        :return: The stat of this StatsComplianceControl.
        :rtype: Stat
        """
        return self._stat

    @stat.setter
    def stat(self, stat):
        """
        Sets the stat of this StatsComplianceControl.
        Associated Stat

        :param stat: The stat of this StatsComplianceControl.
        :type: Stat
        """

        self._stat = stat

    @property
    def stat_id(self):
        """
        Gets the stat_id of this StatsComplianceControl.
        Associated Stat Id

        :return: The stat_id of this StatsComplianceControl.
        :rtype: int
        """
        return self._stat_id

    @stat_id.setter
    def stat_id(self, stat_id):
        """
        Sets the stat_id of this StatsComplianceControl.
        Associated Stat Id

        :param stat_id: The stat_id of this StatsComplianceControl.
        :type: int
        """

        self._stat_id = stat_id

    @property
    def errors(self):
        """
        Gets the errors of this StatsComplianceControl.
        Array of error messages if the request failed

        :return: The errors of this StatsComplianceControl.
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this StatsComplianceControl.
        Array of error messages if the request failed

        :param errors: The errors of this StatsComplianceControl.
        :type: list[str]
        """

        self._errors = errors

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
        if not isinstance(other, StatsComplianceControl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
