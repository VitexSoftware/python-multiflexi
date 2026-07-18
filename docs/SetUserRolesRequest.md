# SetUserRolesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | **List[str]** | List of RBAC role names to assign | 
**assigned_by** | **int** | Optional user ID of the person performing the assignment | [optional] 

## Example

```python
from multiflexi_client.models.set_user_roles_request import SetUserRolesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetUserRolesRequest from a JSON string
set_user_roles_request_instance = SetUserRolesRequest.from_json(json)
# print the JSON string representation of the object
print(SetUserRolesRequest.to_json())

# convert the object into a dict
set_user_roles_request_dict = set_user_roles_request_instance.to_dict()
# create an instance of SetUserRolesRequest from a dict
set_user_roles_request_from_dict = SetUserRolesRequest.from_dict(set_user_roles_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


