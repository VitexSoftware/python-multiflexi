# multiflexi_client.UserRoleApi

All URIs are relative to *https://virtserver.swaggerhub.com/VitexSoftware/MultiFlexi/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_roles**](UserRoleApi.md#get_user_roles) | **GET** /user/{userId}/roles.{suffix} | Get RBAC roles for a user
[**set_user_roles**](UserRoleApi.md#set_user_roles) | **POST** /user/{userId}/roles/ | Set RBAC roles for a user


# **get_user_roles**
> List[RbacRole] get_user_roles(user_id, suffix, limit=limit)

Get RBAC roles for a user

Returns the list of active RBAC roles assigned to the specified user

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.rbac_role import RbacRole
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
    api_instance = multiflexi_client.UserRoleApi(api_client)
    user_id = 56 # int | ID of the user
    suffix = html # str | force format suffix (default to html)
    limit = 20 # int | maximum number of results to return (optional) (default to 20)

    try:
        # Get RBAC roles for a user
        api_response = api_instance.get_user_roles(user_id, suffix, limit=limit)
        print("The response of UserRoleApi->get_user_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserRoleApi->get_user_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of the user | 
 **suffix** | **str**| force format suffix | [default to html]
 **limit** | **int**| maximum number of results to return | [optional] [default to 20]

### Return type

[**List[RbacRole]**](RbacRole.md)

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
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_roles**
> SetUserRoles200Response set_user_roles(user_id, set_user_roles_request, replace=replace)

Set RBAC roles for a user

Replace (or extend) the RBAC roles assigned to a user

### Example

* Basic Authentication (basicAuth):

```python
import multiflexi_client
from multiflexi_client.models.set_user_roles200_response import SetUserRoles200Response
from multiflexi_client.models.set_user_roles_request import SetUserRolesRequest
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
    api_instance = multiflexi_client.UserRoleApi(api_client)
    user_id = 56 # int | ID of the user
    set_user_roles_request = multiflexi_client.SetUserRolesRequest() # SetUserRolesRequest | 
    replace = True # bool | When true (default), existing roles not in the supplied list are removed (optional) (default to True)

    try:
        # Set RBAC roles for a user
        api_response = api_instance.set_user_roles(user_id, set_user_roles_request, replace=replace)
        print("The response of UserRoleApi->set_user_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserRoleApi->set_user_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of the user | 
 **set_user_roles_request** | [**SetUserRolesRequest**](SetUserRolesRequest.md)|  | 
 **replace** | **bool**| When true (default), existing roles not in the supplied list are removed | [optional] [default to True]

### Return type

[**SetUserRoles200Response**](SetUserRoles200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Roles updated |  -  |
**400** | Invalid request or unknown role names |  -  |
**401** | Authentication information is missing or invalid |  * WWW_Authenticate -  <br>  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

