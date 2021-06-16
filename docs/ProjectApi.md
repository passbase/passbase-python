# passbase.ProjectApi

All URIs are relative to *https://api.passbase.com/verification/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_settings**](ProjectApi.md#get_settings) | **GET** /settings | Get project settings

# **get_settings**
> ProjectSettings get_settings()

Get project settings

Get project settings 

### Example
```python
from __future__ import print_function
import time
import passbase
from passbase.rest import ApiException
from pprint import pprint

# Configure API key authorization: SecretApiKey
configuration = passbase.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = passbase.ProjectApi(passbase.ApiClient(configuration))

try:
    # Get project settings
    api_response = api_instance.get_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProjectSettings**](ProjectSettings.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

