"""Bounded reads of the assigned packet only; never opens evaluation material."""
from pathlib import Path

tasks = [
    ("paired prover attempt", "~/brain_workers/w462/ATTEMPT.md", 100),
    ("paired prover claims", "~/brain_workers/w462/CLAIMS.jsonl", 20),
    ("paired prover status", "~/brain_workers/w462/STATUS.md", 30),
    ("named proof scar", "~/.claude/projects/<project>/memory/perceptron_proof_open_gaps_fleet_2026_07_12.md", 130),
    ("open votes", "~/primary_directive/democracy/OPEN_VOTES.json", 50),
    ("hook proposal schema", "~/primary_directive/hooks1000/README.md", 130),
]
for label, name, cap in tasks:
    path = Path(name)
    print(f"\nFILE {label}: {name}")
    if not path.exists():
        print("MISSING")
        continue
    with path.open(encoding="utf-8-sig", errors="replace") as stream:
        for index, line in enumerate(stream):
            if index >= cap:
                print("[bounded read ended]")
                break
            print(f"{index+1}: {line.rstrip()}")

path = Path("~/.claude/dreaming/brain.py")
lines = path.read_text(encoding="utf-8-sig").splitlines()
for i, line in enumerate(lines):
    if ("add_argument" in line and ("top" in line or "limit" in line)) or "def recall" in line or 'add_parser("recall"' in line:
        print(f"\nBRAIN PARSER {i+1}:")
        for j in range(max(0, i-2), min(len(lines), i+7)):
            print(f"{j+1}: {lines[j]}")
