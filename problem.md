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

Source: https://epoch.ai/frontiermath/open-problems/stretched-lr-coefficients
