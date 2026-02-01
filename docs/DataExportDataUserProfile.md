# DataExportDataUserProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**account_enabled** | **bool** |  | [optional] 
**account_created** | **datetime** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 
**user_settings** | **object** | User preference settings (if any) | [optional] 

## Example

```python
from multiflexi_client.models.data_export_data_user_profile import DataExportDataUserProfile

# TODO update the JSON string below
json = "{}"
# create an instance of DataExportDataUserProfile from a JSON string
data_export_data_user_profile_instance = DataExportDataUserProfile.from_json(json)
# print the JSON string representation of the object
print(DataExportDataUserProfile.to_json())

# convert the object into a dict
data_export_data_user_profile_dict = data_export_data_user_profile_instance.to_dict()
# create an instance of DataExportDataUserProfile from a dict
data_export_data_user_profile_from_dict = DataExportDataUserProfile.from_dict(data_export_data_user_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


