# Notes

## Facts

- A candidate is three partitions: `lambda`, `mu`, and `nu`.
- The LR coefficient is counted using Littlewood-Richardson tableaux.
- With at most `n` rows, the stretched polynomial has degree at most
  `(n - 1)(n - 2) / 2`, the number of internal vertices of the corresponding
  hive polytope.
- Values at consecutive integers from zero through that degree determine the
  polynomial exactly.

## Dead ends

- None yet.

## Approach registry

| Approach | Status | Best fact or exact obstruction |
|---|---|---|
| Random bounded partition search | active | Baseline in `search.py` |
| Systematic enumeration with pruning | unexplored | |
| Hive-polytope/Ehrhart search | unexplored | |
| Search around known positive families | unexplored | |
| Constraint or SAT encoding | unexplored | |
| Attack the checker and degree bound | active | Regression tests exist |

Allowed statuses: `unexplored`, `active`, `promising`, `blocked`, `dead`.

A route is `blocked` when its next step is an unproved lemma of comparable
strength. Record the exact missing lemma. Do not call it “routine.”

## Research log

For each serious attempt, append:

```text
### YYYY-MM-DD — short approach name

Attempt:
Exact output:
Failure or candidate:
Diagnosis:
Next materially different move:
```

## If something passes

1. Do not celebrate yet.
2. Recompute with SageMath `lrcalc`.
3. Write a second checker that does not import `check.py`.
4. Search the literature for the same triple.
5. Send the certificate to a specialist.
