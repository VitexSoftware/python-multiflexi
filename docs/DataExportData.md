# DataExportData

Complete user personal data export structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export_metadata** | [**DataExportDataExportMetadata**](DataExportDataExportMetadata.md) |  | 
**user_profile** | [**DataExportDataUserProfile**](DataExportDataUserProfile.md) |  | 
**company_associations** | [**List[DataExportDataCompanyAssociationsInner]**](DataExportDataCompanyAssociationsInner.md) |  | 
**credentials** | [**List[DataExportDataCredentialsInner]**](DataExportDataCredentialsInner.md) | Credential metadata only (no actual passwords/secrets) | 
**activity_logs** | [**List[DataExportDataActivityLogsInner]**](DataExportDataActivityLogsInner.md) |  | 
**job_history** | [**List[DataExportDataJobHistoryInner]**](DataExportDataJobHistoryInner.md) |  | 
**consent_records** | [**DataExportDataConsentRecords**](DataExportDataConsentRecords.md) |  | 
**session_history** | [**DataExportDataSessionHistory**](DataExportDataSessionHistory.md) |  | 
**audit_trails** | [**DataExportDataAuditTrails**](DataExportDataAuditTrails.md) |  | 

## Example

```python
from multiflexi_client.models.data_export_data import DataExportData

# TODO update the JSON string below
json = "{}"
# create an instance of DataExportData from a JSON string
data_export_data_instance = DataExportData.from_json(json)
# print the JSON string representation of the object
print(DataExportData.to_json())

# convert the object into a dict
data_export_data_dict = data_export_data_instance.to_dict()
# create an instance of DataExportData from a dict
data_export_data_from_dict = DataExportData.from_dict(data_export_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


