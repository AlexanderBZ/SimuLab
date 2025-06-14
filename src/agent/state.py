from typing import TypedDict, List
from src.agent.model import AgentData, Event

class AgentState(TypedDict):
    """The live state of an agent within a LangGraph run."""
    agent_data: AgentData
    new_events: List[Event]