"""Step 2 - Give the agent a tool.

CONCEPT: a tool is a normal Python function the agent can choose to call. Mark it with
@function_tool; its name + docstring + type hints tell the model how to use it. You never call it
yourself - the agent decides when to.

(Step 1's agent is still here; we only added the tool.)

RUN IT:  python 1_openai_agents_sdk/steps/step_2_tool.py
Try asking, e.g.:  where is my order A1001?

TRY THIS:
  - Add a new order to ORDERS below, then ask the agent about it.
"""
import asyncio

from dotenv import load_dotenv
from agents import Agent, Runner, function_tool

load_dotenv()
MODEL = "gpt-5.4-mini"

# --- BASELINE: a small fake "order database" the tool reads ---
ORDERS = {
    "A1001": {"item": "wireless headphones", "status": "shipped", "eta": "2 days"},
    "A1002": {"item": "laptop stand", "status": "processing", "eta": "5 days"},
}


@function_tool
def lookup_order(order_id: str) -> str:
    """Look up the status of a customer's order by its ID.

    Args:
        order_id: The order ID, for example "A1001".
    """
    order = ORDERS.get(order_id)
    if order is None:
        return f"No order found with ID {order_id}."
    return f"Order {order_id}: {order['item']} - {order['status']} (ETA {order['eta']})."


SYSTEM_PROMPT = (
    "You are a friendly customer-support assistant for a small online store. "
    "If the customer mentions an order ID, use the lookup_order tool to check it. Be concise."
)

agent = Agent(
    name="Support Assistant",
    instructions=SYSTEM_PROMPT,
    model=MODEL,
    tools=[lookup_order],
)


async def main():
    print("Step 2 - agent with a tool. Ask about an order (e.g. 'where is order A1001?'). 'quit' to exit.")
    while True:
        user = input("\nyou> ").strip()
        if user.lower() in {"quit", "exit", "q"}:
            break
        result = await Runner.run(agent, user)
        print(f"agent> {result.final_output}")


if __name__ == "__main__":
    asyncio.run(main())
