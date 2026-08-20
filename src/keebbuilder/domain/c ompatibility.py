from keebbuilder.domain.models import KeyboardSwitches, SoundProfile

_SOUND_PROFILE_SWITCH_TYPES: dict[SoundProfile, list[KeyboardSwitches]] = {
    SoundProfile.THOCKY: [KeyboardSwitches.LINEAR, KeyboardSwitches.TACTILE],
    SoundProfile.CLACKY: [KeyboardSwitches.CLICKY, KeyboardSwitches.TACTILE],
    SoundProfile.BALANCED: [
        KeyboardSwitches.LINEAR,
        KeyboardSwitches.TACTILE,
        KeyboardSwitches.CLICKY,
    ],
}

def get_compatible_switch_types(sound_profile: SoundProfile) -> list[KeyboardSwitches]:
    """Return switch types that are compatible with the given sound profile."""
    return _SOUND_PROFILE_SWITCH_TYPES[sound_profile]


