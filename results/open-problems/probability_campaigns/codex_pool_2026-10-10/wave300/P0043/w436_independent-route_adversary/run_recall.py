"""One 60-second, supervised recall; evidence and logs stay in this folder."""
from pathlib import Path
import json
import os
import subprocess
import sys
import time

root = Path(__file__).resolve().parent
reports = root / "reports"
reports.mkdir(exist_ok=True)
env = os.environ.copy()
env["PYTHONDONTWRITEBYTECODE"] = "1"
env["BRAIN_RECALL_LOG_PATH"] = str(reports / "recall_log.jsonl")
env["BRAIN_RECALL_REFRESH"] = "0"
command = [sys.executable, "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", "P0043 critical percolation independent proof mistakes", "-n", "3"]
started = time.perf_counter()
with (reports / "RECALL_REPORT.txt").open("w", encoding="utf-8") as output:
    try:
        result = subprocess.run(command, timeout=60, stdout=output, stderr=subprocess.STDOUT, env=env)
        status = {"status": "completed", "returncode": result.returncode}
    except subprocess.TimeoutExpired:
        status = {"status": "timeout", "fallback": "Targeted index lookup and the packet-named proof scars; no waiting for recall."}
status.update(elapsed_seconds=round(time.perf_counter()-started, 3), command=command)
(reports / "RECALL_RECEIPT.json").write_text(json.dumps(status, indent=2)+"\n", encoding="utf-8")
print(json.dumps(status), flush=True)
