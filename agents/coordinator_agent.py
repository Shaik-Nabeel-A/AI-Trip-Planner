from core.agent_manager import BaseAgent
from agents.activity_agent import ActivityAgent
from agents.hotel_agent import HotelAgent
from agents.restaurant_agent import RestaurantAgent
from agents.transport_agent import TransportAgent
from agents.budget_agent import BudgetAgent
from agents.itinerary_agent import ItineraryAgent
from core.logging import logger
import json

class CoordinatorAgent(BaseAgent):
    def __init__(self, client):
        super().__init__("CoordinatorAgent", client)
        self.activity_agent = ActivityAgent(client)
        self.hotel_agent = HotelAgent(client)
        self.restaurant_agent = RestaurantAgent(client)
        self.transport_agent = TransportAgent(client)
        self.budget_agent = BudgetAgent(client)
        self.itinerary_agent = ItineraryAgent(client)

    def execute(self, user_request):
        logger.info(f"Coordinator received request: {user_request}")
        
        # 1. Parse Request
        extraction_prompt = f"""
        Extract the following from the user request:
        - destination (city/location)
        - duration_days (int)
        - interests (list of strings)
        - budget_level (low, medium, high)
        
        Request: "{user_request}"
        
        Return JSON only.
        """
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=extraction_prompt,
            config={'response_mime_type': 'application/json'}
        )
        try:
            plan_data = json.loads(response.text)
        except:
            # Fallback defaults
            plan_data = {"destination": "Goa", "duration_days": 3, "interests": [], "budget_level": "medium"}
            
        location = plan_data.get("destination")
        duration = int(plan_data.get("duration_days", 3))
        interests = plan_data.get("interests", [])
        
        # 2. Parallel Execution (Sequential for now for simplicity)
        activities = self.activity_agent.execute(location, interests)
        hotels = self.hotel_agent.execute(location, comfort_level=plan_data.get("budget_level"))
        restaurants = self.restaurant_agent.execute(location)
        
        # 3. Transport Logic
        # Create a simple route from hotel -> activity 1 -> activity 2 ...
        route_points = []
        if hotels:
            route_points.append(hotels[0].get('name', location)) # Start at hotel
        for act in activities:
            route_points.append(act.get('name'))
            
        transport_plan = self.transport_agent.execute(route_points)
        
        # 4. Budget
        budget = self.budget_agent.execute(hotels, restaurants, transport_plan, duration)
        
        # 5. Final Itinerary
        final_plan = self.itinerary_agent.execute(
            user_request, activities, hotels, restaurants, transport_plan, budget
        )
        
        return final_plan
