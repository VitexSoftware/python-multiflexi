# LogoutPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Uživatelský token k invalidaci | [optional] 

## Example

```python
from multiflexi_client.models.logout_post_request import LogoutPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LogoutPostRequest from a JSON string
logout_post_request_instance = LogoutPostRequest.from_json(json)
# print the JSON string representation of the object
print(LogoutPostRequest.to_json())

# convert the object into a dict
logout_post_request_dict = logout_post_request_instance.to_dict()
# create an instance of LogoutPostRequest from a dict
logout_post_request_from_dict = LogoutPostRequest.from_dict(logout_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


