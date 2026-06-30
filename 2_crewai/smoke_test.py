"""Smoke test - confirm your CrewAI setup works.

Run it:  python 2_crewai/smoke_test.py
It builds a tiny one-agent crew, runs it once, and prints "Setup works!" if your
environment and OpenAI key are good.
"""
import sys

# Windows consoles default to cp1252; use UTF-8 so emoji in library logs print cleanly.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

from dotenv import load_dotenv, find_dotenv
from crewai import Agent, Task, Crew, Process

load_dotenv(find_dotenv())
MODEL = "openai/gpt-5.4-mini"


def main():
    greeter = Agent(
        role="Greeter",
        goal="Say a short, friendly hello.",
        backstory="You are a cheerful assistant.",
        llm=MODEL,
    )
    say_hello = Task(
        description="Say hello in exactly one short sentence.",
        expected_output="One short, friendly sentence.",
        agent=greeter,
    )
    crew = Crew(agents=[greeter], tasks=[say_hello], process=Process.sequential)
    result = crew.kickoff()
    print("\nagent said:", result.raw)
    print("\nSetup works!")


if __name__ == "__main__":
    main()
