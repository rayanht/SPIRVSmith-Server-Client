# spirvsmith_server_sdk.DefaultYeet


All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**flush_queues_queues_delete**](DefaultYeet
.md#flush_queues_queues_delete) | **DELETE** /queues | Flush Queues
[**get_next_shader_next_shader_post**](DefaultYeet
.md#get_next_shader_next_shader_post) | **POST** /next_shader | Get Next Shader
[**get_queues_queues_get**](DefaultYeet
.md#get_queues_queues_get) | **GET** /queues | Get Queues
[**get_queues_queues_queue_id_get**](DefaultYeet
.md#get_queues_queues_queue_id_get) | **GET** /queues/{queue_id} | Get Queues
[**get_shader_shaders_shader_id_get**](DefaultYeet
.md#get_shader_shaders_shader_id_get) | **GET** /shaders/{shader_id} | Get Shader
[**register_executor_executors_post**](DefaultYeet
.md#register_executor_executors_post) | **POST** /executors | Register Executor
[**register_generator_generators_post**](DefaultYeet
.md#register_generator_generators_post) | **POST** /generators | Register Generator
[**root_get**](DefaultYeet
.md#root_get) | **GET** / | Root
[**submit_buffers_buffers_shader_id_post**](DefaultYeet
.md#submit_buffers_buffers_shader_id_post) | **POST** /buffers/{shader_id} | Submit Buffers
[**submit_shader_shaders_post**](DefaultYeet
.md#submit_shader_shaders_post) | **POST** /shaders | Submit Shader


# **flush_queues_queues_delete**
> bool, date, datetime, dict, float, int, list, str, none_type flush_queues_queues_delete()

Flush Queues

### Example


```python
import time
import spirvsmith_server_sdk
from spirvsmith_server_sdk.api import default_yeet

from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spirvsmith_server_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with spirvsmith_server_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_yeet
.DefaultYeet
(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Flush Queues
        api_response = api_instance.flush_queues_queues_delete()
        pprint(api_response)
    except spirvsmith_server_sdk.ApiException as e:
        print("Exception when calling DefaultYeet
->flush_queues_queues_delete: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_next_shader_next_shader_post**
> RetrievedShader get_next_shader_next_shader_post(execution_platform)

Get Next Shader

### Example


```python
import time
import spirvsmith_server_sdk
from spirvsmith_server_sdk.api import default_yeet

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
with spirvsmith_server_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_yeet
.DefaultYeet
(api_client)
    execution_platform = ExecutionPlatform(
        vulkan_backend=VulkanBackend("MoltenVK"),
        operating_system=OperatingSystem("Linux"),
        available_hardware={
            "key": [
                HardwareInformation(
                    hardware_type=HardwareType("CPU"),
                    hardware_vendor=HardwareVendor("GenuineIntel"),
                    hardware_model="hardware_model_example",
                    driver_version="driver_version_example",
                ),
            ],
        },
    ) # ExecutionPlatform | 

    # example passing only required values which don't have defaults set
    try:
        # Get Next Shader
        api_response = api_instance.get_next_shader_next_shader_post(execution_platform)
        pprint(api_response)
    except spirvsmith_server_sdk.ApiException as e:
        print("Exception when calling DefaultYeet
->get_next_shader_next_shader_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_platform** | [**ExecutionPlatform**](ExecutionPlatform.md)|  |

### Return type

[**RetrievedShader**](RetrievedShader.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_queues_queues_get**
> ExecutionQueues get_queues_queues_get()

Get Queues

### Example


```python
import time
import spirvsmith_server_sdk
from spirvsmith_server_sdk.api import default_yeet

from spirvsmith_server_sdk.model.execution_queues import ExecutionQueues
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spirvsmith_server_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with spirvsmith_server_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_yeet
.DefaultYeet
(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Queues
        api_response = api_instance.get_queues_queues_get()
        pprint(api_response)
    except spirvsmith_server_sdk.ApiException as e:
        print("Exception when calling DefaultYeet
->get_queues_queues_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ExecutionQueues**](ExecutionQueues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_queues_queues_queue_id_get**
> ExecutionQueue get_queues_queues_queue_id_get(queue_id)

Get Queues

### Example


```python
import time
import spirvsmith_server_sdk
from spirvsmith_server_sdk.api import default_yeet

from spirvsmith_server_sdk.model.execution_queue import ExecutionQueue
from spirvsmith_server_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spirvsmith_server_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with spirvsmith_server_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_yeet
.DefaultYeet
(api_client)
    queue_id = "queue_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Queues
        api_response = api_instance.get_queues_queues_queue_id_get(queue_id)
        pprint(api_response)
    except spirvsmith_server_sdk.ApiException as e:
        print("Exception when calling DefaultYeet
->get_queues_queues_queue_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queue_id** | **str**|  |

### Return type

[**ExecutionQueue**](ExecutionQueue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shader_shaders_shader_id_get**
> RetrievedShader get_shader_shaders_shader_id_get(shader_id)

Get Shader

### Example


```python
import time
import spirvsmith_server_sdk
from spirvsmith_server_sdk.api import default_yeet

from spirvsmith_server_sdk.model.retrieved_shader import RetrievedShader
from spirvsmith_server_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spirvsmith_server_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with spirvsmith_server_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_yeet
.DefaultYeet
(api_client)
    shader_id = "shader_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Shader
        api_response = api_instance.get_shader_shaders_shader_id_get(shader_id)
        pprint(api_response)
    except spirvsmith_server_sdk.ApiException as e:
        print("Exception when calling DefaultYeet
->get_shader_shaders_shader_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shader_id** | **str**|  |

### Return type

[**RetrievedShader**](RetrievedShader.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_executor_executors_post**
> bool, date, datetime, dict, float, int, list, str, none_type register_executor_executors_post(execution_platform)

Register Executor

### Example


```python
import time
import spirvsmith_server_sdk
from spirvsmith_server_sdk.api import default_yeet

from spirvsmith_server_sdk.model.execution_platform import ExecutionPlatform
from spirvsmith_server_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spirvsmith_server_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with spirvsmith_server_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_yeet
.DefaultYeet
(api_client)
    execution_platform = ExecutionPlatform(
        vulkan_backend=VulkanBackend("MoltenVK"),
        operating_system=OperatingSystem("Linux"),
        available_hardware={
            "key": [
                HardwareInformation(
                    hardware_type=HardwareType("CPU"),
                    hardware_vendor=HardwareVendor("GenuineIntel"),
                    hardware_model="hardware_model_example",
                    driver_version="driver_version_example",
                ),
            ],
        },
    ) # ExecutionPlatform | 

    # example passing only required values which don't have defaults set
    try:
        # Register Executor
        api_response = api_instance.register_executor_executors_post(execution_platform)
        pprint(api_response)
    except spirvsmith_server_sdk.ApiException as e:
        print("Exception when calling DefaultYeet
->register_executor_executors_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_platform** | [**ExecutionPlatform**](ExecutionPlatform.md)|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_generator_generators_post**
> bool, date, datetime, dict, float, int, list, str, none_type register_generator_generators_post(generator_info)

Register Generator

### Example


```python
import time
import spirvsmith_server_sdk
from spirvsmith_server_sdk.api import default_yeet

from spirvsmith_server_sdk.model.generator_info import GeneratorInfo
from spirvsmith_server_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spirvsmith_server_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with spirvsmith_server_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_yeet
.DefaultYeet
(api_client)
    generator_info = GeneratorInfo(
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
    ) # GeneratorInfo | 

    # example passing only required values which don't have defaults set
    try:
        # Register Generator
        api_response = api_instance.register_generator_generators_post(generator_info)
        pprint(api_response)
    except spirvsmith_server_sdk.ApiException as e:
        print("Exception when calling DefaultYeet
->register_generator_generators_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generator_info** | [**GeneratorInfo**](GeneratorInfo.md)|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_get**
> bool, date, datetime, dict, float, int, list, str, none_type root_get()

Root

### Example


```python
import time
import spirvsmith_server_sdk
from spirvsmith_server_sdk.api import default_yeet

from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spirvsmith_server_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with spirvsmith_server_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_yeet
.DefaultYeet
(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Root
        api_response = api_instance.root_get()
        pprint(api_response)
    except spirvsmith_server_sdk.ApiException as e:
        print("Exception when calling DefaultYeet
->root_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_buffers_buffers_shader_id_post**
> bool, date, datetime, dict, float, int, list, str, none_type submit_buffers_buffers_shader_id_post(shader_id, body_submit_buffers_buffers_shader_id_post)

Submit Buffers

### Example


```python
import time
import spirvsmith_server_sdk
from spirvsmith_server_sdk.api import default_yeet

from spirvsmith_server_sdk.model.body_submit_buffers_buffers_shader_id_post import BodySubmitBuffersBuffersShaderIdPost
from spirvsmith_server_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spirvsmith_server_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with spirvsmith_server_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_yeet
.DefaultYeet
(api_client)
    shader_id = "shader_id_example" # str | 
    body_submit_buffers_buffers_shader_id_post = BodySubmitBuffersBuffersShaderIdPost(
        buffers=BufferSubmission(
            buffer_dump="buffer_dump_example",
        ),
        executor=ExecutionPlatform(
            vulkan_backend=VulkanBackend("MoltenVK"),
            operating_system=OperatingSystem("Linux"),
            available_hardware={
                "key": [
                    HardwareInformation(
                        hardware_type=HardwareType("CPU"),
                        hardware_vendor=HardwareVendor("GenuineIntel"),
                        hardware_model="hardware_model_example",
                        driver_version="driver_version_example",
                    ),
                ],
            },
        ),
    ) # BodySubmitBuffersBuffersShaderIdPost | 

    # example passing only required values which don't have defaults set
    try:
        # Submit Buffers
        api_response = api_instance.submit_buffers_buffers_shader_id_post(shader_id, body_submit_buffers_buffers_shader_id_post)
        pprint(api_response)
    except spirvsmith_server_sdk.ApiException as e:
        print("Exception when calling DefaultYeet
->submit_buffers_buffers_shader_id_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shader_id** | **str**|  |
 **body_submit_buffers_buffers_shader_id_post** | [**BodySubmitBuffersBuffersShaderIdPost**](BodySubmitBuffersBuffersShaderIdPost.md)|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_shader_shaders_post**
> bool, date, datetime, dict, float, int, list, str, none_type submit_shader_shaders_post(shader_submission)

Submit Shader

### Example


```python
import time
import spirvsmith_server_sdk
from spirvsmith_server_sdk.api import default_yeet

from spirvsmith_server_sdk.model.http_validation_error import HTTPValidationError
from spirvsmith_server_sdk.model.shader_submission import ShaderSubmission
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spirvsmith_server_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with spirvsmith_server_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_yeet
.DefaultYeet
(api_client)
    shader_submission = ShaderSubmission(
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
    ) # ShaderSubmission | 

    # example passing only required values which don't have defaults set
    try:
        # Submit Shader
        api_response = api_instance.submit_shader_shaders_post(shader_submission)
        pprint(api_response)
    except spirvsmith_server_sdk.ApiException as e:
        print("Exception when calling DefaultYeet
->submit_shader_shaders_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shader_submission** | [**ShaderSubmission**](ShaderSubmission.md)|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

