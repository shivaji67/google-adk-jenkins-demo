from google.adk.agents import Agent

root_agent = Agent(
    name="travel_agent",
    model="gemini-2.5-flash",
    description="Travel planning assistant",
    instruction="""
    Help users plan trips, hotels, budgets,
    tourist attractions and itineraries.
    """
)
