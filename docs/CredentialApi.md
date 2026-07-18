# multiflexi_client.CredentialApi

All URIs are relative to *https://virtserver.swaggerhub.com/VitexSoftware/MultiFlexi/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_user_credentials**](CredentialApi.md#get_all_user_credentials) | **GET** /credentials.{suffix} | Get All User Credentials
[**get_credential**](CredentialApi.md#get_credential) | **GET** /credential/{credentialId}.{suffix} | Get User Credentials
[**update_credentials**](CredentialApi.md#update_credentials) | **POST** /credential/{credentialId}.{suffix} | Update Credentials


# **get_all_user_credentials**
> List[Credential] get_all_user_credentials(suffix, limit=limit, offset=offset, order=order)

Get All User Credentials

Retrieve all user credentials

### Example


```python
import multiflexi_client
from multiflexi_client.models.credential import Credential
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
    api_instance = multiflexi_client.CredentialApi(api_client)
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)
    offset = 0 # int | number of records to skip (for pagination) (optional) (default to 0)
    order = '-id' # str | field name to order results by (use '-' prefix for descending, e.g. '-id') (optional)

    try:
        # Get All User Credentials
        api_response = api_instance.get_all_user_credentials(suffix, limit=limit, offset=offset, order=order)
        print("The response of CredentialApi->get_all_user_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialApi->get_all_user_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| number of records to skip (for pagination) | [optional] [default to 0]
 **order** | **str**| field name to order results by (use &#39;-&#39; prefix for descending, e.g. &#39;-id&#39;) | [optional] 

### Return type

[**List[Credential]**](Credential.md)

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

# **get_credential**
> Credential get_credential(token, credential_id, suffix, limit=limit)

Get User Credentials

Retrieve user credentials based on provided token

### Example


```python
import multiflexi_client
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
    api_instance = multiflexi_client.CredentialApi(api_client)
    token = 'token_example' # str | User's access token
    credential_id = 56 # int | ID of Credential to return
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Get User Credentials
        api_response = api_instance.get_credential(token, credential_id, suffix, limit=limit)
        print("The response of CredentialApi->get_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialApi->get_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| User&#39;s access token | 
 **credential_id** | **int**| ID of Credential to return | 
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

[**Credential**](Credential.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Invalid token supplied |  -  |
**401** | Authentication information is missing or invalid |  * WWW_Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_credentials**
> UpdateCredentials201Response update_credentials(token, credential_id, suffix, limit=limit)

Update Credentials

Update credentials

### Example


```python
import multiflexi_client
from multiflexi_client.models.update_credentials201_response import UpdateCredentials201Response
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
    api_instance = multiflexi_client.CredentialApi(api_client)
    token = 'token_example' # str | User's access token
    credential_id = 56 # int | ID of Credential to return
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Update Credentials
        api_response = api_instance.update_credentials(token, credential_id, suffix, limit=limit)
        print("The response of CredentialApi->update_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialApi->update_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| User&#39;s access token | 
 **credential_id** | **int**| ID of Credential to return | 
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

[**UpdateCredentials201Response**](UpdateCredentials201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Record was updated |  -  |
**400** | Invalid token supplied |  -  |
**401** | Authentication information is missing or invalid |  * WWW_Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

