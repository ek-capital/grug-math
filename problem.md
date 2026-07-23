# Problem: stretched Littlewood-Richardson coefficients

For integer partitions `lambda`, `mu`, and `nu` with

```text
sum(lambda) = sum(mu) + sum(nu),
```

let

```text
c(t) = LR(t * lambda, t * mu, t * nu),
```

where `LR(lambda, mu, nu)` is the Littlewood-Richardson coefficient
`c^lambda_(mu,nu)` and `t * lambda` means multiply every part by `t`.

The function `c(t)` is a polynomial in `t`.

Find partitions such that:

- every partition has at most 7 parts;
- every partition has sum at most 30; and
- at least one coefficient of the polynomial `c(t)` is negative.

Return:

```json
{
  "lambda": [0],
  "mu": [0],
  "nu": [0]
}
```

with zero parts omitted in an actual candidate.

## Complete success

A complete result must provide one fixed triple and establish all of these:

1. `lambda`, `mu`, and `nu` are valid integer partitions.
2. `sum(lambda) = sum(mu) + sum(nu)`.
3. Each partition has at most 7 parts and sum at most 30.
4. The exact stretched LR polynomial is computed, not guessed.
5. At least one ordinary-basis coefficient of that polynomial is negative.
6. `python3 check.py candidate.json` prints `PASS`.
7. A second implementation, not importing `check.py`, gives the same result.

## Things that do not count

- A negative floating-point approximation.
- A polynomial fitted from too few values without a valid degree bound.
- A negative finite difference rather than a negative ordinary-basis
  coefficient.
- A negative coefficient caused by including the special `t = 0` convention.
- A triple that uses the wrong ordering convention for LR arguments.
- An invalid or out-of-bounds partition.
- A zero LR polynomial.
- A candidate accepted only after weakening this statement or editing the
  checker.
- Another AI saying the calculation looks correct.

## Traps to attack

- LR notation differs between sources. This repository uses
  `c^lambda_(mu,nu)`.
- Stretched values are sampled at positive integers. Do not infer the
  polynomial from the empty partitions at `t = 0`.
- Interpolation and coefficient comparisons must use exact rational
  arithmetic.
- Verify the degree bound for the number of rows being used.
- Check tableau row order, column strictness, content, and the lattice-word
  condition independently.
- Search for the candidate in existing literature before claiming novelty.

Source: https://epoch.ai/frontiermath/open-problems/stretched-lr-coefficients
