"""Step 4 - Get structured output.

CONCEPT: By default a crew returns text. To get clean DATA, define the shape you want with a
Pydantic model and pass it as output_pydantic on the final task. The result then has .pydantic -
real fields you can use in code (just like Session 1's structured ticket).

RUN IT:  python 2_crewai/steps/step_4_structured_output.py
You'll get back a BlogPost object with title, body, and tags. Type 'quit' to stop.

TRY THIS:
  - Add a field to BlogPost (e.g. hook: str = Field(description="a one-line hook")) and re-run.
"""
import sys

# Windows consoles default to cp1252; use UTF-8 so emoji in library logs print cleanly.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

from dotenv import load_dotenv, find_dotenv
from pydantic import BaseModel, Field
from crewai import Agent, Task, Crew, Process
from crewai.tools import tool

load_dotenv(find_dotenv())
MODEL = "openai/gpt-5.4-mini"


@tool("Trending Angles")
def trending_angles(topic: str) -> str:
    """Return a few angle ideas to inspire a post about the given topic."""
    return (
        f"- A beginner's intro to {topic}\n"
        f"- 3 common mistakes people make with {topic}\n"
        f"- What changed about {topic} in 2026\n"
        f"- A quick win you can try today with {topic}"
    )


# --- BASELINE: the shape we want back ---
class BlogPost(BaseModel):
    title: str = Field(description="A catchy title for the post.")
    body: str = Field(description="The post text, around 120-180 words.")
    tags: list[str] = Field(description="3-5 short topic tags, without the '#'.")


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
    description="Using the research, write a short post (120-180 words) about {topic} and fill the BlogPost fields.",
    expected_output="A BlogPost with a title, the body, and 3-5 tags.",
    agent=writer,
    context=[research],
    output_pydantic=BlogPost,
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[research, write_post],
    process=Process.sequential,
    verbose=True,
)


def main():
    print("Step 4 - structured output. Type a topic (or 'quit').")
    while True:
        topic = input("\ntopic> ").strip()
        if topic.lower() in {"quit", "exit", "q"}:
            break
        post = crew.kickoff(inputs={"topic": topic}).pydantic
        print(f"\n  title: {post.title}")
        print(f"  tags : {', '.join(post.tags)}")
        print(f"  body :\n{post.body}")


if __name__ == "__main__":
    main()
