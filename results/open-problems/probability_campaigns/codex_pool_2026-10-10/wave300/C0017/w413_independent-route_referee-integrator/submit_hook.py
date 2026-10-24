"""Submit one complete C0017 hook proposal without overwriting a peer file."""

import json
from pathlib import Path

source = Path(__file__).with_name("HOOK_PROPOSAL.jsonl")
line = source.read_text(encoding="utf-8").strip()
obj = json.loads(line)
assert obj["id"] == "math-w413-01" and obj["area"] == "math"
assert len(obj["text"]) <= 300
dest = Path(r"~\primary_directive\hooks1000\proposals\math-w413.jsonl")
if dest.exists():
    if line not in dest.read_text(encoding="utf-8").splitlines():
        raise FileExistsError(f"Proposal file already contains other rows: {dest}")
else:
    with dest.open("x", encoding="utf-8") as out:
        out.write(line + "\n")
print(f"PROPOSED {dest}")
