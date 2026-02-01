# DataExportDataActivityLogsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_id** | **int** |  | [optional] 
**company_id** | **int** |  | [optional] 
**application_id** | **int** |  | [optional] 
**severity** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from multiflexi_client.models.data_export_data_activity_logs_inner import DataExportDataActivityLogsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DataExportDataActivityLogsInner from a JSON string
data_export_data_activity_logs_inner_instance = DataExportDataActivityLogsInner.from_json(json)
# print the JSON string representation of the object
print(DataExportDataActivityLogsInner.to_json())

# convert the object into a dict
data_export_data_activity_logs_inner_dict = data_export_data_activity_logs_inner_instance.to_dict()
# create an instance of DataExportDataActivityLogsInner from a dict
data_export_data_activity_logs_inner_from_dict = DataExportDataActivityLogsInner.from_dict(data_export_data_activity_logs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


