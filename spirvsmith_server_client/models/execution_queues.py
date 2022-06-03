from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.execution_queues_queues import ExecutionQueuesQueues
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionQueues")


@attr.s(auto_attribs=True)
class ExecutionQueues:
    """
    Attributes:
        queues (Union[Unset, ExecutionQueuesQueues]):
    """

    queues: Union[Unset, ExecutionQueuesQueues] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        queues: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.queues, Unset):
            queues = self.queues.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if queues is not UNSET:
            field_dict["queues"] = queues

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _queues = d.pop("queues", UNSET)
        queues: Union[Unset, ExecutionQueuesQueues]
        if isinstance(_queues, Unset):
            queues = UNSET
        else:
            queues = ExecutionQueuesQueues.from_dict(_queues)

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
