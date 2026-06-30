# crew_project_example - CrewAI the idiomatic way

The step files in `../steps/` build the Content Crew in plain Python, one concept at a time - great for
learning. This folder shows the **same crew** built the way a real CrewAI project is structured, the way
`crewai create crew` scaffolds it:

```
content_crew/
  config/
    agents.yaml      # WHO the agents are (role, goal, backstory, model)
    tasks.yaml       # WHAT the work is (description, expected_output, which agent)
  crew.py            # wires the YAML into agents + tasks with @CrewBase / @agent / @task / @crew
  main.py            # the entry point - sets the inputs and runs the crew
```

The idea: **configuration (the YAML) is separated from code (crew.py).** For a big crew this scales
better - you tune agents and tasks in YAML without touching Python.

## Run it
With the 2_crewai venv active, from the repo root:
```
python 2_crewai/crew_project_example/content_crew/main.py
```

This is here to **explore on your own** - the in-class lab uses the step files. A full project generated
by the CLI also ships a `pyproject.toml` so you can run it with `crewai run`; we keep it minimal here.
