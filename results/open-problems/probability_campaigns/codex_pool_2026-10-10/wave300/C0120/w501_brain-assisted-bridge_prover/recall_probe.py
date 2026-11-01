"""Bounded required recall; persist evidence locally before printing it."""
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
QUERY = "C0120 directed polymer Gaussian overlap variance proof mistakes"
started = time.monotonic()
try:
    run = subprocess.run(
        [sys.executable, "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", QUERY, "-n", "3"],
        capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )
    receipt = {"query": QUERY, "timeout_seconds": 60, "elapsed_seconds": time.monotonic()-started,
               "exit_code": run.returncode, "timed_out": False, "stdout": run.stdout, "stderr": run.stderr}
except subprocess.TimeoutExpired as exc:
    def decode(value):
        return value.decode("utf-8", errors="replace") if isinstance(value, bytes) else (value or "")
    receipt = {"query": QUERY, "timeout_seconds": 60, "elapsed_seconds": time.monotonic()-started,
               "exit_code": None, "timed_out": True, "stdout": decode(exc.stdout), "stderr": decode(exc.stderr)}
(ROOT / "recall_receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps(receipt, ensure_ascii=False))
