"""Run the required targeted recall with a strict wall-clock timeout."""
import subprocess

command = [
    "python", "-X", "utf8", "~/.claude/dreaming/brain.py",
    "recall", "C0023 critical percolation proof quantifiers mistakes",
]
try:
    result = subprocess.run(command, capture_output=True, text=True,
                            encoding="utf-8", timeout=60)
    print(result.stdout[:18000])
    print(result.stderr[:1000])
except subprocess.TimeoutExpired:
    print("RECALL_TIMEOUT_60_SECONDS: use targeted MEMORY.md fallback")
