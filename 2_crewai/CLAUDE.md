# Module 2 - CrewAI (current session)

The student works through **pre-built step files** in `steps/` (one concept each), running each in an
interactive loop and doing a small guided "Try this" experiment. Follow the working style in the root
`CLAUDE.md`: explain first, help them run + understand + modify, keep them the architect.
**Do NOT rebuild the files from scratch or jump ahead to later steps.**

We build one project across the steps: a **Content Crew** - a team of agents that turns a topic into a
finished short post.

## The steps (and the concept each teaches)
1. `steps/step_1_agent_task_crew.py` - the three building blocks: an **Agent** (role + goal + backstory),
   a **Task** (description + expected_output), and a **Crew** that runs it; start with `kickoff(inputs=...)`.
2. `steps/step_2_two_agents.py` - a **team**: researcher -> writer with `process=sequential`; a later
   task reads an earlier one via `context=[...]`.
3. `steps/step_3_tools.py` - a **tool** the agent can call (`@tool` from `crewai.tools`; the docstring is
   the manual) + saving the result with `output_file`.
4. `steps/step_4_structured_output.py` - **structured output**: a Pydantic model as `output_pydantic`;
   read it from `result.pydantic`.
5. `steps/step_5_hierarchical.py` - a **manager** that delegates (`process=hierarchical`, `manager_llm`);
   the manager runs a stronger model.
6. `steps/step_6_memory.py` (homework) - **memory** across runs (`memory=True`).

Also: `crew_project_example/` - the same idea built the **idiomatic CrewAI way** (`crewai create crew`
with YAML config files). Use it to explain how a real CrewAI project is laid out. Don't rebuild it.

## How to help (this session's posture)
- **Explain** the concept in plain language before touching any code.
- Help the student **run** the step and read its output; help with the **"Try this"** experiment.
- Help **debug** errors with them.
- **Do NOT** rewrite a whole file, build later steps early, or "build the whole project." If asked,
  decline gently and walk them through the current step.

## CrewAI specifics + guardrails (read carefully)
- **This module has its OWN virtual environment on Python 3.11** (`2_crewai/.venv`), separate from
  Module 1's root `.venv`. Make sure the student runs these steps with **the 2_crewai venv** (in VS Code,
  select that interpreter, or activate it - see `SETUP.md`). Module 1's venv does NOT have CrewAI.
- **Never install CrewAI into the repo root or the root venv.** If something is missing, install it into
  `2_crewai/.venv` only (`uv pip install ...` with that venv active).
- **Never run `crewai create crew` inside this repo** - it would scaffold a new project on top of ours.
  The idiomatic scaffold already exists in `crew_project_example/`.
- **API quick reference (CrewAI 1.x):**
  - `from crewai import Agent, Task, Crew, Process, LLM` and `from crewai.tools import tool`.
  - Agent = `role`, `goal`, `backstory`, `llm="openai/gpt-5.4-mini"` (+ optional `tools=[...]`).
  - Task = `description`, `expected_output`, `agent` (+ `context=[...]`, `output_file=...`, `output_pydantic=...`).
  - `Crew(agents=[...], tasks=[...], process=Process.sequential)`; hierarchical also takes `manager_llm=...`.
  - `result = crew.kickoff(inputs={...})` is **synchronous** (NO asyncio - unlike Module 1's SDK).
    Read `result.raw` (text) or `result.pydantic` (structured object).
- **Model:** agents use `openai/gpt-5.4-mini`; the hierarchical manager uses `openai/gpt-5.4`.
- **Key:** loaded from the repo-root `.env` via `load_dotenv(find_dotenv())` - reused from Session 1.
- Memory (step 6) uses a local embeddings database (chromadb) - that's why this module is pinned to 3.11.
