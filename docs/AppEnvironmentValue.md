# AppEnvironmentValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Field type | [optional] 
**description** | **str** | Field description | [optional] 
**defval** | **str** | Default value | [optional] 
**required** | **bool** | Whether this field is required | [optional] 

## Example

```python
from multiflexi_client.models.app_environment_value import AppEnvironmentValue

# TODO update the JSON string below
json = "{}"
# create an instance of AppEnvironmentValue from a JSON string
app_environment_value_instance = AppEnvironmentValue.from_json(json)
# print the JSON string representation of the object
print(AppEnvironmentValue.to_json())

# convert the object into a dict
app_environment_value_dict = app_environment_value_instance.to_dict()
# create an instance of AppEnvironmentValue from a dict
app_environment_value_from_dict = AppEnvironmentValue.from_dict(app_environment_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


