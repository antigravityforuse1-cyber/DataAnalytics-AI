from fastapi import APIRouter
from core.state_manager import state_manager

router = APIRouter()

@router.get("/{session_id}")
async def get_progress(session_id: str):
    state = state_manager.get_state(session_id)
    if not state:
        return {"error": "Session not found"}
    return state.get("progress", {"completion_percentage": 0})
