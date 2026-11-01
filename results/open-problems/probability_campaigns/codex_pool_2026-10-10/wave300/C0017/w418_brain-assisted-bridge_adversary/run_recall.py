"""Bounded, synchronous recall evidence; files only in this worker folder."""
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
query = "C0017 square lattice bond percolation parafermionic observable conformal invariance mistakes"
command = [sys.executable, "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", query, "-n", "3"]
started = time.monotonic()
env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
try:
    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=55, env=env)
    record = {"command":command,"elapsed_seconds":time.monotonic()-started,"timeout_seconds":55,"returncode":result.returncode,"timed_out":False,"stdout":result.stdout,"stderr":result.stderr}
except subprocess.TimeoutExpired as exc:
    def decode(value):
        return value.decode("utf-8", errors="replace") if isinstance(value, bytes) else value or ""
    record = {"command":command,"elapsed_seconds":time.monotonic()-started,"timeout_seconds":55,"returncode":None,"timed_out":True,"stdout":decode(exc.stdout),"stderr":decode(exc.stderr),"fallback":"Targeted MEMORY.md search and the named perceptron scar; no continued wait."}
(ROOT / "recall_measurement.json").write_text(json.dumps(record, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps(record, ensure_ascii=False))
