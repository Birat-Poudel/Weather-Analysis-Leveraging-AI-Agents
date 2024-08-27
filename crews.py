from crewai import Crew, Process
from agents import Agents
from tasks import Tasks

agent = Agents()
task = Tasks()

class Crews:

    def research_analysis_crew(self):
        return Crew(
            agents=[agent.weather_research_agent(), agent.weather_analysis_agent()],
            tasks=[task.weather_research_task(), task.weather_analysis_task()],
            verbose=True,
            process=Process.sequential
        )