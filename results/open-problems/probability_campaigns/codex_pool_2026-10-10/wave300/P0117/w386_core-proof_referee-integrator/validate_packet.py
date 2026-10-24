import json
import re
import sqlite3
from pathlib import Path

root = Path(__file__).parent
source = json.loads((root / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
claims = [json.loads(line) for line in (root / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line]
reviews = [json.loads(line) for line in (root / "REVIEWS.jsonl").read_text(encoding="utf-8").splitlines() if line]
hooks = [json.loads(line) for line in (root / "hook_proposal.jsonl").read_text(encoding="utf-8").splitlines() if line]
bundle = json.loads((root / "bundle_002.json").read_text(encoding="utf-8"))

assert source["target"] == "P0117"
assert source["current_openness"] == "UNKNOWN"
assert bundle["spec"] == "mathbrain-draft-v1"
assert bundle["author_agent"] == "w386"
assert len(bundle["entries"]) == 2 and len(bundle["relations"]) == 2
assert len({entry["logical_name"] for entry in bundle["entries"]}) == len(bundle["entries"])
keys = {entry["key"] for entry in bundle["entries"]}
assert len(keys) == len(bundle["entries"])
for entry in bundle["entries"]:
    assert entry["namespace"] == "probability.core"
    assert entry["kind"] == "concept"
    assert entry["proof_text"] is None
    assert entry["source"]["license"].startswith(("arxiv-nonexclusive", "owner-own-work"))
    assert entry["statement"] and "DRAFT" in entry["title"].upper()

db = "~/math-brain-build/local/population/brain.sqlite3"
conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
target = "math:probability.core:open-problem-p0117-absence-of-bi-infinite-geodesics-in-planar-iid-fpp"
count = sum(
    json.loads(meta).get("logical_id") == target
    for (meta,) in conn.execute(
        "SELECT metadata_json FROM nodes WHERE title=?",
        ("Open problem: Absence of bi-infinite geodesics in planar iid FPP",),
    )
)
assert count == 1, count
for rel in bundle["relations"]:
    assert rel["from_key"] in keys
    assert rel["to_existing_logical"] == target
    assert rel["kind"] == "semantic_association"

assert all(review["verdict"] in {"KEEP", "FIX", "DROP"} for review in reviews)
assert len(hooks) == 1
assert len(hooks[0]["text"]) <= 300
re.compile(hooks[0]["cue"])
print(json.dumps({"source_status": source["current_openness"], "claim_rows": len(claims), "review_rows": len(reviews), "keeps": sum(r["verdict"] == "KEEP" for r in reviews), "fixes": sum(r["verdict"] == "FIX" for r in reviews), "bundle_entries": len(bundle["entries"]), "bundle_relations": len(bundle["relations"]), "existing_target_matches": count, "hook_proposals": len(hooks)}, sort_keys=True))
