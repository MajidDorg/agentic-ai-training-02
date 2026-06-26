# Session 1 — OpenAI Agents SDK: Customer Support Triage Agent

## The problem
A small online store gets a flood of customer messages — "where's my order?", "I was charged twice",
"this doesn't work", "I want a refund." Someone has to read each one, work out what it's about, how
urgent it is, and route it to the right place. That's the job we're handing to an agent.

## What you'll build
A **support triage agent** that reads a customer message, looks up an order when one is mentioned, and
produces a clean, structured **support ticket** a system could act on automatically.

### Architecture — Part 1 (in the session)

```
   customer message
         |
         v
  +----------------------+    calls when an
  |   Triage Agent       |--- order is ------>  lookup_order(order_id)   <- a tool
  |  (OpenAI Agents SDK)  |<-- mentioned ------  returns order status
  +----------+-----------+
             | produces
             v
        SupportTicket   <- structured output (Pydantic)
        { category, urgency, sentiment, summary, needs_human }
```

Three building blocks, in order:
1. **Agent + Runner** — the agent that reads the message.
2. **A tool** — `lookup_order` so the agent can check an order's status.
3. **Structured output** — a `SupportTicket` so you get clean data instead of free text.

You'll build it with Claude Code during the session, in `starter/main.py`.

### Part 2 — homework
Grow the single agent into a small support *team*:
- **Handoffs** — route to a Billing, Technical, or Refund specialist agent.
- **Guardrails** — block abusive or off-topic messages before the agent works.
- **Memory** — remember the conversation across turns (sessions).

Lean on Claude Code for hints — but write this one yourself.
