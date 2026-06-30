"""Step 5 - A manager that delegates (hierarchical).

CONCEPT: So far the tasks ran in a fixed order (sequential). With process=hierarchical you add a
MANAGER (its own LLM) that decides who does what, and when. You give the crew the workers and the
tasks; the manager coordinates them. We give the manager a stronger model, because coordinating is
harder than writing.

RUN IT:  python 2_crewai/steps/step_5_hierarchical.py
Watch the manager delegate to the researcher, writer, and editor. Type 'quit' to stop.

TRY THIS:
  - Change process to Process.sequential and compare how the run feels.
  - Set manager_llm to "openai/gpt-5.4-mini" and see if coordination gets weaker.
"""
import sys

# Windows consoles default to cp1252; use UTF-8 so emoji in library logs print cleanly.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

from dotenv import load_dotenv, find_dotenv
from crewai import Agent, Task, Crew, Process
from crewai.tools import tool

load_dotenv(find_dotenv())
MODEL = "openai/gpt-5.4-mini"
MANAGER_MODEL = "openai/gpt-5.4"  # a stronger brain for the manager


@tool("Trending Angles")
def trending_angles(topic: str) -> str:
    """Return a few angle ideas to inspire a post about the given topic."""
    return (
        f"- A beginner's intro to {topic}\n"
        f"- 3 common mistakes people make with {topic}\n"
        f"- What changed about {topic} in 2026\n"
        f"- A quick win you can try today with {topic}"
    )


# --- BASELINE: three workers + a manager that delegates ---
researcher = Agent(
    role="Researcher",
    goal="Find the key points and a fresh angle worth covering about {topic}.",
    backstory="You quickly gather the most useful, accurate points on any topic.",
    llm=MODEL,
    tools=[trending_angles],
)

writer = Agent(
    role="Content Writer",
    goal="Write a clear, engaging short post about {topic}.",
    backstory="You are a skilled writer who explains ideas simply for a general audience.",
    llm=MODEL,
)

editor = Agent(
    role="Editor",
    goal="Polish the post: improve clarity, flow, and length.",
    backstory="You are a sharp editor who tightens copy without changing its meaning.",
    llm=MODEL,
)

# In hierarchical mode we describe the work; the manager assigns it (no agent= on the tasks).
research = Task(
    description="Research {topic}: gather key points and one fresh angle.",
    expected_output="A short bullet list of key points plus one angle.",
)
write_post = Task(
    description="Write a short, engaging post (120-180 words) about {topic}, using the research.",
    expected_output="A draft post, around 120-180 words.",
)
edit_post = Task(
    description="Edit the draft for clarity, flow, and length. Return the final post.",
    expected_output="The final, polished post.",
)

crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[research, write_post, edit_post],
    process=Process.hierarchical,
    manager_llm=MANAGER_MODEL,
    verbose=True,
)


def main():
    print("Step 5 - a manager-led crew. Type a topic (or 'quit').")
    while True:
        topic = input("\ntopic> ").strip()
        if topic.lower() in {"quit", "exit", "q"}:
            break
        result = crew.kickoff(inputs={"topic": topic})
        print(f"\n--- final post ---\n{result.raw}")


if __name__ == "__main__":
    main()
