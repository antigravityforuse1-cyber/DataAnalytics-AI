import pandas as pd
import uuid

def train_model(df: pd.DataFrame, target_column: str, task_type: str):
    # Dummy mock implementation to prevent sklearn from failing if imports missing
    return {
        "status": "success",
        "model_id": str(uuid.uuid4()),
        "metrics": {"accuracy": 0.85} if task_type == "classification" else {"r2": 0.85},
        "feature_importance": {col: 0.1 for col in df.columns if col != target_column}
    }

def predict(model_id: str, data: list):
    # Return dummy predictions
    return [0 for _ in data]
