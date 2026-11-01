"""Append one evidence-backed w449 hook to the specified rolling proposals file."""
import json
from pathlib import Path

root = Path(__file__).parent
source = root / "proposals" / "math-w449.jsonl"
target = Path("~/primary_directive/hooks1000/proposals/math-w449.jsonl")
line = source.read_text(encoding="utf-8").strip()
proposal = json.loads(line)
assert proposal["proposer"] == "w449"
assert len(proposal["text"]) <= 300
assert proposal["fire_when"] and proposal["silent_when"] and proposal["evidence"]
target.parent.mkdir(parents=True, exist_ok=True)
if target.exists():
    old = target.read_text(encoding="utf-8")
    if any(json.loads(x).get("id") == proposal["id"] for x in old.splitlines() if x.strip()):
        print(f"already proposed: {proposal['id']}")
    else:
        with target.open("a", encoding="utf-8", newline="\n") as out:
            out.write(line + "\n")
        print(f"appended: {proposal['id']}")
else:
    target.write_text(line + "\n", encoding="utf-8")
    print(f"created: {proposal['id']}")
