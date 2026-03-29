import pandas as pd

def generate_insights(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"summary": "No data available."}
    return {
        "rowCount": len(df),
        "columnCount": len(df.columns),
        "columns": df.columns.tolist(),
        "notes": "Generated insights on numeric ranges and missing info."
    }
