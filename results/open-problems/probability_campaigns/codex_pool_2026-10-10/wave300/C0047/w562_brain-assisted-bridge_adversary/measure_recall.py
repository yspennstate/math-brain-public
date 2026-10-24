"""Bounded recall required by the brief; save output even on timeout."""
import json
import pathlib
import subprocess
import time

root = pathlib.Path(__file__).resolve().parent
command = ["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", "C0047 Benjamini Schramm probability bridge proof mistakes", "-n", "3"]
start = time.perf_counter()
try:
    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
    record = {"command": command, "elapsed_seconds": time.perf_counter()-start, "returncode": result.returncode, "timeout": False}
    stdout, stderr = result.stdout, result.stderr
except subprocess.TimeoutExpired as exc:
    record = {"command": command, "elapsed_seconds": time.perf_counter()-start, "returncode": None, "timeout": True, "timeout_seconds":60}
    def decode(value):
        return value.decode("utf-8", errors="replace") if isinstance(value, bytes) else value or ""
    stdout, stderr = decode(exc.stdout), decode(exc.stderr)
(root / "recall_output.txt").write_text(stdout, encoding="utf-8")
(root / "recall_stderr.txt").write_text(stderr, encoding="utf-8")
(root / "recall_measurement.json").write_text(json.dumps(record, indent=2), encoding="utf-8")
print(json.dumps(record))
print(stdout[:12000])
print(stderr[:1000])
