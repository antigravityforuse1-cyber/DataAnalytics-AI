from fastapi import APIRouter, HTTPException
from core.state_manager import state_manager
from schemas.enhanced_models import MLTrainRequest, MLPredictRequest
from modules import ml_service

router = APIRouter()

@router.post("/train")
async def train_model(request: MLTrainRequest):
    df = state_manager.get_dataframe(request.session_id)
    if df is None:
        raise HTTPException(status_code=404, detail="Session data not found")
    
    if request.target_column not in df.columns:
        raise HTTPException(status_code=400, detail="Target column not found in data")
        
    try:
        result = ml_service.train_model(df, request.target_column, request.task_type)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/predict")
async def predict_model(request: MLPredictRequest):
    try:
        result = ml_service.predict(request.model_id, request.data)
        return {"predictions": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
