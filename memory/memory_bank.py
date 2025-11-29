from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class UserPreferences:
    cuisines: List[str] = field(default_factory=list)
    budget_range: Dict[str, int] = field(default_factory=lambda: {"min": 0, "max": 10000})
    hotel_comfort: str = "medium" # budget, medium, luxury
    interests: List[str] = field(default_factory=list) # history, beach, adventure

class MemoryBank:
    def __init__(self):
        self._store = {} # user_id -> UserPreferences

    def get_preferences(self, user_id: str) -> UserPreferences:
        if user_id not in self._store:
            self._store[user_id] = UserPreferences()
        return self._store[user_id]

    def update_preferences(self, user_id: str, **kwargs):
        prefs = self.get_preferences(user_id)
        for key, value in kwargs.items():
            if hasattr(prefs, key):
                setattr(prefs, key, value)
        self._store[user_id] = prefs
