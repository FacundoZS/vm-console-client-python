# coding: utf-8

"""
    Python InsightVM API Client

    OpenAPI spec version: 3
    Contact: support@rapid7.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UpdateInfo(object):
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
        'content': 'str',
        'content_partial': 'str',
        'id': 'UpdateId',
        'product': 'str'
    }

    attribute_map = {
        'content': 'content',
        'content_partial': 'contentPartial',
        'id': 'id',
        'product': 'product'
    }

    def __init__(self, content=None, content_partial=None, id=None, product=None):  # noqa: E501
        """UpdateInfo - a model defined in Swagger"""  # noqa: E501

        self._content = None
        self._content_partial = None
        self._id = None
        self._product = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if content_partial is not None:
            self.content_partial = content_partial
        if id is not None:
            self.id = id
        if product is not None:
            self.product = product

    @property
    def content(self):
        """Gets the content of this UpdateInfo.  # noqa: E501

        The most recent content update.  # noqa: E501

        :return: The content of this UpdateInfo.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this UpdateInfo.

        The most recent content update.  # noqa: E501

        :param content: The content of this UpdateInfo.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def content_partial(self):
        """Gets the content_partial of this UpdateInfo.  # noqa: E501

        The most recent, partially-applied (in-memory), content update.  # noqa: E501

        :return: The content_partial of this UpdateInfo.  # noqa: E501
        :rtype: str
        """
        return self._content_partial

    @content_partial.setter
    def content_partial(self, content_partial):
        """Sets the content_partial of this UpdateInfo.

        The most recent, partially-applied (in-memory), content update.  # noqa: E501

        :param content_partial: The content_partial of this UpdateInfo.  # noqa: E501
        :type: str
        """

        self._content_partial = content_partial

    @property
    def id(self):
        """Gets the id of this UpdateInfo.  # noqa: E501

        Details of update identifiers.  # noqa: E501

        :return: The id of this UpdateInfo.  # noqa: E501
        :rtype: UpdateId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateInfo.

        Details of update identifiers.  # noqa: E501

        :param id: The id of this UpdateInfo.  # noqa: E501
        :type: UpdateId
        """

        self._id = id

    @property
    def product(self):
        """Gets the product of this UpdateInfo.  # noqa: E501

        The most recent product update.  # noqa: E501

        :return: The product of this UpdateInfo.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this UpdateInfo.

        The most recent product update.  # noqa: E501

        :param product: The product of this UpdateInfo.  # noqa: E501
        :type: str
        """

        self._product = product

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
        if issubclass(UpdateInfo, dict):
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
        if not isinstance(other, UpdateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
