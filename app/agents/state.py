from typing import TypedDict, Annotated, List, Dict, Any, Optional
import operator

class AgentState(TypedDict):
    # --- Input ---
    user_message: str
    user_profile: Dict[str, Any]
    
    # --- Agent 1: Context Analysis ---
    intent: str
    analysis: str # Deep understanding of the user's current need
    
    # --- Agent 2: Planner ---
    workout_plan: Optional[Dict[str, Any]]
    diet_plan: Optional[Dict[str, Any]]
    
    # --- Agent 3: Habit Tracker ---
    habit_data: Optional[Dict[str, Any]] # e.g., "Missed yesterday's run", "3 day streak"
    streak_info: Dict[str, Any]
    
    # --- Final Output (Agent 4: Coach) ---
    final_response: str
    reasoning_trail: str # For frontend debug/transparency
    recommendations: List[str]
