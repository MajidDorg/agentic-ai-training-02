# Agentic AI — Course Repository

Welcome. This is the working repository for the **Agentic AI** course. Over the program you'll build
real agentic-AI applications, one framework at a time, ending with a capstone project.

You won't be coding alone: **Claude Code is your AI pair-builder** throughout. It's set up (via the
`CLAUDE.md` files in this repo) to *help you build while keeping you the architect* — it explains
concepts, builds with you in small steps, and asks you to make the design decisions. The goal by the
end of the course: a workspace where Claude Code is your assistant for building agentic AI, and **you**
know how to design the systems.

## Before the first session — prerequisites

You need two things ready:

1. **Claude Code** working inside VS Code (the extension, signed in with your Claude subscription).
2. **An OpenAI API key** with some credit, from <https://platform.openai.com/api-keys>.

## Setup (do this once)

```bash
# 1. Clone this repo and open it in VS Code, then open a terminal in the project folder.

# 2. Create and activate a virtual environment
python -m venv .venv
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# macOS / Linux:
source .venv/bin/activate

# 3. Install the dependencies
pip install -r requirements.txt

# 4. Add your OpenAI key
#    Copy .env.example to .env and paste your real key into it.
```

> Requirements: **Python 3.10 or newer**. If anything in setup fails, just ask Claude Code — it knows
> this project's setup and the common errors, and will walk you through the fix.

## Check your setup works

With the venv activated and your `.env` in place:

```bash
python 1_openai_agents_sdk/starter/smoke_test.py
```

If it prints a short reply from the model, you're ready.

## How to use Claude Code in this course

- Ask it to **explain** anything you don't understand — concepts come before code.
- Build **with** it: tell it the design you want, and let it help you implement it step by step.
- When you hit an error, paste it in — Claude Code will diagnose it with you.
- For **homework**, lean on it for hints and unblocking, but write the code yourself — that's where the
  learning sticks.

## Sessions

| # | Module | Topic |
|---|---|---|
| 1 | `1_openai_agents_sdk/` | OpenAI Agents SDK — build your first agents |
| 2+ | _added each session_ | the next frameworks, then the capstone |

New modules and updated instructions are pushed to this repo as the course goes on — `git pull` at the
start of each session.
