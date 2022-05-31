# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**flush_queues_queues_delete**](DefaultApi.md#flush_queues_queues_delete) | **DELETE** /queues | Flush Queues
[**get_next_shader_next_shader_post**](DefaultApi.md#get_next_shader_next_shader_post) | **POST** /next_shader | Get Next Shader
[**get_queue_queues_queue_id_get**](DefaultApi.md#get_queue_queues_queue_id_get) | **GET** /queues/{queue_id} | Get Queue
[**get_queues_queues_get**](DefaultApi.md#get_queues_queues_get) | **GET** /queues | Get Queues
[**get_shader_shaders_shader_id_get**](DefaultApi.md#get_shader_shaders_shader_id_get) | **GET** /shaders/{shader_id} | Get Shader
[**register_executor_executors_post**](DefaultApi.md#register_executor_executors_post) | **POST** /executors | Register Executor
[**register_generator_generators_post**](DefaultApi.md#register_generator_generators_post) | **POST** /generators | Register Generator
[**root_get**](DefaultApi.md#root_get) | **GET** / | Root
[**submit_buffers_buffers_shader_id_post**](DefaultApi.md#submit_buffers_buffers_shader_id_post) | **POST** /buffers/{shader_id} | Submit Buffers
[**submit_shader_shaders_post**](DefaultApi.md#submit_shader_shaders_post) | **POST** /shaders | Submit Shader


# **flush_queues_queues_delete**
> bool, date, datetime, dict, float, int, list, str, none_type flush_queues_queues_delete()

Flush Queues

### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Flush Queues
        api_response = api_instance.flush_queues_queues_delete()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->flush_queues_queues_delete: %s\n" % e)
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
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.retrieved_shader import RetrievedShader
from openapi_client.model.execution_platform import ExecutionPlatform
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
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
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_next_shader_next_shader_post: %s\n" % e)
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

# **get_queue_queues_queue_id_get**
> ExecutionQueue get_queue_queues_queue_id_get(queue_id)

Get Queue

### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.execution_queue import ExecutionQueue
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    queue_id = "queue_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Queue
        api_response = api_instance.get_queue_queues_queue_id_get(queue_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_queue_queues_queue_id_get: %s\n" % e)
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

# **get_queues_queues_get**
> ExecutionQueues get_queues_queues_get()

Get Queues

### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.execution_queues import ExecutionQueues
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Queues
        api_response = api_instance.get_queues_queues_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_queues_queues_get: %s\n" % e)
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

# **get_shader_shaders_shader_id_get**
> RetrievedShader get_shader_shaders_shader_id_get(shader_id)

Get Shader

### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.retrieved_shader import RetrievedShader
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    shader_id = "shader_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Shader
        api_response = api_instance.get_shader_shaders_shader_id_get(shader_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_shader_shaders_shader_id_get: %s\n" % e)
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
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.execution_platform import ExecutionPlatform
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
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
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->register_executor_executors_post: %s\n" % e)
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
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.generator_info import GeneratorInfo
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
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
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->register_generator_generators_post: %s\n" % e)
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
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Root
        api_response = api_instance.root_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->root_get: %s\n" % e)
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
> bool, date, datetime, dict, float, int, list, str, none_type submit_buffers_buffers_shader_id_post(shader_id, buffer_submission)

Submit Buffers

### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.buffer_submission import BufferSubmission
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    shader_id = "shader_id_example" # str | 
    buffer_submission = BufferSubmission(
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
        buffer_dump="buffer_dump_example",
    ) # BufferSubmission | 

    # example passing only required values which don't have defaults set
    try:
        # Submit Buffers
        api_response = api_instance.submit_buffers_buffers_shader_id_post(shader_id, buffer_submission)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->submit_buffers_buffers_shader_id_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shader_id** | **str**|  |
 **buffer_submission** | [**BufferSubmission**](BufferSubmission.md)|  |

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
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.shader_submission import ShaderSubmission
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
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
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->submit_shader_shaders_post: %s\n" % e)
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

