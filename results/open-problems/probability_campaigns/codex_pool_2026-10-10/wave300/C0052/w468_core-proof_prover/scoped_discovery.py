from pathlib import Path
import subprocess

base = Path("~/<private-repo>/06_math_research")
scopes = sorted(base.glob("probability_1000_intake_*")) + [
    base / "probability_1000_attempts_H_20260912",
    base / "probability_1000_attempts_I_20260914",
    base / "prob1000_lean_20260908",
]
for scope in scopes:
    if scope.is_dir():
        r = subprocess.run(["rg", "-l", "-g", "*.md", "-g", "*.json", "-g", "*.jsonl", "-g", "*.csv", "-g", "*.lean",
                            "C0052", str(scope)], capture_output=True, text=True, encoding="utf-8", timeout=45)
        print(r.stdout[:14000], end="")
memory = Path("~/.claude/projects/<project>/memory/perceptron_proof_open_gaps_fleet_2026_07_12.md")
if memory.exists():
    print("NAMED_SCAR", memory)
    print(memory.read_text(encoding="utf-8")[:14000])
else:
    print("NAMED_SCAR_MISSING", memory)
