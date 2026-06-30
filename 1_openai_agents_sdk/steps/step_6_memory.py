"""Step 6 (homework) - Memory: remember the conversation.

CONCEPT: a session stores the conversation so the agent remembers earlier turns. Pass the same
session into each run and it keeps the context.

(Step 5's guarded team is still here; we added a session so it remembers across your messages.)

RUN IT:  python 1_openai_agents_sdk/steps/step_6_memory.py
Try:  "I was charged twice for order A1002"   then   "can I get a refund for it?"
      (it should remember the order is A1002)

TRY THIS:
  - Comment out the `session=session` argument in Runner.run and re-run: notice it forgets. Put it back.
"""
import asyncio

from dotenv import load_dotenv
from pydantic import BaseModel
from agents import (
    Agent,
    Runner,
    GuardrailFunctionOutput,
    input_guardrail,
    InputGuardrailTripwireTriggered,
    SQLiteSession,
)

load_dotenv()
MODEL = "gpt-5.4-mini"


class TopicCheck(BaseModel):
    is_support_request: bool
    is_abusive: bool


guard_agent = Agent(
    name="Topic Guard",
    instructions=(
        "Decide if the message is a genuine customer-support request, and whether it is abusive. "
        "Jokes, poems, and unrelated questions are NOT support requests."
    ),
    model=MODEL,
    output_type=TopicCheck,
)


@input_guardrail
async def support_guardrail(ctx, agent, user_input) -> GuardrailFunctionOutput:
    check = (await Runner.run(guard_agent, user_input, context=ctx.context)).final_output
    blocked = check.is_abusive or not check.is_support_request
    return GuardrailFunctionOutput(output_info=check, tripwire_triggered=blocked)


billing_agent = Agent(name="Billing Specialist", handoff_description="Billing, charges, payments.", instructions="You are the billing specialist. Reply to the customer's billing/payment issue: acknowledge it and explain the next step. Write a short, helpful reply - never just repeat the customer's message back.", model=MODEL)
technical_agent = Agent(name="Technical Specialist", handoff_description="Product/technical problems.", instructions="You are the technical-support specialist. Reply with simple step-by-step help. Write a short, helpful reply - never just repeat the customer's message back.", model=MODEL)
refund_agent = Agent(name="Refund Specialist", handoff_description="Refunds and returns.", instructions="You are the refund specialist. Reply to the refund/return request: acknowledge it and explain how it will be handled, by policy. Write a short, helpful reply - never just repeat the customer's message back.", model=MODEL)

triage_agent = Agent(
    name="Support Triage Agent",
    instructions="You are the front desk for customer support. Hand off to the right specialist: billing, technical, or refund.",
    model=MODEL,
    handoffs=[billing_agent, technical_agent, refund_agent],
    input_guardrails=[support_guardrail],
)


async def main():
    session = SQLiteSession("student-demo")
    print("Step 6 - memory. It remembers the conversation. Type a message (or 'quit').")
    while True:
        user = input("\nyou> ").strip()
        if user.lower() in {"quit", "exit", "q"}:
            break
        try:
            result = await Runner.run(triage_agent, user, session=session)
            print(f"  handled by: {result.last_agent.name}")
            print(f"  reply: {result.final_output}")
        except InputGuardrailTripwireTriggered:
            print("  [blocked by guardrail - not a valid support request]")


if __name__ == "__main__":
    asyncio.run(main())
