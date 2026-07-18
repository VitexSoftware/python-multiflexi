# TestEventSourceConnection200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reachable** | **bool** | Whether the adapter database is reachable | [optional] 
**message** | **str** | Test result message | [optional] 

## Example

```python
from multiflexi_client.models.test_event_source_connection200_response import TestEventSourceConnection200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TestEventSourceConnection200Response from a JSON string
test_event_source_connection200_response_instance = TestEventSourceConnection200Response.from_json(json)
# print the JSON string representation of the object
print(TestEventSourceConnection200Response.to_json())

# convert the object into a dict
test_event_source_connection200_response_dict = test_event_source_connection200_response_instance.to_dict()
# create an instance of TestEventSourceConnection200Response from a dict
test_event_source_connection200_response_from_dict = TestEventSourceConnection200Response.from_dict(test_event_source_connection200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


