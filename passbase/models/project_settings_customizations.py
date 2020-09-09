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

class ProjectSettingsCustomizations(object):
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
        'button_color': 'str',
        'accent_color': 'str',
        'font_family': 'str'
    }

    attribute_map = {
        'button_color': 'button_color',
        'accent_color': 'accent_color',
        'font_family': 'font_family'
    }

    def __init__(self, button_color=None, accent_color=None, font_family=None):  # noqa: E501
        """ProjectSettingsCustomizations - a model defined in Swagger"""  # noqa: E501
        self._button_color = None
        self._accent_color = None
        self._font_family = None
        self.discriminator = None
        if button_color is not None:
            self.button_color = button_color
        if accent_color is not None:
            self.accent_color = accent_color
        if font_family is not None:
            self.font_family = font_family

    @property
    def button_color(self):
        """Gets the button_color of this ProjectSettingsCustomizations.  # noqa: E501

        \\\"Verify Me\\\" button background color  # noqa: E501

        :return: The button_color of this ProjectSettingsCustomizations.  # noqa: E501
        :rtype: str
        """
        return self._button_color

    @button_color.setter
    def button_color(self, button_color):
        """Sets the button_color of this ProjectSettingsCustomizations.

        \\\"Verify Me\\\" button background color  # noqa: E501

        :param button_color: The button_color of this ProjectSettingsCustomizations.  # noqa: E501
        :type: str
        """

        self._button_color = button_color

    @property
    def accent_color(self):
        """Gets the accent_color of this ProjectSettingsCustomizations.  # noqa: E501

        Accent color during the verification flow (button, breadcrumb, etc…)  # noqa: E501

        :return: The accent_color of this ProjectSettingsCustomizations.  # noqa: E501
        :rtype: str
        """
        return self._accent_color

    @accent_color.setter
    def accent_color(self, accent_color):
        """Sets the accent_color of this ProjectSettingsCustomizations.

        Accent color during the verification flow (button, breadcrumb, etc…)  # noqa: E501

        :param accent_color: The accent_color of this ProjectSettingsCustomizations.  # noqa: E501
        :type: str
        """

        self._accent_color = accent_color

    @property
    def font_family(self):
        """Gets the font_family of this ProjectSettingsCustomizations.  # noqa: E501

        Font used in the verification flow  # noqa: E501

        :return: The font_family of this ProjectSettingsCustomizations.  # noqa: E501
        :rtype: str
        """
        return self._font_family

    @font_family.setter
    def font_family(self, font_family):
        """Sets the font_family of this ProjectSettingsCustomizations.

        Font used in the verification flow  # noqa: E501

        :param font_family: The font_family of this ProjectSettingsCustomizations.  # noqa: E501
        :type: str
        """
        allowed_values = ["Arial", "Exo", "Open Sans", "Lato", "Baskerville"]  # noqa: E501
        if font_family not in allowed_values:
            raise ValueError(
                "Invalid value for `font_family` ({0}), must be one of {1}"  # noqa: E501
                .format(font_family, allowed_values)
            )

        self._font_family = font_family

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
        if issubclass(ProjectSettingsCustomizations, dict):
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
        if not isinstance(other, ProjectSettingsCustomizations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other