from typing import TypedDict, List
from src.agent.state import AgentState
from src.world.model import Location

class WorldState(TypedDict):
    """The state of the entire world, orchestrating all agents."""
    agents: List[AgentState]
    locations: List[Location]
    turn_number: int
    simulation_over: bool
