import os
import sys
import unittest

# This is a hack to get the tests to run in this environment.
sys.path.append('/home/jules/.pyenv/versions/3.12.11/lib/python3.12/site-packages')
os.environ["GOOGLE_API_KEY"] = "your_actual_api_key_here"

from google_adk.agents import Agent
from google_adk.sessions import Session
from multi_tool_agent import agent


class TestAgent(unittest.TestCase):
    def setUp(self):
        self.agent = agent.root_agent
        self.session = Session(agent=self.agent)

    def test_get_weather(self):
        response = self.session.send("What's the weather like in New York?")
        self.assertIn("The weather in New York is sunny", response)
        self.assertTrue(response)

    def test_get_time(self):
        response = self.session.send("What time is it in New York?")
        self.assertIn("The current time in New York is", response)
        self.assertTrue(response)


if __name__ == "__main__":
    unittest.main()
