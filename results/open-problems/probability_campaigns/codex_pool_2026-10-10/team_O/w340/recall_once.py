"""Run only the task's read-only recall, with a bounded wait and local receipt."""
import json
import os
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parent
env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONIOENCODING="utf-8")
cmd = [sys.executable, "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", "open probability problems proof attempts mistakes", "-n", "3"]
try:
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=50, env=env)
    receipt = {"command": cmd, "exit_code": result.returncode, "stdout": result.stdout, "stderr": result.stderr}
except subprocess.TimeoutExpired as exc:
    receipt = {"command": cmd, "timeout_seconds": 50, "fallback": "Targeted MEMORY.md search required"}
(root / "recall_receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(receipt, ensure_ascii=False))
