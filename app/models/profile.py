from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.database.engine import Base

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # Store JSON blobs for flexibility in this MVP phase
    basic_info = Column(JSON)
    fitness_profile = Column(JSON)
    nutrition_preferences = Column(JSON)
    
    user = relationship("User", backref="profile")
