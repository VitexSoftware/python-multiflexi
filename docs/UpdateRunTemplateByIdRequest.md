# UpdateRunTemplateByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Must match runTemplateId from URL | 
**active** | **int** | Enable (1) or disable (0) the RunTemplate | [optional] 
**interv** | **str** | Execution interval code | [optional] 
**name** | **str** | RunTemplate name | [optional] 
**delay** | **int** | Delay in seconds before job execution | [optional] 
**executor** | **str** | Executor type (Native, Docker, etc.) | [optional] 
**cron** | **str** | Cron expression for scheduling | [optional] 
**note** | **str** | Additional notes | [optional] 

## Example

```python
from multiflexi_client.models.update_run_template_by_id_request import UpdateRunTemplateByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRunTemplateByIdRequest from a JSON string
update_run_template_by_id_request_instance = UpdateRunTemplateByIdRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateRunTemplateByIdRequest.to_json())

# convert the object into a dict
update_run_template_by_id_request_dict = update_run_template_by_id_request_instance.to_dict()
# create an instance of UpdateRunTemplateByIdRequest from a dict
update_run_template_by_id_request_from_dict = UpdateRunTemplateByIdRequest.from_dict(update_run_template_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


