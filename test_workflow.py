import os
from dotenv import load_dotenv
from google import genai
from agents.coordinator_agent import CoordinatorAgent
from core.logging import logger

load_dotenv()

def test_workflow():
    api_key = os.getenv("GEMINI_KEY")
    if not api_key:
        print("GEMINI_KEY not found")
        return

    client = genai.Client(api_key=api_key)
    coordinator = CoordinatorAgent(client)

    request = "I want to visit Paris for 2 days. I love art and history. Medium budget."
    print(f"Testing with request: {request}")
    
    try:
        result = coordinator.execute(request)
        print("\n=== FINAL ITINERARY ===\n")
        print(result)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_workflow()
