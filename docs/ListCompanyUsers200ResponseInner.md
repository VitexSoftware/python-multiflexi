# ListCompanyUsers200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID | [optional] 
**user_id** | **int** | User ID | [optional] 
**role** | **str** | Access role in the company (e.g. viewer, manager, admin) | [optional] [default to 'viewer']
**created_at** | **datetime** | Timestamp when the assignment was created | [optional] 
**user** | [**User**](User.md) |  | [optional] 

## Example

```python
from multiflexi_client.models.list_company_users200_response_inner import ListCompanyUsers200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListCompanyUsers200ResponseInner from a JSON string
list_company_users200_response_inner_instance = ListCompanyUsers200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListCompanyUsers200ResponseInner.to_json())

# convert the object into a dict
list_company_users200_response_inner_dict = list_company_users200_response_inner_instance.to_dict()
# create an instance of ListCompanyUsers200ResponseInner from a dict
list_company_users200_response_inner_from_dict = ListCompanyUsers200ResponseInner.from_dict(list_company_users200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


