# DataExportDataConsentRecordsConsentAuditTrailInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**consent_type** | **str** |  | [optional] 
**old_value** | **object** |  | [optional] 
**new_value** | **object** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**ip_address** | **str** |  | [optional] 

## Example

```python
from multiflexi_client.models.data_export_data_consent_records_consent_audit_trail_inner import DataExportDataConsentRecordsConsentAuditTrailInner

# TODO update the JSON string below
json = "{}"
# create an instance of DataExportDataConsentRecordsConsentAuditTrailInner from a JSON string
data_export_data_consent_records_consent_audit_trail_inner_instance = DataExportDataConsentRecordsConsentAuditTrailInner.from_json(json)
# print the JSON string representation of the object
print(DataExportDataConsentRecordsConsentAuditTrailInner.to_json())

# convert the object into a dict
data_export_data_consent_records_consent_audit_trail_inner_dict = data_export_data_consent_records_consent_audit_trail_inner_instance.to_dict()
# create an instance of DataExportDataConsentRecordsConsentAuditTrailInner from a dict
data_export_data_consent_records_consent_audit_trail_inner_from_dict = DataExportDataConsentRecordsConsentAuditTrailInner.from_dict(data_export_data_consent_records_consent_audit_trail_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


