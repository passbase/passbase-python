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

class Identity(object):
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
        'status': 'str',
        'created': 'int',
        'updated': 'int',
        'resources': 'list[IdentityResource]',
        'watchlist': 'WatchlistResponse'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'created': 'created',
        'updated': 'updated',
        'resources': 'resources',
        'watchlist': 'watchlist'
    }

    def __init__(self, id=None, status=None, created=None, updated=None, resources=None, watchlist=None):  # noqa: E501
        """Identity - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._status = None
        self._created = None
        self._updated = None
        self._resources = None
        self._watchlist = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if resources is not None:
            self.resources = resources
        if watchlist is not None:
            self.watchlist = watchlist

    @property
    def id(self):
        """Gets the id of this Identity.  # noqa: E501

        Unique ID of the identity  # noqa: E501

        :return: The id of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Identity.

        Unique ID of the identity  # noqa: E501

        :param id: The id of this Identity.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this Identity.  # noqa: E501

        Current state of the identity in Passbase's systems  # noqa: E501

        :return: The status of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Identity.

        Current state of the identity in Passbase's systems  # noqa: E501

        :param status: The status of this Identity.  # noqa: E501
        :type: str
        """
        allowed_values = ["created", "processing", "pending", "approved", "declined"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def created(self):
        """Gets the created of this Identity.  # noqa: E501

        Unix-timestamp of when the identity was created  # noqa: E501

        :return: The created of this Identity.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Identity.

        Unix-timestamp of when the identity was created  # noqa: E501

        :param created: The created of this Identity.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this Identity.  # noqa: E501

        Unix-timestamp of when the identity was updated  # noqa: E501

        :return: The updated of this Identity.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Identity.

        Unix-timestamp of when the identity was updated  # noqa: E501

        :param updated: The updated of this Identity.  # noqa: E501
        :type: int
        """

        self._updated = updated

    @property
    def resources(self):
        """Gets the resources of this Identity.  # noqa: E501

        resources attached to a verification  # noqa: E501

        :return: The resources of this Identity.  # noqa: E501
        :rtype: list[IdentityResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this Identity.

        resources attached to a verification  # noqa: E501

        :param resources: The resources of this Identity.  # noqa: E501
        :type: list[IdentityResource]
        """

        self._resources = resources

    @property
    def watchlist(self):
        """Gets the watchlist of this Identity.  # noqa: E501


        :return: The watchlist of this Identity.  # noqa: E501
        :rtype: WatchlistResponse
        """
        return self._watchlist

    @watchlist.setter
    def watchlist(self, watchlist):
        """Sets the watchlist of this Identity.


        :param watchlist: The watchlist of this Identity.  # noqa: E501
        :type: WatchlistResponse
        """

        self._watchlist = watchlist

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
        if issubclass(Identity, dict):
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
        if not isinstance(other, Identity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
