# CredentialType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 
**dat_create** | **datetime** |  | [optional] 
**dat_update** | **str** |  | [optional] 

## Example

```python
from multiflexi_client.models.credential_type import CredentialType

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialType from a JSON string
credential_type_instance = CredentialType.from_json(json)
# print the JSON string representation of the object
print(CredentialType.to_json())

# convert the object into a dict
credential_type_dict = credential_type_instance.to_dict()
# create an instance of CredentialType from a dict
credential_type_from_dict = CredentialType.from_dict(credential_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


