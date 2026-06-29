# Session 1 - OpenAI Agents SDK: Customer Support Agent (step by step)

You'll build a customer-support agent for a small online store - **one concept at a time**. Each step
is a small, ready-to-run file in `steps/`. You run it, play with it, then move to the next.

## How the steps work
Every file in `steps/` is already written and working. For each one you:
1. **Read it** - with the trainer, or ask Claude Code to explain it.
2. **Run it** - it drops into an interactive loop: type a message, see the reply, type another, and
   type `quit` to stop.
3. **Try the experiment** at the top of the file - change one thing, run again, see what changed.

Then move to the next step, which adds the next concept on top of the last.

## The steps
| Step | File | Concept | When |
|---|---|---|---|
| 1 | `steps/step_1_agent.py` | an agent + system prompt + runner | in session |
| 2 | `steps/step_2_tool.py` | a tool the agent can call | in session |
| 3 | `steps/step_3_structured_output.py` | clean structured output (Pydantic) | in session |
| 4 | `steps/step_4_handoffs.py` | handoffs to specialist agents | homework |
| 5 | `steps/step_5_guardrails.py` | guardrails (block bad input) | homework |
| 6 | `steps/step_6_memory.py` | memory across turns | homework |

## Run a step
From the project root, with your virtual environment active (see `SETUP.md`):
```
python 1_openai_agents_sdk/steps/step_1_agent.py
```
First, check your setup works:
```
python 1_openai_agents_sdk/smoke_test.py
```

**Claude Code is your assistant** - ask it to explain any step, help with the "Try this" experiments,
or fix errors. (It won't build the whole project for you - that's not how you learn it. It helps you
run, understand, and tinker.)
