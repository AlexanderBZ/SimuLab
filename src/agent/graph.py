from src.agent.state import AgentState
from langgraph.graph import StateGraph, END
from src.agent.nodes import observe_node, think_node, act_node

# Add nodes to the graph
agent_builder = StateGraph(AgentState)

agent_builder.add_node("observe", observe_node)
agent_builder.add_node("think", think_node)
agent_builder.add_node("act", act_node)

agent_builder.set_entry_point("observe")
agent_builder.add_edge("observe", "think")
agent_builder.add_edge("think", "act")
agent_builder.add_edge("act", END)

# Compile the reusable "brain"
agent_app = agent_builder.compile()