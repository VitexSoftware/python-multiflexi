# DataExportDataAuditTrails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_export_requests** | [**List[DataExportDataAuditTrailsDataExportRequestsInner]**](DataExportDataAuditTrailsDataExportRequestsInner.md) |  | [optional] 

## Example

```python
from multiflexi_client.models.data_export_data_audit_trails import DataExportDataAuditTrails

# TODO update the JSON string below
json = "{}"
# create an instance of DataExportDataAuditTrails from a JSON string
data_export_data_audit_trails_instance = DataExportDataAuditTrails.from_json(json)
# print the JSON string representation of the object
print(DataExportDataAuditTrails.to_json())

# convert the object into a dict
data_export_data_audit_trails_dict = data_export_data_audit_trails_instance.to_dict()
# create an instance of DataExportDataAuditTrails from a dict
data_export_data_audit_trails_from_dict = DataExportDataAuditTrails.from_dict(data_export_data_audit_trails_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


