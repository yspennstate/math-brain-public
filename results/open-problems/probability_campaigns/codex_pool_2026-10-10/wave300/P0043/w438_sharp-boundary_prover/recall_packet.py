"""One bounded, read-only recall; logs stay in this worker folder."""
import os
from pathlib import Path
import subprocess
import sys
import time

root = Path(__file__).resolve().parent
env = os.environ.copy()
env["BRAIN_RECALL_LOG_PATH"] = str(root / "recall_lane.jsonl")
start = time.monotonic()
with (root / "recall.txt").open("w", encoding="utf-8") as output:
    try:
        run = subprocess.run(
            [sys.executable, "-X", "utf8", "~/.claude/dreaming/brain.py",
             "recall", "P0043 critical percolation proof mistakes", "-n", "3"],
            env=env, stdout=output, stderr=subprocess.STDOUT, timeout=55,
        )
        status = f"exit={run.returncode}"
    except subprocess.TimeoutExpired:
        status = "timeout=55s; use targeted memory-index fallback"
    output.write(f"\nRECALL_STATUS: {status}; elapsed={time.monotonic()-start:.3f}s\n")
print((root / "recall.txt").read_text(encoding="utf-8"))
