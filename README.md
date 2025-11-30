# 🧳 SAI Multi-Agent Trip Planner
### *Powered by Gemini 2.0 + Google Maps APIs + Modern Agentic AI Design*

## 📌 1. Overview

The **Smart Travel Concierge** is a multi-agent travel planning system that helps tourists generate a complete travel plan using natural language.
A user simply says:

> “I'm visiting Goa for 3–4 days. Suggest places, hotels, restaurants, transport options, and my budget.”

The system outputs:
✔ Full itinerary
✔ Distances + navigation links
✔ Bus/metro routes
✔ Hotels to stay (Google Hotels / Places API)
✔ Best restaurants nearby
✔ Minimum & maximum budget
✔ Personalized recommendations based on saved preferences

This project uses **Gemini**, **Google APIs**, and the full **Agentic AI tool stack** to create a high-quality, production-ready travel planner.

## 📌 Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd smart-travel-concierge
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Setup Environment:**
    Create a `.env` file with your API keys:
    ```
    GEMINI_KEY=your_key_here
    GOOGLE_MAPS_KEY=your_key_here
    ```

## 📌 Usage

1.  **Run the application:**

    ```bash
    python main.py
    ```

2.  **Access the platform:**
    Open your browser and navigate to `http://127.0.0.1:5000`.

3.  **Example Prompt:**
    "Plan a 3-day trip to Kanyakumari with medium budget"

## 📌 2. System Flow

    User Prompt
    ↓
    Coordinator Agent
    ├── Activity Search Agent → Google Places API
    ├── Hotel Agent → Places + Hotels API
    ├── Restaurant Agent → Places API
    ├── Transport Agent → Directions API
    ├── Budget Agent → Custom Budget Tool
    └── Memory Agent → Session + Memory Bank
    Coordinator Compiles Results
    ↓
    Final Travel Plan (Itinerary + Hotels + Food + Budget)

## 📌 3. Tech Stack

| Component | Technology |
|-----------|------------|
| **Language** | Python 3.8+ |
| **Framework** | Flask |
| **AI Model** | Google Gemini 2.0 (Pro/Flash) |
| **APIs** | Google Maps Platform (Places, Directions, Distance Matrix) |
| **Frontend** | HTML/CSS + Marked.js |

## 📌 4. Project Folder Structure

```
smart-travel-concierge/
│
├── agents/          # AI agents (Coordinator, Activity, Hotel, etc.)
├── tools/           # API wrappers (Google Places, Directions, etc.)
├── memory/          # Session management & Memory Bank
├── core/            # Utilities (Logging, Tracing, Metrics)
├── api/             # Flask routes
├── templates/       # HTML
├── static/          # CSS/JS
├── main.py          # Entry point
└── requirements.txt
```

## 📌 5. Data & Memory

### Sessions & Memory
- **Session Service**: Remembers conversation context.
- **Memory Bank**: Stores user preferences:
  - Preferred cuisines
  - Hotel comfort level
  - Average budget
  - Travel preferences (historic, beaches, adventure)

## 📌 6. Backend Components

### Google APIs Used
- **Google Places API**: Find attractions, hotels, restaurants.
- **Google Maps Directions API**: Navigation, bus routes, travel time.
- **Google Distance Matrix API**: Calculate distance & cost.
- **Google Search API**: Fetch latest travel info.

### Custom Tools
- `places_search_tool.py`
- `directions_tool.py`
- `distance_tool.py`
- `budget_estimator_tool.py`

## 📌 7. AI Agent Capabilities

| Agent | Responsibilities |
|-------|------------------|
| **Coordinator Agent** | Controls workflow, routes tasks, merges outputs |
| **Activity Search Agent** | Uses Google Places API to find popular attractions |
| **Hotel Recommendation Agent** | Searches hotels + booking URLs |
| **Restaurant Finder Agent** | Finds high-rated local restaurants |
| **Transport Agent** | Provides bus routes, taxi estimates, distances |
| **Itinerary Agent** | Converts activities into a polished day-wise plan |
| **Budget Planner Agent** | Computes min and max budget for the trip |
| **Preference Memory Agent** | Stores user food taste, budget range, comfort level |

## 📌 8. Example Output

### 📅 Trip: 3 Days in Goa
**User**: *“I’m traveling to Goa for 3 days on a medium budget.”*

#### 🗓️ Day 1 – Aguada → Sinquerim → Baga
- **Fort Aguada**: Historic fort + lighthouse (8.6 km)
- **Sinquerim Beach**: Clean water, peaceful (2.1 km)
- **Baga Beach**: Water sports, nightlife (6.8 km)

**Transport**: Bus No. 17 (Panjim → Sinquerim) or Taxi (₹150–250).

#### 🛏️ Recommended Hotels
- **Taj Fort Aguada Resort & Spa**: 5-star, beachfront (₹12,000–18,000/night)
- **Bloom Hotel – Calangute**: 3-star (₹3,000–4,000/night)

#### 💰 Budget Estimate
| Category | Min | Max |
|----------|-----|-----|
| Stay | ₹3,000/day | ₹18,000/day |
| Food | ₹800/day | ₹2,500/day |
| Transport | ₹400/day | ₹1,200/day |
| Activities | ₹1,000/day | ₹4,000/day |
| **Total (3 days)** | **₹16,000** | **₹75,000+** |

## 📌 9. Required Python Packages

```bash
pip install flask google-generativeai googlemaps python-dotenv
```

## 📌 10. Summary

This Smart Travel Concierge combines:
- Practical Google API integrations
- Strong multi-agent design
- Modern LLM reasoning using Gemini
- Memory + tools + sessions + observability
- Realistic India-focused recommendations
