import json
from pathlib import Path

root = Path(__file__).resolve().parent
claims = [json.loads(line) for line in (root / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
source = json.loads((root / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
draft = json.loads((root / "draft_bundles" / "bundle_001.json").read_text(encoding="utf-8"))
hooks = [json.loads(line) for line in (root / "hook_proposals" / "math-w392.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]

assert source["target_id"] == "P0117"
assert source["recent_primary_claim"]["status"] == "CLAIMED_RESOLUTION_UNAUDITED"
assert len({row["id"] for row in claims}) == len(claims)
assert all({"statement", "assumptions", "source", "independent_reviewer", "remaining_gap", "status"} <= row.keys() for row in claims)
assert draft["spec"] == "mathbrain-draft-v1"
assert len(draft["entries"]) <= 200
keys = {entry["key"] for entry in draft["entries"]}
assert len(keys) == len(draft["entries"])
assert all(entry["kind"] == "concept" and entry["proof_text"] is None for entry in draft["entries"])
assert all(entry["source"]["license"].startswith("owner-own-work") for entry in draft["entries"])
assert all(rel["from_key"] in keys and rel["kind"] == "semantic_association" for rel in draft["relations"])
assert all(rel["to_existing_logical"] == "math:probability.core:open-problem-p0117-absence-of-bi-infinite-geodesics-in-planar-iid-fpp" for rel in draft["relations"])
assert all({"id", "area", "event", "cue", "fire_when", "silent_when", "text", "evidence", "proposer"} <= hook.keys() and len(hook["text"]) <= 300 for hook in hooks)
print(json.dumps({"claim_rows": len(claims), "kept_peer_rows": sum(row.get("verdict") == "KEEP" for row in claims), "draft_entries": len(draft["entries"]), "draft_relations": len(draft["relations"]), "hook_proposals": len(hooks)}))
