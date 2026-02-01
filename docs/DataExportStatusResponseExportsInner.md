# DataExportStatusResponseExportsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Export request description | 
**requested_at** | **datetime** | ISO 8601 timestamp when the export was requested | 

## Example

```python
from multiflexi_client.models.data_export_status_response_exports_inner import DataExportStatusResponseExportsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DataExportStatusResponseExportsInner from a JSON string
data_export_status_response_exports_inner_instance = DataExportStatusResponseExportsInner.from_json(json)
# print the JSON string representation of the object
print(DataExportStatusResponseExportsInner.to_json())

# convert the object into a dict
data_export_status_response_exports_inner_dict = data_export_status_response_exports_inner_instance.to_dict()
# create an instance of DataExportStatusResponseExportsInner from a dict
data_export_status_response_exports_inner_from_dict = DataExportStatusResponseExportsInner.from_dict(data_export_status_response_exports_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


