import pandas as pd

def generate_chart(df: pd.DataFrame):
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    
    if not numeric_cols:
        return {"type": "none", "data": []}
        
    # Just return a simple representation ready for recharts
    if len(numeric_cols) >= 2: # Scatter or Bar
        sampled = df.head(10)[numeric_cols].to_dict('records')
        return {
            "type": "bar",
            "xAxis": numeric_cols[0],
            "yAxis": numeric_cols[1],
            "data": sampled
        }
    else:
        sampled = df.head(10)[numeric_cols].to_dict('records')
        return {
            "type": "line",
            "xAxis": "index",
            "yAxis": numeric_cols[0],
            "data": sampled
        }
