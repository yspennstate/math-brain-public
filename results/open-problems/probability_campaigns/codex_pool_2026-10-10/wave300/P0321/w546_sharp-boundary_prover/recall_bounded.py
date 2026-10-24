"""Run the explicitly requested recall once with its authorized 60 second gate."""
import json
from pathlib import Path
import subprocess
import time

root = Path(__file__).resolve().parent
command = ["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", "P0321 hexatic Riesz gases proof mistakes"]
started = time.monotonic()
try:
    run = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", timeout=60)
    record = {"command": command, "seconds": time.monotonic()-started, "returncode": run.returncode, "stdout": run.stdout, "stderr": run.stderr}
except subprocess.TimeoutExpired as exc:
    record = {"command": command, "seconds": time.monotonic()-started, "status": "TIMEOUT_60S", "stdout": str(exc.stdout or ""), "next": "targeted MEMORY.md and cited scar fallback"}
(root / "RECALL_RECEIPT.json").write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(record, ensure_ascii=False)[:14500])
