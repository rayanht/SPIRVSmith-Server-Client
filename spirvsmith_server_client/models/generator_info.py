from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.fuzzing_strategy import FuzzingStrategy
from ..types import UNSET, Unset

T = TypeVar("T", bound="GeneratorInfo")


@attr.s(auto_attribs=True)
class GeneratorInfo:
    """
    Attributes:
        id (str):
        fuzzer_version (str):
        strategy (Union[Unset, FuzzingStrategy]):
    """

    id: str
    fuzzer_version: str
    strategy: Union[Unset, FuzzingStrategy] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        fuzzer_version = self.fuzzer_version
        strategy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.strategy, Unset):
            strategy = self.strategy.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "fuzzer_version": fuzzer_version,
            }
        )
        if strategy is not UNSET:
            field_dict["strategy"] = strategy

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        fuzzer_version = d.pop("fuzzer_version")

        _strategy = d.pop("strategy", UNSET)
        strategy: Union[Unset, FuzzingStrategy]
        if isinstance(_strategy, Unset):
            strategy = UNSET
        else:
            strategy = FuzzingStrategy.from_dict(_strategy)

        generator_info = cls(
            id=id,
            fuzzer_version=fuzzer_version,
            strategy=strategy,
        )

        generator_info.additional_properties = d
        return generator_info

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
