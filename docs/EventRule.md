# EventRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**event_source_id** | **int** | References EventSource | [optional] 
**evidence** | **str** | Evidence type pattern to match (null &#x3D; any) | [optional] 
**operation** | **str** | Operation to match | [optional] [default to 'any']
**runtemplate_id** | **int** | RunTemplate ID to trigger when rule matches | [optional] 
**priority** | **int** | Higher priority rules are evaluated first | [optional] [default to 0]
**enabled** | **bool** | Whether this rule is active | [optional] [default to True]
**env_mapping** | **str** | JSON mapping of change fields to environment variables | [optional] 
**created** | **datetime** |  | [optional] 
**modified** | **datetime** |  | [optional] 

## Example

```python
from multiflexi_client.models.event_rule import EventRule

# TODO update the JSON string below
json = "{}"
# create an instance of EventRule from a JSON string
event_rule_instance = EventRule.from_json(json)
# print the JSON string representation of the object
print(EventRule.to_json())

# convert the object into a dict
event_rule_dict = event_rule_instance.to_dict()
# create an instance of EventRule from a dict
event_rule_from_dict = EventRule.from_dict(event_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


