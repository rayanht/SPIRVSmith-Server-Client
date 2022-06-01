# spirvsmith_server_sdk.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**flush_queues_queues_delete**](DefaultApi.md#flush_queues_queues_delete) | **DELETE** /queues | Flush Queues
[**get_next_shader_shaders_next_post**](DefaultApi.md#get_next_shader_shaders_next_post) | **POST** /shaders/next | Get Next Shader
[**get_queue_queues_queue_id_get**](DefaultApi.md#get_queue_queues_queue_id_get) | **GET** /queues/{queue_id} | Get Queue
[**get_queues_queues_get**](DefaultApi.md#get_queues_queues_get) | **GET** /queues | Get Queues
[**get_shader_shaders_shader_id_get**](DefaultApi.md#get_shader_shaders_shader_id_get) | **GET** /shaders/{shader_id} | Get Shader
[**register_executor_queues_put**](DefaultApi.md#register_executor_queues_put) | **PUT** /queues | Register Executor
[**register_generator_generators_post**](DefaultApi.md#register_generator_generators_post) | **POST** /generators | Register Generator
[**submit_buffers_buffers_shader_id_post**](DefaultApi.md#submit_buffers_buffers_shader_id_post) | **POST** /buffers/{shader_id} | Submit Buffers
[**submit_shader_shaders_post**](DefaultApi.md#submit_shader_shaders_post) | **POST** /shaders | Submit Shader

# **flush_queues_queues_delete**
> bool, date, datetime, dict, float, int, list, str, none_type flush_queues_queues_delete()

Flush Queues

### Example

```python
import spirvsmith_server_sdk
from spirvsmith_server_sdk.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spirvsmith_server_sdk.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with spirvsmith_server_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Flush Queues
        api_response = api_instance.flush_queues_queues_delete()
        pprint(api_response)
    except spirvsmith_server_sdk.ApiException as e:
        print("Exception when calling DefaultApi->flush_queues_queues_delete: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[dict, frozendict, str, date, datetime, int, float, bool, Decimal, None, list, tuple, bytes] | |


**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_next_shader_shaders_next_post**
> RetrievedShader get_next_shader_shaders_next_post(execution_platform)

Get Next Shader

### Example

```python
import spirvsmith_server_sdk
from spirvsmith_server_sdk.api import default_api
from spirvsmith_server_sdk.model.retrieved_shader import RetrievedShader
from spirvsmith_server_sdk.model.execution_platform import ExecutionPlatform
from spirvsmith_server_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spirvsmith_server_sdk.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with spirvsmith_server_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    body = ExecutionPlatform(
        vulkan_backend=VulkanBackend("MoltenVK"),
        operating_system=OperatingSystem("Linux"),
        available_hardware=dict(
            "key": [
                HardwareInformation(
                    hardware_type=HardwareType("CPU"),
                    hardware_vendor=HardwareVendor("GenuineIntel"),
                    hardware_model="hardware_model_example",
                    driver_version="driver_version_example",
                )
            ],
        ),
    )
    try:
        # Get Next Shader
        api_response = api_instance.get_next_shader_shaders_next_post(
            body=body,
        )
        pprint(api_response)
    except spirvsmith_server_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_next_shader_shaders_next_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ExecutionPlatform**](ExecutionPlatform.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response
422 | ApiResponseFor422 | Validation Error

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RetrievedShader**](RetrievedShader.md) |  | 


#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



[**RetrievedShader**](RetrievedShader.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_queue_queues_queue_id_get**
> ExecutionQueue get_queue_queues_queue_id_get(queue_id)

Get Queue

### Example

```python
import spirvsmith_server_sdk
from spirvsmith_server_sdk.api import default_api
from spirvsmith_server_sdk.model.execution_queue import ExecutionQueue
from spirvsmith_server_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spirvsmith_server_sdk.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with spirvsmith_server_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'queue_id': "queue_id_example",
    }
    try:
        # Get Queue
        api_response = api_instance.get_queue_queues_queue_id_get(
            path_params=path_params,
        )
        pprint(api_response)
    except spirvsmith_server_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_queue_queues_queue_id_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
queue_id | QueueIdSchema | | 

#### QueueIdSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response
422 | ApiResponseFor422 | Validation Error

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ExecutionQueue**](ExecutionQueue.md) |  | 


#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



[**ExecutionQueue**](ExecutionQueue.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_queues_queues_get**
> ExecutionQueues get_queues_queues_get()

Get Queues

### Example

```python
import spirvsmith_server_sdk
from spirvsmith_server_sdk.api import default_api
from spirvsmith_server_sdk.model.execution_queues import ExecutionQueues
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spirvsmith_server_sdk.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with spirvsmith_server_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Queues
        api_response = api_instance.get_queues_queues_get()
        pprint(api_response)
    except spirvsmith_server_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_queues_queues_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ExecutionQueues**](ExecutionQueues.md) |  | 



[**ExecutionQueues**](ExecutionQueues.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shader_shaders_shader_id_get**
> RetrievedShader get_shader_shaders_shader_id_get(shader_id)

Get Shader

### Example

```python
import spirvsmith_server_sdk
from spirvsmith_server_sdk.api import default_api
from spirvsmith_server_sdk.model.retrieved_shader import RetrievedShader
from spirvsmith_server_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spirvsmith_server_sdk.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with spirvsmith_server_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'shader_id': "shader_id_example",
    }
    try:
        # Get Shader
        api_response = api_instance.get_shader_shaders_shader_id_get(
            path_params=path_params,
        )
        pprint(api_response)
    except spirvsmith_server_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_shader_shaders_shader_id_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
shader_id | ShaderIdSchema | | 

#### ShaderIdSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response
422 | ApiResponseFor422 | Validation Error

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RetrievedShader**](RetrievedShader.md) |  | 


#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



[**RetrievedShader**](RetrievedShader.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_executor_queues_put**
> bool, date, datetime, dict, float, int, list, str, none_type register_executor_queues_put(execution_platform)

Register Executor

### Example

```python
import spirvsmith_server_sdk
from spirvsmith_server_sdk.api import default_api
from spirvsmith_server_sdk.model.execution_platform import ExecutionPlatform
from spirvsmith_server_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spirvsmith_server_sdk.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with spirvsmith_server_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    body = ExecutionPlatform(
        vulkan_backend=VulkanBackend("MoltenVK"),
        operating_system=OperatingSystem("Linux"),
        available_hardware=dict(
            "key": [
                HardwareInformation(
                    hardware_type=HardwareType("CPU"),
                    hardware_vendor=HardwareVendor("GenuineIntel"),
                    hardware_model="hardware_model_example",
                    driver_version="driver_version_example",
                )
            ],
        ),
    )
    try:
        # Register Executor
        api_response = api_instance.register_executor_queues_put(
            body=body,
        )
        pprint(api_response)
    except spirvsmith_server_sdk.ApiException as e:
        print("Exception when calling DefaultApi->register_executor_queues_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ExecutionPlatform**](ExecutionPlatform.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response
422 | ApiResponseFor422 | Validation Error

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[dict, frozendict, str, date, datetime, int, float, bool, Decimal, None, list, tuple, bytes] | |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_generator_generators_post**
> bool, date, datetime, dict, float, int, list, str, none_type register_generator_generators_post(generator_info)

Register Generator

### Example

```python
import spirvsmith_server_sdk
from spirvsmith_server_sdk.api import default_api
from spirvsmith_server_sdk.model.generator_info import GeneratorInfo
from spirvsmith_server_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spirvsmith_server_sdk.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with spirvsmith_server_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    body = GeneratorInfo(
        id="id_example",
        fuzzer_version="fuzzer_version_example",
        strategy=FuzzingStrategy(
            mutations_config=MutationsConfig(
null,
null,
null,
null,
null,
null,
null,
null,
null,
null,
null,
null,
            ),
            enable_ext_glsl_std_450=True,
            w_memory_operation=1,
            w_logical_operation=1,
            w_arithmetic_operation=1,
            w_control_flow_operation=1,
            w_function_operation=1,
            w_bitwise_operation=1,
            w_conversion_operation=1,
            w_composite_operation=1,
            w_scalar_type=1,
            w_container_type=1,
            w_composite_constant=1,
            w_scalar_constant=1,
            p_statement=3.14,
            p_picking_statement_operand=3.14,
            mutation_rate=3.14,
        ),
    )
    try:
        # Register Generator
        api_response = api_instance.register_generator_generators_post(
            body=body,
        )
        pprint(api_response)
    except spirvsmith_server_sdk.ApiException as e:
        print("Exception when calling DefaultApi->register_generator_generators_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GeneratorInfo**](GeneratorInfo.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response
422 | ApiResponseFor422 | Validation Error

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[dict, frozendict, str, date, datetime, int, float, bool, Decimal, None, list, tuple, bytes] | |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_buffers_buffers_shader_id_post**
> bool, date, datetime, dict, float, int, list, str, none_type submit_buffers_buffers_shader_id_post(shader_idbuffer_submission)

Submit Buffers

### Example

```python
import spirvsmith_server_sdk
from spirvsmith_server_sdk.api import default_api
from spirvsmith_server_sdk.model.buffer_submission import BufferSubmission
from spirvsmith_server_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spirvsmith_server_sdk.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with spirvsmith_server_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'shader_id': "shader_id_example",
    }
    body = BufferSubmission(
        executor=ExecutionPlatform(
            vulkan_backend=VulkanBackend("MoltenVK"),
            operating_system=OperatingSystem("Linux"),
            available_hardware=dict(
                "key": [
                    HardwareInformation(
                        hardware_type=HardwareType("CPU"),
                        hardware_vendor=HardwareVendor("GenuineIntel"),
                        hardware_model="hardware_model_example",
                        driver_version="driver_version_example",
                    )
                ],
            ),
        ),
        buffer_dump="buffer_dump_example",
    )
    try:
        # Submit Buffers
        api_response = api_instance.submit_buffers_buffers_shader_id_post(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except spirvsmith_server_sdk.ApiException as e:
        print("Exception when calling DefaultApi->submit_buffers_buffers_shader_id_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BufferSubmission**](BufferSubmission.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
shader_id | ShaderIdSchema | | 

#### ShaderIdSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response
422 | ApiResponseFor422 | Validation Error

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[dict, frozendict, str, date, datetime, int, float, bool, Decimal, None, list, tuple, bytes] | |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_shader_shaders_post**
> bool, date, datetime, dict, float, int, list, str, none_type submit_shader_shaders_post(shader_submission)

Submit Shader

### Example

```python
import spirvsmith_server_sdk
from spirvsmith_server_sdk.api import default_api
from spirvsmith_server_sdk.model.shader_submission import ShaderSubmission
from spirvsmith_server_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spirvsmith_server_sdk.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with spirvsmith_server_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    body = ShaderSubmission(
        shader_id="shader_id_example",
        shader_assembly="shader_assembly_example",
        generator_info=GeneratorInfo(
            id="id_example",
            fuzzer_version="fuzzer_version_example",
            strategy=FuzzingStrategy(
                mutations_config=MutationsConfig(
null,
null,
null,
null,
null,
null,
null,
null,
null,
null,
null,
null,
                ),
                enable_ext_glsl_std_450=True,
                w_memory_operation=1,
                w_logical_operation=1,
                w_arithmetic_operation=1,
                w_control_flow_operation=1,
                w_function_operation=1,
                w_bitwise_operation=1,
                w_conversion_operation=1,
                w_composite_operation=1,
                w_scalar_type=1,
                w_container_type=1,
                w_composite_constant=1,
                w_scalar_constant=1,
                p_statement=3.14,
                p_picking_statement_operand=3.14,
                mutation_rate=3.14,
            ),
        ),
        prioritize=True,
        n_buffers=1,
    )
    try:
        # Submit Shader
        api_response = api_instance.submit_shader_shaders_post(
            body=body,
        )
        pprint(api_response)
    except spirvsmith_server_sdk.ApiException as e:
        print("Exception when calling DefaultApi->submit_shader_shaders_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShaderSubmission**](ShaderSubmission.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response
422 | ApiResponseFor422 | Validation Error

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[dict, frozendict, str, date, datetime, int, float, bool, Decimal, None, list, tuple, bytes] | |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

