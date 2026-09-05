def calculate_design_force(force_n: float, safety_factor: float) -> float:
    """
    Calculate the design force using the applied force
    and safety factor.
    """
    return force_n * safety_factor