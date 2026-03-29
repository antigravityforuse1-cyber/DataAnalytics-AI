import sys
import traceback

try:
    import uvicorn
    import os
    from fastapi import FastAPI
    from fastapi.middleware.cors import CORSMiddleware
    from config.production import settings

    from routes import analysis_handler, export_routes, ml_routes, progress_routes

    app = FastAPI(
        title="Data Assistant API",
        description="Backend API for conversational data analysis",
        version="1.0.0"
    )

    # CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.get_cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include routers
    app.include_router(analysis_handler.router, prefix="/api/analysis", tags=["Analysis"])
    app.include_router(export_routes.router, prefix="/api/export", tags=["Export"])
    app.include_router(ml_routes.router, prefix="/api/ml", tags=["Machine Learning"])
    app.include_router(progress_routes.router, prefix="/api/progress", tags=["Progress tracking"])

    # Ensure upload/export dirs exist
    if not os.path.exists(settings.upload_dir):
        os.makedirs(settings.upload_dir)
    if not os.path.exists(settings.export_dir):
        os.makedirs(settings.export_dir)

    @app.get("/health")
    async def health_check():
        return {"status": "ok"}

    if __name__ == "__main__":
        uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

except Exception as e:
    print("CRITICAL ERROR DURING STARTUP:", file=sys.stderr)
    traceback.print_exc(file=sys.stderr)
    sys.exit(1)
