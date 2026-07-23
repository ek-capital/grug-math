# grug-math

Tiny harness for attacking a concrete open math problem with coding agents.

Complexity bad. Candidate either pass checker or candidate not pass checker.

## Files

```text
problem.md   exact problem; do not let agents rewrite it
PROMPT.md    paste-ready research instructions for a coding agent
search.py    agents change this to search better
check.py     exact checker; agents do not change this
best.json    best candidate found so far
notes.md     useful facts and dead ends
test.py      small tests for checker
```

The first target is the stretched Littlewood-Richardson positivity conjecture.
The checker is pure Python and uses exact integer and rational arithmetic.

## Use

```bash
python3 test.py
python3 check.py best.json
python3 search.py --trials 100
```

`search.py` replaces `best.json` when it finds a candidate with a smaller
polynomial coefficient. A negative coefficient is a counterexample.

To start a long agent run, give the agent `PROMPT.md`. The prompt requires
independent approaches, explicit blocked-route tracking, and adversarial review.

The default search is deliberately small and dumb. Improve `search.py`, not the
harness.

When choosing a future problem, prefer one that:

- mathematicians already care about;
- has an exact statement and checkable finish line;
- is not merely a disguised Millennium-scale conjecture;
- permits useful computation, counterexample search, or finite certificates.

For long research runs, use the strongest reasoning model available, give it
`PROMPT.md`, and expect hours rather than minutes.

## Rules

1. Do not change `problem.md` to make search easier.
2. Search code may use guesses and floating point.
3. Checker uses exact arithmetic.
4. Another model saying "looks correct" is not verification.
5. Before announcing a result, write a second independent checker and ask a
   mathematician who works in the area.

## Research loop

```text
attempt -> failure -> diagnosis -> new approach -> candidate -> attack -> repair
```

Keep several genuinely different approaches alive. When an approach reduces
the problem to another unproved claim of similar difficulty, mark it blocked
in `notes.md`. Reopen it only when there is a new mechanism.

This workflow was adapted from
[Shouqiao Wang's thread](https://x.com/Qiaoqiao2001/status/2080003441821163958)
and [published Erdős problem prompts](https://github.com/ShouqiaoW/erdos).

## Why Littlewood-Richardson coefficients?

The answer is a small object: three integer partitions. It can be checked
exactly, and a counterexample would be a meaningful result in algebraic
combinatorics.

## License

MIT
