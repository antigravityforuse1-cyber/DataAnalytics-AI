import os
import uuid
import pandas as pd

EXPORT_DIR = "./exports"

def export_dataframe(df: pd.DataFrame, format_type: str) -> str:
    os.makedirs(EXPORT_DIR, exist_ok=True)
    file_id = str(uuid.uuid4())
    
    if format_type == "csv":
        path = f"{EXPORT_DIR}/{file_id}.csv"
        df.to_csv(path, index=False)
        return path
    elif format_type == "json":
        path = f"{EXPORT_DIR}/{file_id}.json"
        df.to_json(path, orient="records")
        return path
    else:
        # Fallback to csv
        path = f"{EXPORT_DIR}/{file_id}.csv"
        df.to_csv(path, index=False)
        return path
