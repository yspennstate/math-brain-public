"""Bounded read-only recall; writes its receipt only to this worker folder."""
from pathlib import Path
import os
import subprocess
import time

root = Path(__file__).resolve().parent
cmd = ["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", "P0110 iid FPP KPZ exponent relation proof mistakes", "-n", "3"]
started = time.monotonic()
env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
try:
    proc = subprocess.run(cmd, capture_output=True, encoding="utf-8", errors="replace", timeout=60, env=env)
    result = f"command: {cmd!r}\nelapsed_seconds: {time.monotonic()-started:.3f}\nexit_code: {proc.returncode}\n{proc.stdout}\n{proc.stderr}"
except subprocess.TimeoutExpired as exc:
    out = exc.stdout or b""
    if isinstance(out, bytes):
        out = out.decode("utf-8", errors="replace")
    result = f"command: {cmd!r}\nelapsed_seconds: {time.monotonic()-started:.3f}\nresult: TIMEOUT (60 seconds; use memory fallback)\n{out}"
(root / "recall_receipt.txt").write_text(result, encoding="utf-8")
print(result)
