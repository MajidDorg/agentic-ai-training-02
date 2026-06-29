# Setup - get ready for Session 1

Follow the steps for your computer. By the end you'll have the project running and your first agent
replying to you. If anything goes wrong, ask Claude Code - or the trainer.

## What you need
- **VS Code** with the **Claude Code** extension, signed in
- An **OpenAI API key** (with a little credit): https://platform.openai.com/api-keys
- **Python 3.10 or newer**

---

## Windows

1. Install **Python 3.10+** from python.org - during install, tick **"Add Python to PATH"**.
2. Open **VS Code** -> open a terminal: **Terminal > New Terminal**.
3. Clone the project and open the folder:
   ```
   git clone https://github.com/MajidDorg/agentic-ai-training-02.git
   ```
   Then **File > Open Folder** and choose the `agentic-ai-training-02` folder.
4. Create and activate a virtual environment:
   ```
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```
   You'll see `(.venv)` at the start of the line. (If activation is blocked, skip it and use
   `.venv\Scripts\python.exe` instead of `python` in the commands below.)
5. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
6. Add your key: copy `.env.example` to a new file named **`.env`**, and paste your OpenAI key into it.
7. Check it works:
   ```
   python 1_openai_agents_sdk\smoke_test.py
   ```
   It should print **`Setup works!`**
8. Run your first agent:
   ```
   python 1_openai_agents_sdk\steps\step_1_agent.py
   ```
   Type a message, see the reply, type another - type `quit` to stop.

---

## Mac

1. Install **Python 3.10+** (python.org, or `brew install python`).
2. Open **VS Code** -> open a terminal.
3. Clone the project and open the folder:
   ```
   git clone https://github.com/MajidDorg/agentic-ai-training-02.git
   ```
   Then **File > Open Folder** and choose the `agentic-ai-training-02` folder.
4. Create and activate a virtual environment:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
   You'll see `(.venv)` at the start of the line.
5. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
6. Add your key: copy `.env.example` to a new file named **`.env`**, and paste your OpenAI key into it.
7. Check it works:
   ```
   python 1_openai_agents_sdk/smoke_test.py
   ```
   It should print **`Setup works!`**
8. Run your first agent:
   ```
   python 1_openai_agents_sdk/steps/step_1_agent.py
   ```
   Type a message, see the reply, type another - type `quit` to stop.

---

## If the repo was updated
If you cloned an earlier version, get the latest fresh: clone it again into a new folder (or run
`git pull`), then re-do steps 4-7 (recreate the venv, install, and your `.env`).
