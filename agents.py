from crewai import Agent
from models import Model
from prompts import Prompts

model = Model()

class Agents:

    def weather_research_agent(self):
        return Agent(
            role = "Senior Weather Researcher",
            goal = Prompts.researcher_agent_goal,
            backstory = Prompts.researcher_agent_backstory,
            verbose = True,
            allow_delegation = False,
            llm = model.google_gemini_pro()
        )
    
    def weather_analysis_agent(self):
        return Agent(
            role = "Senior Weather Analyst",
            goal = Prompts.analyser_agent_goal,
            backstory = Prompts.analyser_agent_backstory,
            verbose = True,
            allow_delegation = False,
            llm = model.google_gemini_pro()
        )