from pydantic import BaseModel
from typing import Optional, Dict, Any, List

class MLTrainRequest(BaseModel):
    session_id: str
    target_column: str
    task_type: str = "classification"  # or regression
    features: Optional[List[str]] = None
    hyperparameters: Optional[Dict[str, Any]] = None

class MLPredictRequest(BaseModel):
    session_id: str
    model_id: str
    data: List[Dict[str, Any]]

class MLTrainResponse(BaseModel):
    status: str
    model_id: str
    metrics: Dict[str, Any]
    feature_importance: Optional[Dict[str, float]] = None

class MLPredictResponse(BaseModel):
    status: str
    predictions: List[Any]
