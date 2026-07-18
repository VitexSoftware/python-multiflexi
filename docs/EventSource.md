# EventSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** | Human-readable name for this event source | [optional] 
**adapter_type** | **str** | Type of webhook adapter | [optional] 
**db_connection** | **str** | Database driver | [optional] [default to 'mysql']
**db_host** | **str** | Database host | [optional] [default to 'localhost']
**db_port** | **str** | Database port | [optional] [default to '3306']
**db_database** | **str** | Database name | [optional] 
**db_username** | **str** | Database username | [optional] 
**db_password** | **str** | Database password | [optional] 
**poll_interval** | **int** | How often to poll for new changes (seconds) | [optional] [default to 60]
**enabled** | **bool** | Whether this source is active | [optional] [default to True]
**last_processed_id** | **int** | Last processed change inversion ID | [optional] [default to 0]
**created** | **datetime** |  | [optional] 
**modified** | **datetime** |  | [optional] 

## Example

```python
from multiflexi_client.models.event_source import EventSource

# TODO update the JSON string below
json = "{}"
# create an instance of EventSource from a JSON string
event_source_instance = EventSource.from_json(json)
# print the JSON string representation of the object
print(EventSource.to_json())

# convert the object into a dict
event_source_dict = event_source_instance.to_dict()
# create an instance of EventSource from a dict
event_source_from_dict = EventSource.from_dict(event_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


