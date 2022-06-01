from enum import Enum


class HardwareType(str, Enum):
    CPU = "CPU"
    GPU = "GPU"

    def __str__(self) -> str:
        return str(self.value)
