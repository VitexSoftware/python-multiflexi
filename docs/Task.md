# Task


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**runtemplate_id** | **int** | FK to the RunTemplate that spawned this task | [optional] 
**window_start** | **datetime** | Start of the scheduling window | [optional] 
**window_end** | **datetime** | End of the scheduling window | [optional] 
**deadline** | **datetime** | Deadline by which the result must be ready | [optional] 
**state** | **str** | Current task state | [optional] 
**fulfilled_by_job_id** | **int** | ID of the job that fulfilled this task | [optional] 
**fulfilled_at** | **datetime** | When the task was fulfilled | [optional] 
**attempts** | **int** | Number of job attempts made | [optional] 
**created_at** | **datetime** |  | [optional] 
**jobs** | [**List[Job]**](Job.md) | Job attempt history (only present in single-task responses) | [optional] 

## Example

```python
from multiflexi_client.models.task import Task

# TODO update the JSON string below
json = "{}"
# create an instance of Task from a JSON string
task_instance = Task.from_json(json)
# print the JSON string representation of the object
print(Task.to_json())

# convert the object into a dict
task_dict = task_instance.to_dict()
# create an instance of Task from a dict
task_from_dict = Task.from_dict(task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


