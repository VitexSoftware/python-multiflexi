# multiflexi_client.RuntemplateApi

All URIs are relative to *https://virtserver.swaggerhub.com/VitexSoftware/MultiFlexi/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_run_template_by_id**](RuntemplateApi.md#get_run_template_by_id) | **GET** /runtemplate/{runTemplateId}.{suffix} | Get RunTemplate by ID
[**list_run_templates**](RuntemplateApi.md#list_run_templates) | **GET** /runtemplates.{suffix} | Show All RunTemplates
[**set_run_template_by_id**](RuntemplateApi.md#set_run_template_by_id) | **POST** /runtemplate | Create or Update RunTemplate
[**update_run_template_by_id**](RuntemplateApi.md#update_run_template_by_id) | **POST** /runtemplate/{runTemplateId}.{suffix} | Update RunTemplate by ID


# **get_run_template_by_id**
> RunTemplate get_run_template_by_id(run_template_id, suffix, limit=limit)

Get RunTemplate by ID

Returns a single RunTemplate

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.run_template import RunTemplate
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
    api_instance = multiflexi_client.RuntemplateApi(api_client)
    run_template_id = 56 # int | ID of RunTemplate to return
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Get RunTemplate by ID
        api_response = api_instance.get_run_template_by_id(run_template_id, suffix, limit=limit)
        print("The response of RuntemplateApi->get_run_template_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntemplateApi->get_run_template_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_template_id** | **int**| ID of RunTemplate to return | 
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

[**RunTemplate**](RunTemplate.md)

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
**404** | RunTemplate not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_run_templates**
> List[RunTemplate] list_run_templates(suffix, limit=limit, offset=offset, order=order)

Show All RunTemplates

All RunTemplates registered

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.run_template import RunTemplate
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
    api_instance = multiflexi_client.RuntemplateApi(api_client)
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)
    offset = 0 # int | number of records to skip (for pagination) (optional) (default to 0)
    order = '-id' # str | field name to order results by (use '-' prefix for descending, e.g. '-id') (optional)

    try:
        # Show All RunTemplates
        api_response = api_instance.list_run_templates(suffix, limit=limit, offset=offset, order=order)
        print("The response of RuntemplateApi->list_run_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntemplateApi->list_run_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| number of records to skip (for pagination) | [optional] [default to 0]
 **order** | **str**| field name to order results by (use &#39;-&#39; prefix for descending, e.g. &#39;-id&#39;) | [optional] 

### Return type

[**List[RunTemplate]**](RunTemplate.md)

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

# **set_run_template_by_id**
> RunTemplate set_run_template_by_id(run_template_id=run_template_id, limit=limit)

Create or Update RunTemplate

Create or Update RunTemplate by ID

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.run_template import RunTemplate
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
    api_instance = multiflexi_client.RuntemplateApi(api_client)
    run_template_id = 56 # int | ID of RunTemplate to return (optional)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Create or Update RunTemplate
        api_response = api_instance.set_run_template_by_id(run_template_id=run_template_id, limit=limit)
        print("The response of RuntemplateApi->set_run_template_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntemplateApi->set_run_template_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_template_id** | **int**| ID of RunTemplate to return | [optional] 
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

[**RunTemplate**](RunTemplate.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | RunTemplate created or updated |  -  |
**400** | Invalid ID supplied |  -  |
**401** | Authentication information is missing or invalid |  * WWW_Authenticate -  <br>  |
**404** | RunTemplate not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_run_template_by_id**
> RunTemplate update_run_template_by_id(run_template_id, suffix, update_run_template_by_id_request, limit=limit)

Update RunTemplate by ID

Updates a RunTemplate. Request body must include id field matching
URL parameter. Only fields present in request body will be updated
(partial update).


### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.run_template import RunTemplate
from multiflexi_client.models.update_run_template_by_id_request import UpdateRunTemplateByIdRequest
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
    api_instance = multiflexi_client.RuntemplateApi(api_client)
    run_template_id = 56 # int | ID of RunTemplate to update
    suffix = html # str | force format suffix (default to html)
    update_run_template_by_id_request = {"id":15,"active":1} # UpdateRunTemplateByIdRequest | 
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Update RunTemplate by ID
        api_response = api_instance.update_run_template_by_id(run_template_id, suffix, update_run_template_by_id_request, limit=limit)
        print("The response of RuntemplateApi->update_run_template_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntemplateApi->update_run_template_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_template_id** | **int**| ID of RunTemplate to update | 
 **suffix** | **str**| force format suffix | [default to html]
 **update_run_template_by_id_request** | [**UpdateRunTemplateByIdRequest**](UpdateRunTemplateByIdRequest.md)|  | 
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

[**RunTemplate**](RunTemplate.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | RunTemplate updated successfully |  -  |
**400** | Invalid ID supplied or ID mismatch |  -  |
**401** | Authentication information is missing or invalid |  * WWW_Authenticate -  <br>  |
**404** | RunTemplate not found |  -  |
**500** | Update failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

