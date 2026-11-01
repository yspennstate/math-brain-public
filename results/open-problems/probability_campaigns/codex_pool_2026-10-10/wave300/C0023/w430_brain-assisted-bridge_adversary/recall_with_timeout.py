import json
from pathlib import Path
import subprocess
import time

root = Path(__file__).resolve().parent
command = ["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", "C0023 critical percolation bridge mistakes", "-n", "3"]
started = time.perf_counter()
result = {"command": command}
try:
    run = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", timeout=60)
    body = run.stdout + "\nSTDERR:\n" + run.stderr
    result.update(status="completed", returncode=run.returncode)
except subprocess.TimeoutExpired as exc:
    body = exc.stdout or ""
    if isinstance(body, bytes):
        body = body.decode("utf-8", errors="replace")
    result.update(status="timeout", timeout_seconds=60)
result["elapsed_seconds"] = round(time.perf_counter() - started, 3)
(root / "recall_mistakes.txt").write_text(body, encoding="utf-8")
(root / "recall_mistakes_metrics.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps(result))
print(body[:16000])
