from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="BoundedInt")


@attr.s(auto_attribs=True)
class BoundedInt:
    """
    Attributes:
        min_ (int):
        max_ (int):
    """

    min_: int
    max_: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        min_ = self.min_
        max_ = self.max_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "min": min_,
                "max": max_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        min_ = d.pop("min")

        max_ = d.pop("max")

        bounded_int = cls(
            min_=min_,
            max_=max_,
        )

        bounded_int.additional_properties = d
        return bounded_int

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
