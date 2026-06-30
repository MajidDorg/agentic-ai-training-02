"""Step 6 (homework) - Memory across runs.

CONCEPT: Turn on memory=True and the crew remembers across runs - it can recall earlier topics and
preferences you stated. (Memory uses a small local database for embeddings - that's why this module
is pinned to Python 3.11 - and it uses your OpenAI key to create those embeddings.)

RUN IT:  python 2_crewai/steps/step_6_memory.py
Try a few related topics in a row, and state a preference - watch it carry over. Type 'quit' to stop.

TRY THIS:
  - First topic: "remote work - and I prefer a casual, funny tone".
  - Next topic: "productivity tips" - notice it keeps the casual, funny tone without being told again.
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

# --- BASELINE: the same writer crew, now with memory turned on ---
writer = Agent(
    role="Content Writer",
    goal="Write a clear, engaging short post about {topic}, honoring the reader's stated preferences.",
    backstory="You are a skilled writer who remembers what the reader likes and adapts to it.",
    llm=MODEL,
)

write_post = Task(
    description="Write a short, engaging post (120-180 words) about {topic}.",
    expected_output="A finished short post, around 120-180 words.",
    agent=writer,
)

crew = Crew(
    agents=[writer],
    tasks=[write_post],
    process=Process.sequential,
    memory=True,
    verbose=True,
)


def main():
    print("Step 6 - a crew with memory. Type a topic (or 'quit').")
    while True:
        topic = input("\ntopic> ").strip()
        if topic.lower() in {"quit", "exit", "q"}:
            break
        result = crew.kickoff(inputs={"topic": topic})
        print(f"\n--- post ---\n{result.raw}")


if __name__ == "__main__":
    main()
