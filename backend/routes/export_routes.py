from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from core.state_manager import state_manager
from modules import export_service

router = APIRouter()

class ExportRequest(BaseModel):
    session_id: str
    format: str  # csv, excel, pdf, json

@router.post("/")
async def export_data(request: ExportRequest):
    df = state_manager.get_dataframe(request.session_id)
    if df is None:
        raise HTTPException(status_code=404, detail="Data not found for session")
    
    try:
        file_path = export_service.export_dataframe(df, request.format)
        return {"download_url": f"/api/export/download?path={file_path}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/download")
async def download_file(path: str):
    return FileResponse(path)
