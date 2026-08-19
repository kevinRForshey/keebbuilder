from enum import Enum
from dataclasses import dataclass

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


class KeyboardSize(str, Enum):
    FULL_SIZE = "100"
    NINETY_SIX_PERCENT = "96"
    TKL = "80"
    SEVENTY_FIVE_PERCENT = "75"
    SIXTY_FIVE_PERCENT = "65"
    SIXTY_PERCENT = "60"
    FORTY_PERCENT = "40"
    
class KeyboardSwitches(str, Enum):
    LINEAR = "linear"
    TACTILE = "tactile"
    CLICKY = "clicky"
    
@dataclass(frozen=True)
class Switch:
    name: str
    manufacturer: str
    switch_type: KeyboardSwitches

@dataclass(frozen=True)
class BuildPreferences:
    sound_profile: SoundProfile
    keyboard_size: KeyboardSize
    switch_type: KeyboardSwitches
    
@dataclass(frozen=True)
class BuildRecommendation: 
    case_materials: list[CaseMaterial]
    switches: list[Switch]
    switch_type: list[KeyboardSwitches]


