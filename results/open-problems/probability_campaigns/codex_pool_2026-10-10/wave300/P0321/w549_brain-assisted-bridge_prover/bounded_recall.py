import json
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
command = ["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", "P0321 hexatic Riesz bridge mistakes"]
start = time.monotonic()
result = {"command": command}
try:
    completed = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", timeout=60)
    result.update(returncode=completed.returncode, output=completed.stdout, stderr=completed.stderr)
except subprocess.TimeoutExpired as exc:
    output = exc.stdout or ""
    if isinstance(output, bytes):
        output = output.decode("utf-8", "replace")
    result.update(timeout_seconds=60, output=output)
result["elapsed_seconds"] = time.monotonic() - start
(ROOT / "recall_measurement.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(result, ensure_ascii=False)[:14000])
