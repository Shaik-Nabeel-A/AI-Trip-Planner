from flask import Blueprint, request, jsonify
from agents.coordinator_agent import CoordinatorAgent
from google import genai
import os

api_bp = Blueprint('api', __name__)

# Initialize client here or in main and pass it? 
# For simplicity, we'll init here or use a global.
# Better: Dependency injection. We'll assume 'coordinator' is available in app config or global.

@api_bp.route('/plan', methods=['POST'])
def generate_plan():
    data = request.json
    user_prompt = data.get('prompt')
    
    if not user_prompt:
        return jsonify({"error": "No prompt provided"}), 400
        
    # Get coordinator from app context or global
    from flask import current_app
    coordinator = current_app.config['COORDINATOR']
    
    try:
        result = coordinator.execute(user_prompt)
        return jsonify({"plan": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
