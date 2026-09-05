from fastapi import APIRouter
from app.schemas.generate import GenerateRequest
from app.services.design_service import create_design, get_design, get_all_designs

router = APIRouter()


@router.post("/")
def save_design(request: GenerateRequest):
    return create_design(
        {
            "description": request.description,
            "material": request.material,
            "force_n": request.force_n,
            "design_force_n": request.force_n * request.safety_factor,
            "safety_factor": request.safety_factor,
            "length_mm": request.length_mm,
            "width_mm": request.width_mm,
            "height_mm": request.height_mm,
        }
    )


@router.get("/{design_id}")
def fetch_design(design_id: int):
    return get_design(design_id)


@router.get("/")
def fetch_all_designs():
    return get_all_designs()