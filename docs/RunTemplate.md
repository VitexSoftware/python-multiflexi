# RunTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**app_id** | **int** | Application ID | [optional] 
**company_id** | **int** | Company ID | [optional] 
**interv** | **str** | Execution interval code | [optional] 
**prepared** | **bool** | Whether the RunTemplate is prepared for execution | [optional] 
**success** | **Dict[str, object]** | Success action configuration (unserialized) | [optional] 
**fail** | **Dict[str, object]** | Failure action configuration (unserialized) | [optional] 
**name** | **str** | RunTemplate name | [optional] 
**delay** | **int** | Delay in seconds before job execution | [optional] [default to 0]
**executor** | **str** | Executor type (Native, Docker, etc.) | [optional] [default to 'Native']
**active** | **bool** | Whether the RunTemplate is active | [optional] [default to True]
**cron** | **str** | Cron expression for scheduling | [optional] 
**last_schedule** | **datetime** | Last scheduled execution timestamp | [optional] 
**next_schedule** | **datetime** | Next scheduled execution timestamp | [optional] 
**note** | **str** | Additional notes about the RunTemplate | [optional] 
**dat_create** | **datetime** | Creation timestamp | [optional] 
**dat_save** | **datetime** | Last modification timestamp | [optional] 
**successfull_jobs_count** | **int** | Count of successful jobs | [optional] [default to 0]
**failed_jobs_count** | **int** | Count of failed jobs | [optional] [default to 0]

## Example

```python
from multiflexi_client.models.run_template import RunTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of RunTemplate from a JSON string
run_template_instance = RunTemplate.from_json(json)
# print the JSON string representation of the object
print(RunTemplate.to_json())

# convert the object into a dict
run_template_dict = run_template_instance.to_dict()
# create an instance of RunTemplate from a dict
run_template_from_dict = RunTemplate.from_dict(run_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


