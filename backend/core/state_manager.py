"""
State Manager - Manages DataFrames in memory per session.
"""
import uuid
import pandas as pd
from typing import Dict, Optional


class StateManager:
    def __init__(self):
        self._sessions: Dict[str, dict] = {}

    def create_session(self) -> str:
        session_id = str(uuid.uuid4())
        self._sessions[session_id] = {
            "df": None,
            "filename": None,
            "columns": [],
            "row_count": 0
        }
        return session_id

    def set_dataframe(self, session_id: str, df: pd.DataFrame, filename: str):
        if session_id not in self._sessions:
            self._sessions[session_id] = {}
        self._sessions[session_id]["df"] = df
        self._sessions[session_id]["filename"] = filename
        self._sessions[session_id]["columns"] = list(df.columns)
        self._sessions[session_id]["row_count"] = len(df)

    def get_dataframe(self, session_id: str) -> Optional[pd.DataFrame]:
        session = self._sessions.get(session_id)
        if session:
            return session.get("df")
        return None

    def get_session_info(self, session_id: str) -> Optional[dict]:
        return self._sessions.get(session_id)

    def session_exists(self, session_id: str) -> bool:
        return session_id in self._sessions and self._sessions[session_id].get("df") is not None

    def delete_session(self, session_id: str):
        if session_id in self._sessions:
            del self._sessions[session_id]


# Singleton instance
state_manager = StateManager()
