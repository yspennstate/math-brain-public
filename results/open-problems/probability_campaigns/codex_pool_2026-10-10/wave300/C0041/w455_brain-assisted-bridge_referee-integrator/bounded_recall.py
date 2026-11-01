import json
import os
import subprocess
import sys
import time
from pathlib import Path

root = Path(__file__).resolve().parent
query = "C0041 directional transience ballisticity regeneration proof mistakes"
command = [sys.executable, "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", query]
started = time.monotonic()
env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
receipt = {"command": command, "query": query, "timeout_seconds": 60}
try:
    completed = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60, env=env)
    receipt.update(returncode=completed.returncode, stdout=completed.stdout, stderr=completed.stderr)
except subprocess.TimeoutExpired as exc:
    receipt.update(timed_out=True, stdout=(exc.stdout or b"").decode("utf-8", "replace") if isinstance(exc.stdout, bytes) else (exc.stdout or ""), stderr=(exc.stderr or b"").decode("utf-8", "replace") if isinstance(exc.stderr, bytes) else (exc.stderr or ""))
receipt["elapsed_seconds"] = round(time.monotonic() - started, 3)
(root / "recall_receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(receipt, ensure_ascii=False))
