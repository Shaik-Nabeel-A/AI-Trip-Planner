from core.agent_manager import BaseAgent
from core.logging import logger

class ItineraryAgent(BaseAgent):
    def __init__(self, client):
        super().__init__("ItineraryAgent", client)

    def execute(self, user_request, activities, hotels, restaurants, transport, budget):
        logger.info("ItineraryAgent generating final itinerary")
        
        # Extract location data for clustering
        activities_with_location = []
        for a in activities:
            activities_with_location.append({
                'name': a.get('name'),
                'vicinity': a.get('vicinity', ''),
                'lat': a.get('geometry', {}).get('location', {}).get('lat'),
                'lng': a.get('geometry', {}).get('location', {}).get('lng')
            })
        
        prompt = f"""
        Create a detailed travel itinerary based on the following data:
        
        User Request: {user_request}
        
        Selected Activities with Locations: {activities_with_location}
        Selected Hotels: {[h.get('name') for h in hotels]}
        Selected Restaurants: {[r.get('name') for r in restaurants]}
        Transport Details: {len(transport)} legs calculated
        Budget Estimate: {budget}
        
        CRITICAL INSTRUCTIONS FOR DAY PLANNING:
        1. **Group attractions by proximity**: Activities that are close to each other (within 1-2 km) should be visited on the SAME day
        2. **Logical flow**: Plan each day geographically - don't make tourists zigzag across the city
        3. **Realistic timing**: Each day should have 2-4 major activities, not just 1-2
        4. **Nearby clustering**: If multiple attractions are in the same area (like beach, memorial, and statue all at the same location), group them together in one day's itinerary
        5. **Fill the days**: Don't spread 3 nearby attractions across 3 days - combine them and suggest additional activities or relaxation time
        
        IMPORTANT FORMATTING INSTRUCTIONS:
        - For EVERY location, hotel, restaurant, or attraction you mention, format it as a clickable Google Maps link
        - Use this format: [Place Name](https://www.google.com/maps/search/?api=1&query=Place+Name+City)
        - Replace spaces with + in the URL
        - Example: [Taj Mahal](https://www.google.com/maps/search/?api=1&query=Taj+Mahal+Agra)
        
        Format the output as a beautiful Markdown itinerary with:
        - Day-by-day plan with proper headers (## for main sections, ### for subsections)
        - Each day should have Morning, Afternoon, and Evening sections
        - Hotel recommendations (each hotel name should be a clickable Google Maps link)
        - Dining suggestions (each restaurant name should be a clickable Google Maps link)
        - Activities and attractions (each should be a clickable Google Maps link)
        - Transport tips
        - Budget summary in a markdown table format
        
        Use proper markdown formatting including headers, bold text, bullet points, and tables.
        Remember: Make ALL place names clickable Google Maps links!
        """
        
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text
