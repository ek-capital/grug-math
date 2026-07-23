# grug-math

Tiny harness for math-solving agents.

Agent proposes thing. Checker checks thing. No vibes.

## Setup

1. Put the exact task and finish line in `problem.md`.
2. Implement the exact test in `verifier.py`.
3. Give `PROMPT.md` to an agent.

```bash
python3 test.py
python3 check.py best.json
python3 search.py
```

Agents may change `search.py`, `best.json`, and `notes.md`.
Agents must not change `problem.md`, `check.py`, or `verifier.py`.

A result is not real until the checker passes, a second independent checker
agrees, and a human expert reviews it.

Workflow inspired by
[Shouqiao Wang's research thread](https://x.com/Qiaoqiao2001/status/2080003441821163958).

MIT licensed.
