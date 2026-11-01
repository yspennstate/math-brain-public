"""One authorized read-only recall, capped at 60 seconds; save the receipt locally."""
import os
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parent
command = ["python", "-B", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", "P0309 Riesz crystalline Gibbs phases proof mistakes", "-n", "3"]
try:
    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", timeout=60, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    receipt = f"COMMAND: {command!r}\nEXIT: {result.returncode}\n{result.stdout}\n{result.stderr}"
except subprocess.TimeoutExpired as error:
    receipt = "TIMEOUT: 60 seconds; use targeted MEMORY.md fallback.\n"
    for part in (error.stdout, error.stderr):
        if part:
            receipt += part.decode("utf-8", errors="replace") if isinstance(part, bytes) else part
(root / "recall_receipt.txt").write_text(receipt, encoding="utf-8")
print(receipt)
