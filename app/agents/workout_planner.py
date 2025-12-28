from app.agents.state import AgentState
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from app.config import settings
import json

llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=settings.GEMINI_API_KEY)

def plan_content(state: AgentState):
    print("--- 📝 Agent 2: Planner ---")
    intent = state['intent']
    profile = state['user_profile']
    
    workout_plan = {}
    diet_plan = {}
    
    # Only plan if needed
    if intent not in ["GENERATE_WORKOUT", "GENERATE_DIET"]:
        return {"workout_plan": None, "diet_plan": None}

    system_prompt = f"""You are the AdaFit Strategic Planner.
    User Profile: {json.dumps(profile)}
    Context Analysis: {state['analysis']}
    
    Task: Generate a specific plan based on the user's intent: {intent}.
    
    If GENERATE_WORKOUT:
    Return JSON with: {{ "title": "Workout Name", "duration": "mins", "warmup": "description", "exercises": ["ex1", "ex2"], "cooldown": "description" }}
    
    If GENERATE_DIET:
    Return JSON with: {{ "title": "Meal/Plan Name", "calories": 500, "macros": {{ "p": 30, "c": 40, "f": 10 }}, "foods": ["item1", "item2"] }}
    
    Output JSON ONLY.
    """
    
    try:
        response = llm.invoke([SystemMessage(content=system_prompt), HumanMessage(content="Generate the plan.")])
        content = response.content.strip()
        if content.startswith("```json"):
            content = content.replace("```json", "").replace("```", "")
        
        data = json.loads(content)
        
        if intent == "GENERATE_WORKOUT":
            workout_plan = data
        elif intent == "GENERATE_DIET":
            diet_plan = data
            
    except Exception as e:
        print(f"Error in Planner: {e}")
    
    return {"workout_plan": workout_plan, "diet_plan": diet_plan}
