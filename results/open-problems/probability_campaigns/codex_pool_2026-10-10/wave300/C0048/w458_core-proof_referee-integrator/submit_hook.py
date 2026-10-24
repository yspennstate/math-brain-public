"""Submit only the one evidence-backed w458 hooks1000 proposal."""
import json
from pathlib import Path

src = Path(__file__).parent / "hooks-proposal.jsonl"
line = src.read_text(encoding="utf-8").strip()
obj = json.loads(line)
assert obj["id"] == "c0048-w458-01"
assert obj["proposer"] == "w458"
assert len(obj["text"]) <= 300
dest = Path("~/primary_directive/hooks1000/proposals/math-w458.jsonl")
existing = dest.read_text(encoding="utf-8") if dest.exists() else ""
if any(json.loads(x)["id"] == obj["id"] for x in existing.splitlines() if x):
    print("already_present", dest)
else:
    with dest.open("a", encoding="utf-8", newline="\n") as out:
        out.write(line + "\n")
    print("submitted", dest)
