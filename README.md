# grug-math

Tiny harness for attacking a concrete open math problem with coding agents.

Complexity bad. Candidate either pass checker or candidate not pass checker.

## Files

```text
problem.md   exact problem; do not let agents rewrite it
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

The default search is deliberately small and dumb. Improve `search.py`, not the
harness.

## Rules

1. Do not change `problem.md` to make search easier.
2. Search code may use guesses and floating point.
3. Checker uses exact arithmetic.
4. Another model saying "looks correct" is not verification.
5. Before announcing a result, write a second independent checker and ask a
   mathematician who works in the area.

## Why Littlewood-Richardson coefficients?

The answer is a small object: three integer partitions. It can be checked
exactly, and a counterexample would be a meaningful result in algebraic
combinatorics.

## License

MIT
