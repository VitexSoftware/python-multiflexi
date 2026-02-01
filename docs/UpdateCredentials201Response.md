# UpdateCredentials201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**company_id** | **int** |  | [optional] 
**type** | **str** | Type of credential | [optional] 

## Example

```python
from multiflexi_client.models.update_credentials201_response import UpdateCredentials201Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCredentials201Response from a JSON string
update_credentials201_response_instance = UpdateCredentials201Response.from_json(json)
# print the JSON string representation of the object
print(UpdateCredentials201Response.to_json())

# convert the object into a dict
update_credentials201_response_dict = update_credentials201_response_instance.to_dict()
# create an instance of UpdateCredentials201Response from a dict
update_credentials201_response_from_dict = UpdateCredentials201Response.from_dict(update_credentials201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


