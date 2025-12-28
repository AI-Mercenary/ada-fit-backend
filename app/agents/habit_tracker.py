from app.agents.state import AgentState

def track_habit(state: AgentState):
    print("--- 📅 Agent 3: Habit Tracker ---")
    
    # In a real app, query DB for user's history here.
    # For MVP, we mock a streak context to show the agent's capability.
    
    mock_streak = {
        "current_streak": 3,
        "last_workout": "yesterday",
        "compliance_rate": "85%"
    }
    
    habit_msg = f"User is on a {mock_streak['current_streak']} day streak! They are consistent."
    
    return {"habit_data": mock_streak, "reasoning_trail": f"Analyzed History: {habit_msg}"}
