"""Write exact quote-backed draft edge rows from the local bundle."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent
bundle = json.loads((root / "bundle_001.json").read_text(encoding="utf-8"))
entries = {entry["key"]: entry for entry in bundle["entries"]}
rows = []
for relation in bundle["relations"]:
    if "to_key" not in relation:
        continue
    rows.append({
        "id": "w479-C0052-E" + str(len(rows) + 1).zfill(3),
        "from_key": relation["from_key"],
        "to_key": relation["to_key"],
        "kind": relation["kind"],
        "rationale": relation["rationale"],
        "from_card_quote": entries[relation["from_key"]]["statement"],
        "to_card_quote": entries[relation["to_key"]]["statement"],
        "source": "~/brain_workers/w479/bundle_001.json",
        "independent_reviewer": "w482 pending for own derivation; coordinator checks bundle relation",
        "remaining_gap": "No near-critical Q bound or C0052 proof; draft relation not ingested.",
        "status": "sketch",
    })
(root / "EDGES.jsonl").write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n", encoding="utf-8")
print(f"wrote {len(rows)} exact-quote draft edges")
