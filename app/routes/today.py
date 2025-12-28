from fastapi import APIRouter, HTTPException
from app.schemas.today import AgentRequest, AgentResponse
from app.agents.graph import agent_graph

router = APIRouter()

@router.post("/", response_model=AgentResponse)
async def interact_with_agent(request: AgentRequest):
    try:
        # Prepare initial state
        initial_state = {
            "user_message": request.message,
            "user_profile": request.context, # Assuming context matches profile dict roughly
            "intent": "",
            "analysis": "",
            "workout_plan": {},
            "diet_plan": {},
            "final_response": ""
        }
        
        # Run Graph
        result = agent_graph.invoke(initial_state)
        
        return AgentResponse(
            response=result.get("final_response", "Error processing request."),
            data=result.get("workout_plan", {}) 
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
