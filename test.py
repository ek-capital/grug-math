#!/usr/bin/env python3
"""Small tests for harness plumbing."""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

from check import load_config, run_checker


def main() -> None:
    command, timeout = load_config()
    assert command == ["python3", "verifier.py"]
    assert timeout == 300

    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        candidate = root / "candidate.json"
        checker = root / "fake_checker.py"
        candidate.write_text(json.dumps({"certificate": "test"}))
        checker.write_text(
            "import json, pathlib, sys\n"
            "data = json.loads(pathlib.Path(sys.argv[1]).read_text())\n"
            "raise SystemExit(0 if data.get('certificate') == 'test' else 1)\n"
        )
        assert run_checker(
            candidate,
            [sys.executable, str(checker)],
            timeout=5,
            cwd=root,
        ) == 0

    print("ok")


if __name__ == "__main__":
    main()
