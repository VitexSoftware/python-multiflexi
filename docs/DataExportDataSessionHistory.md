# DataExportDataSessionHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** |  | [optional] 
**current_session_info** | [**DataExportDataSessionHistoryCurrentSessionInfo**](DataExportDataSessionHistoryCurrentSessionInfo.md) |  | [optional] 

## Example

```python
from multiflexi_client.models.data_export_data_session_history import DataExportDataSessionHistory

# TODO update the JSON string below
json = "{}"
# create an instance of DataExportDataSessionHistory from a JSON string
data_export_data_session_history_instance = DataExportDataSessionHistory.from_json(json)
# print the JSON string representation of the object
print(DataExportDataSessionHistory.to_json())

# convert the object into a dict
data_export_data_session_history_dict = data_export_data_session_history_instance.to_dict()
# create an instance of DataExportDataSessionHistory from a dict
data_export_data_session_history_from_dict = DataExportDataSessionHistory.from_dict(data_export_data_session_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


