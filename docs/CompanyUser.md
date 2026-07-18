# CompanyUser

Many-to-many assignment of a user to a company with an access role

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID | [optional] 
**user_id** | **int** | User ID | [optional] 
**role** | **str** | Access role in the company (e.g. viewer, manager, admin) | [optional] [default to 'viewer']
**created_at** | **datetime** | Timestamp when the assignment was created | [optional] 

## Example

```python
from multiflexi_client.models.company_user import CompanyUser

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyUser from a JSON string
company_user_instance = CompanyUser.from_json(json)
# print the JSON string representation of the object
print(CompanyUser.to_json())

# convert the object into a dict
company_user_dict = company_user_instance.to_dict()
# create an instance of CompanyUser from a dict
company_user_from_dict = CompanyUser.from_dict(company_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


