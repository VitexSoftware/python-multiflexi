# DataExportDataCredentialsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_id** | **int** |  | [optional] 
**credential_name** | **str** |  | [optional] 
**company_id** | **int** |  | [optional] 
**credential_type** | **str** |  | [optional] 
**note** | **str** |  | [optional] 

## Example

```python
from multiflexi_client.models.data_export_data_credentials_inner import DataExportDataCredentialsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DataExportDataCredentialsInner from a JSON string
data_export_data_credentials_inner_instance = DataExportDataCredentialsInner.from_json(json)
# print the JSON string representation of the object
print(DataExportDataCredentialsInner.to_json())

# convert the object into a dict
data_export_data_credentials_inner_dict = data_export_data_credentials_inner_instance.to_dict()
# create an instance of DataExportDataCredentialsInner from a dict
data_export_data_credentials_inner_from_dict = DataExportDataCredentialsInner.from_dict(data_export_data_credentials_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


