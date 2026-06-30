# Setup - CrewAI (Session 2)

CrewAI is a bigger framework than Session 1's SDK, so it gets its **own virtual environment**, pinned to
**Python 3.11** (a couple of CrewAI's parts don't yet ship ready-made installers for the newest Python on
Windows). This keeps it separate from your Session-1 setup, which still works exactly as before.

You do this once. ~2 minutes.

## Easiest way (recommended) - using uv
`uv` creates the environment AND fetches Python 3.11 for you automatically - no separate Python install.

1. Install uv once (if you don't have it):
   - Windows (PowerShell): `pip install uv`
   - Mac: `pip3 install uv`   (or `brew install uv`)
2. From the repo root, create the CrewAI environment:
   ```
   uv venv 2_crewai/.venv --python 3.11
   ```
3. Activate it:
   - Windows: `2_crewai\.venv\Scripts\Activate.ps1`
   - Mac: `source 2_crewai/.venv/bin/activate`

   You'll see `(.venv)` at the start of the line. (Windows: if activation is blocked, skip it and use
   `2_crewai\.venv\Scripts\python.exe` instead of `python` in the commands below.)
4. Install CrewAI:
   ```
   uv pip install -r 2_crewai/requirements.txt
   ```

## Manual way (if you prefer) - Python 3.11 directly
1. Install **Python 3.11** from python.org (Windows: tick **"Add Python to PATH"**).
2. From the repo root, create the environment:
   - Windows: `py -3.11 -m venv 2_crewai\.venv`
   - Mac: `python3.11 -m venv 2_crewai/.venv`
3. Activate it (same as step 3 above), then install:
   ```
   pip install -r 2_crewai/requirements.txt
   ```

## Your API key
Your Session-1 `.env` (with `OPENAI_API_KEY`) is **reused** - no new key needed. (If you don't have it
anymore, copy `.env.example` from the repo root to a file named `.env` and paste your OpenAI key in.)

## Check it works
With the CrewAI venv active, from the repo root:
```
python 2_crewai/smoke_test.py
```
You should see a tiny crew run and print **`Setup works!`**.

## Run the first step
```
python 2_crewai/steps/step_1_agent_task_crew.py
```
Type a topic, watch the crew work, type another - type `quit` to stop.

## If something breaks
Ask **Claude Code** in the chat - that's what it's for. The usual culprits: the venv isn't activated,
the wrong Python version (this module needs **3.11**), or the key isn't in your `.env`.
