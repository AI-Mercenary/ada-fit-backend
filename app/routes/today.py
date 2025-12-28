from fastapi import APIRouter, HTTPException
from app.schemas.today import AgentRequest, AgentResponse
from app.agents.graph import agent_graph
import logging
import traceback
import asyncio

logger = logging.getLogger(__name__)

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
        logger.info(f"Invoking agent with message: {request.message}")
        result = await asyncio.to_thread(agent_graph.invoke, initial_state)
        
        return AgentResponse(
            response=result.get("final_response", "Error processing request."),
            data=result.get("workout_plan", {}) 
        )
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))
