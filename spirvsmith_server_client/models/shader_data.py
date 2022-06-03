from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ShaderData")


@attr.s(auto_attribs=True)
class ShaderData:
    """
    Attributes:
        shader_id (str):
        shader_assembly (str):
        generator_version (str):
    """

    shader_id: str
    shader_assembly: str
    generator_version: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shader_id = self.shader_id
        shader_assembly = self.shader_assembly
        generator_version = self.generator_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shader_id": shader_id,
                "shader_assembly": shader_assembly,
                "generator_version": generator_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        shader_id = d.pop("shader_id")

        shader_assembly = d.pop("shader_assembly")

        generator_version = d.pop("generator_version")

        shader_data = cls(
            shader_id=shader_id,
            shader_assembly=shader_assembly,
            generator_version=generator_version,
        )

        shader_data.additional_properties = d
        return shader_data

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
