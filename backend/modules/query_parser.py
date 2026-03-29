import pandas as pd
from typing import Dict, Any
from . import visualization_engine
from . import insight_generator

def process_query(df: pd.DataFrame, query: str) -> Dict[str, Any]:
    query_lower = query.lower()
    
    # Simple simulated NLP parsing
    if "show" in query_lower and "chart" in query_lower:
        viz = visualization_engine.generate_chart(df)
        return {
            "message": "Here is the visualization based on your data.",
            "visualizations": [viz]
        }
    elif "summarize" in query_lower or "insight" in query_lower:
        summary = insight_generator.generate_insights(df)
        return {
            "message": "I have summarized the data for you.",
            "data": summary
        }
    else:
        # Default fallback
        desc = df.describe().to_dict()
        return {
            "message": "I've analyzed your request and provided general descriptive stats.",
            "data": {"describe": desc}
        }
