"""Filename-only searches in the brief's exact local prior-work roots."""
from pathlib import Path
import json
import subprocess

base = Path(__file__).resolve().parent
research = Path("~/<private-repo>/06_math_research")
roots = sorted(research.glob("probability_1000_intake_*"))
roots += [research / "probability_1000_attempts_H_20260912", research / "probability_1000_attempts_I_20260914", research / "prob1000_lean_20260908"]
roots = [p for p in roots if p.is_dir()]
command = ["rg", "-l", "-F", "C0044", "-g", "*.md", "-g", "*.json", "-g", "*.jsonl", "-g", "*.csv"] + [str(p) for p in roots]
run = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=90)
result = {"command": command, "exit_code": run.returncode, "matching_files": run.stdout.splitlines(), "stderr": run.stderr[:1000]}
(base / "intake_search_receipt.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(result, ensure_ascii=False, indent=2))
