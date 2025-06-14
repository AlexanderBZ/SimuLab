from langgraph.graph import StateGraph, END
from src.world.state import WorldState
from src.world.nodes import add_time_node, run_agents_sequentially_node, check_end_node

world_builder = StateGraph(WorldState)

world_builder.add_node("add_time", add_time_node)
world_builder.add_node("run_agents", run_agents_sequentially_node)
world_builder.add_node("check_end", check_end_node)

world_builder.set_entry_point("add_time")
world_builder.add_edge("add_time", "run_agents")
world_builder.add_edge("run_agents", "check_end")
world_builder.add_conditional_edges(
    "check_end",
    lambda state: "end" if state.get("simulation_over") else "continue",
    {"continue": "add_time", "end": END}
)

# Compile the final application
world_app = world_builder.compile()