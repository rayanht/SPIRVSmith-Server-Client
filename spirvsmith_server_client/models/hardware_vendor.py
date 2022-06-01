from enum import Enum


class HardwareVendor(str, Enum):
    GENUINEINTEL = "GenuineIntel"
    NVIDIA = "Nvidia"

    def __str__(self) -> str:
        return str(self.value)
