from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_profile():
    return {"message": "Profile endpoints coming soon"}
