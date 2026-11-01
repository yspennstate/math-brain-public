"""One foreground recall, bounded at 60 seconds; save the receipt locally."""
import json
from pathlib import Path
import subprocess
import time

root = Path(__file__).resolve().parent
query = "C0056 Anderson delocalisation spectral measure mistakes"
receipt = {"query": query}
started = time.monotonic()
try:
    result = subprocess.run(
        ["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", query],
        capture_output=True, text=True, encoding="utf-8", timeout=60,
    )
    receipt.update(returncode=result.returncode, stdout=result.stdout, stderr=result.stderr)
except subprocess.TimeoutExpired as error:
    value = error.stdout or ""
    if isinstance(value, bytes):
        value = value.decode("utf-8", "replace")
    receipt.update(timed_out=True, stdout=value, stderr="60-second limit; targeted MEMORY.md fallback required")
receipt["elapsed_seconds"] = time.monotonic() - started
(root / "recall_initial.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(receipt, ensure_ascii=False)[:10000])
