"""Step 3 - Get structured output.

CONCEPT: by default an agent replies in free text. To get clean DATA, define the shape you want with
a Pydantic model and pass it as output_type. The agent then fills those fields - which you can feed
straight into a system.

(Step 2's agent + tool are still here; we added the SupportTicket output.)

RUN IT:  python 1_openai_agents_sdk/steps/step_3_structured_output.py
Type a customer message; you'll get a structured ticket back.

TRY THIS:
  - Add a field to SupportTicket (e.g. language: str = Field(description="the customer's language")) and re-run.
"""
import asyncio

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from agents import Agent, Runner, function_tool

load_dotenv()
MODEL = "gpt-5.4-mini"

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


# --- BASELINE: the structured shape we want back ---
class SupportTicket(BaseModel):
    category: str = Field(description="One of: order_status, billing, technical, refund, other.")
    urgency: str = Field(description="low, medium, or high.")
    sentiment: str = Field(description="positive, neutral, or negative.")
    summary: str = Field(description="One short sentence describing what the customer needs.")
    needs_human: bool = Field(description="True if a human agent should follow up.")


SYSTEM_PROMPT = (
    "You are the front desk for a small online store's customer support. Read the customer's message. "
    "If they mention an order ID, use the lookup_order tool. Then produce a structured support ticket."
)

agent = Agent(
    name="Support Triage Agent",
    instructions=SYSTEM_PROMPT,
    model=MODEL,
    tools=[lookup_order],
    output_type=SupportTicket,
)


async def main():
    print("Step 3 - structured output. Type a customer message (or 'quit').")
    while True:
        user = input("\nyou> ").strip()
        if user.lower() in {"quit", "exit", "q"}:
            break
        ticket = (await Runner.run(agent, user)).final_output
        print(f"  category : {ticket.category}")
        print(f"  urgency  : {ticket.urgency}")
        print(f"  sentiment: {ticket.sentiment}")
        print(f"  summary  : {ticket.summary}")
        print(f"  human?   : {ticket.needs_human}")


if __name__ == "__main__":
    asyncio.run(main())
