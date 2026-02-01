# Customer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**settings** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**firstname** | **str** |  | [optional] 
**lastname** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**login** | **str** |  | [optional] 
**dat_create** | **datetime** |  | [optional] 
**dat_save** | **datetime** |  | [optional] 

## Example

```python
from multiflexi_client.models.customer import Customer

# TODO update the JSON string below
json = "{}"
# create an instance of Customer from a JSON string
customer_instance = Customer.from_json(json)
# print the JSON string representation of the object
print(Customer.to_json())

# convert the object into a dict
customer_dict = customer_instance.to_dict()
# create an instance of Customer from a dict
customer_from_dict = Customer.from_dict(customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


