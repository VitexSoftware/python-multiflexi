# DataExportDataExportMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export_date** | **datetime** | When the export was generated | 
**user_id** | **int** | ID of the user whose data is exported | 
**export_version** | **str** | Version of the export format | [optional] 
**gdpr_article** | **str** | GDPR article reference | 
**data_controller** | **str** | Name of the data controller | 
**retention_info** | **str** | Data retention policy information | [optional] 
**contact_info** | **str** | Contact information for data protection inquiries | [optional] 

## Example

```python
from multiflexi_client.models.data_export_data_export_metadata import DataExportDataExportMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of DataExportDataExportMetadata from a JSON string
data_export_data_export_metadata_instance = DataExportDataExportMetadata.from_json(json)
# print the JSON string representation of the object
print(DataExportDataExportMetadata.to_json())

# convert the object into a dict
data_export_data_export_metadata_dict = data_export_data_export_metadata_instance.to_dict()
# create an instance of DataExportDataExportMetadata from a dict
data_export_data_export_metadata_from_dict = DataExportDataExportMetadata.from_dict(data_export_data_export_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


