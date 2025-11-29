from core.agent_manager import BaseAgent
from tools.google_directions_tool import GoogleDirectionsTool
from tools.google_distance_tool import GoogleDistanceTool
from core.logging import logger

class TransportAgent(BaseAgent):
    def __init__(self, client):
        super().__init__("TransportAgent", client)
        self.directions_tool = GoogleDirectionsTool()
        self.distance_tool = GoogleDistanceTool()

    def execute(self, itinerary_points):
        """
        itinerary_points: list of place names or coordinates in order
        """
        logger.info("TransportAgent calculating transport details")
        
        transport_plan = []
        for i in range(len(itinerary_points) - 1):
            origin = itinerary_points[i]
            destination = itinerary_points[i+1]
            
            # Get directions (driving as default)
            directions = self.directions_tool.get_directions(origin, destination)
            
            # Get distance matrix for precise time/distance
            matrix = self.distance_tool.get_distance_matrix([origin], [destination])
            
            segment = {
                "from": origin,
                "to": destination,
                "directions": directions[0]['legs'][0] if directions else {},
                "matrix": matrix['rows'][0]['elements'][0] if matrix and 'rows' in matrix else {}
            }
            transport_plan.append(segment)
            
        return transport_plan
