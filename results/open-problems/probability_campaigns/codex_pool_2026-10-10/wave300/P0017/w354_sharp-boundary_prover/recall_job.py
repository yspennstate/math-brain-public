import os
import subprocess
import sys
import time
from pathlib import Path

base = Path(__file__).resolve().parent
start = time.monotonic()
env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONUTF8="1")
command = [sys.executable, "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", "P0017 KLS conditional Poincare proof mistakes"]
try:
    completed = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace", env=env, timeout=60)
    result = completed.stdout + completed.stderr
    code = completed.returncode
except subprocess.TimeoutExpired as exc:
    result = "RECALL_TIMEOUT_60S: use targeted MEMORY.md fallback.\n"
    if exc.stdout:
        result += exc.stdout.decode("utf-8", errors="replace") if isinstance(exc.stdout, bytes) else exc.stdout
    code = 124
elapsed = time.monotonic() - start
(base / "RECALL_RESULT.txt").write_text(f"command: {command!r}\nelapsed_seconds: {elapsed:.3f}\nreturncode: {code}\n{result}", encoding="utf-8")
print(f"recall elapsed_seconds={elapsed:.3f}, returncode={code}; saved {base / 'RECALL_RESULT.txt'}")
