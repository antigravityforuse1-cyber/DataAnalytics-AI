from fastapi import APIRouter
from core.state_manager import state_manager

router = APIRouter()

@router.get("/{session_id}")
async def get_progress(session_id: str):
    state = state_manager.get_session_info(session_id)
    if not state:
        return {"error": "Session not found"}
    return {"completion_percentage": 100, "status": "ready"}
