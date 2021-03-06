# esp_sdk.RolesApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](RolesApi.md#list) | **GET** /api/v2/roles.json_api | Get a list of Roles
[**show**](RolesApi.md#show) | **GET** /api/v2/roles/{id}.json_api | Show a single Role


# **list**
> PaginatedCollection list(page=page, include=include)

Get a list of Roles



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.RolesApi()
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page (optional) (default to {:number=>1,+:size=>20})
include = 'include_example' # str | Related objects that can be included in the response:   See Including Objects for more information. (optional)

try: 
    # Get a list of Roles
    api_response = api_instance.list(page=page, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| Page Number and Page Size.  number is the page number of the collection to return, size is the number of items to return per page | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]
 **include** | **str**| Related objects that can be included in the response:   See Including Objects for more information. | [optional] 

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> Role show(id, include=include)

Show a single Role



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.RolesApi()
id = 56 # int | Role ID
include = 'include_example' # str | Related objects that can be included in the response:   See Including Objects for more information. (optional)

try: 
    # Show a single Role
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Role ID | 
 **include** | **str**| Related objects that can be included in the response:   See Including Objects for more information. | [optional] 

### Return type

[**Role**](Role.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python2#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

