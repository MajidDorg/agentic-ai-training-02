# Module 1 - OpenAI Agents SDK (current session)

The student works through **pre-built step files** in `steps/` (one concept each), running each in an
interactive loop and doing a small guided "Try this" experiment. See `README.md` for the step map.
Follow the working style in the root `CLAUDE.md`: explain first, help them run + understand + modify,
keep them the architect. **Do NOT rebuild the files from scratch or jump ahead to later steps.**

## The steps (and the concept each teaches)
1. `steps/step_1_agent.py` - an agent = name + instructions (system prompt) + model; run with the Runner; reply in `result.final_output`.
2. `steps/step_2_tool.py` - a function tool (`@function_tool`); the docstring is the model's manual; the agent decides when to call it.
3. `steps/step_3_structured_output.py` - a Pydantic model as `output_type` turns free text into clean data.
4. `steps/step_4_handoffs.py` (homework) - a handoff passes control ACROSS to a specialist agent (it does not come back).
5. `steps/step_5_guardrails.py` (homework) - an input guardrail blocks bad input before the agent works (a tripwire).
6. `steps/step_6_memory.py` (homework) - a session remembers the conversation across turns.

## How to help (this session's posture)
- **Explain** the concept in plain language before touching any code.
- Help the student **run** the step and read its output; help them with the **"Try this"** experiment.
- Help **debug** errors with them.
- **Do NOT** rewrite a whole file, build later steps early, or "just build the whole project." If asked,
  decline gently and walk them through the current step instead. The files are theirs to run and tinker
  with - the learning is in understanding them, not in generating them.

## Reminders
- `model="gpt-5.4-mini"`; scripts not notebooks (`asyncio.run(main())`, no top-level `await`).
- Key from `.env` via `load_dotenv()`.
- Pydantic for structured output: `from pydantic import BaseModel, Field` (ships with the SDK).
