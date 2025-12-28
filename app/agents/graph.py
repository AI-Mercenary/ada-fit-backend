from langgraph.graph import StateGraph, END
from app.agents.state import AgentState
from app.agents.context_analyzer import analyze_context
from app.agents.workout_planner import plan_content
from app.agents.habit_tracker import track_habit
from app.agents.motivation_coach import generate_response

# Define the graph
workflow = StateGraph(AgentState)

# Add Nodes
workflow.add_node("analyzer", analyze_context)
workflow.add_node("planner", plan_content)
workflow.add_node("tracker", track_habit)
workflow.add_node("coach", generate_response)

# Add Edges (Sequential Flow)
workflow.set_entry_point("analyzer")
workflow.add_edge("analyzer", "planner")
workflow.add_edge("planner", "tracker")
workflow.add_edge("tracker", "coach")
workflow.add_edge("coach", END)

# Compile
agent_graph = workflow.compile()
