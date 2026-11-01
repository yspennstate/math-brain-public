import json
import subprocess
import time
from pathlib import Path

root = Path(__file__).resolve().parent
query = "P0104 first passage percolation KPZ fluctuation proof bridge mistakes"
start = time.monotonic()
try:
    result = subprocess.run(
        ["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", query, "3"],
        capture_output=True, text=True, encoding="utf-8", timeout=55,
    )
    row = {"query": query, "seconds": time.monotonic()-start,
           "returncode": result.returncode, "stdout": result.stdout, "stderr": result.stderr}
except subprocess.TimeoutExpired:
    row = {"query": query, "seconds": time.monotonic()-start, "status": "timeout_55s"}
(root / "brain_recall.json").write_text(json.dumps(row, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(row, ensure_ascii=False)[:16000])
