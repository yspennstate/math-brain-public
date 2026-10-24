"""Bounded read-only recall; outputs are confined to this worker folder."""
from pathlib import Path
import json
import subprocess
import time

HERE = Path(__file__).resolve().parent
query = "C0052 three dimensional Ising nontrivial scaling limit proof mistakes"
start = time.monotonic()
try:
    completed = subprocess.run(
        ["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", query],
        capture_output=True, text=True, encoding="utf-8", timeout=55,
    )
    result = {"query": query, "seconds": time.monotonic() - start,
              "returncode": completed.returncode,
              "stdout": completed.stdout[:14000], "stderr": completed.stderr[:1200]}
except subprocess.TimeoutExpired as exc:
    result = {"query": query, "seconds": time.monotonic() - start,
              "status": "55-second timeout; use the specifically named memory files",
              "stdout": (exc.stdout or b"").decode("utf-8", errors="replace")[:1000]}
(HERE / "RECALL_RECEIPT.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(result, ensure_ascii=False))
