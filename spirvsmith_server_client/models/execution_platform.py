from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.execution_platform_available_hardware import ExecutionPlatformAvailableHardware
from ..models.operating_system import OperatingSystem
from ..models.vulkan_backend import VulkanBackend
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionPlatform")


@attr.s(auto_attribs=True)
class ExecutionPlatform:
    """
    Attributes:
        vulkan_backend (VulkanBackend): An enumeration.
        operating_system (Union[Unset, OperatingSystem]): An enumeration.
        available_hardware (Union[Unset, ExecutionPlatformAvailableHardware]):
    """

    vulkan_backend: VulkanBackend
    operating_system: Union[Unset, OperatingSystem] = UNSET
    available_hardware: Union[Unset, ExecutionPlatformAvailableHardware] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vulkan_backend = self.vulkan_backend.value

        operating_system: Union[Unset, str] = UNSET
        if not isinstance(self.operating_system, Unset):
            operating_system = self.operating_system.value

        available_hardware: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.available_hardware, Unset):
            available_hardware = self.available_hardware.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vulkan_backend": vulkan_backend,
            }
        )
        if operating_system is not UNSET:
            field_dict["operating_system"] = operating_system
        if available_hardware is not UNSET:
            field_dict["available_hardware"] = available_hardware

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        vulkan_backend = VulkanBackend(d.pop("vulkan_backend"))

        _operating_system = d.pop("operating_system", UNSET)
        operating_system: Union[Unset, OperatingSystem]
        if isinstance(_operating_system, Unset):
            operating_system = UNSET
        else:
            operating_system = OperatingSystem(_operating_system)

        _available_hardware = d.pop("available_hardware", UNSET)
        available_hardware: Union[Unset, ExecutionPlatformAvailableHardware]
        if isinstance(_available_hardware, Unset):
            available_hardware = UNSET
        else:
            available_hardware = ExecutionPlatformAvailableHardware.from_dict(_available_hardware)

        execution_platform = cls(
            vulkan_backend=vulkan_backend,
            operating_system=operating_system,
            available_hardware=available_hardware,
        )

        execution_platform.additional_properties = d
        return execution_platform

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
