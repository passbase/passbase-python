# coding: utf-8

"""
    Verification API

    # Introduction  <span class=\"subtext\"> Welcome to the Passbase Verifications API docs. This documentation will help you understand our models and the Verification API with its endpoints. Based on this you can build your own system (i.e. verification) and hook it up to Passbase.  In case of feedback or questions you can reach us under this email address: [developer@passbase.com](mailto:developer@passbase.com). </span>  A User submits a video selfie and valid identifying __Resources__ during a __Verification__ guided by the Passbase client-side integration. Once all the necessary __Resources__ are submitted, __Data points__ are extracted, digitized, and authenticated. These Data points then becomes part of the User's __Identity__. The User then consents to share __Resources__ and/or __Data points__ from their Identity with you. This information is passed to you and can be used to make decisions about a User (e.g. activate account). This table below explains our terminology further.  | Term                                    | Description | |-----------------------------------------|-------------| | [Identity](#tag/identity_model)         | A set of Data points and Resources related to and owned by one single User. This data can be accessed by you through a Verification. | | Data points                             | Any data about a User extracted from a Resource (E.g. Passport Number, or Age). | | [Resource](#tag/resource_model)         | A source document used to generate the Data points for a User (E.g. Passport). | | [User](#tag/user_model)                 | The owner of an email address associated with an Identity. | | Verification                            | A transaction through which a User consents to share Data points with you. If the Data points you request are not already available in the User's Identity, the Passbase client will ask the User to submit the necessary Resource required to extract them. | | Re-authentication (login)               | A transaction through which a User can certify the ownership of Personal data previously shared through an Authentication. |   # Authentication  <span class=\"subtext\"> There are two forms of authentication for the API: <br/>&bull; API Key <br/>&bull; Bearer JWT Token  </span>   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ResourceInput(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'ResourceType',
        'country': 'str',
        'resource_files': 'list[ResourceFilesInput]',
        'resource_data': 'object',
        'resource_raw_data': 'object'
    }

    attribute_map = {
        'type': 'type',
        'country': 'country',
        'resource_files': 'resource_files',
        'resource_data': 'resourceData',
        'resource_raw_data': 'resourceRawData'
    }

    def __init__(self, type=None, country=None, resource_files=None, resource_data=None, resource_raw_data=None):  # noqa: E501
        """ResourceInput - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._country = None
        self._resource_files = None
        self._resource_data = None
        self._resource_raw_data = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if country is not None:
            self.country = country
        if resource_files is not None:
            self.resource_files = resource_files
        if resource_data is not None:
            self.resource_data = resource_data
        if resource_raw_data is not None:
            self.resource_raw_data = resource_raw_data

    @property
    def type(self):
        """Gets the type of this ResourceInput.  # noqa: E501


        :return: The type of this ResourceInput.  # noqa: E501
        :rtype: ResourceType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResourceInput.


        :param type: The type of this ResourceInput.  # noqa: E501
        :type: ResourceType
        """

        self._type = type

    @property
    def country(self):
        """Gets the country of this ResourceInput.  # noqa: E501

        2-letter code of the country  # noqa: E501

        :return: The country of this ResourceInput.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ResourceInput.

        2-letter code of the country  # noqa: E501

        :param country: The country of this ResourceInput.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def resource_files(self):
        """Gets the resource_files of this ResourceInput.  # noqa: E501


        :return: The resource_files of this ResourceInput.  # noqa: E501
        :rtype: list[ResourceFilesInput]
        """
        return self._resource_files

    @resource_files.setter
    def resource_files(self, resource_files):
        """Sets the resource_files of this ResourceInput.


        :param resource_files: The resource_files of this ResourceInput.  # noqa: E501
        :type: list[ResourceFilesInput]
        """

        self._resource_files = resource_files

    @property
    def resource_data(self):
        """Gets the resource_data of this ResourceInput.  # noqa: E501


        :return: The resource_data of this ResourceInput.  # noqa: E501
        :rtype: object
        """
        return self._resource_data

    @resource_data.setter
    def resource_data(self, resource_data):
        """Sets the resource_data of this ResourceInput.


        :param resource_data: The resource_data of this ResourceInput.  # noqa: E501
        :type: object
        """

        self._resource_data = resource_data

    @property
    def resource_raw_data(self):
        """Gets the resource_raw_data of this ResourceInput.  # noqa: E501


        :return: The resource_raw_data of this ResourceInput.  # noqa: E501
        :rtype: object
        """
        return self._resource_raw_data

    @resource_raw_data.setter
    def resource_raw_data(self, resource_raw_data):
        """Sets the resource_raw_data of this ResourceInput.


        :param resource_raw_data: The resource_raw_data of this ResourceInput.  # noqa: E501
        :type: object
        """

        self._resource_raw_data = resource_raw_data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ResourceInput, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResourceInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
