# Module 1 — OpenAI Agents SDK (current session)

The student's project this module is a **Customer Support Triage Agent** — see `README.md` in this
folder for the full brief and architecture. Help them build it per the working style in the root
`CLAUDE.md`: explain first, build in small reviewable steps, keep them the architect.

## Concepts in scope — Part 1 (build together in the session), in this order
1. **Agent + Runner** — name, instructions, model; run it and read `result.final_output`.
2. **Function tool** — `@function_tool` `lookup_order(order_id)` over a small mock dict. The docstring
   is the model's instruction manual for the tool — write it clearly.
3. **Structured output** — a Pydantic `SupportTicket` model passed as `output_type`; read the typed
   fields off `result.final_output`.

Build these **one at a time**. After each piece, run it so the student sees it work before adding the
next. When there's a design choice (which ticket fields, what the tool returns), ask the student.

## Part 2 — homework (coach, don't solve)
**handoffs** (triage → Billing / Technical / Refund specialists), **guardrails** (block abusive /
off-topic input), **sessions/memory** (multi-turn support chat). Give hints and ask leading questions;
let the student write the code.

## Reminders for this module
- `model="gpt-5.4-mini"` on every agent.
- Scripts, not notebooks: put async code in `async def main()` and call `asyncio.run(main())`. No
  top-level `await`.
- Load the key from `.env` with `load_dotenv()` before creating an agent.
- The student works in `starter/main.py`. Don't paste a finished solution — build it with them.
