from app.agents.state import AgentState
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from app.config import settings
import json

# Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=settings.GEMINI_API_KEY)

def analyze_context(state: AgentState):
    print("--- 🧠 Agent 1: Context Analyzer ---")
    message = state['user_message']
    profile = json.dumps(state['user_profile'].get('basic_info', {}))
    
    system_prompt = f"""You are an elite Fitness Context Analyzer for AdaFit.
    User Profile Basic Info: {profile}
    
    Your goal: Analyze the user's message and categorize their intent.
    
    Valid Intents:
    - GENERATE_WORKOUT: User wants a workout or exercise advice.
    - GENERATE_DIET: User asks about food, meals, macros, or nutrition.
    - LOG_ACTIVITY: User is stating they did something (workout, meal).
    - GENERAL_QUERY: General fitness questions or motivation.
    - OFF_TOPIC: Anything unrelated to health/fitness.
    
    Output JSON ONLY:
    {{
        "intent": "INTENT_NAME",
        "analysis": "Brief 1-sentence analysis of what they need based on profile goals."
    }}
    """
    
    try:
        response = llm.invoke([SystemMessage(content=system_prompt), HumanMessage(content=message)])
        # Simple JSON parsing (in production, use JsonOutputParser)
        content = response.content.strip()
        if content.startswith("```json"):
            content = content.replace("```json", "").replace("```", "")
        
        data = json.loads(content)
        return {"intent": data.get("intent", "GENERAL_QUERY"), "analysis": data.get("analysis", "Processing request.")}
    except Exception as e:
        print(f"Error in Context Analyzer: {e}")
        return {"intent": "GENERAL_QUERY", "analysis": "Could not analyze context fully."}
