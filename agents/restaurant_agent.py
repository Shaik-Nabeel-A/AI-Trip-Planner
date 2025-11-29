from core.agent_manager import BaseAgent
from tools.google_places_tool import GooglePlacesTool
from core.logging import logger

class RestaurantAgent(BaseAgent):
    def __init__(self, client):
        super().__init__("RestaurantAgent", client)
        self.places_tool = GooglePlacesTool()

    def execute(self, location, cuisines=None):
        logger.info(f"RestaurantAgent searching for restaurants in {location} with cuisines {cuisines}")
        
        queries = []
        if cuisines:
            for cuisine in cuisines:
                queries.append(f"best {cuisine} restaurants in {location}")
        else:
            queries.append(f"best restaurants in {location}")
            
        all_restaurants = []
        for query in queries:
            results = self.places_tool.search_places(location, query, type="restaurant")
            all_restaurants.extend(results[:3])
            
        unique_restaurants = {r['place_id']: r for r in all_restaurants}.values()
        return list(unique_restaurants)
