from core.agent_manager import BaseAgent
from tools.google_places_tool import GooglePlacesTool
from core.logging import logger

class HotelAgent(BaseAgent):
    def __init__(self, client):
        super().__init__("HotelAgent", client)
        self.places_tool = GooglePlacesTool()

    def execute(self, location, budget_range=None, comfort_level="medium"):
        logger.info(f"HotelAgent searching for hotels in {location}")
        
        query = f"{comfort_level} hotels in {location}"
        results = self.places_tool.search_places(location, query, type="lodging")
        
        # Filter by rating (simple heuristic)
        filtered = [h for h in results if h.get('rating', 0) >= 4.0]
        return filtered[:5]
