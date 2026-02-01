# RequestDataExport200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**download_url** | **str** | Secure download URL for the exported data | 
**format** | **str** | Format of the exported data | 
**generated_at** | **datetime** | ISO 8601 timestamp when the export was generated | 
**expires_at** | **datetime** | ISO 8601 timestamp when the download link expires | 
**notification_sent** | **bool** | Whether email notification was sent to user | [optional] 
**exports** | [**List[DataExportStatusResponseExportsInner]**](DataExportStatusResponseExportsInner.md) |  | 

## Example

```python
from multiflexi_client.models.request_data_export200_response import RequestDataExport200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RequestDataExport200Response from a JSON string
request_data_export200_response_instance = RequestDataExport200Response.from_json(json)
# print the JSON string representation of the object
print(RequestDataExport200Response.to_json())

# convert the object into a dict
request_data_export200_response_dict = request_data_export200_response_instance.to_dict()
# create an instance of RequestDataExport200Response from a dict
request_data_export200_response_from_dict = RequestDataExport200Response.from_dict(request_data_export200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


