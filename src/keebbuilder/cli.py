import typer
from rich.console import Console
from rich.table import Table
from keebbuilder.domain.models import BuildPreferences, CaseMaterial, KeyboardSize, SoundProfile, KeyboardSwitches
from keebbuilder.domain.sound_profiles import recommended_case_materials
from keebbuilder.services.build_service import recommend_build
app = typer.Typer()
console = Console()

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
    case_material: CaseMaterial = typer.Option(
    ..., prompt="Case material (aluminum/polycarbonate/acrylic/wood/abs)", case_sensitive=False
),
) -> None:
    """Recommend case materials for a given sound profile."""
    preferences = BuildPreferences( 
        case_material=case_material,
        sound_profile=sound_profile,
        keyboard_size=keyboard_size,
        switch_type=switch_type,
    )

    recommendation = recommend_build(preferences)
    
    size_label = f"{keyboard_size.value}%" + (
        " (TKL)" if keyboard_size == KeyboardSize.TKL else ""
    )
       
    selections = Table(title="Your build Summary")
    selections.add_column("Preference", style="bold")
    selections.add_column("Choice")
    selections.add_row("Sound Profile", sound_profile.value)
    selections.add_row("Keyboard Size", size_label)
    selections.add_row("Switch Type", switch_type.value)
    console.print(selections)
    
    
    recommendations = Table(title="Recommended Case Materials")
    recommendations.add_column("Category", style="bold")
    recommendations.add_column("Options")
    recommendations.add_row(
        "Case Materials", ", ".join([material.value for material in recommendation.case_materials])
    )
    recommendations.add_row(
        "switches",
        ", ".join(f"{s.manufacturer} {s.name}" for s in recommendation.switches),
    )
    console.print(recommendations)
    
    
    