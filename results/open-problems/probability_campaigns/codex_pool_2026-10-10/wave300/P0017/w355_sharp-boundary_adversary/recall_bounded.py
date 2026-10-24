"""One task-scoped recall with the owner's 60-second bound."""
import json
import os
from pathlib import Path
import subprocess
import sys
import time

folder = Path(__file__).resolve().parent
command = [sys.executable, "-X", "utf8", "-B", "~/.claude/dreaming/brain.py", "recall", "P0017 KLS conditional Poincare proof mistakes"]
started = time.monotonic()
try:
    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    receipt = {"command": command, "elapsed_seconds": time.monotonic() - started, "returncode": result.returncode, "stdout": result.stdout, "stderr": result.stderr}
except subprocess.TimeoutExpired as exc:
    def decode(value):
        return value.decode("utf-8", errors="replace") if isinstance(value, bytes) else value or ""
    receipt = {"command": command, "elapsed_seconds": time.monotonic() - started, "timed_out": True, "stdout": decode(exc.stdout), "stderr": decode(exc.stderr), "fallback": "Read targeted memory-index matches and named perceptron scar."}
(folder / "RECALL_RECEIPT.json").write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps(receipt, ensure_ascii=False)[:14000])
