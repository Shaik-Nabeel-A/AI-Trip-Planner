import requests
import os
from dotenv import load_dotenv
from core.tracing import trace_tool
from core.logging import logger

load_dotenv()

class GoogleSearchTool:
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_SEARCH_KEY")
        self.cx = os.getenv("GOOGLE_SEARCH_CX")
        if not self.api_key or not self.cx:
            logger.warning("GOOGLE_SEARCH_KEY or GOOGLE_SEARCH_CX not found. Search tool will return empty results.")

    @trace_tool
    def search(self, query, num_results=5):
        if not self.api_key or not self.cx:
            return []
            
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "key": self.api_key,
            "cx": self.cx,
            "q": query,
            "num": num_results
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("items", [])
        except Exception as e:
            logger.error(f"Error performing Google Search: {e}")
            return []
