"""Bound the explicitly requested memory recall to 60 seconds."""
import json
import subprocess
import sys
import time
from pathlib import Path

root = Path(__file__).resolve().parent
query = "C0052 three dimensional Ising scaling limit nontriviality mistakes"
started = time.perf_counter()
try:
    result = subprocess.run(
        [sys.executable, "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", query],
        capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60,
    )
    receipt = {"query": query, "elapsed_seconds": time.perf_counter()-started,
               "returncode": result.returncode, "stdout": result.stdout,
               "stderr": result.stderr, "timed_out": False}
except subprocess.TimeoutExpired as exc:
    receipt = {"query": query, "elapsed_seconds": time.perf_counter()-started,
               "timed_out": True, "stdout": (exc.stdout or b"").decode("utf-8", "replace")
               if isinstance(exc.stdout, bytes) else (exc.stdout or "")}
(root / "recall_receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(receipt, ensure_ascii=False))
