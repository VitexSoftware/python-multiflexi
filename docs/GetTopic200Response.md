# GetTopic200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**color** | **str** |  | [optional] 

## Example

```python
from multiflexi_client.models.get_topic200_response import GetTopic200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTopic200Response from a JSON string
get_topic200_response_instance = GetTopic200Response.from_json(json)
# print the JSON string representation of the object
print(GetTopic200Response.to_json())

# convert the object into a dict
get_topic200_response_dict = get_topic200_response_instance.to_dict()
# create an instance of GetTopic200Response from a dict
get_topic200_response_from_dict = GetTopic200Response.from_dict(get_topic200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


