# Agent instructions

Read `problem.md`, then work on it as a long-running research goal.

## Hard boundary

- Do not edit, weaken, or reinterpret `problem.md`.
- A result counts only if it meets every stated success condition.
- Special cases, finite checks, equivalent-strength reductions, plausible missing
  lemmas, and “best effort” arguments do not count unless `problem.md` says so.
- Create whatever code, proofs, experiments, tests, and notes the work needs.

## Manage the search

- Begin with a genuinely diverse portfolio of approaches.
- Use available subagents dynamically. Preserve their independence early; do not
  tell most of them the currently favored route.
- Maintain `research.md` with an explicit registry of approach families, concrete
  outputs, failures, and exact gaps.
- Keep several incompatible routes alive through multiple rounds. Cross-pollinate
  only after each has exposed its real strengths and weaknesses.
- Redirect effort when too many attempts collapse into the same approach family.
- Mark a route `blocked` when it ends at an unproved statement of comparable
  strength. Reopen it only for a materially new mechanism, invariant, or
  construction.
- Require concrete lemmas, constructions, equations, programs, certificates, or
  counterexamples to proposed sublemmas. Reject vague progress reports.

## Attack the work

- Assign adversarial checks throughout, not only at the end.
- Try to falsify every important lemma and candidate.
- Check every definition, convention, boundary case, quantifier, hidden
  assumption, reduction, and computational result named in `problem.md`.
- For a computational certificate, build an independent verifier.
- For a proof, seek independent reconstruction and formalize in Lean when
  practical. Audit `#print axioms`; `sorryAx` or undeclared custom assumptions
  mean the proof is incomplete.

## Research loop

```text
attempt -> failure -> exact diagnosis -> different repair
        -> candidate -> adversarial audit -> repair or discard
```

Repeatedly synthesize, challenge, redirect, and launch new rounds. Do not stop
because the first waves fail. Unless the user sets a different budget, spend at
least eight hours before considering giving up.

Return success only when the exact requested result survives adversarial audit.
If forced to stop, report only rigorously established results and the exact
remaining gap; never convert a gap into optimistic prose.

Use public search for ordinary background and standard theorems, not as a
substitute for doing the research. Before claiming novelty, search the literature
and obtain review from a relevant mathematician.
