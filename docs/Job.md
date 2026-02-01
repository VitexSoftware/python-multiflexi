# Job


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**app_id** | **int** |  | [optional] 
**begin** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 
**company_id** | **int** |  | [optional] 
**exitcode** | **int** |  | [optional] 
**stdout** | **bytearray** |  | [optional] 
**stderr** | **bytearray** |  | [optional] 
**launched_by** | **str** |  | [optional] 
**env** | **str** |  | [optional] 
**command** | **str** |  | [optional] 
**schedule** | **str** |  | [optional] 
**executor** | **str** |  | [optional] [default to 'Native']
**runtemplate_id** | **int** |  | [optional] 
**app_version** | **str** |  | [optional] [default to 'n/a']

## Example

```python
from multiflexi_client.models.job import Job

# TODO update the JSON string below
json = "{}"
# create an instance of Job from a JSON string
job_instance = Job.from_json(json)
# print the JSON string representation of the object
print(Job.to_json())

# convert the object into a dict
job_dict = job_instance.to_dict()
# create an instance of Job from a dict
job_from_dict = Job.from_dict(job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


