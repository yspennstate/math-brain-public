"""One authorized 60-second recall; checkpoint output locally."""
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parent
command = ["python", "-X", "utf8", "~/.claude/dreaming/brain.py",
           "recall", "C0052 three-dimensional Ising scaling limit proof mistakes", "-n", "3"]
try:
    result = subprocess.run(command, capture_output=True, text=True,
                            encoding="utf-8", timeout=60)
    output = result.stdout + "\nSTDERR:\n" + result.stderr
    (root / "recall.txt").write_text(output, encoding="utf-8")
    print(output[:9500])
except subprocess.TimeoutExpired:
    (root / "recall.txt").write_text(
        "Recall timed out at 60 seconds; use targeted memory-index fallback.\n", encoding="utf-8")
    print("RECALL_TIMEOUT_60S")
