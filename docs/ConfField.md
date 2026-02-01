# ConfField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**app_id** | **int** |  | [optional] 
**keyname** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**defval** | **str** |  | [optional] 

## Example

```python
from multiflexi_client.models.conf_field import ConfField

# TODO update the JSON string below
json = "{}"
# create an instance of ConfField from a JSON string
conf_field_instance = ConfField.from_json(json)
# print the JSON string representation of the object
print(ConfField.to_json())

# convert the object into a dict
conf_field_dict = conf_field_instance.to_dict()
# create an instance of ConfField from a dict
conf_field_from_dict = ConfField.from_dict(conf_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


