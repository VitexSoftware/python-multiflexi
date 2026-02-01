# DataExportDataConsentRecords


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent_records** | [**List[DataExportDataConsentRecordsConsentRecordsInner]**](DataExportDataConsentRecordsConsentRecordsInner.md) |  | [optional] 
**consent_audit_trail** | [**List[DataExportDataConsentRecordsConsentAuditTrailInner]**](DataExportDataConsentRecordsConsentAuditTrailInner.md) |  | [optional] 

## Example

```python
from multiflexi_client.models.data_export_data_consent_records import DataExportDataConsentRecords

# TODO update the JSON string below
json = "{}"
# create an instance of DataExportDataConsentRecords from a JSON string
data_export_data_consent_records_instance = DataExportDataConsentRecords.from_json(json)
# print the JSON string representation of the object
print(DataExportDataConsentRecords.to_json())

# convert the object into a dict
data_export_data_consent_records_dict = data_export_data_consent_records_instance.to_dict()
# create an instance of DataExportDataConsentRecords from a dict
data_export_data_consent_records_from_dict = DataExportDataConsentRecords.from_dict(data_export_data_consent_records_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


