# JobsStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** |  | [optional] 
**successful_jobs** | **int** | Successful jobs | [optional] 
**failed_jobs** | **int** | Failed jobs | [optional] 
**incomplete_jobs** | **int** | Incomplete jobs | [optional] 
**total_applications** | **int** | Total applications | [optional] 
**repeated_jobs** | **int** | Repeated jobs | [optional] 
**total_jobs** | **int** | Total jobs | [optional] 

## Example

```python
from multiflexi_client.models.jobs_status import JobsStatus

# TODO update the JSON string below
json = "{}"
# create an instance of JobsStatus from a JSON string
jobs_status_instance = JobsStatus.from_json(json)
# print the JSON string representation of the object
print(JobsStatus.to_json())

# convert the object into a dict
jobs_status_dict = jobs_status_instance.to_dict()
# create an instance of JobsStatus from a dict
jobs_status_from_dict = JobsStatus.from_dict(jobs_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


