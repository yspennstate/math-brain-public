"""One bounded recall attempt; no daemon or follow-up model invocation."""
import subprocess

command = [
    "python", "-X", "utf8", "~/.claude/dreaming/brain.py",
    "recall", "C0120 directed polymer variance sharp boundary proof mistakes",
]
try:
    result = subprocess.run(command, capture_output=True, text=True,
                            encoding="utf-8", timeout=60)
    print(result.stdout)
    print(result.stderr)
except subprocess.TimeoutExpired:
    print("RECALL_TIMEOUT_60S; fallback scar: perceptron_proof_open_gaps_fleet_2026_07_12")
