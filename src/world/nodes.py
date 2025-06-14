from src.world.state import WorldState
from colorama import Fore, Style
from src.agent.graph import agent_app
from src.agent.model import Event

def add_time_node(state: WorldState) -> dict:
    """NODE: Advances the world clock by one turn."""
    turn = state.get('turn_number', 0) + 1
    print(f"\n{Style.BRIGHT}{Fore.YELLOW}--- 🌍 World Turn {turn} ---{Style.RESET_ALL}")
    return {"turn_number": turn}

async def run_agents_sequentially_node(state: WorldState) -> dict:
    """NODE: Runs the 'agent_app' for all agents one-by-one."""
    updated_agent_states = []
    
    # We create a new list of events that agents in this turn will generate
    events_this_turn = []

    for agent_state in state['agents']:
        agent_name = agent_state['agent_data'].full_name
        print(f"  - Orchestrator: Running turn for {Fore.CYAN}{agent_name}{Style.RESET_ALL}")
        
        # Pass events from previous agents in this turn to the current agent
        agent_state['new_events'] = events_this_turn

        # Invoke the individual agent's "brain"
        updated_state = await agent_app.ainvoke(agent_state)
        
        # For demo, let's create an event from the agent's action
        last_memory = updated_state['agent_data'].memories[-1].description
        new_event = Event(description=f"{agent_name}'s action: {last_memory}")
        events_this_turn.append(new_event)
        
        # Add the updated state to our list for the next turn
        updated_agent_states.append(updated_state)

    return {"agents": updated_agent_states}

def check_end_node(state: WorldState) -> dict:
    """NODE: Checks if the simulation's end condition has been met."""
    if state.get('turn_number', 0) >= 4: # Stop after 4 turns for demo
        print(f"\n{Style.BRIGHT}{Fore.RED}--- 🏁 Simulation End Condition Met ---{Style.RESET_ALL}")
        return {"simulation_over": True}
    return {"simulation_over": False}
