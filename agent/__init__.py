from google_adk.agents import Agent
from google_adk.sessions import Session
from . import tools

def create_agent() -> Agent:
    """Creates a new agent."""
    return Agent(
        instructions="""
You are a helpful assistant.

You can help users plan day trips. You can also provide the current weather and time for a given location.

When a user asks for a day trip, you should provide a detailed itinerary, including suggestions for activities, restaurants, and transportation.

When a user asks for the weather or time, you should use the appropriate tool to get the information and then provide it to the user.
""",
        tools=[
            tools.get_live_weather_forecast,
            tools.get_current_time,
        ],
    )
