import googlemaps
import os
from dotenv import load_dotenv
from core.tracing import trace_tool
from core.logging import logger

load_dotenv()

class GooglePlacesTool:
    def __init__(self):
        api_key = os.getenv("GOOGLE_MAPS_KEY")
        if not api_key:
            logger.error("GOOGLE_MAPS_KEY not found in environment variables")
            raise ValueError("GOOGLE_MAPS_KEY not found")
        self.client = googlemaps.Client(key=api_key)

    @trace_tool
    def search_places(self, location, query, radius=5000, type=None):
        """
        Search for places near a location.
        location: str or dict (lat/lng)
        query: str (e.g., "restaurants", "museums")
        radius: int (meters)
        type: str (optional place type)
        """
        try:
            # If location is a string name, geocode it first
            if isinstance(location, str):
                geocode_result = self.client.geocode(location)
                if geocode_result:
                    location = geocode_result[0]['geometry']['location']
                else:
                    return []

            results = self.client.places_nearby(
                location=location,
                keyword=query,
                radius=radius,
                type=type
            )
            return results.get('results', [])
        except Exception as e:
            logger.error(f"Error searching places: {e}")
            return []

    @trace_tool
    def get_place_details(self, place_id):
        try:
            result = self.client.place(place_id=place_id)
            return result.get('result', {})
        except Exception as e:
            logger.error(f"Error getting place details: {e}")
            return {}
