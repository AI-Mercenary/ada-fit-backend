from pydantic import BaseModel
from typing import Optional, Dict, Any

class AgentRequest(BaseModel):
    user_id: str
    message: str
    context: Dict[str, Any] # Contains profile, history, etc.

class AgentResponse(BaseModel):
    response: str
    actions: Optional[list] = []
    data: Optional[Dict[str, Any]] = {}
