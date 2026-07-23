# Current task

Work in this repository until you find a genuine counterexample to the
stretched Littlewood-Richardson positivity conjecture stated in `problem.md`.

Read `problem.md`, `check.py`, `search.py`, and `notes.md` before acting.

## Hard boundary

- Do not edit `problem.md` or `check.py`.
- You may freely replace `search.py` and add small experiment scripts.
- A proposed triple is not a result unless `python3 check.py <candidate>`
  prints `PASS`.
- Even a passing candidate remains provisional until it survives a second
  independent implementation that does not import `check.py`.
- Preserve exact arithmetic throughout final verification.

## What complete means

Return only a fixed valid triple of partitions together with its exact
stretched LR polynomial, a negative ordinary-basis coefficient, the checker
output, and an independent verification.

The weaker outcomes listed under “Things that do not count” in `problem.md`
are not solutions.

## Search management

Start with several genuinely independent approaches. At minimum explore:

1. systematic enumeration with mathematical pruning;
2. randomized or evolutionary search over partition triples;
3. hive-polytope or Ehrhart-polynomial structure;
4. perturbations of known families and near-boundary examples;
5. an adversarial audit of the checker, degree bound, interpolation, and LR
   conventions.

Do not make every approach imitate the first promising one. Keep incompatible
routes alive long enough to expose their different strengths and failures.

Maintain the approach registry and research log in `notes.md`.

If a route reduces the task to an unproved lemma of comparable strength, mark
it `blocked` and write the exact lemma. Reopen it only when there is a
materially new construction, invariant, bound, algorithm, or certificate.

Require concrete output from every attempt: code, exact coefficients,
candidate triples, pruning lemmas, counterexamples to proposed lemmas, or a
precise obstruction. Vague progress reports do not count.

## Adversarial loop

For every promising idea:

```text
attempt
failure
diagnose the exact failure
try a materially different repair
produce candidate
attack every assumption and convention
repair or discard
```

Try actively to falsify intermediate lemmas. In particular, test:

- swapped LR argument conventions;
- insufficient polynomial samples;
- accidental use of `t = 0`;
- wrong row or column tableau inequalities;
- invalid lattice-word checks;
- zero polynomials being ranked as promising;
- integer overflow or floating-point interpolation;
- candidates outside the stated size bounds;
- duplicate candidates hidden by partition symmetries;
- a supposed new result already present in the literature.

Use computation to discover patterns and destroy bad ideas. Computation alone
is not a proof unless it produces the finite exact certificate requested by
`problem.md`.

Continue the research loop while there are materially different unexplored
approaches. Do not turn a missing theorem-strength lemma into optimistic prose.
