from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.shader_submission import ShaderSubmission

T = TypeVar("T", bound="ExecutionQueue")


@attr.s(auto_attribs=True)
class ExecutionQueue:
    """
    Attributes:
        queue (List[ShaderSubmission]):
    """

    queue: List[ShaderSubmission]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        queue = []
        for queue_item_data in self.queue:
            queue_item = queue_item_data.to_dict()

            queue.append(queue_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "queue": queue,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        queue = []
        _queue = d.pop("queue")
        for queue_item_data in _queue:
            queue_item = ShaderSubmission.from_dict(queue_item_data)

            queue.append(queue_item)

        execution_queue = cls(
            queue=queue,
        )

        execution_queue.additional_properties = d
        return execution_queue

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
