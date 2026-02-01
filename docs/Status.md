# Status


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**companies** | **int** |  | [optional] 
**apps** | **int** |  | [optional] 
**runtemplates** | **int** |  | [optional] 
**topics** | **int** |  | [optional] 
**credentials** | **int** |  | [optional] 
**credentialtypes** | **int** |  | [optional] 
**database** | **str** |  | [optional] 
**daemon** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from multiflexi_client.models.status import Status

# TODO update the JSON string below
json = "{}"
# create an instance of Status from a JSON string
status_instance = Status.from_json(json)
# print the JSON string representation of the object
print(Status.to_json())

# convert the object into a dict
status_dict = status_instance.to_dict()
# create an instance of Status from a dict
status_from_dict = Status.from_dict(status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


