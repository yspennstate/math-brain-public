"""One authorized recall, bounded to 60 seconds; reports stay in the worker folder."""
import json
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
cmd = [sys.executable, "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", "C0023 critical percolation proof mistakes", "-n", "3"]
start = time.monotonic()
try:
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
    receipt = {"command": cmd, "seconds": time.monotonic()-start, "returncode": result.returncode, "stdout": result.stdout, "stderr": result.stderr}
except subprocess.TimeoutExpired as exc:
    def txt(value):
        return value.decode("utf-8", errors="replace") if isinstance(value, bytes) else (value or "")
    receipt = {"command": cmd, "seconds": time.monotonic()-start, "status": "timeout; use targeted memory fallback", "stdout": txt(exc.stdout), "stderr": txt(exc.stderr)}
(ROOT / "RECALL_REPORT.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(receipt, ensure_ascii=False))
