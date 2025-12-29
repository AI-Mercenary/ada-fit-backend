# AdaFit Backend 🧠💪

The intelligent core of the AdaFit application, powered by **FastAPI**, **LangGraph**, and **Google Gemini 2.0**.

## 🚀 Features

- **Multi-Agent Orchestration**: Uses LangGraph to manage state between specialized agents '(Analyzer, Planner, Habit Tracker, Coach).
🧠 1. Context Analyzer (
context_analyzer.py
)
Role: The entry point and decision maker.
What it does: It reads your message and your profile to understand your Intent.
Categories: It classifies your request into one of these:
GENERATE_WORKOUT: You want exercise advice.
GENERATE_DIET: You want food/nutrition advice.
LOG_ACTIVITY: You are tracking what you did.
GENERAL_QUERY or OFF_TOPIC: Just chatting.
📝 2. Strategic Planner (
workout_planner.py
)
Role: The architect.
When it runs: Only runs if the Analyzer decides you need a Plan (Workout or Diet).
What it does: Generates structured JSON data for:
Hard Workouts: Exercises, sets, warmups.
Diet Plans: Calories, macros (protein/carbs/fats), and specific foods.
📅 3. Habit Tracker (
habit_tracker.py
)
Role: The accountability partner.
What it does: currently acts as a mock service for the MVP.
Output: It injects data about your "Streaks" (e.g., "Current streak: 3 days") to help the Coach define its tone (proud or encouraging).
🗣️ 4. Motivation Coach (
motivation_coach.py
)
Role: The voice of "Ada" (the user-facing persona).
What it does: It takes all the raw data from the previous agents (intents, JSON plans, streak stats) and synthesizes the Final Response.
Personality: Warm, friendly, and motivational. It ensures you don't just get a robot JSON response, but a helpful message like "Hey! Ready to crush some goals? Here is your workout..."
- **Smart Routing**: automatically distinguishes between simple chat ("Hi") and complex tasks ("Make me a workout") to optimize latency.
- **Gemini 2.0 Integration**: Leveraging the latest `gemini-2.0-flash-exp` for rapid responses.
- **Resilient Architecture**: Handles rate limits gracefully with user-friendly fallback messages.
- **Deploy Ready**: Configured for cloud platforms (Render/Leapcell) with health checks and environment variable port binding.

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **AI/LLM**: LangChain + LangGraph + Google Gemini
- **Database**: SQLite (via SQLAlchemy)
- **Validation**: Pydantic
- **Async Runtime**: Uvicorn + Asyncio

## ⚡ Quick Start

### 1. Prerequisites
- Python 3.10+
- A Google Gemini API Key

### 2. Installation

```bash
# Clone the repo (if you haven't)
git clone https://github.com/AI-Mercenary/ada-fit-backend.git
cd ada-fit-backend

# Create virtual env
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration (.env)

Create a `.env` file in the root directory.
**IMPORTANT**: You MUST replace `your_api_key_here` with a valid Google Gemini API Key from [Google AI Studio](https://aistudio.google.com/).

```ini
GEMINI_API_KEY=your_api_key_here
AGENT_MODEL=gemini-2.0-flash-exp
DEBUG=True
DATABASE_URL=sqlite:///./adfit.db
# Permissive CORS for dev
BACKEND_CORS_ORIGINS=["*"]
```

### 4. Run Server

```bash
# Using the helper script (Windows)
python main.py

# OR directly with Uvicorn
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`.

## 🧠 Agent Workflow

The system uses a **Conditional Graph**:

1.  **User Message** -> enters **Context Analyzer**.
2.  **Router**: checks intent.
    *   *Chat/Greeting* -> **Fast Track** -> Skips to Motivation Coach.
    *   *Request Plan* -> **Deep Track** -> Workout Planner -> Habit Tracker -> Motivation Coach.
3.  **Motivation Coach**: Synthesizes the final response with a friendly persona.

## ⚠️ Troubleshooting

- **"Thinking too fast!" Error**: This means the Gemini 2.0 free tier rate limit was hit. Wait 10-20 seconds.
- **CORS Errors**: The `app/main.py` is configured to allow all origins (`*`) for easy development across network devices.

## ☁️ Deployment

This backend is ready for deployment.
- It respects the `PORT` environment variable.
- It includes a `/health` and `/kaithhealthcheck` endpoint for load balancers.
- Dependencies are pinned in `requirements.txt` for stability.
