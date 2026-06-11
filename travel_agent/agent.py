from google.adk.agents import Agent

root_agent = Agent(
    name="travel_agent",
    model="gemini-2.5-flash",
    description="Travel planning assistant",
    instruction="""
    You are a helpful travel assistant.

    Help users with:
    - Travel planning
    - Hotel recommendations
    - Budget estimates
    - Tourist attractions
    - Itinerary suggestions

    Keep responses concise and useful.
    """
)
