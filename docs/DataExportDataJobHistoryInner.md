# DataExportDataJobHistoryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** |  | [optional] 
**application_id** | **int** |  | [optional] 
**company_id** | **int** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**completed_at** | **datetime** |  | [optional] 
**exit_code** | **int** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from multiflexi_client.models.data_export_data_job_history_inner import DataExportDataJobHistoryInner

# TODO update the JSON string below
json = "{}"
# create an instance of DataExportDataJobHistoryInner from a JSON string
data_export_data_job_history_inner_instance = DataExportDataJobHistoryInner.from_json(json)
# print the JSON string representation of the object
print(DataExportDataJobHistoryInner.to_json())

# convert the object into a dict
data_export_data_job_history_inner_dict = data_export_data_job_history_inner_instance.to_dict()
# create an instance of DataExportDataJobHistoryInner from a dict
data_export_data_job_history_inner_from_dict = DataExportDataJobHistoryInner.from_dict(data_export_data_job_history_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


