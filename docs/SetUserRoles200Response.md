# SetUserRoles200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**replace** | **bool** |  | [optional] 
**roles** | **List[str]** |  | [optional] 
**role_details** | [**List[RbacRole]**](RbacRole.md) |  | [optional] 

## Example

```python
from multiflexi_client.models.set_user_roles200_response import SetUserRoles200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SetUserRoles200Response from a JSON string
set_user_roles200_response_instance = SetUserRoles200Response.from_json(json)
# print the JSON string representation of the object
print(SetUserRoles200Response.to_json())

# convert the object into a dict
set_user_roles200_response_dict = set_user_roles200_response_instance.to_dict()
# create an instance of SetUserRoles200Response from a dict
set_user_roles200_response_from_dict = SetUserRoles200Response.from_dict(set_user_roles200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


