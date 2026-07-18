# SetjobByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**runtemplate_id** | **int** | RunTemplate to schedule | 
**scheduled** | **str** | \&quot;now\&quot; or a \&quot;Y-m-d H:i:s\&quot; timestamp | [optional] [default to 'now']
**executor** | **str** | Overrides the RunTemplate executor | [optional] 
**env** | **Dict[str, str]** | Environment variable overrides (KEY&#x3D;&gt;VALUE) injected into the job | [optional] 

## Example

```python
from multiflexi_client.models.setjob_by_id_request import SetjobByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetjobByIdRequest from a JSON string
setjob_by_id_request_instance = SetjobByIdRequest.from_json(json)
# print the JSON string representation of the object
print(SetjobByIdRequest.to_json())

# convert the object into a dict
setjob_by_id_request_dict = setjob_by_id_request_instance.to_dict()
# create an instance of SetjobByIdRequest from a dict
setjob_by_id_request_from_dict = SetjobByIdRequest.from_dict(setjob_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


