from keebbuilder.domain.models import KeyboardSwitches, Switch


_SWITCH_CATALOG: list[Switch] = [
     Switch(name="Cherry MX Red", manufacturer="Cherry", switch_type=KeyboardSwitches.LINEAR),
    Switch(name="Gateron Yellow", manufacturer="Gateron", switch_type=KeyboardSwitches.LINEAR),
    Switch(name="Cherry MX Brown", manufacturer="Cherry", switch_type=KeyboardSwitches.TACTILE),
    Switch(name="Boba U4", manufacturer="Boba", switch_type=KeyboardSwitches.TACTILE),
    Switch(name="Cherry MX Blue", manufacturer="Cherry", switch_type=KeyboardSwitches.CLICKY),
    Switch(name="Kailh Box White", manufacturer="Kailh", switch_type=KeyboardSwitches.CLICKY),
]

def get_switches_by_type(switch_type: KeyboardSwitches) -> list[Switch]:
    """Return catalog switches matching the given switch type."""
    return [switch for switch in _SWITCH_CATALOG if switch.switch_type == switch_type]