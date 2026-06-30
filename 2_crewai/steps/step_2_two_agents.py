"""Step 2 - A team of two: researcher -> writer.

CONCEPT: A crew is a TEAM. Here a Researcher gathers points first, then the Writer turns them into
a post. With process=sequential the tasks run in order, and a later task can read an earlier task's
result (we pass it explicitly with context=[...]). This is the heart of a crew: split the work
across agents that each have their own role.

RUN IT:  python 2_crewai/steps/step_2_two_agents.py
Type a topic; you'll see the research, then the final post. Type 'quit' to stop.

TRY THIS:
  - Change the researcher's task to "find one contrarian angle" and see how the post shifts.
  - Remove context=[research] from the writer's task and notice it stops building on the research.
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

# --- BASELINE: two agents, each with its own role ---
researcher = Agent(
    role="Researcher",
    goal="Find the key points and a fresh angle worth covering about {topic}.",
    backstory="You quickly gather the most useful, accurate points on any topic.",
    llm=MODEL,
)

writer = Agent(
    role="Content Writer",
    goal="Turn research into a clear, engaging short post about {topic}.",
    backstory="You are a skilled writer who explains ideas simply for a general audience.",
    llm=MODEL,
)

research = Task(
    description="Identify 3-5 key points and one fresh angle for a post about {topic}.",
    expected_output="A short bullet list of key points plus one angle.",
    agent=researcher,
)

write_post = Task(
    description="Using the research, write a short, engaging post (120-180 words) about {topic}.",
    expected_output="A finished short post, around 120-180 words.",
    agent=writer,
    context=[research],
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[research, write_post],
    process=Process.sequential,
    verbose=True,
)


def main():
    print("Step 2 - a two-agent crew. Type a topic (or 'quit').")
    while True:
        topic = input("\ntopic> ").strip()
        if topic.lower() in {"quit", "exit", "q"}:
            break
        result = crew.kickoff(inputs={"topic": topic})
        print(f"\n--- research ---\n{result.tasks_output[0].raw}")
        print(f"\n--- post ---\n{result.raw}")


if __name__ == "__main__":
    main()
