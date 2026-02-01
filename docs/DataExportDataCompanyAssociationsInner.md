# DataExportDataCompanyAssociationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** |  | [optional] 
**company_code** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**company_identifier** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**associated_since** | **datetime** |  | [optional] 
**relationship_type** | **str** |  | [optional] 

## Example

```python
from multiflexi_client.models.data_export_data_company_associations_inner import DataExportDataCompanyAssociationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DataExportDataCompanyAssociationsInner from a JSON string
data_export_data_company_associations_inner_instance = DataExportDataCompanyAssociationsInner.from_json(json)
# print the JSON string representation of the object
print(DataExportDataCompanyAssociationsInner.to_json())

# convert the object into a dict
data_export_data_company_associations_inner_dict = data_export_data_company_associations_inner_instance.to_dict()
# create an instance of DataExportDataCompanyAssociationsInner from a dict
data_export_data_company_associations_inner_from_dict = DataExportDataCompanyAssociationsInner.from_dict(data_export_data_company_associations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


