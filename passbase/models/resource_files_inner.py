# coding: utf-8

"""
    Verification API

    # Introduction  <span class=\"subtext\"> Welcome to the Passbase Verifications API docs. This documentation will help you understand our models and the Verification API with its endpoints. Based on this you can build your own system (i.e. verification) and hook it up to Passbase.  In case of feedback or questions you can reach us under this email address: [developer@passbase.com](mailto:developer@passbase.com). </span>  A User submits a video selfie and valid identifying __Resources__ during a __Verification__ guided by the Passbase client-side integration. Once all the necessary __Resources__ are submitted, __Data points__ are extracted, digitized, and authenticated. These Data points then becomes part of the User's __Identity__. The User then consents to share __Resources__ and/or __Data points__ from their Identity with you. This information is passed to you and can be used to make decisions about a User (e.g. activate account). This table below explains our terminology further.  | Term                                    | Description | |-----------------------------------------|-------------| | Data points                             | Any data about a User extracted from a Resource (E.g. Passport Number, or Age). | | [Resource](#tag/resource_model)         | A source document used to generate the Data points for a User (E.g. Passport). | | [Identity](#tag/identity_model)         | A set of Data points and Resources related to and owned by one single User. This data can be accessed by you through a Verification. | | [User](#tag/user_model)                 | The owner of an email address associated with an Identity. | | Verification (signup)                   | A transaction through which a User consents to share Data points with you. If the Data points you request are not already available in the User's Identity, the Passbase client will ask the User to submit the necessary Resource required to extract them. | | Re-authentication (login)               | A transaction through which a User can certify the ownership of Personal data previously shared through an Authentication. |   # Authentication  <span class=\"subtext\"> There are two forms of authentication for the API: <br/>&bull; API Key <br/>&bull; Bearer JWT Token  </span>   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ResourceFilesInner(object):
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
        'id': 'str',
        'type': 'str',
        'page': 'int',
        'created': 'int',
        'updated': 'int'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'page': 'page',
        'created': 'created',
        'updated': 'updated'
    }

    def __init__(self, id=None, type=None, page=None, created=None, updated=None):  # noqa: E501
        """ResourceFilesInner - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._page = None
        self._created = None
        self._updated = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if page is not None:
            self.page = page
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated

    @property
    def id(self):
        """Gets the id of this ResourceFilesInner.  # noqa: E501

        Unique ID representing a resource file  # noqa: E501

        :return: The id of this ResourceFilesInner.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResourceFilesInner.

        Unique ID representing a resource file  # noqa: E501

        :param id: The id of this ResourceFilesInner.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this ResourceFilesInner.  # noqa: E501


        :return: The type of this ResourceFilesInner.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResourceFilesInner.


        :param type: The type of this ResourceFilesInner.  # noqa: E501
        :type: str
        """
        allowed_values = ["face_video", "document_image"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def page(self):
        """Gets the page of this ResourceFilesInner.  # noqa: E501

        Page number of the document. Generally 1 would represent the front of a document, and 2 might represent the back of the same document.   # noqa: E501

        :return: The page of this ResourceFilesInner.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ResourceFilesInner.

        Page number of the document. Generally 1 would represent the front of a document, and 2 might represent the back of the same document.   # noqa: E501

        :param page: The page of this ResourceFilesInner.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def created(self):
        """Gets the created of this ResourceFilesInner.  # noqa: E501

        Unix-timestamp of when the resource was created  # noqa: E501

        :return: The created of this ResourceFilesInner.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ResourceFilesInner.

        Unix-timestamp of when the resource was created  # noqa: E501

        :param created: The created of this ResourceFilesInner.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this ResourceFilesInner.  # noqa: E501

        Unix-timestamp of when the resource was updated  # noqa: E501

        :return: The updated of this ResourceFilesInner.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ResourceFilesInner.

        Unix-timestamp of when the resource was updated  # noqa: E501

        :param updated: The updated of this ResourceFilesInner.  # noqa: E501
        :type: int
        """

        self._updated = updated

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
        if issubclass(ResourceFilesInner, dict):
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
        if not isinstance(other, ResourceFilesInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
