from src.world.model import Location
from src.agent.model import AgentData, Plan
from src.agent.state import AgentState
from src.world.state import WorldState
from src.world.graph import world_app
import asyncio
from colorama import Fore, Style

async def main():
    """Initializes and runs the world simulation."""
    print("🚀 Initializing Simulation...")

    # 1. Create Locations
    cafe_location = Location(name="The Rusty Mug Cafe", description="A cozy, rustic cafe.")
    library_location = Location(name="Oakshade Library", description="A quiet, old library.")
    locations = [cafe_location, library_location]

    # 2. Create Agent Data
    agent1_data = AgentData(
        full_name="Alex",
        private_bio="A curious writer seeking inspiration.",
        location=cafe_location,
        plans=[Plan(description="Finish the first chapter of my novel.")]
    )
    agent2_data = AgentData(
        full_name="Ben",
        private_bio="A historian researching local town records.",
        location=library_location,
        plans=[Plan(description="Find records of the town's founding.")]
    )
    
    # 3. Assemble Initial World State
    initial_world_state = WorldState(
        agents=[
            AgentState(agent_data=agent1_data, new_events=[]),
            AgentState(agent_data=agent2_data, new_events=[])
        ],
        locations=locations,
        turn_number=0,
        simulation_over=False
    )

    # 4. Run the simulation graph
    final_state = await world_app.ainvoke(initial_world_state)

    # 5. Print final results
    print("\n--- ✅ Simulation Complete ---\n")
    for agent_state in final_state['agents']:
        agent = agent_state['agent_data']
        print(f"{Style.BRIGHT}Final State for {Fore.CYAN}{agent.full_name}{Style.RESET_ALL}:")
        print(f"  - Final Location: {agent.location.name}")
        print(f"  - Total Memories Created: {len(agent.memories)}")
        print(f"  - Last Memory: '{agent.memories[-1].description}'")

if __name__ == "__main__":
    asyncio.run(main())