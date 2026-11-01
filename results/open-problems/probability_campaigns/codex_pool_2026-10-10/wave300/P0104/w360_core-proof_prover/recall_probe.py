"""One authorized recall, bounded to 60 seconds, with all receipts local."""
import json
import pathlib
import subprocess
import time

root = pathlib.Path(__file__).resolve().parent
cmd = ["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", "P0104 first passage KPZ fluctuation proof mistakes", "-n", "3"]
start = time.monotonic()
receipt = {"command": cmd}
try:
    p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
    stdout, stderr = p.stdout, p.stderr
    receipt["returncode"] = p.returncode
except subprocess.TimeoutExpired as exc:
    receipt.update(timeout_seconds=60, returncode=None)
    stdout, stderr = exc.stdout or "", exc.stderr or ""
    if isinstance(stdout, bytes):
        stdout = stdout.decode("utf-8", "replace")
    if isinstance(stderr, bytes):
        stderr = stderr.decode("utf-8", "replace")
receipt["elapsed_seconds"] = round(time.monotonic() - start, 3)
(root / "recall.txt").write_text(stdout + "\nSTDERR\n" + stderr, encoding="utf-8")
(root / "recall_receipt.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
print(json.dumps(receipt))
print(stdout[:10000])
print(stderr[:1000])
