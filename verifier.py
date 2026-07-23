#!/usr/bin/env python3
"""Trusted problem verifier. Replace this before starting a research run."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate", type=Path)
    args = parser.parse_args()

    json.loads(args.candidate.read_text())
    print("REJECT: implement verifier.py for the task in problem.md")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
