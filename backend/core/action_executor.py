"""
Action Executor - Processes NLP queries and executes dataframe operations.
"""
import pandas as pd
from core.state_manager import state_manager


class ActionExecutor:
    def execute(self, session_id: str, query: str) -> dict:
        df = state_manager.get_dataframe(session_id)
        if df is None:
            return {"reply": "No dataset loaded. Please upload a file first.", "visualizations": [], "data": None}

        query_lower = query.lower()

        # Basic stats
        if any(w in query_lower for w in ["describe", "summary", "statistics", "stats"]):
            desc = df.describe().to_dict()
            return {"reply": f"Here are the statistics for your dataset:\n{df.describe().to_string()}", "visualizations": [], "data": desc}

        # Show columns
        if "column" in query_lower:
            cols = list(df.columns)
            return {"reply": f"Your dataset has {len(cols)} columns:\n{', '.join(cols)}", "visualizations": [], "data": None}

        # Show head
        if any(w in query_lower for w in ["head", "first", "top", "preview", "show"]):
            sample = df.head(5).to_dict(orient="records")
            return {"reply": f"Here are the first 5 rows of your dataset:", "visualizations": [], "data": sample}

        # Show missing values
        if any(w in query_lower for w in ["missing", "null", "nan", "empty"]):
            missing = df.isnull().sum().to_dict()
            total_missing = sum(missing.values())
            return {
                "reply": f"Found {total_missing} missing values across your dataset:\n" +
                         "\n".join([f"  {col}: {cnt}" for col, cnt in missing.items() if cnt > 0]) or "No missing values!",
                "visualizations": [], "data": missing
            }

        # Count rows
        if any(w in query_lower for w in ["count", "rows", "records", "how many"]):
            return {"reply": f"Your dataset has {len(df):,} rows and {len(df.columns)} columns.", "visualizations": [], "data": None}

        # Default fallback
        return {
            "reply": f"I understood your query: '{query}'. Your dataset has {len(df):,} rows and {len(df.columns)} columns. Try asking for 'summary', 'columns', 'missing values', or 'show first rows'.",
            "visualizations": [],
            "data": None
        }


# Singleton instance
action_executor = ActionExecutor()
