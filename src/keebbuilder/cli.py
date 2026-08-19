import typer

from keebbuilder.domain.models import SoundProfile
from keebbuilder.domain.sound_profiles import recommended_case_materials

app = typer.Typer()


@app.command()
def pick_case(
    sound_profile: SoundProfile = typer.Option(
        ..., prompt="Sound profile", case_sensitive=False
    ),
) -> None:
    """Recommend case materials for a given sound profile."""
    materials = recommended_case_materials(sound_profile)
    typer.echo(f"Recommended case materials for {sound_profile.value}:")
    for material in materials:
        typer.echo(f"  - {material.value}")
