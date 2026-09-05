from pydantic import BaseModel, Field
from typing import Optional


class GenerateRequest(BaseModel):
    description: str = Field(..., min_length=5)

    material: Optional[str] = None

    force_n: Optional[float] = Field(
        None,
        gt=0,
        description="Applied force in Newtons"
    )

    safety_factor: Optional[float] = Field(
        None,
        gt=0,
        description="Required safety factor"
    )

    length_mm: Optional[float] = Field(
        None,
        gt=0,
        description="Length in millimeters"
    )

    width_mm: Optional[float] = Field(
        None,
        gt=0,
        description="Width in millimeters"
    )

    height_mm: Optional[float] = Field(
        None,
        gt=0,
        description="Height in millimeters"
    )