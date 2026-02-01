# GetCredentialType200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 

## Example

```python
from multiflexi_client.models.get_credential_type200_response import GetCredentialType200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCredentialType200Response from a JSON string
get_credential_type200_response_instance = GetCredentialType200Response.from_json(json)
# print the JSON string representation of the object
print(GetCredentialType200Response.to_json())

# convert the object into a dict
get_credential_type200_response_dict = get_credential_type200_response_instance.to_dict()
# create an instance of GetCredentialType200Response from a dict
get_credential_type200_response_from_dict = GetCredentialType200Response.from_dict(get_credential_type200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


