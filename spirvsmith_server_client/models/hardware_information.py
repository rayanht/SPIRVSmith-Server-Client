from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.hardware_type import HardwareType
from ..models.hardware_vendor import HardwareVendor

T = TypeVar("T", bound="HardwareInformation")


@attr.s(auto_attribs=True)
class HardwareInformation:
    """
    Attributes:
        hardware_type (HardwareType): An enumeration.
        hardware_vendor (HardwareVendor): An enumeration.
        hardware_model (str):
        driver_version (str):
    """

    hardware_type: HardwareType
    hardware_vendor: HardwareVendor
    hardware_model: str
    driver_version: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hardware_type = self.hardware_type.value

        hardware_vendor = self.hardware_vendor.value

        hardware_model = self.hardware_model
        driver_version = self.driver_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hardware_type": hardware_type,
                "hardware_vendor": hardware_vendor,
                "hardware_model": hardware_model,
                "driver_version": driver_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hardware_type = HardwareType(d.pop("hardware_type"))

        hardware_vendor = HardwareVendor(d.pop("hardware_vendor"))

        hardware_model = d.pop("hardware_model")

        driver_version = d.pop("driver_version")

        hardware_information = cls(
            hardware_type=hardware_type,
            hardware_vendor=hardware_vendor,
            hardware_model=hardware_model,
            driver_version=driver_version,
        )

        hardware_information.additional_properties = d
        return hardware_information

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
