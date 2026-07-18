# multiflexi_client.UserCompanyApi

All URIs are relative to *https://virtserver.swaggerhub.com/VitexSoftware/MultiFlexi/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_user_to_company**](UserCompanyApi.md#assign_user_to_company) | **POST** /company/{companyId}/user/ | Assign a user to a company
[**list_company_users**](UserCompanyApi.md#list_company_users) | **GET** /company/{companyId}/users.{suffix} | List users assigned to a company
[**unassign_user_from_company**](UserCompanyApi.md#unassign_user_from_company) | **DELETE** /company/{companyId}/user/{userId} | Remove a user from a company


# **assign_user_to_company**
> CompanyUser assign_user_to_company(company_id, assign_user_to_company_request)

Assign a user to a company

Create or update the role of a user in a company (upsert)

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.assign_user_to_company_request import AssignUserToCompanyRequest
from multiflexi_client.models.company_user import CompanyUser
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
    api_instance = multiflexi_client.UserCompanyApi(api_client)
    company_id = 56 # int | ID of the company
    assign_user_to_company_request = multiflexi_client.AssignUserToCompanyRequest() # AssignUserToCompanyRequest | 

    try:
        # Assign a user to a company
        api_response = api_instance.assign_user_to_company(company_id, assign_user_to_company_request)
        print("The response of UserCompanyApi->assign_user_to_company:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCompanyApi->assign_user_to_company: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| ID of the company | 
 **assign_user_to_company_request** | [**AssignUserToCompanyRequest**](AssignUserToCompanyRequest.md)|  | 

### Return type

[**CompanyUser**](CompanyUser.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User assigned to company |  -  |
**400** | Invalid request |  -  |
**401** | Authentication information is missing or invalid |  * WWW_Authenticate -  <br>  |
**404** | Company or user not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_company_users**
> List[ListCompanyUsers200ResponseInner] list_company_users(company_id, suffix, limit=limit, offset=offset, order=order)

List users assigned to a company

Returns users with their assigned roles in the given company

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.list_company_users200_response_inner import ListCompanyUsers200ResponseInner
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
    api_instance = multiflexi_client.UserCompanyApi(api_client)
    company_id = 56 # int | ID of the company
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)
    offset = 0 # int | number of records to skip (for pagination) (optional) (default to 0)
    order = '-id' # str | field name to order results by (use '-' prefix for descending, e.g. '-id') (optional)

    try:
        # List users assigned to a company
        api_response = api_instance.list_company_users(company_id, suffix, limit=limit, offset=offset, order=order)
        print("The response of UserCompanyApi->list_company_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCompanyApi->list_company_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| ID of the company | 
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]
 **offset** | **int**| number of records to skip (for pagination) | [optional] [default to 0]
 **order** | **str**| field name to order results by (use &#39;-&#39; prefix for descending, e.g. &#39;-id&#39;) | [optional] 

### Return type

[**List[ListCompanyUsers200ResponseInner]**](ListCompanyUsers200ResponseInner.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Invalid ID supplied |  -  |
**401** | Authentication information is missing or invalid |  * WWW_Authenticate -  <br>  |
**404** | Company not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_user_from_company**
> UnassignUserFromCompany200Response unassign_user_from_company(company_id, user_id)

Remove a user from a company

Unassign the specified user from the company

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.unassign_user_from_company200_response import UnassignUserFromCompany200Response
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
    api_instance = multiflexi_client.UserCompanyApi(api_client)
    company_id = 56 # int | ID of the company
    user_id = 56 # int | ID of the user to remove

    try:
        # Remove a user from a company
        api_response = api_instance.unassign_user_from_company(company_id, user_id)
        print("The response of UserCompanyApi->unassign_user_from_company:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCompanyApi->unassign_user_from_company: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| ID of the company | 
 **user_id** | **int**| ID of the user to remove | 

### Return type

[**UnassignUserFromCompany200Response**](UnassignUserFromCompany200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User unassigned (or was not assigned) |  -  |
**400** | Invalid ID supplied |  -  |
**401** | Authentication information is missing or invalid |  * WWW_Authenticate -  <br>  |
**404** | Company or user not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

