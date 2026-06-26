"""Session 1 - Customer Support Triage Agent (Part 1).

You'll build this WITH Claude Code, step by step. Read the project brief in
1_openai_agents_sdk/README.md first, then work through the TODOs below with your AI pair-builder.

Remember: you are the architect. Decide what each piece should do; let Claude Code help you write it,
and make sure you can explain why each part is there.

Run it with:  python 1_openai_agents_sdk/starter/main.py
"""
import asyncio

from dotenv import load_dotenv

load_dotenv()

MODEL = "gpt-5.4-mini"


# TODO 1 - A tool.
#   Write a function lookup_order(order_id) the agent can call to check an order.
#   Mark it with @function_tool and give it a clear docstring. Back it with a small fake dict of orders.

# TODO 2 - The structured output.
#   Define a Pydantic model `SupportTicket` describing the fields you want back
#   (e.g. category, urgency, sentiment, summary, needs_human).

# TODO 3 - The agent.
#   Create the triage Agent with instructions, model=MODEL, your tool, and output_type=SupportTicket.

# TODO 4 - Run it.
#   In main(), send a few sample customer messages through Runner.run and print the ticket fields.


async def main():
    # TODO: run your triage agent here once it's built
    ...


if __name__ == "__main__":
    asyncio.run(main())
