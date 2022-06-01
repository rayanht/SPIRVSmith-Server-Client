from enum import Enum


class VulkanBackend(str, Enum):
    MOLTENVK = "MoltenVK"
    SWIFTSHADER = "SwiftShader"
    VULKAN = "Vulkan"

    def __str__(self) -> str:
        return str(self.value)
