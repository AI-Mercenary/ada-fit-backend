from app.agents.state import AgentState
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from app.config import settings
import json

llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=settings.GEMINI_API_KEY)

def generate_response(state: AgentState):
    print("--- 🗣️ Agent 4: Motivation Coach ---")
    
    profile = state['user_profile']
    intent = state['intent']
    plan = state['workout_plan'] or state['diet_plan']
    habit = state['habit_data']
    
    system_prompt = f"""You are 'Ada', the advanced AI Coach.
    User Profile: {json.dumps(profile)}
    
    Context:
    - User Intent: {intent}
    - Proposed Plan: {json.dumps(plan) if plan else "No specific plan generated (general chat)"}
    - Habit Context: {json.dumps(habit)}
    
    Goal: Synthesize a friendly, motivating response.
    1. Acknowledge the user's request.
    2. If a plan exists, present it enthusiastically.
    3. Use the Habit Data to motivate (e.g., "Keep that 3-day streak alive!").
    4. Be concise but warm.
    """
    
    try:
        response = llm.invoke([SystemMessage(content=system_prompt), HumanMessage(content=state['user_message'])])
        return {"final_response": response.content}
    except Exception as e:
        print(f"Error in Coach: {e}")
        return {"final_response": "I'm having trouble connecting to my motivation core, but I believe in you! Let's just focus on moving today."}
