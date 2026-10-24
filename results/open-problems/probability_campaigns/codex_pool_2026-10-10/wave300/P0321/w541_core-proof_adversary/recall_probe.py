"""Run the requested narrow recall with a hard 60-second child timeout."""
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
cmd = [sys.executable, "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", "P0321 hexatic phase Riesz gases core proof mistakes"]
try:
    run = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
    result = f"exit_code={run.returncode}\n" + run.stdout + run.stderr
except subprocess.TimeoutExpired as exc:
    result = "TIMEOUT after 60 seconds; use the named memory index fallback.\n"
    if exc.stdout:
        result += exc.stdout.decode("utf-8", "replace") if isinstance(exc.stdout, bytes) else exc.stdout
(root / "recall_probe.txt").write_text(result, encoding="utf-8")
print(result[:10000])
