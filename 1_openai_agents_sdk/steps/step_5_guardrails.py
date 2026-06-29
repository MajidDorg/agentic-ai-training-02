"""Step 5 (homework) - Guardrails: block bad input.

CONCEPT: a guardrail is an automatic check that runs BEFORE the agent works. If its tripwire
triggers, the run is blocked - the agent never sees the bad input. Here we block off-topic / abusive
messages. (The guardrail is itself a tiny agent.)

(Step 4's team is still here; we added an input guardrail on the triage agent.)

RUN IT:  python 1_openai_agents_sdk/steps/step_5_guardrails.py
Try:  "I was charged twice" (allowed)    "write me a poem about cats" (blocked)

TRY THIS:
  - Edit the guard's instructions so it ALSO blocks messages that aren't in English, then re-run.
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
)

load_dotenv()
MODEL = "gpt-5.4-mini"


# --- BASELINE: the guardrail (a tiny agent that judges the input) ---
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


# --- the team from step 4 ---
billing_agent = Agent(name="Billing Specialist", handoff_description="Billing, charges, payments.", instructions="Handle billing clearly and reassuringly.", model=MODEL)
technical_agent = Agent(name="Technical Specialist", handoff_description="Product/technical problems.", instructions="Give simple step-by-step help.", model=MODEL)
refund_agent = Agent(name="Refund Specialist", handoff_description="Refunds and returns.", instructions="Handle refunds politely and by policy.", model=MODEL)

triage_agent = Agent(
    name="Support Triage Agent",
    instructions="You are the front desk for customer support. Hand off to the right specialist: billing, technical, or refund.",
    model=MODEL,
    handoffs=[billing_agent, technical_agent, refund_agent],
    input_guardrails=[support_guardrail],
)


async def main():
    print("Step 5 - guardrails. Type a message (or 'quit'). Off-topic messages get blocked.")
    while True:
        user = input("\nyou> ").strip()
        if user.lower() in {"quit", "exit", "q"}:
            break
        try:
            result = await Runner.run(triage_agent, user)
            print(f"  handled by: {result.last_agent.name}")
            print(f"  reply: {result.final_output}")
        except InputGuardrailTripwireTriggered:
            print("  [blocked by guardrail - not a valid support request]")


if __name__ == "__main__":
    asyncio.run(main())
