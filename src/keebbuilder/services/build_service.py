from keebbuilder.domain.models import BuildPreferences, BuildRecommendation, KeyboardSwitches
from keebbuilder.domain.sound_profiles import recommended_case_materials
from keebbuilder.domain.switches import get_switches_by_type

def recommend_build(preferences: BuildPreferences) -> BuildRecommendation:
    """Recommend case materials and switches based on user preferences."""
    case_materials = recommended_case_materials(preferences.sound_profile)
    switches = get_switches_by_type(preferences.switch_type)
    return BuildRecommendation(case_materials=case_materials, switches=switches)
