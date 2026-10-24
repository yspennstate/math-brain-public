import json
from pathlib import Path

root = Path(__file__).resolve().parent
bundle = json.loads((root / "drafts" / "bundle_001.json").read_text(encoding="utf-8"))
assert json.loads((root / "SOURCE_STATUS.json").read_text(encoding="utf-8"))["current_openness"] == "UNKNOWN"
row_counts = {}
for filename in ("CLAIMS.jsonl", "CORRECTIONS.jsonl"):
    rows = [json.loads(line) for line in (root / filename).read_text(encoding="utf-8").splitlines()]
    assert all(rows)
    row_counts[filename] = len(rows)
proposal = json.loads((root / "proposals" / "math-w383.jsonl").read_text(encoding="utf-8"))
assert proposal["fire_when"] and proposal["silent_when"] and len(proposal["text"]) <= 300
assert bundle["spec"] == "mathbrain-draft-v1" and bundle["author_agent"] == "w383"
entries = {entry["key"]: entry for entry in bundle["entries"]}
assert len(entries) == len(bundle["entries"]) <= 200
for entry in entries.values():
    assert entry["kind"] in {"definition", "lemma", "theorem", "concept"}
    assert entry["proof_text"] if entry["kind"] in {"lemma", "theorem"} else entry["proof_text"] is None
    assert entry["source"]["license"].startswith("owner-own-work")
    assert entry["statement"] and entry["logical_name"] and entry["namespace"]

cards = json.loads((root / "TARGET_CARDS.json").read_text(encoding="utf-8"))["cards"]
target = next(c for c in cards if c["title"].startswith("Open problem: An iid FPP law"))
support = []
for relation in bundle["relations"]:
    assert relation["from_key"] in entries
    assert ("to_key" in relation) != ("to_existing_logical" in relation)
    if "to_key" in relation:
        assert relation["to_key"] in entries
        target_quote = entries[relation["to_key"]]["statement"]
    else:
        assert relation["to_existing_logical"] == "math:probability.core:open-problem-p0110-an-iid-fpp-law-with-proved-kpz-exponent-relation"
        target_quote = target["body"].split("\n")[0]
    assert relation["kind"] in {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
    support.append({"from_key": relation["from_key"], "from_quote": entries[relation["from_key"]]["statement"],
                    "to": relation.get("to_key", relation.get("to_existing_logical")), "to_quote": target_quote,
                    "kind": relation["kind"], "rationale": relation["rationale"]})
(root / "EDGE_SUPPORT.jsonl").write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in support), encoding="utf-8")
receipt = {"spec": bundle["spec"], "entries": len(entries), "relations": len(support),
           "row_counts": row_counts,
           "both_ends_quoted": True, "source_license_prefix": "owner-own-work",
           "mathematical_review": "adjacent-edge lemma independently checked by w383; source correction needs second audit",
           "submitted": False, "ingested": False, "retrievable": False, "failures": 0}
(root / "BUNDLE_VALIDATION.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
print(json.dumps(receipt))
