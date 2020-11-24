# passbase.IdentityApi

All URIs are relative to *https://api.passbase.com/verification/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_identity_by_id**](IdentityApi.md#get_identity_by_id) | **GET** /identities/{id} | Get identity
[**get_identity_resource_by_id**](IdentityApi.md#get_identity_resource_by_id) | **GET** /identity/{id}/resources/{resource_id} | Get resource
[**get_identity_resource_file_by_id**](IdentityApi.md#get_identity_resource_file_by_id) | **GET** /identity/{id}/resources/{resource_id}/resource_files/{resource_file_id} | Get resource file
[**list_identities**](IdentityApi.md#list_identities) | **GET** /identities | List identities
[**list_identity_resources**](IdentityApi.md#list_identity_resources) | **GET** /identity/{id}/resources | List resources

# **get_identity_by_id**
> Identity get_identity_by_id(id)

Get identity

Retrieve an identity by providing the identity ID.

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
api_instance = passbase.IdentityApi(passbase.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Unique ID of the identity to return

try:
    # Get identity
    api_response = api_instance.get_identity_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityApi->get_identity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Unique ID of the identity to return | 

### Return type

[**Identity**](Identity.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_resource_by_id**
> Resource get_identity_resource_by_id(id, resource_id)

Get resource

Get a resource attached to an identity by providing the resource ID. 

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
api_instance = passbase.IdentityApi(passbase.ApiClient(configuration))
id = 'id_example' # str | Identity id
resource_id = 'resource_id_example' # str | Resource id

try:
    # Get resource
    api_response = api_instance.get_identity_resource_by_id(id, resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityApi->get_identity_resource_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identity id | 
 **resource_id** | **str**| Resource id | 

### Return type

[**Resource**](Resource.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_resource_file_by_id**
> ResourceFile get_identity_resource_file_by_id(id, resource_id, resource_file_id)

Get resource file

Get a raw resource file attached to an identity by providing the resource ID and the resource file ID. This is a protected route and you'll need a specific government authorization to access it. 

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
api_instance = passbase.IdentityApi(passbase.ApiClient(configuration))
id = 'id_example' # str | Identity id
resource_id = 'resource_id_example' # str | Resource id
resource_file_id = 'resource_file_id_example' # str | Resource file id

try:
    # Get resource file
    api_response = api_instance.get_identity_resource_file_by_id(id, resource_id, resource_file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityApi->get_identity_resource_file_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identity id | 
 **resource_id** | **str**| Resource id | 
 **resource_file_id** | **str**| Resource file id | 

### Return type

[**ResourceFile**](ResourceFile.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_identities**
> PaginatedIdentities list_identities(limit=limit, cursor=cursor)

List identities

List all the identities retrievable by the provided API Secret Key.

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
api_instance = passbase.IdentityApi(passbase.ApiClient(configuration))
limit = 56 # int |  (optional)
cursor = 'cursor_example' # str |  (optional)

try:
    # List identities
    api_response = api_instance.list_identities(limit=limit, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityApi->list_identities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **cursor** | **str**|  | [optional] 

### Return type

[**PaginatedIdentities**](PaginatedIdentities.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_identity_resources**
> PaginatedResources list_identity_resources(id, limit=limit, cursor=cursor)

List resources

List resources attached to an identity by providing the identity ID.

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
api_instance = passbase.IdentityApi(passbase.ApiClient(configuration))
id = 'id_example' # str | Identity id
limit = 56 # int |  (optional)
cursor = 'cursor_example' # str |  (optional)

try:
    # List resources
    api_response = api_instance.list_identity_resources(id, limit=limit, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityApi->list_identity_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identity id | 
 **limit** | **int**|  | [optional] 
 **cursor** | **str**|  | [optional] 

### Return type

[**PaginatedResources**](PaginatedResources.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

