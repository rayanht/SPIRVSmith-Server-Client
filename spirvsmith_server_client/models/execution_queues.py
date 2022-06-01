from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.execution_queues_queues import ExecutionQueuesQueues

T = TypeVar("T", bound="ExecutionQueues")


@attr.s(auto_attribs=True)
class ExecutionQueues:
    """
    Attributes:
        queues (ExecutionQueuesQueues):
    """

    queues: ExecutionQueuesQueues
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        queues = self.queues.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "queues": queues,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        queues = ExecutionQueuesQueues.from_dict(d.pop("queues"))

        execution_queues = cls(
            queues=queues,
        )

        execution_queues.additional_properties = d
        return execution_queues

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
