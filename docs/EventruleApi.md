# multiflexi_client.EventruleApi

All URIs are relative to *https://virtserver.swaggerhub.com/VitexSoftware/MultiFlexi/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_event_rule_by_id**](EventruleApi.md#delete_event_rule_by_id) | **DELETE** /eventrule/{eventRuleId}.{suffix} | Delete EventRule by ID
[**get_event_rule_by_id**](EventruleApi.md#get_event_rule_by_id) | **GET** /eventrule/{eventRuleId}.{suffix} | Get EventRule by ID
[**list_event_rules**](EventruleApi.md#list_event_rules) | **GET** /eventrules.{suffix} | Show All EventRules
[**set_event_rule_by_id**](EventruleApi.md#set_event_rule_by_id) | **POST** /eventrule/ | Create or Update EventRule


# **delete_event_rule_by_id**
> delete_event_rule_by_id(event_rule_id, suffix, limit=limit)

Delete EventRule by ID

Remove an EventRule

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
    api_instance = multiflexi_client.EventruleApi(api_client)
    event_rule_id = 56 # int | ID of EventRule to delete
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Delete EventRule by ID
        api_instance.delete_event_rule_by_id(event_rule_id, suffix, limit=limit)
    except Exception as e:
        print("Exception when calling EventruleApi->delete_event_rule_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_rule_id** | **int**| ID of EventRule to delete | 
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
**200** | EventRule deleted |  -  |
**401** | Authentication information is missing or invalid |  * WWW_Authenticate -  <br>  |
**404** | EventRule not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_rule_by_id**
> EventRule get_event_rule_by_id(event_rule_id, suffix, limit=limit)

Get EventRule by ID

Returns a single EventRule (event-to-RunTemplate mapping)

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.event_rule import EventRule
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
    api_instance = multiflexi_client.EventruleApi(api_client)
    event_rule_id = 56 # int | ID of EventRule to return
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Get EventRule by ID
        api_response = api_instance.get_event_rule_by_id(event_rule_id, suffix, limit=limit)
        print("The response of EventruleApi->get_event_rule_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventruleApi->get_event_rule_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_rule_id** | **int**| ID of EventRule to return | 
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

[**EventRule**](EventRule.md)

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
**404** | EventRule not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_event_rules**
> List[EventRule] list_event_rules(suffix, limit=limit, offset=offset, order=order)

Show All EventRules

All EventRules registered

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.event_rule import EventRule
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
    api_instance = multiflexi_client.EventruleApi(api_client)
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)
    offset = 0 # int | number of records to skip (for pagination) (optional) (default to 0)
    order = '-id' # str | field name to order results by (use '-' prefix for descending, e.g. '-id') (optional)

    try:
        # Show All EventRules
        api_response = api_instance.list_event_rules(suffix, limit=limit, offset=offset, order=order)
        print("The response of EventruleApi->list_event_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventruleApi->list_event_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| number of records to skip (for pagination) | [optional] [default to 0]
 **order** | **str**| field name to order results by (use &#39;-&#39; prefix for descending, e.g. &#39;-id&#39;) | [optional] 

### Return type

[**List[EventRule]**](EventRule.md)

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

# **set_event_rule_by_id**
> EventRule set_event_rule_by_id(event_rule, event_rule_id=event_rule_id, limit=limit)

Create or Update EventRule

Create or Update EventRule (event-to-RunTemplate mapping)

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.event_rule import EventRule
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
    api_instance = multiflexi_client.EventruleApi(api_client)
    event_rule = multiflexi_client.EventRule() # EventRule | 
    event_rule_id = 56 # int | ID of EventRule to update (omit for create) (optional)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Create or Update EventRule
        api_response = api_instance.set_event_rule_by_id(event_rule, event_rule_id=event_rule_id, limit=limit)
        print("The response of EventruleApi->set_event_rule_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventruleApi->set_event_rule_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_rule** | [**EventRule**](EventRule.md)|  | 
 **event_rule_id** | **int**| ID of EventRule to update (omit for create) | [optional] 
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

[**EventRule**](EventRule.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | EventRule created or updated |  -  |
**400** | Invalid data supplied |  -  |
**401** | Authentication information is missing or invalid |  * WWW_Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

