"""Bounded, read-only recall probe; save only inside this worker folder."""
import json
import pathlib
import subprocess
import time

root = pathlib.Path(__file__).resolve().parent
cmd = ["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", "P0321 two-dimensional Riesz gases hexatic missing bridge mistakes"]
t0 = time.perf_counter()
try:
    p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
    result = {"command": cmd, "seconds": time.perf_counter() - t0, "returncode": p.returncode, "stdout": p.stdout, "stderr": p.stderr, "timeout": False}
except subprocess.TimeoutExpired as e:
    def decode(x):
        return x.decode("utf-8", "replace") if isinstance(x, bytes) else (x or "")
    result = {"command": cmd, "seconds": time.perf_counter() - t0, "returncode": None, "stdout": decode(e.stdout), "stderr": decode(e.stderr), "timeout": True}
(root / "recall_measurement.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(result, ensure_ascii=False))
