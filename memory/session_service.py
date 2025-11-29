import uuid
from typing import Dict, List

class SessionService:
    def __init__(self):
        self._sessions: Dict[str, List[Dict]] = {} # session_id -> history

    def create_session(self) -> str:
        session_id = str(uuid.uuid4())
        self._sessions[session_id] = []
        return session_id

    def add_message(self, session_id: str, role: str, content: str):
        if session_id not in self._sessions:
            raise ValueError("Session not found")
        self._sessions[session_id].append({"role": role, "content": content})

    def get_history(self, session_id: str) -> List[Dict]:
        return self._sessions.get(session_id, [])
