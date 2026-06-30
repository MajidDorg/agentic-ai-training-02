"""Step 1 - Your first crew: one agent, one task.

CONCEPT: In CrewAI you describe an AGENT with three parts - role (who it is), goal (what it's
trying to do), and backstory (the persona it works from). You give it a TASK (a description plus
expected_output = what "done" looks like). A CREW runs the agent on the task. You start it with
kickoff(), passing inputs that fill the {placeholders}.

(Unlike Session 1's SDK, CrewAI's kickoff() is synchronous - no asyncio needed.)

RUN IT:  python 2_crewai/steps/step_1_agent_task_crew.py
Type a topic, see a short post, type another. Type 'quit' to stop.

TRY THIS (change one thing, run again, see the difference):
  - Edit the writer's backstory below (e.g. "You write witty posts for Instagram") and re-run.
  - Tighten expected_output (e.g. "exactly 3 sentences") and watch the output change shape.
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

# --- BASELINE (we will experiment with this together) ---
writer = Agent(
    role="Content Writer",
    goal="Write a clear, engaging short post about {topic}.",
    backstory="You are a skilled writer who explains ideas simply for a general audience.",
    llm=MODEL,
)

write_post = Task(
    description="Write a short, engaging post (about 120-180 words) about {topic}. Use plain language.",
    expected_output="A finished short post about {topic}, around 120-180 words.",
    agent=writer,
)

crew = Crew(agents=[writer], tasks=[write_post], process=Process.sequential)


def main():
    print("Step 1 - your first crew. Type a topic (or 'quit' to exit).")
    while True:
        topic = input("\ntopic> ").strip()
        if topic.lower() in {"quit", "exit", "q"}:
            break
        result = crew.kickoff(inputs={"topic": topic})
        print(f"\n--- post ---\n{result.raw}")


if __name__ == "__main__":
    main()
