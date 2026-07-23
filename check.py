#!/usr/bin/env python3
"""Run the repository's trusted verifier against one JSON candidate."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CONFIG = ROOT / "harness.json"


def load_config(path: Path = CONFIG) -> tuple[list[str], int]:
    data = json.loads(path.read_text())
    command = data.get("checker")
    timeout = data.get("timeout_seconds", 300)
    if not isinstance(command, list) or not command:
        raise ValueError("harness.json checker must be a non-empty list")
    if not all(isinstance(part, str) and part for part in command):
        raise ValueError("checker command parts must be non-empty strings")
    if not isinstance(timeout, int) or timeout < 1:
        raise ValueError("timeout_seconds must be a positive integer")
    return command, timeout


def run_checker(
    candidate: Path,
    command: list[str],
    timeout: int,
    cwd: Path = ROOT,
) -> int:
    candidate = candidate.resolve()
    json.loads(candidate.read_text())
    result = subprocess.run(
        [*command, str(candidate)],
        cwd=cwd,
        text=True,
        timeout=timeout,
    )
    return result.returncode


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate", type=Path)
    args = parser.parse_args()

    try:
        command, timeout = load_config()
        return run_checker(args.candidate, command, timeout)
    except (
        FileNotFoundError,
        json.JSONDecodeError,
        subprocess.TimeoutExpired,
        ValueError,
    ) as error:
        print(f"HARNESS ERROR: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
