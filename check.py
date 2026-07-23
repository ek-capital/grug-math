#!/usr/bin/env python3
"""Exact, intentionally boring checker for a stretched LR candidate."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Iterable


Partition = tuple[int, ...]


def partition(value: Iterable[int]) -> Partition:
    parts = tuple(int(x) for x in value if int(x) != 0)
    if any(x < 0 for x in parts):
        raise ValueError("partition parts must be non-negative")
    if any(a < b for a, b in zip(parts, parts[1:])):
        raise ValueError("partition parts must be weakly decreasing")
    return parts


def scale(parts: Partition, factor: int) -> Partition:
    if factor == 0:
        return ()
    return tuple(factor * x for x in parts)


def lr_coefficient(outer: Partition, inner: Partition, content: Partition) -> int:
    """Count LR tableaux in reading order: rows top-down, right-to-left."""
    if sum(outer) != sum(inner) + sum(content):
        return 0

    rows = len(outer)
    padded_inner = inner + (0,) * (rows - len(inner))
    if len(inner) > rows:
        return 0
    if any(padded_inner[r] > outer[r] for r in range(rows)):
        return 0

    cells = tuple(
        (r, c)
        for r in range(rows)
        for c in range(outer[r] - 1, padded_inner[r] - 1, -1)
    )
    max_symbol = len(content)
    start_remaining = tuple(content)

    @lru_cache(maxsize=None)
    def visit(
        index: int,
        remaining: tuple[int, ...],
        assigned_items: tuple[tuple[int, int, int], ...],
    ) -> int:
        if index == len(cells):
            return int(not any(remaining))

        assigned = {(r, c): value for r, c, value in assigned_items}
        r, c = cells[index]
        total = 0

        for value in range(1, max_symbol + 1):
            slot = value - 1
            if remaining[slot] == 0:
                continue

            right = assigned.get((r, c + 1))
            if right is not None and value > right:
                continue

            above = assigned.get((r - 1, c))
            if above is not None and above >= value:
                continue

            new_remaining = list(remaining)
            new_remaining[slot] -= 1
            used = [content[i] - new_remaining[i] for i in range(max_symbol)]
            if any(used[i] < used[i + 1] for i in range(max_symbol - 1)):
                continue

            new_assigned = assigned_items + ((r, c, value),)
            total += visit(index + 1, tuple(new_remaining), new_assigned)

        return total

    return visit(0, start_remaining, ())


def interpolate(values: list[int], start: int = 0) -> list[Fraction]:
    """Return ordinary-basis coefficients from consecutive exact values."""
    differences = [Fraction(value) for value in values]
    newton: list[Fraction] = []
    factorial = 1
    order = 0
    while differences:
        if order > 0:
            factorial *= order
        newton.append(differences[0] / factorial)
        differences = [
            differences[i + 1] - differences[i]
            for i in range(len(differences) - 1)
        ]
        order += 1

    polynomial = [Fraction(0)]
    basis = [Fraction(1)]
    for degree, coefficient in enumerate(newton):
        if len(polynomial) < len(basis):
            polynomial.extend([Fraction(0)] * (len(basis) - len(polynomial)))
        for i, value in enumerate(basis):
            polynomial[i] += coefficient * value

        next_basis = [Fraction(0)] * (len(basis) + 1)
        for i, value in enumerate(basis):
            next_basis[i] -= (start + degree) * value
            next_basis[i + 1] += value
        basis = next_basis

    while len(polynomial) > 1 and polynomial[-1] == 0:
        polynomial.pop()
    return polynomial


def analyse(candidate: dict) -> dict:
    outer = partition(candidate["lambda"])
    inner = partition(candidate["mu"])
    content = partition(candidate["nu"])

    for name, parts in (("lambda", outer), ("mu", inner), ("nu", content)):
        if len(parts) > 7:
            raise ValueError(f"{name} has more than 7 parts")
        if sum(parts) > 30:
            raise ValueError(f"{name} has sum greater than 30")
    if sum(outer) != sum(inner) + sum(content):
        raise ValueError("sum(lambda) must equal sum(mu) + sum(nu)")

    row_count = max(map(len, (outer, inner, content)), default=0)
    degree_bound = max(0, (row_count - 1) * (row_count - 2) // 2)
    sample_points = list(range(1, degree_bound + 2))
    values = [
        lr_coefficient(scale(outer, t), scale(inner, t), scale(content, t))
        for t in sample_points
    ]
    coefficients = interpolate(values, start=1)

    return {
        "degree_bound": degree_bound,
        "sample_points": sample_points,
        "values": values,
        "coefficients": [
            str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"
            for x in coefficients
        ],
        "smallest_coefficient": str(min(coefficients)),
        "counterexample": any(x < 0 for x in coefficients),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate", type=Path)
    args = parser.parse_args()

    try:
        candidate = json.loads(args.candidate.read_text())
        result = analyse(candidate)
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        print(f"INVALID: {error}")
        return 2

    print(json.dumps(result, indent=2))
    if result["counterexample"]:
        print("PASS: counterexample found")
        return 0
    print("FAIL: valid candidate, but no negative coefficient")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
