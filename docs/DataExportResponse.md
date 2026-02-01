# DataExportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**download_url** | **str** | Secure download URL for the exported data | 
**format** | **str** | Format of the exported data | 
**generated_at** | **datetime** | ISO 8601 timestamp when the export was generated | 
**expires_at** | **datetime** | ISO 8601 timestamp when the download link expires | 
**notification_sent** | **bool** | Whether email notification was sent to user | [optional] 

## Example

```python
from multiflexi_client.models.data_export_response import DataExportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DataExportResponse from a JSON string
data_export_response_instance = DataExportResponse.from_json(json)
# print the JSON string representation of the object
print(DataExportResponse.to_json())

# convert the object into a dict
data_export_response_dict = data_export_response_instance.to_dict()
# create an instance of DataExportResponse from a dict
data_export_response_from_dict = DataExportResponse.from_dict(data_export_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


