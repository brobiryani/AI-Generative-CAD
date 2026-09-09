import json
import requests

from app.schemas.llm import CADParameters


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:7b"


def extract_cad_parameters(description: str) -> CADParameters:
    """
    Extract CAD parameters using Ollama.
    """

    prompt = f"""
Extract CAD parameters from the following description.

Return ONLY valid JSON.

The JSON must contain exactly these fields:
- material
- force_n
- safety_factor
- length_mm
- width_mm
- height_mm

Rules:
1. Do not invent missing values.
2. Use null for parameters that are not provided.
3. Convert force to Newtons.
4. Convert dimensions to millimeters.

Description:
{description}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
            "format": "json"
        }
    )

    response.raise_for_status()

    result = response.json()

    data = json.loads(result["response"])

    return CADParameters(
        material=data.get("material"),
        force_n=data.get("force_n"),
        safety_factor=data.get("safety_factor"),
        length_mm=data.get("length_mm"),
        width_mm=data.get("width_mm"),
        height_mm=data.get("height_mm"),
    )