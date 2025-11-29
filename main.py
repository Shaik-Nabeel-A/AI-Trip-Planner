import os
from flask import Flask
from dotenv import load_dotenv
from google import genai
from api.routes import api_bp
from agents.coordinator_agent import CoordinatorAgent
from core.logging import logger

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Initialize Gemini Client
    api_key = os.getenv("GEMINI_KEY")
    if not api_key:
        logger.error("GEMINI_KEY not found")
        raise ValueError("GEMINI_KEY not found")
        
    client = genai.Client(api_key=api_key)
    
    # Initialize Coordinator
    coordinator = CoordinatorAgent(client)
    
    # Store in app config
    app.config['COORDINATOR'] = coordinator
    
    # Register Blueprints
    app.register_blueprint(api_bp, url_prefix='/api')
    
    @app.route('/')
    def index():
        from flask import render_template
        return render_template('index.html')

    return app

if __name__ == "__main__":
    app = create_app()
    logger.info("Starting Smart Travel Concierge API...")
    app.run(debug=True, port=5000)
