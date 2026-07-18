# AssignUserToCompanyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | ID of the user to assign | 
**role** | **str** | Access role in the company (e.g. viewer, manager, admin) | [optional] [default to 'viewer']

## Example

```python
from multiflexi_client.models.assign_user_to_company_request import AssignUserToCompanyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignUserToCompanyRequest from a JSON string
assign_user_to_company_request_instance = AssignUserToCompanyRequest.from_json(json)
# print the JSON string representation of the object
print(AssignUserToCompanyRequest.to_json())

# convert the object into a dict
assign_user_to_company_request_dict = assign_user_to_company_request_instance.to_dict()
# create an instance of AssignUserToCompanyRequest from a dict
assign_user_to_company_request_from_dict = AssignUserToCompanyRequest.from_dict(assign_user_to_company_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


