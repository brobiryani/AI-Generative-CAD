from fastapi import FastAPI

app = FastAPI(
    title="AI Generative CAD API",
    description="Backend API for the AI-Driven Generative CAD Platform",
    version="1.0.0"
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