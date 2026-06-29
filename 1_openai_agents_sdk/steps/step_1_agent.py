"""Step 1 - Your first agent.

CONCEPT: an agent is a name + instructions (its system prompt) + a model. You run it with the
Runner, and the reply is in result.final_output.

RUN IT (interactive):  python 1_openai_agents_sdk/steps/step_1_agent.py
Type a message, see the reply, type another. Type 'quit' to stop.

TRY THIS (change one thing, run again, see the difference):
  - Edit SYSTEM_PROMPT below (e.g. tell it to always reply in ONE short sentence) and run again.
"""
import asyncio

from dotenv import load_dotenv
from agents import Agent, Runner

load_dotenv()
MODEL = "gpt-5.4-mini"

# --- BASELINE (we will experiment with this together) ---
SYSTEM_PROMPT = (
    "You are a friendly customer-support assistant for a small online store. Be concise and helpful."
)

agent = Agent(
    name="Support Assistant",
    instructions=SYSTEM_PROMPT,
    model=MODEL,
)


async def main():
    print("Step 1 - your first agent. Type a message (or 'quit' to exit).")
    while True:
        user = input("\nyou> ").strip()
        if user.lower() in {"quit", "exit", "q"}:
            break
        result = await Runner.run(agent, user)
        print(f"agent> {result.final_output}")


if __name__ == "__main__":
    asyncio.run(main())
