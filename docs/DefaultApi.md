# multiflexi_client.DefaultApi

All URIs are relative to *https://virtserver.swaggerhub.com/VitexSoftware/MultiFlexi/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_credential_types**](DefaultApi.md#get_all_credential_types) | **GET** /credential_types.{suffix} | Get All Credential Types
[**get_all_topics**](DefaultApi.md#get_all_topics) | **GET** /topics.{suffix} | Get All Topics
[**get_all_user_credentials**](DefaultApi.md#get_all_user_credentials) | **GET** /credentials.{suffix} | Get All User Credentials
[**get_api_index**](DefaultApi.md#get_api_index) | **GET** /index.{suffix} | Endpoints listing
[**get_credential**](DefaultApi.md#get_credential) | **GET** /credential/{credentialId}.{suffix} | Get User Credentials
[**get_credential_type**](DefaultApi.md#get_credential_type) | **GET** /credential_type/{credentialTypeID}.{suffix} | Get Credential Type by ID
[**get_jobs_status**](DefaultApi.md#get_jobs_status) | **GET** /jobs/status.{suffix} | Get Jobs Status
[**get_topic**](DefaultApi.md#get_topic) | **GET** /topic/{topicId}.{suffix} | Get Topic by ID
[**login_suffix_get**](DefaultApi.md#login_suffix_get) | **GET** /login.{suffix} | Return User&#39;s token
[**login_suffix_post**](DefaultApi.md#login_suffix_post) | **POST** /login.{suffix} | Return User&#39;s token
[**logout_post**](DefaultApi.md#logout_post) | **POST** /logout | Odhlášení uživatele (invalidate token/session)
[**ping_suffix_get**](DefaultApi.md#ping_suffix_get) | **GET** /ping.{suffix} | job heartbeat operation
[**root_get**](DefaultApi.md#root_get) | **GET** / | Redirect to index
[**status_suffix_get**](DefaultApi.md#status_suffix_get) | **GET** /status.{suffix} | Get API status
[**update_credential_type**](DefaultApi.md#update_credential_type) | **POST** /credential_type/{credentialTypeID}.{suffix} | Update Credential Type
[**update_credentials**](DefaultApi.md#update_credentials) | **POST** /credential/{credentialId}.{suffix} | Update Credentials
[**update_topic**](DefaultApi.md#update_topic) | **POST** /topic/{topicId}.{suffix} | Update Topic


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
    api_instance = multiflexi_client.DefaultApi(api_client)
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)
    offset = 0 # int | number of records to skip (for pagination) (optional) (default to 0)
    order = '-id' # str | field name to order results by (use '-' prefix for descending, e.g. '-id') (optional)

    try:
        # Get All Credential Types
        api_response = api_instance.get_all_credential_types(suffix, limit=limit, offset=offset, order=order)
        print("The response of DefaultApi->get_all_credential_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_credential_types: %s\n" % e)
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

# **get_all_topics**
> List[Topic] get_all_topics(suffix, limit=limit, offset=offset, order=order)

Get All Topics

Retrieve all topics

### Example


```python
import multiflexi_client
from multiflexi_client.models.topic import Topic
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
    api_instance = multiflexi_client.DefaultApi(api_client)
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)
    offset = 0 # int | number of records to skip (for pagination) (optional) (default to 0)
    order = '-id' # str | field name to order results by (use '-' prefix for descending, e.g. '-id') (optional)

    try:
        # Get All Topics
        api_response = api_instance.get_all_topics(suffix, limit=limit, offset=offset, order=order)
        print("The response of DefaultApi->get_all_topics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_topics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| number of records to skip (for pagination) | [optional] [default to 0]
 **order** | **str**| field name to order results by (use &#39;-&#39; prefix for descending, e.g. &#39;-id&#39;) | [optional] 

### Return type

[**List[Topic]**](Topic.md)

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
    api_instance = multiflexi_client.DefaultApi(api_client)
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)
    offset = 0 # int | number of records to skip (for pagination) (optional) (default to 0)
    order = '-id' # str | field name to order results by (use '-' prefix for descending, e.g. '-id') (optional)

    try:
        # Get All User Credentials
        api_response = api_instance.get_all_user_credentials(suffix, limit=limit, offset=offset, order=order)
        print("The response of DefaultApi->get_all_user_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_user_credentials: %s\n" % e)
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

# **get_api_index**
> get_api_index(suffix, limit=limit)

Endpoints listing

Show current API

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
    api_instance = multiflexi_client.DefaultApi(api_client)
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Endpoints listing
        api_instance.get_api_index(suffix, limit=limit)
    except Exception as e:
        print("Exception when calling DefaultApi->get_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

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
    api_instance = multiflexi_client.DefaultApi(api_client)
    token = 'token_example' # str | User's access token
    credential_id = 56 # int | ID of Credential to return
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Get User Credentials
        api_response = api_instance.get_credential(token, credential_id, suffix, limit=limit)
        print("The response of DefaultApi->get_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_credential: %s\n" % e)
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
    api_instance = multiflexi_client.DefaultApi(api_client)
    credential_type_id = 56 # int | ID of Credential Type to return
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Get Credential Type by ID
        api_response = api_instance.get_credential_type(credential_type_id, suffix, limit=limit)
        print("The response of DefaultApi->get_credential_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_credential_type: %s\n" % e)
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

# **get_jobs_status**
> List[JobsStatus] get_jobs_status(suffix, limit=limit)

Get Jobs Status

Retrieve all jobs status

### Example


```python
import multiflexi_client
from multiflexi_client.models.jobs_status import JobsStatus
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
    api_instance = multiflexi_client.DefaultApi(api_client)
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Get Jobs Status
        api_response = api_instance.get_jobs_status(suffix, limit=limit)
        print("The response of DefaultApi->get_jobs_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_jobs_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

[**List[JobsStatus]**](JobsStatus.md)

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

# **get_topic**
> GetTopic200Response get_topic(topic_id, suffix, limit=limit)

Get Topic by ID

Retrieve topic by ID

### Example


```python
import multiflexi_client
from multiflexi_client.models.get_topic200_response import GetTopic200Response
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
    api_instance = multiflexi_client.DefaultApi(api_client)
    topic_id = 56 # int | ID of Topic to return
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Get Topic by ID
        api_response = api_instance.get_topic(topic_id, suffix, limit=limit)
        print("The response of DefaultApi->get_topic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_topic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_id** | **int**| ID of Topic to return | 
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

[**GetTopic200Response**](GetTopic200Response.md)

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

# **login_suffix_get**
> login_suffix_get(username, password, suffix, limit=limit)

Return User's token

Send login & password to obtain oAuth token

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
    api_instance = multiflexi_client.DefaultApi(api_client)
    username = 'username_example' # str | existing user name
    password = 'password_example' # str | existing user password
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Return User's token
        api_instance.login_suffix_get(username, password, suffix, limit=limit)
    except Exception as e:
        print("Exception when calling DefaultApi->login_suffix_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| existing user name | 
 **password** | **str**| existing user password | 
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_suffix_post**
> login_suffix_post(username, password, suffix, limit=limit)

Return User's token

Send login & password to obtain oAuth token

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
    api_instance = multiflexi_client.DefaultApi(api_client)
    username = 'username_example' # str | existing user name
    password = 'password_example' # str | existing user password
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Return User's token
        api_instance.login_suffix_post(username, password, suffix, limit=limit)
    except Exception as e:
        print("Exception when calling DefaultApi->login_suffix_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| existing user name | 
 **password** | **str**| existing user password | 
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout_post**
> logout_post(logout_post_request)

Odhlášení uživatele (invalidate token/session)

Invalidační aktuální uživatelskou session nebo token (OAuth2, JWT, případně session cookie).

### Example


```python
import multiflexi_client
from multiflexi_client.models.logout_post_request import LogoutPostRequest
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
    api_instance = multiflexi_client.DefaultApi(api_client)
    logout_post_request = multiflexi_client.LogoutPostRequest() # LogoutPostRequest | 

    try:
        # Odhlášení uživatele (invalidate token/session)
        api_instance.logout_post(logout_post_request)
    except Exception as e:
        print("Exception when calling DefaultApi->logout_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logout_post_request** | [**LogoutPostRequest**](LogoutPostRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Odhlášení proběhlo úspěšně |  -  |
**401** | Uživatel není přihlášen nebo token je neplatný |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_suffix_get**
> ping_suffix_get(suffix, limit=limit)

job heartbeat operation

This operation shows how to override the global security defined above, as we want to open it up for all users.

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
    api_instance = multiflexi_client.DefaultApi(api_client)
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # job heartbeat operation
        api_instance.ping_suffix_get(suffix, limit=limit)
    except Exception as e:
        print("Exception when calling DefaultApi->ping_suffix_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_get**
> root_get(limit=limit)

Redirect to index

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
    api_instance = multiflexi_client.DefaultApi(api_client)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Redirect to index
        api_instance.root_get(limit=limit)
    except Exception as e:
        print("Exception when calling DefaultApi->root_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**301** | redirect to index.html |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_suffix_get**
> Status status_suffix_get(suffix, limit=limit)

Get API status

This operation shows how to override the global security defined above, as we want to open it up for all users.

### Example


```python
import multiflexi_client
from multiflexi_client.models.status import Status
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
    api_instance = multiflexi_client.DefaultApi(api_client)
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Get API status
        api_response = api_instance.status_suffix_get(suffix, limit=limit)
        print("The response of DefaultApi->status_suffix_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->status_suffix_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

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
    api_instance = multiflexi_client.DefaultApi(api_client)
    credential_type_id = 56 # int | ID of Credential Type to return
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Update Credential Type
        api_response = api_instance.update_credential_type(credential_type_id, suffix, limit=limit)
        print("The response of DefaultApi->update_credential_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_credential_type: %s\n" % e)
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
    api_instance = multiflexi_client.DefaultApi(api_client)
    token = 'token_example' # str | User's access token
    credential_id = 56 # int | ID of Credential to return
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Update Credentials
        api_response = api_instance.update_credentials(token, credential_id, suffix, limit=limit)
        print("The response of DefaultApi->update_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_credentials: %s\n" % e)
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

# **update_topic**
> GetTopic200Response update_topic(topic_id, suffix, limit=limit)

Update Topic

Update topic

### Example


```python
import multiflexi_client
from multiflexi_client.models.get_topic200_response import GetTopic200Response
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
    api_instance = multiflexi_client.DefaultApi(api_client)
    topic_id = 56 # int | ID of Topic to return
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Update Topic
        api_response = api_instance.update_topic(topic_id, suffix, limit=limit)
        print("The response of DefaultApi->update_topic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_topic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topic_id** | **int**| ID of Topic to return | 
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

[**GetTopic200Response**](GetTopic200Response.md)

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

