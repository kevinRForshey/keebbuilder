import typer

from keebbuilder.domain.models import KeyboardSize, SoundProfile
from keebbuilder.domain.sound_profiles import recommended_case_materials

app = typer.Typer()


@app.command()
def pick_case(
    sound_profile: SoundProfile = typer.Option(
        ..., prompt="Sound profile", case_sensitive=False
    ),
    keyboard_size: KeyboardSize = typer.Option(
        ..., prompt="Keyboard size (100/96/80/75/65/60/40)", case_sensitive=False
    ),
) -> None:
    """Recommend case materials for a given sound profile."""
    materials = recommended_case_materials(sound_profile)
    size_label = f"{keyboard_size.value}%" + (
        " (TKL)" if keyboard_size == KeyboardSize.TKL else ""
    )
    typer.echo(f"Recommended case materials for {sound_profile.value}:")
    for material in materials:
        typer.echo(f"  - {material.value}")
        
        
    typer.echo(f"Keyboard size: {size_label}")
