"""Run the expressly authorized recall with a 60-second deadline; save locally."""
from pathlib import Path
import json
import subprocess
import time

ROOT = Path(__file__).resolve().parent
command = ["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", "C0041 directional transience ballisticity regeneration mistakes"]
started = time.monotonic()
try:
    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", timeout=60)
    record = {"command": command, "seconds": time.monotonic()-started, "exit_code": result.returncode, "timed_out": False, "stdout": result.stdout, "stderr": result.stderr}
except subprocess.TimeoutExpired as exc:
    def decode(value):
        return value.decode("utf-8", "replace") if isinstance(value, bytes) else value or ""
    record = {"command": command, "seconds": time.monotonic()-started, "exit_code": None, "timed_out": True, "stdout": decode(exc.stdout), "stderr": decode(exc.stderr)}
(ROOT / "recall_result.json").write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(record, ensure_ascii=False, indent=2))
