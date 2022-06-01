import spirvsmith_server_sdk
from pprint import pprint
from spirvsmith_server_sdk.api import default_api
from spirvsmith_server_sdk.model.execution_platform import ExecutionPlatform
from spirvsmith_server_sdk.model.hardware_information import HardwareInformation
from spirvsmith_server_sdk.model.hardware_type import HardwareType
from spirvsmith_server_sdk.model.hardware_vendor import HardwareVendor
from spirvsmith_server_sdk.model.operating_system import OperatingSystem
from spirvsmith_server_sdk.model.vulkan_backend import VulkanBackend

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spirvsmith_server_sdk.Configuration(host="http://localhost:8000")


# Enter a context with an instance of the API client
with spirvsmith_server_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    executor = ExecutionPlatform(
        vulkan_backend=VulkanBackend("MoltenVK"),
        operating_system=OperatingSystem("Linux"),
        available_hardware={
            "CPU": [
                HardwareInformation(
                    hardware_type=HardwareType("CPU"),
                    hardware_vendor=HardwareVendor("GenuineIntel"),
                    hardware_model="hardware_model_example",
                    driver_version="driver_version_example",
                ),
            ],
            "GPU": [],
        },
    )
    queue_id = api_instance.register_executor_queues_put(executor)
    pprint(queue_id)
    queues = api_instance.get_queues_queues_get()
    pprint(queues)
