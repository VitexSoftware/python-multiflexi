# AppExitCodesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**severity** | **str** | Exit code severity level | [optional] 
**retry** | **bool** | Whether to retry on this exit code | [optional] 
**description** | **Dict[str, str]** | Multilingual descriptions (en, cs, etc.) | [optional] 

## Example

```python
from multiflexi_client.models.app_exit_codes_inner import AppExitCodesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AppExitCodesInner from a JSON string
app_exit_codes_inner_instance = AppExitCodesInner.from_json(json)
# print the JSON string representation of the object
print(AppExitCodesInner.to_json())

# convert the object into a dict
app_exit_codes_inner_dict = app_exit_codes_inner_instance.to_dict()
# create an instance of AppExitCodesInner from a dict
app_exit_codes_inner_from_dict = AppExitCodesInner.from_dict(app_exit_codes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


