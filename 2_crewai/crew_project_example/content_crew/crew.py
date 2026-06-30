"""The Content Crew, built the idiomatic CrewAI way (YAML config + @CrewBase).

This is the SAME crew as the step files, but structured the way `crewai create crew` lays out a real
project: agents and tasks live in config/*.yaml, and this class wires them together with decorators.
Compare it to ../steps/step_2_two_agents.py - same idea, more scalable shape.
"""
from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew


@CrewBase
class ContentCrew:
    """A two-agent crew: researcher -> writer."""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def researcher(self) -> Agent:
        return Agent(config=self.agents_config["researcher"])

    @agent
    def writer(self) -> Agent:
        return Agent(config=self.agents_config["writer"])

    @task
    def research(self) -> Task:
        return Task(config=self.tasks_config["research"])

    @task
    def write_post(self) -> Task:
        return Task(config=self.tasks_config["write_post"])

    @crew
    def crew(self) -> Crew:
        return Crew(agents=self.agents, tasks=self.tasks, process=Process.sequential, verbose=True)
