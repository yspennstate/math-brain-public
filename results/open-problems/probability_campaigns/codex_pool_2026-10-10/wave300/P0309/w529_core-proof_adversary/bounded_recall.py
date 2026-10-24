"""Run the requested recall once, bounded at sixty seconds; save locally."""
import subprocess
from pathlib import Path

folder = Path(__file__).resolve().parent
args = ["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", "P0309 Riesz crystalline Gibbs proof mistakes"]
try:
    result = subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
    output = result.stdout + result.stderr
except subprocess.TimeoutExpired:
    output = "RECALL_TIMEOUT_60S: use the two explicitly named proof-scar memory slugs as fallback.\n"
(folder / "RECALL.txt").write_text(output, encoding="utf-8")
print(output[:9000])
