from app.optimization.calculations import calculate_design_force


def generate_design(
    description: str,
    material: str | None = None,
    force_n: float | None = None,
    safety_factor: float | None = None,
    length_mm: float | None = None,
    width_mm: float | None = None,
    height_mm: float | None = None,
):
    """
    Process a CAD design request and calculate
    the required design force.
    """

    design_force = None

    if force_n is not None and safety_factor is not None:
        design_force = calculate_design_force(
            force_n,
            safety_factor
        )

    return {
        "description": description,
        "material": material,
        "force_n": force_n,
        "safety_factor": safety_factor,
        "design_force_n": design_force,
        "length_mm": length_mm,
        "width_mm": width_mm,
        "height_mm": height_mm,
    }