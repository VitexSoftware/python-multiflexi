# multiflexi_client.AppApi

All URIs are relative to *https://virtserver.swaggerhub.com/VitexSoftware/MultiFlexi/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_app_by_id**](AppApi.md#get_app_by_id) | **GET** /app/{appId}.{suffix} | Get App by ID
[**list_apps**](AppApi.md#list_apps) | **GET** /apps.{suffix} | Show All Apps
[**set_app_by_id**](AppApi.md#set_app_by_id) | **POST** /app/ | Create or Update Application


# **get_app_by_id**
> App get_app_by_id(app_id, suffix, limit=limit)

Get App by ID

Returns a single App wrapped in apps object

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.app import App
from multiflexi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/VitexSoftware/MultiFlexi/1.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = multiflexi_client.Configuration(
    host = "https://virtserver.swaggerhub.com/VitexSoftware/MultiFlexi/1.0.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = multiflexi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with multiflexi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = multiflexi_client.AppApi(api_client)
    app_id = 56 # int | ID of app to return
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Get App by ID
        api_response = api_instance.get_app_by_id(app_id, suffix, limit=limit)
        print("The response of AppApi->get_app_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->get_app_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**| ID of app to return | 
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

[**App**](App.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid ID supplied |  -  |
**401** | Authentication information is missing or invalid |  * WWW_Authenticate -  <br>  |
**404** | App not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_apps**
> List[App] list_apps(suffix, limit=limit, offset=offset, order=order)

Show All Apps

All apps registeres

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.app import App
from multiflexi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/VitexSoftware/MultiFlexi/1.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = multiflexi_client.Configuration(
    host = "https://virtserver.swaggerhub.com/VitexSoftware/MultiFlexi/1.0.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = multiflexi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with multiflexi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = multiflexi_client.AppApi(api_client)
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)
    offset = 0 # int | number of records to skip (for pagination) (optional) (default to 0)
    order = '-id' # str | field name to order results by (use '-' prefix for descending, e.g. '-id') (optional)

    try:
        # Show All Apps
        api_response = api_instance.list_apps(suffix, limit=limit, offset=offset, order=order)
        print("The response of AppApi->list_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->list_apps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| number of records to skip (for pagination) | [optional] [default to 0]
 **order** | **str**| field name to order results by (use &#39;-&#39; prefix for descending, e.g. &#39;-id&#39;) | [optional] 

### Return type

[**List[App]**](App.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid status value |  -  |
**401** | Authentication information is missing or invalid |  * WWW_Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_app_by_id**
> App set_app_by_id(app_id=app_id, limit=limit)

Create or Update Application

Create or Update App by ID

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.app import App
from multiflexi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/VitexSoftware/MultiFlexi/1.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = multiflexi_client.Configuration(
    host = "https://virtserver.swaggerhub.com/VitexSoftware/MultiFlexi/1.0.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = multiflexi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with multiflexi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = multiflexi_client.AppApi(api_client)
    app_id = 56 # int | ID of app to return (optional)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Create or Update Application
        api_response = api_instance.set_app_by_id(app_id=app_id, limit=limit)
        print("The response of AppApi->set_app_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->set_app_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**| ID of app to return | [optional] 
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

[**App**](App.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | application created or updated |  -  |
**400** | Invalid ID supplied |  -  |
**401** | Authentication information is missing or invalid |  * WWW_Authenticate -  <br>  |
**404** | App not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

