"""Run the assigned read-only recall with the contract's 60-second deadline."""
import json
import pathlib
import subprocess
import time

root = pathlib.Path(__file__).resolve().parent
cmd = ["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", "P0174 free Brownian unimodality sharp support diameter mistakes", "-n", "3"]
start = time.perf_counter()
try:
    result = subprocess.run(cmd, timeout=60, capture_output=True, text=True, encoding="utf-8", errors="replace")
    receipt = {"command": cmd, "elapsed_seconds": time.perf_counter() - start, "returncode": result.returncode, "stdout": result.stdout, "stderr": result.stderr}
except subprocess.TimeoutExpired:
    receipt = {"command": cmd, "elapsed_seconds": time.perf_counter() - start, "outcome": "timeout; use targeted MEMORY.md fallback"}
(root / "recall_receipt.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
print(json.dumps(receipt, indent=2))
