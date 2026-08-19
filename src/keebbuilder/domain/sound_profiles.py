from keebbuilder.domain.models import CaseMaterial, SoundProfile

_SOUND_PROFILE_MATERIALS: dict[SoundProfile, list[CaseMaterial]] = {
    SoundProfile.THOCKY: [CaseMaterial.POLYCARBONATE, CaseMaterial.WOOD],
    SoundProfile.CLACKY: [CaseMaterial.ALUMINUM, CaseMaterial.ACRYLIC],
    SoundProfile.BALANCED: [CaseMaterial.POLYCARBONATE, CaseMaterial.ABS],
}


def recommended_case_materials(profile: SoundProfile) -> list[CaseMaterial]:
    """Return case materials that best support the given sound profile.

    Case material is one of several contributors to a keyboard's sound
    (alongside mounting style, foam, and plate) -- this narrows the case
    material choice, it does not guarantee the resulting sound alone.
    """
    return _SOUND_PROFILE_MATERIALS[profile]
