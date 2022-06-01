from enum import Enum


class OperatingSystem(str, Enum):
    LINUX = "Linux"
    DARWIN = "Darwin"
    WINDOWS = "Windows"

    def __str__(self) -> str:
        return str(self.value)
