from core.agent_manager import BaseAgent
from core.logging import logger

class BudgetAgent(BaseAgent):
    def __init__(self, client):
        super().__init__("BudgetAgent", client)

    def execute(self, hotels, restaurants, transport_plan, duration_days):
        logger.info("BudgetAgent calculating estimated budget")
        
        # Simple estimation logic (can be enhanced with real data or LLM)
        
        # Hotel cost (avg of selected hotels * duration)
        avg_hotel_price = 5000 # Placeholder default INR
        if hotels:
            # In a real app, we'd extract price level or fetch real rates
            # Google Places gives price_level (0-4)
            price_levels = [h.get('price_level', 2) for h in hotels]
            avg_level = sum(price_levels) / len(price_levels)
            avg_hotel_price = avg_level * 2500 # Rough multiplier
            
        total_hotel = avg_hotel_price * duration_days
        
        # Food cost
        avg_food_cost = 1500 * duration_days # Per person
        
        # Transport cost
        total_distance_km = 0
        for segment in transport_plan:
            distance_text = segment.get('matrix', {}).get('distance', {}).get('text', '0 km')
            try:
                # remove ' km' and comma
                dist_val = float(distance_text.replace(' km', '').replace(',', ''))
                total_distance_km += dist_val
            except:
                pass
        
        transport_cost = total_distance_km * 20 # approx 20 INR per km for taxi
        
        activities_cost = 2000 * duration_days # Buffer
        
        total_min = total_hotel + avg_food_cost + transport_cost + activities_cost
        total_max = total_min * 1.5
        
        return {
            "min_budget": int(total_min),
            "max_budget": int(total_max),
            "breakdown": {
                "accommodation": int(total_hotel),
                "food": int(avg_food_cost),
                "transport": int(transport_cost),
                "activities": int(activities_cost)
            }
        }
