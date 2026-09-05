from fastapi import APIRouter
from app.schemas.generate import GenerateRequest
from app.services.generation_service import generate_design

router = APIRouter()


@router.post("/generate")
def generate(request: GenerateRequest):
    return generate_design(
        description=request.description,
        material=request.material,
        force_n=request.force_n,
        safety_factor=request.safety_factor,
        length_mm=request.length_mm,
        width_mm=request.width_mm,
        height_mm=request.height_mm,
    )