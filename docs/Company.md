# Company


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**settings** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**code** | **str** | Company Code | [optional] 
**ic** | **str** |  | [optional] 
**dat_create** | **datetime** |  | [optional] 
**dat_update** | **datetime** |  | [optional] 
**customer** | **int** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from multiflexi_client.models.company import Company

# TODO update the JSON string below
json = "{}"
# create an instance of Company from a JSON string
company_instance = Company.from_json(json)
# print the JSON string representation of the object
print(Company.to_json())

# convert the object into a dict
company_dict = company_instance.to_dict()
# create an instance of Company from a dict
company_from_dict = Company.from_dict(company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


