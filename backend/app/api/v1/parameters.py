from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, ValidationError

from app.services.llm_service import extract_cad_parameters


router = APIRouter()


class ParameterExtractionRequest(BaseModel):
    description: str = Field(..., min_length=5)


@router.post("/extract-parameters")
def extract_parameters(request: ParameterExtractionRequest):
    try:
        parameters = extract_cad_parameters(request.description)

        return {
            "description": request.description,
            "parameters": parameters.model_dump()
        }

    except ValidationError as e:
        raise HTTPException(
            status_code=422,
            detail={
                "message": "Invalid CAD parameters extracted from the description.",
                "errors": e.errors()
            }
        )