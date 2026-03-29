import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.production import settings

from routes import analysis_handler, export_routes, ml_routes, progress_routes

app = FastAPI(
    title="Data Assistant API",
    description="Conversational AI Data Assistant for Data Analysis",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root path
@app.get("/")
def read_root():
    return {"message": "Welcome to Data Assistant API. Visit /docs for API documentation."}

# Health check
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "environment": settings.environment,
        "version": app.version
    }

# Include routers
app.include_router(analysis_handler.router, prefix="/api/analysis", tags=["Analysis"])
app.include_router(export_routes.router, prefix="/api/export", tags=["Export"])
app.include_router(ml_routes.router, prefix="/api/ml", tags=["Machine Learning"])
app.include_router(progress_routes.router, prefix="/api/progress", tags=["Progress tracking"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
