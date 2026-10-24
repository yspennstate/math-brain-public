"""Bounded, single recall; writes only the worker's receipt.

The exact live recall invocation is explicitly required by the task brief.
"""
from pathlib import Path
import os
import subprocess

ROOT = Path(__file__).resolve().parent
query = "P0297 Liouville quantum gravity proof selection mistakes"
env = os.environ.copy()
env["PYTHONDONTWRITEBYTECODE"] = "1"
try:
    result = subprocess.run(
        ["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", query, "-n", "3"],
        capture_output=True, text=True, encoding="utf-8", timeout=60, env=env,
    )
    receipt = f"exit_code={result.returncode}\n{result.stdout}\nSTDERR\n{result.stderr}"
except subprocess.TimeoutExpired:
    receipt = "RECALL TIMEOUT after 60 seconds; use targeted memory-index fallback.\n"
index = Path("~/.claude/projects/<project>/memory/MEMORY.md")
terms = ("perceptron_proof_open_gaps_fleet_2026_07_12", "proof_steps_need_derived_joint_structure_2026_09_09", "liouville", "p0297")
matches = [f"{i}: {line}" for i, line in enumerate(index.read_text(encoding="utf-8").splitlines(), 1) if any(t in line.lower() for t in terms)]
receipt += "\nINDEX FALLBACK\n" + "\n".join(matches[:12])
(ROOT / "recall.txt").write_text(receipt, encoding="utf-8")
print(receipt)
