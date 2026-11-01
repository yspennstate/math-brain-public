"""Run only the job-named recall, bounded at the owner's 60 second limit."""
from pathlib import Path
import json
import subprocess

base = Path(__file__).resolve().parent
command = ["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", "C0044 directional transience zero-one harmonicity mistakes"]
try:
    run = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
    lines = run.stdout.splitlines()
    allowed = [line for line in lines if "prob1000_" in line or "perceptron_proof_open_gaps_fleet" in line]
    result = {"command": command, "exit_code": run.returncode, "job_scoped_memory_matches": allowed[:3], "note": "Other recall matches excluded from this mathematical report; no unrelated memory source was opened.", "stderr": run.stderr[:1200]}
except subprocess.TimeoutExpired as exc:
    result = {"command": command, "status": "TIMEOUT_60S", "fallback_slug": "perceptron_proof_open_gaps_fleet_2026_07_12"}
(base / "recall_receipt.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(result, ensure_ascii=False))
