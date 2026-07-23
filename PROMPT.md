# Task

Solve the task in `problem.md`.

Read `problem.md`, `verifier.py`, `search.py`, and `notes.md` first.

## Rules

- Never edit `problem.md`, `check.py`, or `verifier.py`.
- Put the current best candidate in `best.json`.
- A candidate counts only when `python3 check.py best.json` exits zero.
- Verify any passing candidate with a second independent implementation.
- Use exact arithmetic for final verification.
- Record useful facts, failures, and blocked routes in `notes.md`.

## Work loop

1. Start several genuinely different approaches.
2. Make each attempt produce code, a candidate, a lemma, or an exact failure.
3. Attack every promising result and every checker assumption.
4. Diagnose failures before changing direction.
5. Mark a route blocked if it only reduces to an equally hard unproved claim.
6. Continue while a materially different route remains.

Do not turn “the model thinks this is right” into a result.
