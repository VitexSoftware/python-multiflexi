# App


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**enabled** | **bool** | Whether the application is enabled | [optional] 
**image** | **str** | Base64-encoded application image or URL | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**executable** | **str** |  | 
**dat_create** | **datetime** | Creation timestamp | [optional] 
**dat_update** | **datetime** | Last update timestamp | [optional] 
**setup** | **str** | Setup command or instructions | [optional] 
**cmdparams** | **str** | Command line parameters | [optional] 
**deploy** | **str** | Deployment instructions | [optional] 
**homepage** | **str** |  | [optional] 
**requirements** | **str** | Comma-separated list of required credential types | [optional] 
**ociimage** | **str** | OCI/Docker container image name | [optional] 
**version** | **str** |  | [optional] 
**code** | **str** | Short application code | [optional] 
**uuid** | **str** |  | [optional] 
**topics** | **str** | Comma-separated list of topics/tags (deprecated — use tags) | [optional] 
**resultfile** | **str** | Result file path | [optional] 
**artifacts** | **str** | Output artifacts produced by the application | [optional] 
**deffile** | **str** | Path to the application definition JSON file | [optional] 
**helmchart** | **str** | URI or local path to Helm chart | [optional] 
**environment** | [**Dict[str, AppEnvironmentValue]**](AppEnvironmentValue.md) | Application environment configuration fields | [optional] 
**exit_codes** | [**Dict[str, ExitCodeDetail]**](ExitCodeDetail.md) | Exit code definitions with multilingual descriptions, keyed by exit code | [optional] 
**tags** | **str** | Comma-separated list of tags (there is no structured Tag entity in the current implementation) | [optional] 
**status** | **str** | App status in the store | [optional] 

## Example

```python
from multiflexi_client.models.app import App

# TODO update the JSON string below
json = "{}"
# create an instance of App from a JSON string
app_instance = App.from_json(json)
# print the JSON string representation of the object
print(App.to_json())

# convert the object into a dict
app_dict = app_instance.to_dict()
# create an instance of App from a dict
app_from_dict = App.from_dict(app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


