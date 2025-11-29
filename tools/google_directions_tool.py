import googlemaps
import os
from dotenv import load_dotenv
from core.tracing import trace_tool
from core.logging import logger

load_dotenv()

class GoogleDirectionsTool:
    def __init__(self):
        api_key = os.getenv("GOOGLE_MAPS_KEY")
        if not api_key:
            logger.error("GOOGLE_MAPS_KEY not found")
            raise ValueError("GOOGLE_MAPS_KEY not found")
        self.client = googlemaps.Client(key=api_key)

    @trace_tool
    def get_directions(self, origin, destination, mode="driving"):
        """
        Get directions between two points.
        mode: "driving", "walking", "bicycling", "transit"
        """
        try:
            directions = self.client.directions(
                origin,
                destination,
                mode=mode
            )
            return directions
        except Exception as e:
            logger.error(f"Error getting directions: {e}")
            return []
