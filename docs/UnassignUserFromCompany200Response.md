# UnassignUserFromCompany200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**deleted** | **int** | Number of rows removed (0 if user was not assigned) | [optional] 

## Example

```python
from multiflexi_client.models.unassign_user_from_company200_response import UnassignUserFromCompany200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UnassignUserFromCompany200Response from a JSON string
unassign_user_from_company200_response_instance = UnassignUserFromCompany200Response.from_json(json)
# print the JSON string representation of the object
print(UnassignUserFromCompany200Response.to_json())

# convert the object into a dict
unassign_user_from_company200_response_dict = unassign_user_from_company200_response_instance.to_dict()
# create an instance of UnassignUserFromCompany200Response from a dict
unassign_user_from_company200_response_from_dict = UnassignUserFromCompany200Response.from_dict(unassign_user_from_company200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


