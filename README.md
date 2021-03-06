![banner](https://passbase-sdk-banner.netlify.app/python.png)

# passbase

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.3.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/passbase/passbase-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/passbase/passbase-python.git`)

Then import the package:
```python
import passbase 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import passbase
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://api.passbase.com/verification/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*IdentityApi* | [**get_identity_by_id**](docs/IdentityApi.md#get_identity_by_id) | **GET** /identities/{id} | Get identity
*IdentityApi* | [**get_identity_resource_by_id**](docs/IdentityApi.md#get_identity_resource_by_id) | **GET** /identity/{id}/resources/{resource_id} | Get resource
*IdentityApi* | [**get_identity_resource_file_by_id**](docs/IdentityApi.md#get_identity_resource_file_by_id) | **GET** /identity/{id}/resources/{resource_id}/resource_files/{resource_file_id} | Get resource file
*IdentityApi* | [**list_identities**](docs/IdentityApi.md#list_identities) | **GET** /identities | List identities
*IdentityApi* | [**list_identity_resources**](docs/IdentityApi.md#list_identity_resources) | **GET** /identity/{id}/resources | List resources
*ProjectApi* | [**get_settings**](docs/ProjectApi.md#get_settings) | **GET** /settings | Get project settings

## Documentation For Models

 - [Cursor](docs/Cursor.md)
 - [DataPoints](docs/DataPoints.md)
 - [Identity](docs/Identity.md)
 - [IdentityOwner](docs/IdentityOwner.md)
 - [IdentityResource](docs/IdentityResource.md)
 - [PaginatedIdentities](docs/PaginatedIdentities.md)
 - [PaginatedResources](docs/PaginatedResources.md)
 - [ProjectSettings](docs/ProjectSettings.md)
 - [ProjectSettingsCustomizations](docs/ProjectSettingsCustomizations.md)
 - [ProjectSettingsVerificationSteps](docs/ProjectSettingsVerificationSteps.md)
 - [Resource](docs/Resource.md)
 - [ResourceFile](docs/ResourceFile.md)
 - [ResourceFiles](docs/ResourceFiles.md)
 - [ResourceFilesInner](docs/ResourceFilesInner.md)
 - [ResourceFilesInput](docs/ResourceFilesInput.md)
 - [ResourceFilesInputInner](docs/ResourceFilesInputInner.md)
 - [ResourceInput](docs/ResourceInput.md)
 - [ResourceType](docs/ResourceType.md)
 - [User](docs/User.md)
 - [WatchlistResponse](docs/WatchlistResponse.md)

## Documentation For Authorization


## IdentityAccessToken


## PublishableApiKey

- **Type**: API key
- **API key parameter name**: X-API-KEY
- **Location**: HTTP header

## SecretApiKey

- **Type**: API key
- **API key parameter name**: X-API-KEY
- **Location**: HTTP header


## Author


