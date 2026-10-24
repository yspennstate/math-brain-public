"""Mandatory recall with the packet's 60-second bound; stores only this worker's report."""
import json
from pathlib import Path
import subprocess
import sys
import time

command = [sys.executable, "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", "C0048 Potts mean-field barrier mistakes"]
start = time.monotonic()
try:
    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
    report = {"command": command, "elapsed_seconds": time.monotonic()-start, "returncode": result.returncode, "stdout_bounded": result.stdout[:3500], "stderr_bounded": result.stderr[:500], "fallback_slug": "perceptron_proof_open_gaps_fleet_2026_07_12"}
except subprocess.TimeoutExpired as exc:
    report = {"command": command, "elapsed_seconds": time.monotonic()-start, "timeout_seconds": 60, "fallback_slug": "perceptron_proof_open_gaps_fleet_2026_07_12", "result": "timed out; continued with the exact named scar"}
Path(__file__).with_name("RECALL_REPORT.json").write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
print(json.dumps(report, indent=2))
