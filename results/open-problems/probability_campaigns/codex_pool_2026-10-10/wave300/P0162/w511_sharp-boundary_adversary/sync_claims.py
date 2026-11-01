"""Merge saved mathematical rows, preserving earlier source rows and their IDs."""
import json
from pathlib import Path

base = Path(__file__).resolve().parent
target = base / "CLAIMS.jsonl"
existing = [json.loads(line) for line in target.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
rows = json.loads((base / "claim_rows.json").read_text(encoding="utf-8"))
present = {row["id"] for row in existing}
new = [row for row in rows if row["id"] not in present]
with target.open("a", encoding="utf-8") as out:
    for row in new:
        out.write(json.dumps(row, ensure_ascii=False) + "\n")
print(f"Saved {len(new)} mathematical claim rows; {len(existing)+len(new)} total.")
