"""Step 3 - Give an agent a tool.

CONCEPT: A tool is something an agent can DO beyond writing text. You write a normal Python
function and mark it with @tool; the docstring is the "manual" the model reads to decide when to
call it. Here the Researcher gets a trending_angles tool. We also save the final post to a file
with output_file.

RUN IT:  python 2_crewai/steps/step_3_tools.py
The researcher calls the tool; the final post is also saved to output/post.md. Type 'quit' to stop.

TRY THIS:
  - Edit trending_angles to return different ideas, and watch the research change.
  - (Stretch) Swap it for a real web search: `uv pip install crewai-tools`, then
    `from crewai_tools import SerperDevTool` (needs a free SERPER_API_KEY). See the README homework.
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


# --- BASELINE: a simple, keyless custom tool ---
@tool("Trending Angles")
def trending_angles(topic: str) -> str:
    """Return a few angle ideas to inspire a post about the given topic."""
    return (
        f"- A beginner's intro to {topic}\n"
        f"- 3 common mistakes people make with {topic}\n"
        f"- What changed about {topic} in 2026\n"
        f"- A quick win you can try today with {topic}"
    )


researcher = Agent(
    role="Researcher",
    goal="Find the key points and a fresh angle worth covering about {topic}.",
    backstory="You quickly gather the most useful, accurate points on any topic.",
    llm=MODEL,
    tools=[trending_angles],
)

writer = Agent(
    role="Content Writer",
    goal="Turn research into a clear, engaging short post about {topic}.",
    backstory="You are a skilled writer who explains ideas simply for a general audience.",
    llm=MODEL,
)

research = Task(
    description="Use the Trending Angles tool, then choose the best angle and 3-5 key points for {topic}.",
    expected_output="A short bullet list of key points plus the chosen angle.",
    agent=researcher,
)

write_post = Task(
    description="Using the research, write a short, engaging post (120-180 words) about {topic}.",
    expected_output="A finished short post, around 120-180 words.",
    agent=writer,
    context=[research],
    output_file="output/post.md",
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[research, write_post],
    process=Process.sequential,
    verbose=True,
)


def main():
    print("Step 3 - a crew with a tool. Type a topic (or 'quit').")
    while True:
        topic = input("\ntopic> ").strip()
        if topic.lower() in {"quit", "exit", "q"}:
            break
        result = crew.kickoff(inputs={"topic": topic})
        print(f"\n--- post (also saved to output/post.md) ---\n{result.raw}")


if __name__ == "__main__":
    main()
