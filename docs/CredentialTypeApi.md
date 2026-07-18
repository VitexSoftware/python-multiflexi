# multiflexi_client.CredentialTypeApi

All URIs are relative to *https://virtserver.swaggerhub.com/VitexSoftware/MultiFlexi/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_credential_types**](CredentialTypeApi.md#get_all_credential_types) | **GET** /credential_types.{suffix} | Get All Credential Types
[**get_credential_type**](CredentialTypeApi.md#get_credential_type) | **GET** /credential_type/{credentialTypeID}.{suffix} | Get Credential Type by ID
[**update_credential_type**](CredentialTypeApi.md#update_credential_type) | **POST** /credential_type/{credentialTypeID}.{suffix} | Update Credential Type


# **get_all_credential_types**
> List[CredentialType] get_all_credential_types(suffix, limit=limit, offset=offset, order=order)

Get All Credential Types

Retrieve all credential types

### Example


```python
import multiflexi_client
from multiflexi_client.models.credential_type import CredentialType
from multiflexi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/VitexSoftware/MultiFlexi/1.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = multiflexi_client.Configuration(
    host = "https://virtserver.swaggerhub.com/VitexSoftware/MultiFlexi/1.0.0"
)


# Enter a context with an instance of the API client
with multiflexi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = multiflexi_client.CredentialTypeApi(api_client)
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)
    offset = 0 # int | number of records to skip (for pagination) (optional) (default to 0)
    order = '-id' # str | field name to order results by (use '-' prefix for descending, e.g. '-id') (optional)

    try:
        # Get All Credential Types
        api_response = api_instance.get_all_credential_types(suffix, limit=limit, offset=offset, order=order)
        print("The response of CredentialTypeApi->get_all_credential_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialTypeApi->get_all_credential_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| number of records to skip (for pagination) | [optional] [default to 0]
 **order** | **str**| field name to order results by (use &#39;-&#39; prefix for descending, e.g. &#39;-id&#39;) | [optional] 

### Return type

[**List[CredentialType]**](CredentialType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**401** | Authentication information is missing or invalid |  * WWW_Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credential_type**
> GetCredentialType200Response get_credential_type(credential_type_id, suffix, limit=limit)

Get Credential Type by ID

Retrieve credential type by ID

### Example


```python
import multiflexi_client
from multiflexi_client.models.get_credential_type200_response import GetCredentialType200Response
from multiflexi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/VitexSoftware/MultiFlexi/1.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = multiflexi_client.Configuration(
    host = "https://virtserver.swaggerhub.com/VitexSoftware/MultiFlexi/1.0.0"
)


# Enter a context with an instance of the API client
with multiflexi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = multiflexi_client.CredentialTypeApi(api_client)
    credential_type_id = 56 # int | ID of Credential Type to return
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Get Credential Type by ID
        api_response = api_instance.get_credential_type(credential_type_id, suffix, limit=limit)
        print("The response of CredentialTypeApi->get_credential_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialTypeApi->get_credential_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_type_id** | **int**| ID of Credential Type to return | 
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

[**GetCredentialType200Response**](GetCredentialType200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Invalid ID supplied |  -  |
**401** | Authentication information is missing or invalid |  * WWW_Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_credential_type**
> GetCredentialType200Response update_credential_type(credential_type_id, suffix, limit=limit)

Update Credential Type

Update credential type

### Example


```python
import multiflexi_client
from multiflexi_client.models.get_credential_type200_response import GetCredentialType200Response
from multiflexi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/VitexSoftware/MultiFlexi/1.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = multiflexi_client.Configuration(
    host = "https://virtserver.swaggerhub.com/VitexSoftware/MultiFlexi/1.0.0"
)


# Enter a context with an instance of the API client
with multiflexi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = multiflexi_client.CredentialTypeApi(api_client)
    credential_type_id = 56 # int | ID of Credential Type to return
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Update Credential Type
        api_response = api_instance.update_credential_type(credential_type_id, suffix, limit=limit)
        print("The response of CredentialTypeApi->update_credential_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialTypeApi->update_credential_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_type_id** | **int**| ID of Credential Type to return | 
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

[**GetCredentialType200Response**](GetCredentialType200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Record was updated |  -  |
**400** | Invalid ID supplied |  -  |
**401** | Authentication information is missing or invalid |  * WWW_Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

