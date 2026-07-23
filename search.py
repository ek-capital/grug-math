#!/usr/bin/env python3
"""Dumb random baseline. Replace this when a better idea appears."""

from __future__ import annotations

import argparse
import json
import random
from fractions import Fraction
from pathlib import Path

from check import analyse


def partitions(total: int, maximum: int | None = None):
    if total == 0:
        yield ()
        return
    maximum = total if maximum is None else min(maximum, total)
    for first in range(maximum, 0, -1):
        for rest in partitions(total - first, first):
            yield (first,) + rest


def parse_fraction(value: str) -> Fraction:
    return Fraction(value)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--trials", type=int, default=20)
    parser.add_argument("--max-sum", type=int, default=8)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--output", type=Path, default=Path("best.json"))
    args = parser.parse_args()

    rng = random.Random(args.seed)
    by_total = {
        total: [p for p in partitions(total) if len(p) <= 4]
        for total in range(1, args.max_sum + 1)
    }

    best_candidate = None
    best_result = None

    for trial in range(1, args.trials + 1):
        mu_total = rng.randint(1, args.max_sum - 1)
        nu_total = rng.randint(1, args.max_sum - mu_total)
        outer_total = mu_total + nu_total
        candidate = {
            "lambda": list(rng.choice(by_total[outer_total])),
            "mu": list(rng.choice(by_total[mu_total])),
            "nu": list(rng.choice(by_total[nu_total])),
        }
        result = analyse(candidate)
        if result["values"][0] == 0:
            continue
        score = parse_fraction(result["smallest_coefficient"])

        if best_result is None or score < parse_fraction(
            best_result["smallest_coefficient"]
        ):
            best_candidate = candidate
            best_result = result
            args.output.write_text(json.dumps(candidate, indent=2) + "\n")
            print(
                f"trial={trial} score={score} candidate={candidate}",
                flush=True,
            )

        if result["counterexample"]:
            print("COUNTEREXAMPLE FOUND. NOW TRY TO BREAK IT.")
            return 0

    print(f"done; best result: {best_result}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
