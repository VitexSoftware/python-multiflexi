# DataExportStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**exports** | [**List[DataExportStatusResponseExportsInner]**](DataExportStatusResponseExportsInner.md) |  | 

## Example

```python
from multiflexi_client.models.data_export_status_response import DataExportStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DataExportStatusResponse from a JSON string
data_export_status_response_instance = DataExportStatusResponse.from_json(json)
# print the JSON string representation of the object
print(DataExportStatusResponse.to_json())

# convert the object into a dict
data_export_status_response_dict = data_export_status_response_instance.to_dict()
# create an instance of DataExportStatusResponse from a dict
data_export_status_response_from_dict = DataExportStatusResponse.from_dict(data_export_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


