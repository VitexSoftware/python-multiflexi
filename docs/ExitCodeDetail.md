# ExitCodeDetail

Severity, retry policy, and multilingual description for a single exit code

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**severity** | **str** | Exit code severity level | [optional] 
**retry** | **bool** | Whether to retry on this exit code | [optional] 
**description** | **Dict[str, str]** | Multilingual descriptions (en, cs, etc.) | [optional] 

## Example

```python
from multiflexi_client.models.exit_code_detail import ExitCodeDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ExitCodeDetail from a JSON string
exit_code_detail_instance = ExitCodeDetail.from_json(json)
# print the JSON string representation of the object
print(ExitCodeDetail.to_json())

# convert the object into a dict
exit_code_detail_dict = exit_code_detail_instance.to_dict()
# create an instance of ExitCodeDetail from a dict
exit_code_detail_from_dict = ExitCodeDetail.from_dict(exit_code_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


