from fastapi import APIRouter, File, UploadFile, HTTPException
import json
import uuid
import pandas as pd
from typing import Dict, Any

from core.state_manager import state_manager
from schemas.models import AnswerRequest
from modules import analysis_stage, query_parser

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith((".csv", ".xlsx")):
        raise HTTPException(status_code=400, detail="Only CSV and Excel files are supported")
    
    session_id = str(uuid.uuid4())
    state_manager.create_session(session_id)
    
    try:
        if file.filename.endswith(".csv"):
            df = pd.read_csv(file.file)
        else:
            df = pd.read_excel(file.file)
        
        state_manager.set_dataframe(session_id, df)
        
        # Initial analysis
        issues = analysis_stage.detect_issues(df)
        state_manager.update_state(session_id, {"stage": "cleaning", "detected_issues": issues})
        
        return {
            "session_id": session_id,
            "filename": file.filename,
            "columns": df.columns.tolist(),
            "rows": len(df),
            "issues": issues
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/ask")
async def ask_question(request: AnswerRequest):
    session_id = request.session_id
    query = request.action
    
    df = state_manager.get_dataframe(session_id)
    if df is None:
        raise HTTPException(status_code=400, detail="Session not found or expired")
    
    # Process the query using parsed logic
    result = query_parser.process_query(df, query)
    
    return {
        "reply": result.get("message", "Processed successfully"),
        "data": result.get("data", None),
        "visualizations": result.get("visualizations", [])
    }
