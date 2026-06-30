# Module 2 - CrewAI: build a Content Crew (step by step)

This session you build a **Content Crew** - a small team of AI agents that turns a topic into a
finished short post. Same style as Session 1: **pre-built step files**, one concept each, run-and-tinker.

> New framework, new tool for the job. In Session 1, one agent did the whole task. CrewAI is for when
> the work is better done by a **team** of agents, each with its own role.

## How the steps work
Every file in `steps/` is already written and working. For each one you:
1. **Read it** - with the trainer, or ask Claude Code to explain it.
2. **Run it** - it drops into an interactive loop: type a topic, watch the crew work, type another,
   then type `quit` to stop.
3. **Try the experiment** at the top of the file - change one thing, run again, see what changed.

Then move to the next step, which adds the next concept on top of the last.

## The steps
| Step | File | Concept | When |
|---|---|---|---|
| 1 | `steps/step_1_agent_task_crew.py` | an agent (role/goal/backstory) + a task + a crew + kickoff | in session |
| 2 | `steps/step_2_two_agents.py` | two agents, working in sequence (researcher -> writer) | in session |
| 3 | `steps/step_3_tools.py` | give an agent a tool (+ save the result to a file) | in session |
| 4 | `steps/step_4_structured_output.py` | clean, structured output with a Pydantic model | in session |
| 5 | `steps/step_5_hierarchical.py` | a manager agent that delegates (hierarchical process) | in session |
| 6 | `steps/step_6_memory.py` | the crew remembers across runs (memory) | homework |

Plus:
- `crew_project_example/` - the **same idea** built the **idiomatic CrewAI way** (`crewai create crew`
  with YAML config files). This is how a real CrewAI project is structured - explore it on your own time.

## Homework
1. Run **steps 5 and 6** and do the "Try this" experiments (you saw these concepts in class).
2. **Make it your crew:** change the agents' `role` / `goal` / `backstory` and the task descriptions so
   the crew writes for a topic or audience you care about. Keep the structure - just change the content.
3. (Optional stretch) swap the custom tool in step 3 for a real web-search tool - see the note in that file.

## Setup
CrewAI needs its **own** virtual environment (separate from Session 1), pinned to **Python 3.11**.
See `SETUP.md` in this folder - it takes about 2 minutes. Your Session-1 `.env` (OpenAI key) is reused.

## Run a step
From the repo root, with the CrewAI venv active (see `SETUP.md`):
```
python 2_crewai/steps/step_1_agent_task_crew.py
```
First, check your setup works:
```
python 2_crewai/smoke_test.py
```

**Claude Code is your assistant** - ask it to explain any step, help with the experiments, or fix
errors. (It won't build the whole project for you - you learn by running, understanding, and tinkering.)
