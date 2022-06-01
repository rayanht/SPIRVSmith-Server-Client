from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.generator_info import GeneratorInfo

T = TypeVar("T", bound="ShaderSubmission")


@attr.s(auto_attribs=True)
class ShaderSubmission:
    """
    Attributes:
        shader_id (str):
        shader_assembly (str):
        generator_info (GeneratorInfo):
        prioritize (bool):
        n_buffers (int):
    """

    shader_id: str
    shader_assembly: str
    generator_info: GeneratorInfo
    prioritize: bool
    n_buffers: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shader_id = self.shader_id
        shader_assembly = self.shader_assembly
        generator_info = self.generator_info.to_dict()

        prioritize = self.prioritize
        n_buffers = self.n_buffers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shader_id": shader_id,
                "shader_assembly": shader_assembly,
                "generator_info": generator_info,
                "prioritize": prioritize,
                "n_buffers": n_buffers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        shader_id = d.pop("shader_id")

        shader_assembly = d.pop("shader_assembly")

        generator_info = GeneratorInfo.from_dict(d.pop("generator_info"))

        prioritize = d.pop("prioritize")

        n_buffers = d.pop("n_buffers")

        shader_submission = cls(
            shader_id=shader_id,
            shader_assembly=shader_assembly,
            generator_info=generator_info,
            prioritize=prioritize,
            n_buffers=n_buffers,
        )

        shader_submission.additional_properties = d
        return shader_submission

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
