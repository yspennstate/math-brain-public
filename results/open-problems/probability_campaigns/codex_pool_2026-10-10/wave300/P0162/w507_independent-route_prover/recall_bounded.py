"""The owner's explicitly required 60-second recall, with local-only receipt."""
from pathlib import Path
import json
import os
import subprocess
import sys
import time

root = Path(__file__).resolve().parent
command = [sys.executable, "-B", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall",
           "P0162 Fourier entropy total influence probability proof mistakes", "3"]
started = time.perf_counter()
env = dict(os.environ)
env["PYTHONDONTWRITEBYTECODE"] = "1"
try:
    run = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace",
                         timeout=60, env=env)
    status, output = "completed", run.stdout + run.stderr
except subprocess.TimeoutExpired as exc:
    status = "timeout_60_seconds"
    output = (exc.stdout or b"") + (exc.stderr or b"")
    if isinstance(output, bytes):
        output = output.decode("utf-8", errors="replace")
(root / "RECALL.txt").write_text(output, encoding="utf-8")
(root / "RECALL_RECEIPT.json").write_text(json.dumps({"status": status, "command": command,
    "elapsed_seconds": time.perf_counter()-started,
    "fallback": "Named scars read directly; targeted MEMORY.md search if no usable recall."}, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"status": status, "output_chars": len(output), "elapsed_seconds": time.perf_counter()-started}))
