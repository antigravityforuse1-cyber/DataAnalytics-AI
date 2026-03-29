import pandas as pd
from typing import List, Dict, Any

def detect_issues(df: pd.DataFrame) -> List[Dict[str, Any]]:
    issues = []
    
    # Missing values
    missing = df.isnull().sum()
    if missing.sum() > 0:
        issues.append({
            "type": "missing_values",
            "description": f"Found {missing.sum()} missing values across columns",
            "columns": missing[missing > 0].to_dict()
        })
        
    # Duplicates
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        issues.append({
            "type": "duplicates",
            "description": f"Found {duplicates} duplicate rows",
            "count": int(duplicates)
        })
        
    return issues
