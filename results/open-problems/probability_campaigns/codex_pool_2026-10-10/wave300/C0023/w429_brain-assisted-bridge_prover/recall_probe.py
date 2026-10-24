import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
query = "C0023 critical percolation quantitative uniqueness brain-assisted bridge mistakes"
cmd = ["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", query]
start = time.monotonic()
try:
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
    output = result.stdout + "\nSTDERR:\n" + result.stderr
    status = f"RETURN {result.returncode}"
except subprocess.TimeoutExpired as exc:
    raw = exc.stdout or b""
    output = raw.decode("utf-8", errors="replace") if isinstance(raw, bytes) else raw
    status = "TIMEOUT after 60 seconds; use named memory index fallback"
elapsed = time.monotonic() - start
text = f"QUERY: {query}\nELAPSED_SECONDS: {elapsed:.3f}\n{status}\n{output}\n"
(ROOT / "recall_mistakes.txt").write_text(text, encoding="utf-8")
print(text[:11000])
