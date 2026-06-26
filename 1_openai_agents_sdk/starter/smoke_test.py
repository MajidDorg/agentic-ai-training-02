"""Setup check — run this once after setup to confirm your environment and API key work.

    python 1_openai_agents_sdk/starter/smoke_test.py

If it prints a short friendly reply, you're ready for the session.
"""
import asyncio

from dotenv import load_dotenv
from agents import Agent, Runner

load_dotenv()


async def main():
    agent = Agent(
        name="Setup Check",
        instructions="You are a friendly assistant.",
        model="gpt-5.4-mini",
    )
    result = await Runner.run(agent, "Say 'Setup works!' in one short, friendly sentence.")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
