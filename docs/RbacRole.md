# RbacRole

RBAC role definition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** | Machine-readable role name | [optional] 
**display_name** | **str** | Human-readable role label | [optional] 
**is_active** | **bool** | Whether the role is currently active | [optional] [default to True]
**assigned_at** | **datetime** | When the role was assigned to the user (present on user-role responses) | [optional] 
**expires_at** | **datetime** | Optional expiry timestamp for the role assignment | [optional] 

## Example

```python
from multiflexi_client.models.rbac_role import RbacRole

# TODO update the JSON string below
json = "{}"
# create an instance of RbacRole from a JSON string
rbac_role_instance = RbacRole.from_json(json)
# print the JSON string representation of the object
print(RbacRole.to_json())

# convert the object into a dict
rbac_role_dict = rbac_role_instance.to_dict()
# create an instance of RbacRole from a dict
rbac_role_from_dict = RbacRole.from_dict(rbac_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


