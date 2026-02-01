# DataExportDataConsentRecordsConsentRecordsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent_id** | **int** |  | [optional] 
**consent_type** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**details** | **object** | Additional consent details | [optional] 
**policy_version** | **str** |  | [optional] 
**granted_at** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**withdrawn_at** | **datetime** |  | [optional] 
**ip_address** | **str** |  | [optional] 

## Example

```python
from multiflexi_client.models.data_export_data_consent_records_consent_records_inner import DataExportDataConsentRecordsConsentRecordsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DataExportDataConsentRecordsConsentRecordsInner from a JSON string
data_export_data_consent_records_consent_records_inner_instance = DataExportDataConsentRecordsConsentRecordsInner.from_json(json)
# print the JSON string representation of the object
print(DataExportDataConsentRecordsConsentRecordsInner.to_json())

# convert the object into a dict
data_export_data_consent_records_consent_records_inner_dict = data_export_data_consent_records_consent_records_inner_instance.to_dict()
# create an instance of DataExportDataConsentRecordsConsentRecordsInner from a dict
data_export_data_consent_records_consent_records_inner_from_dict = DataExportDataConsentRecordsConsentRecordsInner.from_dict(data_export_data_consent_records_consent_records_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


