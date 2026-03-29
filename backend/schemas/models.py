from pydantic import BaseModel
from typing import Optional


class AnswerRequest(BaseModel):
    session_id: str
    action: str
    context: Optional[dict] = None


class ExportRequest(BaseModel):
    session_id: str
    format: str = "csv"  # csv, excel, pdf


class MLRequest(BaseModel):
    session_id: str
    target_column: str
    model_type: str = "auto"
