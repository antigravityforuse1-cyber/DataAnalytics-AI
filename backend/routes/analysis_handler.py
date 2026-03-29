from fastapi import APIRouter, File, UploadFile, HTTPException
import uuid
import pandas as pd

from core.state_manager import state_manager
from core.action_executor import action_executor
from schemas.models import AnswerRequest
from modules import analysis_stage

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith((".csv", ".xlsx")):
        raise HTTPException(status_code=400, detail="Only CSV and Excel files are supported")

    session_id = str(uuid.uuid4())

    try:
        if file.filename.endswith(".csv"):
            df = pd.read_csv(file.file)
        else:
            df = pd.read_excel(file.file)

        state_manager.set_dataframe(session_id, df, file.filename)

        # Initial analysis
        issues = analysis_stage.detect_issues(df)

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

    if not state_manager.session_exists(session_id):
        raise HTTPException(status_code=400, detail="Session not found or expired. Please upload a file first.")

    result = action_executor.execute(session_id, query)

    return {
        "reply": result.get("reply", "Processed successfully"),
        "data": result.get("data", None),
        "visualizations": result.get("visualizations", [])
    }
