from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.mutations_config import MutationsConfig

T = TypeVar("T", bound="FuzzingStrategy")


@attr.s(auto_attribs=True)
class FuzzingStrategy:
    """
    Attributes:
        mutations_config (MutationsConfig):
        enable_ext_glsl_std_450 (bool):
        w_memory_operation (int):
        w_logical_operation (int):
        w_arithmetic_operation (int):
        w_control_flow_operation (int):
        w_function_operation (int):
        w_bitwise_operation (int):
        w_conversion_operation (int):
        w_composite_operation (int):
        w_scalar_type (int):
        w_container_type (int):
        w_composite_constant (int):
        w_scalar_constant (int):
        p_statement (float):
        p_picking_statement_operand (float):
        mutation_rate (float):
    """

    mutations_config: MutationsConfig
    enable_ext_glsl_std_450: bool
    w_memory_operation: int
    w_logical_operation: int
    w_arithmetic_operation: int
    w_control_flow_operation: int
    w_function_operation: int
    w_bitwise_operation: int
    w_conversion_operation: int
    w_composite_operation: int
    w_scalar_type: int
    w_container_type: int
    w_composite_constant: int
    w_scalar_constant: int
    p_statement: float
    p_picking_statement_operand: float
    mutation_rate: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mutations_config = self.mutations_config.to_dict()

        enable_ext_glsl_std_450 = self.enable_ext_glsl_std_450
        w_memory_operation = self.w_memory_operation
        w_logical_operation = self.w_logical_operation
        w_arithmetic_operation = self.w_arithmetic_operation
        w_control_flow_operation = self.w_control_flow_operation
        w_function_operation = self.w_function_operation
        w_bitwise_operation = self.w_bitwise_operation
        w_conversion_operation = self.w_conversion_operation
        w_composite_operation = self.w_composite_operation
        w_scalar_type = self.w_scalar_type
        w_container_type = self.w_container_type
        w_composite_constant = self.w_composite_constant
        w_scalar_constant = self.w_scalar_constant
        p_statement = self.p_statement
        p_picking_statement_operand = self.p_picking_statement_operand
        mutation_rate = self.mutation_rate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mutations_config": mutations_config,
                "enable_ext_glsl_std_450": enable_ext_glsl_std_450,
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
                "p_statement": p_statement,
                "p_picking_statement_operand": p_picking_statement_operand,
                "mutation_rate": mutation_rate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mutations_config = MutationsConfig.from_dict(d.pop("mutations_config"))

        enable_ext_glsl_std_450 = d.pop("enable_ext_glsl_std_450")

        w_memory_operation = d.pop("w_memory_operation")

        w_logical_operation = d.pop("w_logical_operation")

        w_arithmetic_operation = d.pop("w_arithmetic_operation")

        w_control_flow_operation = d.pop("w_control_flow_operation")

        w_function_operation = d.pop("w_function_operation")

        w_bitwise_operation = d.pop("w_bitwise_operation")

        w_conversion_operation = d.pop("w_conversion_operation")

        w_composite_operation = d.pop("w_composite_operation")

        w_scalar_type = d.pop("w_scalar_type")

        w_container_type = d.pop("w_container_type")

        w_composite_constant = d.pop("w_composite_constant")

        w_scalar_constant = d.pop("w_scalar_constant")

        p_statement = d.pop("p_statement")

        p_picking_statement_operand = d.pop("p_picking_statement_operand")

        mutation_rate = d.pop("mutation_rate")

        fuzzing_strategy = cls(
            mutations_config=mutations_config,
            enable_ext_glsl_std_450=enable_ext_glsl_std_450,
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
            p_statement=p_statement,
            p_picking_statement_operand=p_picking_statement_operand,
            mutation_rate=mutation_rate,
        )

        fuzzing_strategy.additional_properties = d
        return fuzzing_strategy

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
