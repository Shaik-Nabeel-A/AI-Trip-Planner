from core.agent_manager import BaseAgent
from tools.google_places_tool import GooglePlacesTool
from core.logging import logger

class ActivityAgent(BaseAgent):
    def __init__(self, client):
        super().__init__("ActivityAgent", client)
        self.places_tool = GooglePlacesTool()

    def execute(self, location, interests=None):
        logger.info(f"ActivityAgent searching for activities in {location} with interests {interests}")
        
        # Use LLM to refine search queries based on interests
        prompt = f"""
        Suggest 3 specific search queries to find top tourist attractions in {location}.
        Interests: {interests if interests else 'general sightseeing'}.
        Return only the queries separated by commas.
        """
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        queries = [q.strip() for q in response.text.split(',')]
        
        all_activities = []
        for query in queries:
            results = self.places_tool.search_places(location, query, type="tourist_attraction")
            all_activities.extend(results[:3]) # Top 3 per query
            
        # Deduplicate by place_id
        unique_activities = {a['place_id']: a for a in all_activities}.values()
        return list(unique_activities)
