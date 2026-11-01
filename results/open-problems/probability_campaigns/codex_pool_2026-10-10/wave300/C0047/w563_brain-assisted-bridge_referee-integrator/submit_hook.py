import json
from pathlib import Path

source = Path(r"~\brain_workers\w563\hook_proposal.jsonl")
line = source.read_text(encoding="utf-8").strip()
row = json.loads(line)
assert row["id"] == "math-w563-01"
assert len(row["text"]) <= 300
destination = Path(r"~\primary_directive\hooks1000\proposals\math-w563.jsonl")
destination.parent.mkdir(parents=True, exist_ok=True)
existing = destination.read_text(encoding="utf-8") if destination.exists() else ""
if row["id"] not in existing:
    with destination.open("a", encoding="utf-8") as handle:
        handle.write(line + "\n")
print(destination, "rows", len(destination.read_text(encoding="utf-8").splitlines()))
