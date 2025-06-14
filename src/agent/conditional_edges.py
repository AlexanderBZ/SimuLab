from src.agent.state import AgentState
from langgraph.graph import END

def should_plan(state: AgentState) -> str:
    """
    Determines if the agent needs to create a new plan or can proceed to thinking.
    """
    if len(state['agent'].plans) == 0:
        return "plan"
    else:
        return "think"

def should_reflect(state: AgentState) -> str:
    """
    After acting, determines if the agent should reflect or finish the step.
    """
    if state['should_reflect']:
        return "reflect"
    else:
        return "finish_step"
        
def is_final_step(state: AgentState) -> str:
    """
    Checks if the process should end.
    """
    if state.get("is_final_step", False):
        return END
    return "act"