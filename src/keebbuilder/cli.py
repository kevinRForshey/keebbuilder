import typer
from keebbuilder.domain.models import KeyboardSize, BuildPreferences, SoundProfile, KeyboardSwitches
from keebbuilder.domain.sound_profiles import recommended_case_materials
from keebbuilder.services.build_service import recommend_build

app = typer.Typer()


@app.command()
def pick_case(
    sound_profile: SoundProfile = typer.Option(
        ..., prompt="Sound profile", case_sensitive=False
    ),
    keyboard_size: KeyboardSize = typer.Option(
        ..., prompt="Keyboard size (100/96/80/75/65/60/40)", case_sensitive=False
    ),
    switch_type: KeyboardSwitches = typer.Option(
        ..., prompt="Switch type (linear/tactile/clicky)", case_sensitive=False
    ),
) -> None:
    """Recommend case materials for a given sound profile."""
    preferences = BuildPreferences( 
        sound_profile=sound_profile,
        keyboard_size=keyboard_size,
        switch_type=switch_type,
    )

    recommendation = recommend_build(preferences)
    
