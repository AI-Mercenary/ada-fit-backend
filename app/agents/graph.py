from langgraph.graph import StateGraph, END, START
from app.agents.state import AgentState
from app.agents.context_analyzer import analyze_context
from app.agents.workout_planner import plan_content
from app.agents.habit_tracker import track_habit
from app.agents.motivation_coach import generate_response

# Define Routing Logic
def route_based_on_intent(state: AgentState):
    intent = state.get("intent", "GENERAL_QUERY")
    # If the user needs a plan generated, go to the Planner agent
    if intent in ["GENERATE_WORKOUT", "GENERATE_DIET"]:
        return "planner"
    # Otherwise (Chat, Greeting, Log Activity), skip planning and go to Habit Tracker -> Coach
    return "tracker"

# Define the graph
workflow = StateGraph(AgentState)

# Add Nodes
workflow.add_node("analyzer", analyze_context)
workflow.add_node("planner", plan_content)
workflow.add_node("tracker", track_habit)
workflow.add_node("coach", generate_response)

# Add Edges
# 1. Start at Analyzer
workflow.add_edge(START, "analyzer")

# 2. Conditional Edge from Analyzer -> (Planner OR Tracker)
workflow.add_conditional_edges(
    "analyzer",
    route_based_on_intent,
    {
        "planner": "planner",
        "tracker": "tracker"
    }
)

# 3. Join back: Planner always goes to Tracker
workflow.add_edge("planner", "tracker")

# 4. Tracker always goes to Coach
workflow.add_edge("tracker", "coach")

# 5. Coach ends the flow
workflow.add_edge("coach", END)

# Compile
agent_graph = workflow.compile()
