import asyncio
from app.routes.today import interact_with_agent
from app.schemas.today import AgentRequest
import sys
import os

# Ensure we can import app
sys.path.append(os.getcwd())

async def test():
    print("--- Testing Agent Logic Directly ---")
    req = AgentRequest(user_id="test", message="Give me a workout", context={})
    try:
        res = await interact_with_agent(req)
        print(f"Success: {res}")
    except Exception as e:
        print(f"FAILURE: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test())
