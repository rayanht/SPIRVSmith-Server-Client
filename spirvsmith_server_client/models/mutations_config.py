from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.bounded_int import BoundedInt

T = TypeVar("T", bound="MutationsConfig")


@attr.s(auto_attribs=True)
class MutationsConfig:
    """
    Attributes:
        w_memory_operation (BoundedInt):
        w_logical_operation (BoundedInt):
        w_arithmetic_operation (BoundedInt):
        w_control_flow_operation (BoundedInt):
        w_function_operation (BoundedInt):
        w_bitwise_operation (BoundedInt):
        w_conversion_operation (BoundedInt):
        w_composite_operation (BoundedInt):
        w_scalar_type (BoundedInt):
        w_container_type (BoundedInt):
        w_composite_constant (BoundedInt):
        w_scalar_constant (BoundedInt):
    """

    w_memory_operation: BoundedInt
    w_logical_operation: BoundedInt
    w_arithmetic_operation: BoundedInt
    w_control_flow_operation: BoundedInt
    w_function_operation: BoundedInt
    w_bitwise_operation: BoundedInt
    w_conversion_operation: BoundedInt
    w_composite_operation: BoundedInt
    w_scalar_type: BoundedInt
    w_container_type: BoundedInt
    w_composite_constant: BoundedInt
    w_scalar_constant: BoundedInt
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        w_memory_operation = self.w_memory_operation.to_dict()

        w_logical_operation = self.w_logical_operation.to_dict()

        w_arithmetic_operation = self.w_arithmetic_operation.to_dict()

        w_control_flow_operation = self.w_control_flow_operation.to_dict()

        w_function_operation = self.w_function_operation.to_dict()

        w_bitwise_operation = self.w_bitwise_operation.to_dict()

        w_conversion_operation = self.w_conversion_operation.to_dict()

        w_composite_operation = self.w_composite_operation.to_dict()

        w_scalar_type = self.w_scalar_type.to_dict()

        w_container_type = self.w_container_type.to_dict()

        w_composite_constant = self.w_composite_constant.to_dict()

        w_scalar_constant = self.w_scalar_constant.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "w_memory_operation": w_memory_operation,
                "w_logical_operation": w_logical_operation,
                "w_arithmetic_operation": w_arithmetic_operation,
                "w_control_flow_operation": w_control_flow_operation,
                "w_function_operation": w_function_operation,
                "w_bitwise_operation": w_bitwise_operation,
                "w_conversion_operation": w_conversion_operation,
                "w_composite_operation": w_composite_operation,
                "w_scalar_type": w_scalar_type,
                "w_container_type": w_container_type,
                "w_composite_constant": w_composite_constant,
                "w_scalar_constant": w_scalar_constant,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        w_memory_operation = BoundedInt.from_dict(d.pop("w_memory_operation"))

        w_logical_operation = BoundedInt.from_dict(d.pop("w_logical_operation"))

        w_arithmetic_operation = BoundedInt.from_dict(d.pop("w_arithmetic_operation"))

        w_control_flow_operation = BoundedInt.from_dict(d.pop("w_control_flow_operation"))

        w_function_operation = BoundedInt.from_dict(d.pop("w_function_operation"))

        w_bitwise_operation = BoundedInt.from_dict(d.pop("w_bitwise_operation"))

        w_conversion_operation = BoundedInt.from_dict(d.pop("w_conversion_operation"))

        w_composite_operation = BoundedInt.from_dict(d.pop("w_composite_operation"))

        w_scalar_type = BoundedInt.from_dict(d.pop("w_scalar_type"))

        w_container_type = BoundedInt.from_dict(d.pop("w_container_type"))

        w_composite_constant = BoundedInt.from_dict(d.pop("w_composite_constant"))

        w_scalar_constant = BoundedInt.from_dict(d.pop("w_scalar_constant"))

        mutations_config = cls(
            w_memory_operation=w_memory_operation,
            w_logical_operation=w_logical_operation,
            w_arithmetic_operation=w_arithmetic_operation,
            w_control_flow_operation=w_control_flow_operation,
            w_function_operation=w_function_operation,
            w_bitwise_operation=w_bitwise_operation,
            w_conversion_operation=w_conversion_operation,
            w_composite_operation=w_composite_operation,
            w_scalar_type=w_scalar_type,
            w_container_type=w_container_type,
            w_composite_constant=w_composite_constant,
            w_scalar_constant=w_scalar_constant,
        )

        mutations_config.additional_properties = d
        return mutations_config

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
