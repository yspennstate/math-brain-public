"""Task-authorized foreground recall, with the requested 60-second cap."""
from pathlib import Path
import os
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
env = os.environ.copy()
env.update(PYTHONDONTWRITEBYTECODE="1", BRAIN_RECALL_REFRESH="0", BRAIN_RECALL_QUERY_EMBED="0")
cmd = [sys.executable, "-X", "utf8", "~/.claude/dreaming/brain.py", "recall",
       "C0023 critical percolation proof conditioning uniform limits mistakes", "-n", "3"]
started = time.monotonic()
try:
    proc = subprocess.run(cmd, env=env, capture_output=True, text=True, encoding="utf-8",
                          errors="replace", timeout=60, check=False)
    status, output = f"exit={proc.returncode}", proc.stdout + proc.stderr
except subprocess.TimeoutExpired as exc:
    status = "TIMEOUT at requested 60 seconds; use cited memory scars and targeted index fallback"
    output = (exc.stdout or b"") + (exc.stderr or b"")
    if isinstance(output, bytes):
        output = output.decode("utf-8", errors="replace")
elapsed = time.monotonic() - started
report = f"Command: {' '.join(cmd)}\nStatus: {status}\nElapsed seconds: {elapsed:.3f}\n\n{output}"
(ROOT / "RECALL_REPORT.md").write_text(report, encoding="utf-8")
print(report)
