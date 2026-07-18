# multiflexi_client.JobApi

All URIs are relative to *https://virtserver.swaggerhub.com/VitexSoftware/MultiFlexi/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getjob_by_id**](JobApi.md#getjob_by_id) | **GET** /job/{jobId}.{suffix} | Get job by ID
[**listjobs**](JobApi.md#listjobs) | **GET** /jobs.{suffix} | Show All jobs
[**setjob_by_id**](JobApi.md#setjob_by_id) | **POST** /job/ | Schedule a job from a RunTemplate


# **getjob_by_id**
> Job getjob_by_id(job_id, suffix, limit=limit)

Get job by ID

Returns a single job

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.job import Job
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
    api_instance = multiflexi_client.JobApi(api_client)
    job_id = 56 # int | ID of app to return
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Get job by ID
        api_response = api_instance.getjob_by_id(job_id, suffix, limit=limit)
        print("The response of JobApi->getjob_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->getjob_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| ID of app to return | 
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

[**Job**](Job.md)

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

# **listjobs**
> Dict[str, Job] listjobs(suffix, limit=limit, offset=offset, order=order)

Show All jobs

All job jobs registered

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.job import Job
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
    api_instance = multiflexi_client.JobApi(api_client)
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)
    offset = 0 # int | number of records to skip (for pagination) (optional) (default to 0)
    order = '-id' # str | field name to order results by (use '-' prefix for descending, e.g. '-id') (optional)

    try:
        # Show All jobs
        api_response = api_instance.listjobs(suffix, limit=limit, offset=offset, order=order)
        print("The response of JobApi->listjobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->listjobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| number of records to skip (for pagination) | [optional] [default to 0]
 **order** | **str**| field name to order results by (use &#39;-&#39; prefix for descending, e.g. &#39;-id&#39;) | [optional] 

### Return type

[**Dict[str, Job]**](Job.md)

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

# **setjob_by_id**
> Job setjob_by_id(setjob_by_id_request, job_id=job_id, limit=limit)

Schedule a job from a RunTemplate

Schedules a job for an existing RunTemplate (mirrors `multiflexi-cli run-template:schedule`). Used as the inbound trigger by external orchestrators such as Node-RED.

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.job import Job
from multiflexi_client.models.setjob_by_id_request import SetjobByIdRequest
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
    api_instance = multiflexi_client.JobApi(api_client)
    setjob_by_id_request = multiflexi_client.SetjobByIdRequest() # SetjobByIdRequest | RunTemplate scheduling request
    job_id = 56 # int | ID of app to return (optional)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Schedule a job from a RunTemplate
        api_response = api_instance.setjob_by_id(setjob_by_id_request, job_id=job_id, limit=limit)
        print("The response of JobApi->setjob_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->setjob_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setjob_by_id_request** | [**SetjobByIdRequest**](SetjobByIdRequest.md)| RunTemplate scheduling request | 
 **job_id** | **int**| ID of app to return | [optional] 
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Job scheduled |  -  |
**400** | Invalid request body |  -  |
**401** | Authentication information is missing or invalid |  * WWW_Authenticate -  <br>  |
**404** | RunTemplate not found |  -  |
**409** | RunTemplate is not active |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

