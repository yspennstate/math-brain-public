"""Append the measured recall hook to the explicitly named proposals file."""

import json
from pathlib import Path

root = Path(__file__).resolve().parent
line = (root / "HOOK_PROPOSAL.jsonl").read_text(encoding="utf-8").strip()
proposal = json.loads(line)
target = Path("~/primary_directive/hooks1000/proposals/math-w527.jsonl")
existing = target.read_text(encoding="utf-8").splitlines() if target.exists() else []
if any(json.loads(row).get("id") == proposal["id"] for row in existing if row.strip()):
    print(f"already proposed: {target}")
else:
    with target.open("a", encoding="utf-8") as stream:
        stream.write(line + "\n")
    print(f"proposed: {target}")
