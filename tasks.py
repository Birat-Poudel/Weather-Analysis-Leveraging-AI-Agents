from crewai import Task
from agents import Agents
from prompts import Prompts

agent = Agents()

class Tasks:

    def weather_research_task(self):
        return Task(
            description=Prompts.researcher_agent_goal,
            expected_output="""
            A detailled weather report of each of the city. The results should be formatted as shown below:

            Weather in City 1:
            - Current Temperature
            - Humidity
            - Wind Speed
            - Weather Patterns 
            """,
            agent=agent.weather_research_agent(),
        )

    def weather_analysis_task(self):
        return Task(
            description=Prompts.analyser_agent_goal,
            expected_output="""
            A detailled weather report of each of the city. The results should be formatted as shown below:

            - Weather in City 1
            - Weather in City 2
            - Weather in City 3
            - Brief Analysis
            """,
            output_file="output.txt",
            agent=agent.weather_analysis_agent(),
        )