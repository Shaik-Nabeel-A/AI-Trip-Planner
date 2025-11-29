import googlemaps
import os
from dotenv import load_dotenv
from core.tracing import trace_tool
from core.logging import logger

load_dotenv()

class GoogleDistanceTool:
    def __init__(self):
        api_key = os.getenv("GOOGLE_MAPS_KEY")
        if not api_key:
            logger.error("GOOGLE_MAPS_KEY not found")
            raise ValueError("GOOGLE_MAPS_KEY not found")
        self.client = googlemaps.Client(key=api_key)

    @trace_tool
    def get_distance_matrix(self, origins, destinations, mode="driving"):
        """
        Get distance and duration between origins and destinations.
        origins: list of locations
        destinations: list of locations
        """
        try:
            matrix = self.client.distance_matrix(
                origins,
                destinations,
                mode=mode
            )
            return matrix
        except Exception as e:
            logger.error(f"Error getting distance matrix: {e}")
            return {}
