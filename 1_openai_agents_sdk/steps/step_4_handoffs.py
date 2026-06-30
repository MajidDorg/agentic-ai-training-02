"""Step 4 (homework) - From one agent to a TEAM: handoffs.

CONCEPT: a handoff lets one agent pass control ACROSS to another agent, which takes over and finishes
the job. Control does not come back. We use it to ROUTE: a triage agent hands off to a billing /
technical / refund specialist.

RUN IT:  python 1_openai_agents_sdk/steps/step_4_handoffs.py
Try:  "I was charged twice"  (-> Billing)    "I want a refund"  (-> Refund)

TRY THIS:
  - Add a new specialist (e.g. a Shipping Specialist) and add it to the triage agent's handoffs list.
"""
import asyncio

from dotenv import load_dotenv
from agents import Agent, Runner

load_dotenv()
MODEL = "gpt-5.4-mini"

# --- BASELINE: three specialist agents (the handoff targets) ---
billing_agent = Agent(
    name="Billing Specialist",
    handoff_description="Handles billing, charges, invoices, and payment questions.",
    instructions="You are the billing specialist for a small online store. Reply to the customer's "
    "billing or payment issue: acknowledge it and explain the next step to resolve it. Write a short, "
    "helpful reply - never just repeat the customer's message back.",
    model=MODEL,
)
technical_agent = Agent(
    name="Technical Specialist",
    handoff_description="Handles product and technical problems and how-to questions.",
    instructions="You are the technical-support specialist. Reply to the customer's product/technical "
    "problem with simple step-by-step help. Write a short, helpful reply - never just repeat the "
    "customer's message back.",
    model=MODEL,
)
refund_agent = Agent(
    name="Refund Specialist",
    handoff_description="Handles refunds and returns.",
    instructions="You are the refund specialist. Reply to the customer's refund or return request: "
    "acknowledge it and explain how it will be handled, by policy. Write a short, helpful reply - "
    "never just repeat the customer's message back.",
    model=MODEL,
)

triage_agent = Agent(
    name="Support Triage Agent",
    instructions=(
        "You are the front desk for customer support. Hand off to the right specialist: "
        "billing, technical, or refund."
    ),
    model=MODEL,
    handoffs=[billing_agent, technical_agent, refund_agent],
)


async def main():
    print("Step 4 - handoffs. Type a customer message (or 'quit'). See which specialist answers.")
    while True:
        user = input("\nyou> ").strip()
        if user.lower() in {"quit", "exit", "q"}:
            break
        result = await Runner.run(triage_agent, user)
        print(f"  handled by: {result.last_agent.name}")
        print(f"  reply: {result.final_output}")


if __name__ == "__main__":
    asyncio.run(main())
