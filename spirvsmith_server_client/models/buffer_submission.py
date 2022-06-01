from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.execution_platform import ExecutionPlatform

T = TypeVar("T", bound="BufferSubmission")


@attr.s(auto_attribs=True)
class BufferSubmission:
    """
    Attributes:
        executor (ExecutionPlatform):
        buffer_dump (str):
    """

    executor: ExecutionPlatform
    buffer_dump: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        executor = self.executor.to_dict()

        buffer_dump = self.buffer_dump

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "executor": executor,
                "buffer_dump": buffer_dump,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        executor = ExecutionPlatform.from_dict(d.pop("executor"))

        buffer_dump = d.pop("buffer_dump")

        buffer_submission = cls(
            executor=executor,
            buffer_dump=buffer_dump,
        )

        buffer_submission.additional_properties = d
        return buffer_submission

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
