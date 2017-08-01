# coding: utf-8

"""
    ESP Documentation

    The Evident Security Platform API (version 2.0) is designed to allow users granular control over their Amazon Web Service security experience by allowing them to review alerts, monitor signatures, and create custom signatures.

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class SignatureSuppressionsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_signature_suppression(self, regions, external_account_ids, reason, resource, **kwargs):
        """
        A successful call to this API creates a new signature suppression for the supplied signature_ids or custom_signature_ids. The body of the request must contain a json API compliant hash of attributes with type suppression/signatures.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_signature_suppression(regions, external_account_ids, reason, resource, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] regions: An array of region names to suppress (required)
        :param list[int] external_account_ids: An Array of the external accounts identified by external_account_id to suppress the signature or custom signature on (required)
        :param str reason: The reason for creating the suppression (required)
        :param str resource: The resource string this suppression will suppress alerts for (required)
        :param list[int] signature_ids: An array of signatures identified by signature_id to suppress. Required if custom_signature_ids is blank
        :param list[int] custom_signature_ids: An array of custom signatures identified by custom_signature_id to suppress. Required if signature_ids is blank
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_signature_suppression_with_http_info(regions, external_account_ids, reason, resource, **kwargs)
        else:
            (data) = self.create_signature_suppression_with_http_info(regions, external_account_ids, reason, resource, **kwargs)
            return data

    def create_signature_suppression_with_http_info(self, regions, external_account_ids, reason, resource, **kwargs):
        """
        A successful call to this API creates a new signature suppression for the supplied signature_ids or custom_signature_ids. The body of the request must contain a json API compliant hash of attributes with type suppression/signatures.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_signature_suppression_with_http_info(regions, external_account_ids, reason, resource, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] regions: An array of region names to suppress (required)
        :param list[int] external_account_ids: An Array of the external accounts identified by external_account_id to suppress the signature or custom signature on (required)
        :param str reason: The reason for creating the suppression (required)
        :param str resource: The resource string this suppression will suppress alerts for (required)
        :param list[int] signature_ids: An array of signatures identified by signature_id to suppress. Required if custom_signature_ids is blank
        :param list[int] custom_signature_ids: An array of custom signatures identified by custom_signature_id to suppress. Required if signature_ids is blank
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['regions', 'external_account_ids', 'reason', 'resource', 'signature_ids', 'custom_signature_ids']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_signature_suppression" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'regions' is set
        if ('regions' not in params) or (params['regions'] is None):
            raise ValueError("Missing the required parameter `regions` when calling `create_signature_suppression`")
        # verify the required parameter 'external_account_ids' is set
        if ('external_account_ids' not in params) or (params['external_account_ids'] is None):
            raise ValueError("Missing the required parameter `external_account_ids` when calling `create_signature_suppression`")
        # verify the required parameter 'reason' is set
        if ('reason' not in params) or (params['reason'] is None):
            raise ValueError("Missing the required parameter `reason` when calling `create_signature_suppression`")
        # verify the required parameter 'resource' is set
        if ('resource' not in params) or (params['resource'] is None):
            raise ValueError("Missing the required parameter `resource` when calling `create_signature_suppression`")


        collection_formats = {}

        resource_path = '/api/v2/suppressions/signatures.json_api'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'signature_ids' in params:
            form_params.append(('signature_ids', params['signature_ids']))
            collection_formats['signature_ids'] = 'csv'
        if 'custom_signature_ids' in params:
            form_params.append(('custom_signature_ids', params['custom_signature_ids']))
            collection_formats['custom_signature_ids'] = 'csv'
        if 'regions' in params:
            form_params.append(('regions', params['regions']))
            collection_formats['regions'] = 'csv'
        if 'external_account_ids' in params:
            form_params.append(('external_account_ids', params['external_account_ids']))
            collection_formats['external_account_ids'] = 'csv'
        if 'reason' in params:
            form_params.append(('reason', params['reason']))
        if 'resource' in params:
            form_params.append(('resource', params['resource']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/vnd.api+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
