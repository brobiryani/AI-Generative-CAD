from fastapi import FastAPI

from app.api.v1.generate import router as generate_router
from app.api.v1.designs import router as designs_router
from app.api.v1.parameters import router as parameters_router
from app.database.database import Base, engine

# Import models so SQLAlchemy knows about them
from app.models.design import Design


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="AI Generative CAD API",
    description="Backend API for the AI-Driven Generative CAD Platform",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "AI Generative CAD API is running",
        "status": "success"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


app.include_router(
    generate_router,
    prefix="/api/v1",
    tags=["Design Generation"]
)

app.include_router(
    parameters_router,
    prefix="/api/v1",
    tags=["Parameter Extraction"]
)

app.include_router(
    designs_router,
    prefix="/api/v1",
    tags=["Designs"]
)