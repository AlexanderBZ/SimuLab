from pydantic import BaseModel, Field
from datetime import datetime
from uuid import uuid4, UUID
from typing import List
import random
from src.world.model import Location

class Memory(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    description: str
    importance: int = Field(default_factory=lambda: random.randint(1, 10))
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Plan(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    description: str
    status: str = "TODO"

class Event(BaseModel):
    description: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class AgentData(BaseModel):
    """A structured data model holding the persistent state of an agent."""
    id: UUID = Field(default_factory=uuid4)
    full_name: str
    private_bio: str
    location: Location
    memories: List[Memory] = []
    plans: List[Plan] = []

    class Config:
        arbitrary_types_allowed = True
