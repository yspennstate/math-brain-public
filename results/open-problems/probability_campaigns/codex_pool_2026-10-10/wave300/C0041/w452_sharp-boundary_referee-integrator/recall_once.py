"""Bound one required brain recall; do not leave an unbounded process."""

import subprocess


try:
    result = subprocess.run(
        ["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", "C0041 RWRE ballisticity referee mistakes"],
        capture_output=True,
        text=True,
        timeout=60,
    )
    print(result.stdout[:8000])
    print(result.stderr[:1000])
    print(f"exit={result.returncode}")
except subprocess.TimeoutExpired:
    print("RECALL_TIMEOUT_60S")
