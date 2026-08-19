from enum import Enum


class SoundProfile(str, Enum):
    THOCKY = "thocky"
    CLACKY = "clacky"
    BALANCED = "balanced"


class CaseMaterial(str, Enum):
    ALUMINUM = "aluminum"
    POLYCARBONATE = "polycarbonate"
    ACRYLIC = "acrylic"
    WOOD = "wood"
    ABS = "abs"

