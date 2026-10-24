"""Bound the requested recall; prohibit refresh/log writes for this process only."""
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
env = dict(os.environ)
env.update(PYTHONDONTWRITEBYTECODE="1", BRAIN_RECALL_REFRESH="0", BRAIN_GRAPH_LAMBDA="0")
command = [sys.executable, "-B", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", "P0017 KLS log-concave Poincare independent proof conditioning mistakes", "-n", "3"]
start = time.monotonic()
try:
    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=55, env=env)
    receipt = {"command": command, "elapsed_seconds": time.monotonic()-start, "exit_code": result.returncode, "timeout": False, "stdout": result.stdout, "stderr": result.stderr, "process_only_settings": {k: env[k] for k in ("PYTHONDONTWRITEBYTECODE", "BRAIN_RECALL_REFRESH", "BRAIN_GRAPH_LAMBDA")}}
except subprocess.TimeoutExpired as exc:
    receipt = {"command": command, "elapsed_seconds": time.monotonic()-start, "timeout": True, "fallback": "Use the named scar files and targeted MEMORY.md search, per the supplied 60-second recall rule."}
(ROOT/"recall_receipt.json").write_text(json.dumps(receipt, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(receipt, ensure_ascii=False)[:14000])
