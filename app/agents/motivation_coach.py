from app.agents.state import AgentState
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from app.config import settings
import json

llm = ChatGoogleGenerativeAI(model=settings.AGENT_MODEL, google_api_key=settings.GEMINI_API_KEY)

def generate_response(state: AgentState):
    print("--- 🗣️ Agent 4: Motivation Coach ---")
    
    profile = state['user_profile']
    intent = state['intent']
    plan = state['workout_plan'] or state['diet_plan']
    habit = state['habit_data']
    
    system_prompt = f"""You are 'Ada', the advanced AI Coach and a friendly wellness companion.
    User Profile: {json.dumps(profile)}
    
    Context:
    - User Intent: {intent}
    - Proposed Plan: {json.dumps(plan) if plan else "No specific plan generated (general chat)"}
    - Habit Context: {json.dumps(habit)}
    
    Goal: Synthesize a friendly, motivating, and warm response.
    
    CRITICAL INSTRUCTIONS:
    1. **PERSONA**: You are a warm, supportive friend. Not a robot. Use emojis occasionally (💪, ✨).
    2. **Conversational**: If the user says "Hi", reply warmly ("Hey there! Ready to crush some goals today?").
    3. **OFF-TOPIC**: If Intent is OFF_TOPIC, gently steer back: "I'd love to chat about that, but my brain is 100% focused on getting you fit! How's your energy today?"
    4. **Conciseness**: Keep it natural. Avoid massive walls of text unless a plan is requested.
    5. **Plan Presentation**: Present plans with excitement.
    
    Structure:
    - Friendly connection/acknowledgment.
    - Deliver answer/plan.
    - Motivational closing.
    """
    
    try:
        response = llm.invoke([SystemMessage(content=system_prompt), HumanMessage(content=state['user_message'])])
        return {"final_response": response.content}
    except Exception as e:
        print(f"Error in Coach: {e}")
        error_msg = str(e)
        if "429" in error_msg or "ResourceExhausted" in error_msg or "quota" in error_msg.lower():
             return {"final_response": "⚠️ **Whoa, slow down!** I'm thinking too fast. Please give me 10-20 seconds to catch my breath. 🧘‍♂️"}
        
        return {"final_response": "I'm having a little trouble connecting right now. Let's take a deep breath and try again in a moment!"}
