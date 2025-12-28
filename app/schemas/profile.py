from pydantic import BaseModel
from typing import Optional, Dict

class ProfileBase(BaseModel):
    basic_info: Dict
    fitness_profile: Dict
    nutrition_preferences: Dict

class ProfileCreate(ProfileBase):
    pass

class Profile(ProfileBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
