"""Run the requested recall once with the owner's explicit 60 second bound."""
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
query = "P0309 three-dimensional Riesz crystalline Gibbs phase bridge mistakes"
cmd = [sys.executable, "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", query, "-n", "3"]
env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
env["BRAIN_RECALL_DUMP_SCORED"] = str(ROOT / "evidence" / "recall_scored.jsonl")
start = time.monotonic()
try:
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60, env=env)
    record = {"command": cmd, "query": query, "elapsed_s": time.monotonic()-start, "timeout_s": 60, "timed_out": False, "returncode": result.returncode}
    output = result.stdout + "\nSTDERR:\n" + result.stderr
except subprocess.TimeoutExpired as error:
    record = {"command": cmd, "query": query, "elapsed_s": time.monotonic()-start, "timeout_s": 60, "timed_out": True, "returncode": None}
    stdout = error.stdout or b""
    stderr = error.stderr or b""
    output = (stdout.decode("utf-8", errors="replace") if isinstance(stdout, bytes) else stdout) + "\nSTDERR:\n" + (stderr.decode("utf-8", errors="replace") if isinstance(stderr, bytes) else stderr)
(ROOT / "evidence" / "recall_output.txt").write_text(output, encoding="utf-8")
(ROOT / "evidence" / "recall_run.json").write_text(json.dumps(record, indent=2), encoding="utf-8")
print(json.dumps(record))
print(output[:2500])
