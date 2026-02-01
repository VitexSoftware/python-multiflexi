# multiflexi_client.CompanyApi

All URIs are relative to *https://virtserver.swaggerhub.com/VitexSoftware/MultiFlexi/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_company_by_id**](CompanyApi.md#get_company_by_id) | **GET** /company/{companyId}.{suffix} | Get Company by ID
[**list_companies**](CompanyApi.md#list_companies) | **GET** /companies.{suffix} | Show All Companies
[**set_company_by_id**](CompanyApi.md#set_company_by_id) | **POST** /company/ | Create or Update Company


# **get_company_by_id**
> Company get_company_by_id(company_id, suffix, limit=limit)

Get Company by ID

Returns a single Company

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.company import Company
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
    api_instance = multiflexi_client.CompanyApi(api_client)
    company_id = 56 # int | ID of Company to return
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Get Company by ID
        api_response = api_instance.get_company_by_id(company_id, suffix, limit=limit)
        print("The response of CompanyApi->get_company_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyApi->get_company_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| ID of Company to return | 
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

[**Company**](Company.md)

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
**404** | Company not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_companies**
> List[Company] list_companies(suffix, limit=limit, offset=offset, order=order)

Show All Companies

All Companies registered

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.company import Company
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
    api_instance = multiflexi_client.CompanyApi(api_client)
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)
    offset = 0 # int | number of records to skip (for pagination) (optional) (default to 0)
    order = '-id' # str | field name to order results by (use '-' prefix for descending, e.g. '-id') (optional)

    try:
        # Show All Companies
        api_response = api_instance.list_companies(suffix, limit=limit, offset=offset, order=order)
        print("The response of CompanyApi->list_companies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyApi->list_companies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| number of records to skip (for pagination) | [optional] [default to 0]
 **order** | **str**| field name to order results by (use &#39;-&#39; prefix for descending, e.g. &#39;-id&#39;) | [optional] 

### Return type

[**List[Company]**](Company.md)

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

# **set_company_by_id**
> Company set_company_by_id(company_id=company_id, limit=limit)

Create or Update Company

Create or Update Company by ID

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.company import Company
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
    api_instance = multiflexi_client.CompanyApi(api_client)
    company_id = 56 # int | ID of Company to return (optional)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Create or Update Company
        api_response = api_instance.set_company_by_id(company_id=company_id, limit=limit)
        print("The response of CompanyApi->set_company_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyApi->set_company_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| ID of Company to return | [optional] 
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

[**Company**](Company.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Company created or updated |  -  |
**400** | Invalid ID supplied |  -  |
**401** | Authentication information is missing or invalid |  * WWW_Authenticate -  <br>  |
**404** | Company not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

