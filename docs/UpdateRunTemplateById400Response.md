# UpdateRunTemplateById400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**expected** | **int** |  | [optional] 
**received** | **int** |  | [optional] 

## Example

```python
from multiflexi_client.models.update_run_template_by_id400_response import UpdateRunTemplateById400Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRunTemplateById400Response from a JSON string
update_run_template_by_id400_response_instance = UpdateRunTemplateById400Response.from_json(json)
# print the JSON string representation of the object
print(UpdateRunTemplateById400Response.to_json())

# convert the object into a dict
update_run_template_by_id400_response_dict = update_run_template_by_id400_response_instance.to_dict()
# create an instance of UpdateRunTemplateById400Response from a dict
update_run_template_by_id400_response_from_dict = UpdateRunTemplateById400Response.from_dict(update_run_template_by_id400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


