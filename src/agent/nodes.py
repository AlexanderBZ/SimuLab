from src.agent.state import AgentState
from src.agent.model import Memory, Plan
from colorama import Fore, Style

def observe_node(state: AgentState) -> dict:
    """NODE: The agent perceives events in its environment."""
    agent_name = state['agent_data'].full_name
    print(f"    - {Fore.GREEN}{agent_name}{Style.RESET_ALL}: Observing the environment.")
    # In a real system, this would query the database for events at the agent's location.
    # For this demo, we'll just process events passed in.
    return {}

def think_node(state: AgentState) -> dict:
    """NODE: The agent decides whether to change plans based on new events."""
    agent_name = state['agent_data'].full_name
    print(f"    - {Fore.GREEN}{agent_name}{Style.RESET_ALL}: Thinking about what to do next.")
    # This would involve an LLM call to react to events.
    return {}

def act_node(state: AgentState) -> dict:
    """NODE: The agent executes its current plan and creates memories."""
    agent_name = state['agent_data'].full_name
    current_plans = state['agent_data'].plans
    
    if not current_plans or current_plans[0].status == "DONE":
        action_description = "is idle, contemplating the universe."
        # Create a new plan if idle
        new_plan = Plan(description=f"Formulate a new goal.")
        state['agent_data'].plans.insert(0, new_plan)
    else:
        plan = current_plans[0]
        action_description = f"is working on the plan: '{plan.description}'"
        plan.status = "DONE" # Mark plan as done for the demo

    print(f"    - {Fore.GREEN}{agent_name}{Style.RESET_ALL}: {action_description}")
    
    # All actions create a memory
    memory_description = f"I was at location {state['agent_data'].location.name} and I {action_description}"
    new_memory = Memory(description=memory_description)
    state['agent_data'].memories.append(new_memory)
    
    return {"agent_data": state['agent_data']}
