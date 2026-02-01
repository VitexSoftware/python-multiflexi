# multiflexi_client.GdprApi

All URIs are relative to *https://virtserver.swaggerhub.com/VitexSoftware/MultiFlexi/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_data_export**](GdprApi.md#download_data_export) | **GET** /data-export-download | Download personal data export file
[**request_data_export**](GdprApi.md#request_data_export) | **GET** /data-export | Request personal data export (GDPR Article 15)
[**request_data_export_post**](GdprApi.md#request_data_export_post) | **POST** /data-export | Request personal data export (GDPR Article 15)


# **download_data_export**
> DataExportData download_data_export(token)

Download personal data export file

Download previously requested personal data export using secure token

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.data_export_data import DataExportData
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
    api_instance = multiflexi_client.GdprApi(api_client)
    token = 'a1b2c3d4e5f6789012345678901234567890123456789012345678901234567890123456' # str | Secure download token received from export request

    try:
        # Download personal data export file
        api_response = api_instance.download_data_export(token)
        print("The response of GdprApi->download_data_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GdprApi->download_data_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Secure download token received from export request | 

### Return type

[**DataExportData**](DataExportData.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data export file download |  -  |
**400** | Invalid or missing token |  -  |
**403** | Token expired, already used, or access denied |  -  |
**500** | Failed to generate export |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_data_export**
> RequestDataExport200Response request_data_export(action, format=format, limit=limit)

Request personal data export (GDPR Article 15)

Request export of all personal data associated with the authenticated user

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.request_data_export200_response import RequestDataExport200Response
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
    api_instance = multiflexi_client.GdprApi(api_client)
    action = 'export' # str | Action to perform
    format = json # str | Export format (required when action=export) (optional) (default to json)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Request personal data export (GDPR Article 15)
        api_response = api_instance.request_data_export(action, format=format, limit=limit)
        print("The response of GdprApi->request_data_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GdprApi->request_data_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| Action to perform | 
 **format** | **str**| Export format (required when action&#x3D;export) | [optional] [default to json]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

[**RequestDataExport200Response**](RequestDataExport200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Export request successful |  -  |
**400** | Invalid request parameters |  -  |
**401** | Authentication information is missing or invalid |  * WWW_Authenticate -  <br>  |
**403** | Access denied or suspicious activity detected |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_data_export_post**
> RequestDataExport200Response request_data_export_post(request_data_export_post_request)

Request personal data export (GDPR Article 15)

Request export of all personal data associated with the authenticated user

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.request_data_export200_response import RequestDataExport200Response
from multiflexi_client.models.request_data_export_post_request import RequestDataExportPostRequest
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
    api_instance = multiflexi_client.GdprApi(api_client)
    request_data_export_post_request = multiflexi_client.RequestDataExportPostRequest() # RequestDataExportPostRequest | 

    try:
        # Request personal data export (GDPR Article 15)
        api_response = api_instance.request_data_export_post(request_data_export_post_request)
        print("The response of GdprApi->request_data_export_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GdprApi->request_data_export_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_data_export_post_request** | [**RequestDataExportPostRequest**](RequestDataExportPostRequest.md)|  | 

### Return type

[**RequestDataExport200Response**](RequestDataExport200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Export request successful |  -  |
**400** | Invalid request parameters |  -  |
**401** | Authentication information is missing or invalid |  * WWW_Authenticate -  <br>  |
**403** | Access denied or suspicious activity detected |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

