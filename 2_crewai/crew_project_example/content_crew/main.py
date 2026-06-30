"""Entry point for the idiomatic Content Crew. Run from the repo root:
    python 2_crewai/crew_project_example/content_crew/main.py
"""
import sys
import os

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Make `from crew import ContentCrew` work when run as a plain script.
sys.path.insert(0, os.path.dirname(__file__))
from crew import ContentCrew


def main():
    topic = input("topic> ").strip() or "AI for small business"
    result = ContentCrew().crew().kickoff(inputs={"topic": topic})
    print(f"\n--- post ---\n{result.raw}")


if __name__ == "__main__":
    main()
