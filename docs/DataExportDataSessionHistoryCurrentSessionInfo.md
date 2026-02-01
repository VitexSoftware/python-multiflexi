# DataExportDataSessionHistoryCurrentSessionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** |  | [optional] 
**started_at** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 

## Example

```python
from multiflexi_client.models.data_export_data_session_history_current_session_info import DataExportDataSessionHistoryCurrentSessionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataExportDataSessionHistoryCurrentSessionInfo from a JSON string
data_export_data_session_history_current_session_info_instance = DataExportDataSessionHistoryCurrentSessionInfo.from_json(json)
# print the JSON string representation of the object
print(DataExportDataSessionHistoryCurrentSessionInfo.to_json())

# convert the object into a dict
data_export_data_session_history_current_session_info_dict = data_export_data_session_history_current_session_info_instance.to_dict()
# create an instance of DataExportDataSessionHistoryCurrentSessionInfo from a dict
data_export_data_session_history_current_session_info_from_dict = DataExportDataSessionHistoryCurrentSessionInfo.from_dict(data_export_data_session_history_current_session_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


