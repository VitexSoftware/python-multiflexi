# multiflexi_client.TaskApi

All URIs are relative to *https://virtserver.swaggerhub.com/VitexSoftware/MultiFlexi/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_task_by_id**](TaskApi.md#get_task_by_id) | **GET** /task/{taskId}.{suffix} | Get Task by ID
[**list_tasks**](TaskApi.md#list_tasks) | **GET** /tasks.{suffix} | List Tasks


# **get_task_by_id**
> Task get_task_by_id(task_id, suffix)

Get Task by ID

Returns a single task together with its job attempt history.

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.task import Task
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
    api_instance = multiflexi_client.TaskApi(api_client)
    task_id = 56 # int | 
    suffix = json # str |  (default to json)

    try:
        # Get Task by ID
        api_response = api_instance.get_task_by_id(task_id, suffix)
        print("The response of TaskApi->get_task_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->get_task_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**|  | 
 **suffix** | **str**|  | [default to json]

### Return type

[**Task**](Task.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**401** | Authentication information is missing or invalid |  * WWW_Authenticate -  <br>  |
**404** | Task not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tasks**
> List[Task] list_tasks(suffix, state=state, runtemplate_id=runtemplate_id, var_from=var_from, to=to, limit=limit)

List Tasks

Returns a list of tasks, optionally filtered by state or runtemplate_id.

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.task import Task
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
    api_instance = multiflexi_client.TaskApi(api_client)
    suffix = json # str |  (default to json)
    state = 'state_example' # str |  (optional)
    runtemplate_id = 56 # int |  (optional)
    var_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # List Tasks
        api_response = api_instance.list_tasks(suffix, state=state, runtemplate_id=runtemplate_id, var_from=var_from, to=to, limit=limit)
        print("The response of TaskApi->list_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->list_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suffix** | **str**|  | [default to json]
 **state** | **str**|  | [optional] 
 **runtemplate_id** | **int**|  | [optional] 
 **var_from** | **datetime**|  | [optional] 
 **to** | **datetime**|  | [optional] 
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

[**List[Task]**](Task.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**401** | Authentication information is missing or invalid |  * WWW_Authenticate -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

