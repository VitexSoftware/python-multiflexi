# RequestDataExportPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**format** | **str** |  | [optional] [default to 'json']

## Example

```python
from multiflexi_client.models.request_data_export_post_request import RequestDataExportPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequestDataExportPostRequest from a JSON string
request_data_export_post_request_instance = RequestDataExportPostRequest.from_json(json)
# print the JSON string representation of the object
print(RequestDataExportPostRequest.to_json())

# convert the object into a dict
request_data_export_post_request_dict = request_data_export_post_request_instance.to_dict()
# create an instance of RequestDataExportPostRequest from a dict
request_data_export_post_request_from_dict = RequestDataExportPostRequest.from_dict(request_data_export_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


