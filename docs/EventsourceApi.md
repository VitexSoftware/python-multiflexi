# multiflexi_client.EventsourceApi

All URIs are relative to *https://virtserver.swaggerhub.com/VitexSoftware/MultiFlexi/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_event_source_by_id**](EventsourceApi.md#delete_event_source_by_id) | **DELETE** /eventsource/{eventSourceId}.{suffix} | Delete EventSource by ID
[**get_event_source_by_id**](EventsourceApi.md#get_event_source_by_id) | **GET** /eventsource/{eventSourceId}.{suffix} | Get EventSource by ID
[**list_event_sources**](EventsourceApi.md#list_event_sources) | **GET** /eventsources.{suffix} | Show All EventSources
[**set_event_source_by_id**](EventsourceApi.md#set_event_source_by_id) | **POST** /eventsource/ | Create or Update EventSource
[**test_event_source_connection**](EventsourceApi.md#test_event_source_connection) | **POST** /eventsource/{eventSourceId}/test.{suffix} | Test EventSource connection


# **delete_event_source_by_id**
> delete_event_source_by_id(event_source_id, suffix, limit=limit)

Delete EventSource by ID

Remove an EventSource

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
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
    api_instance = multiflexi_client.EventsourceApi(api_client)
    event_source_id = 56 # int | ID of EventSource to delete
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Delete EventSource by ID
        api_instance.delete_event_source_by_id(event_source_id, suffix, limit=limit)
    except Exception as e:
        print("Exception when calling EventsourceApi->delete_event_source_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_source_id** | **int**| ID of EventSource to delete | 
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EventSource deleted |  -  |
**401** | Authentication information is missing or invalid |  * WWW_Authenticate -  <br>  |
**404** | EventSource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_source_by_id**
> EventSource get_event_source_by_id(event_source_id, suffix, limit=limit)

Get EventSource by ID

Returns a single EventSource (webhook adapter database connection)

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.event_source import EventSource
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
    api_instance = multiflexi_client.EventsourceApi(api_client)
    event_source_id = 56 # int | ID of EventSource to return
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Get EventSource by ID
        api_response = api_instance.get_event_source_by_id(event_source_id, suffix, limit=limit)
        print("The response of EventsourceApi->get_event_source_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsourceApi->get_event_source_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_source_id** | **int**| ID of EventSource to return | 
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

[**EventSource**](EventSource.md)

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
**404** | EventSource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_event_sources**
> List[EventSource] list_event_sources(suffix, limit=limit, offset=offset, order=order)

Show All EventSources

All EventSources registered

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.event_source import EventSource
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
    api_instance = multiflexi_client.EventsourceApi(api_client)
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)
    offset = 0 # int | number of records to skip (for pagination) (optional) (default to 0)
    order = '-id' # str | field name to order results by (use '-' prefix for descending, e.g. '-id') (optional)

    try:
        # Show All EventSources
        api_response = api_instance.list_event_sources(suffix, limit=limit, offset=offset, order=order)
        print("The response of EventsourceApi->list_event_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsourceApi->list_event_sources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| number of records to skip (for pagination) | [optional] [default to 0]
 **order** | **str**| field name to order results by (use &#39;-&#39; prefix for descending, e.g. &#39;-id&#39;) | [optional] 

### Return type

[**List[EventSource]**](EventSource.md)

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

# **set_event_source_by_id**
> EventSource set_event_source_by_id(event_source, event_source_id=event_source_id, limit=limit)

Create or Update EventSource

Create or Update EventSource (webhook adapter database connection)

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.event_source import EventSource
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
    api_instance = multiflexi_client.EventsourceApi(api_client)
    event_source = multiflexi_client.EventSource() # EventSource | 
    event_source_id = 56 # int | ID of EventSource to update (omit for create) (optional)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Create or Update EventSource
        api_response = api_instance.set_event_source_by_id(event_source, event_source_id=event_source_id, limit=limit)
        print("The response of EventsourceApi->set_event_source_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsourceApi->set_event_source_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_source** | [**EventSource**](EventSource.md)|  | 
 **event_source_id** | **int**| ID of EventSource to update (omit for create) | [optional] 
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

[**EventSource**](EventSource.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | EventSource created or updated |  -  |
**400** | Invalid data supplied |  -  |
**401** | Authentication information is missing or invalid |  * WWW_Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_event_source_connection**
> TestEventSourceConnection200Response test_event_source_connection(event_source_id, suffix, limit=limit)

Test EventSource connection

Test the database connection of an EventSource

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.test_event_source_connection200_response import TestEventSourceConnection200Response
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
    api_instance = multiflexi_client.EventsourceApi(api_client)
    event_source_id = 56 # int | ID of EventSource to test
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Test EventSource connection
        api_response = api_instance.test_event_source_connection(event_source_id, suffix, limit=limit)
        print("The response of EventsourceApi->test_event_source_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsourceApi->test_event_source_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_source_id** | **int**| ID of EventSource to test | 
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

[**TestEventSourceConnection200Response**](TestEventSourceConnection200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connection test result |  -  |
**401** | Authentication information is missing or invalid |  * WWW_Authenticate -  <br>  |
**404** | EventSource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

