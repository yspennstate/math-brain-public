"""Validate this review packet without touching the live math store."""

import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


root = Path(__file__).resolve().parent
draft_path = root / "bundle_001.json"
inbox_path = Path("~/math-brain-inbox/w437/bundle_001.json")
hook_path = Path("~/primary_directive/hooks1000/proposals/math-w437.jsonl")


def read_jsonl(name):
    return [json.loads(line) for line in (root / name).read_text(encoding="utf-8").splitlines() if line]


bundle = json.loads(draft_path.read_text(encoding="utf-8"))
submission = json.loads((root / "SUBMISSION.json").read_text(encoding="utf-8"))
source_status = json.loads((root / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
claims = read_jsonl("CLAIMS.jsonl")
verdicts = read_jsonl("VERDICTS.jsonl")
hook = read_jsonl("HOOK_PROPOSAL.jsonl")

assert bundle["spec"] == "mathbrain-draft-v1"
assert bundle["author_agent"] == "w437"
assert len(bundle["entries"]) <= 200
entry_keys = {entry["key"] for entry in bundle["entries"]}
assert len(entry_keys) == len(bundle["entries"])
required = {"key", "namespace", "logical_name", "kind", "title", "statement", "proof_text", "assumptions", "domain", "source"}
for entry in bundle["entries"]:
    assert required <= entry.keys()
    assert entry["kind"] in {"definition", "lemma", "theorem", "concept"}
    assert bool(entry["proof_text"]) == (entry["kind"] in {"lemma", "theorem"})
    assert entry["source"]["license"].startswith("owner-own-work")

relation_kinds = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
for relation in bundle["relations"]:
    assert relation["from_key"] in entry_keys
    assert relation["kind"] in relation_kinds
    assert (relation.get("to_key") in entry_keys) or relation.get("to_existing_logical")
    assert relation["rationale"]

assert inbox_path.read_bytes() == draft_path.read_bytes()
assert submission["submitted"]["value"] is True
assert submission["ingested"]["value"] is False
assert submission["retrievable"]["value"] is False
assert source_status["current_status"].startswith("CLAIMED SOLVED")
assert len({claim["id"] for claim in claims}) == len(claims)
assert all({"statement", "assumptions", "source", "proof_or_counterexample", "independent_reviewer", "remaining_gap", "status"} <= claim.keys() for claim in claims)

counts = Counter(row["verdict"] for row in verdicts)
assert counts == {"KEEP": 11, "DROP": 1, "FIX": 1}, counts
assert len(hook) == 1 and len(hook[0]["text"]) <= 300
assert hook_path.read_text(encoding="utf-8").splitlines().count((root / "HOOK_PROPOSAL.jsonl").read_text(encoding="utf-8").strip()) == 1

result = {
    "checked_at_utc": datetime.now(timezone.utc).isoformat(),
    "command": "python -X utf8 ~/brain_workers/w437/validate_deliverables.py",
    "bundle_entries": len(bundle["entries"]),
    "bundle_relations": len(bundle["relations"]),
    "claims": len(claims),
    "peer_verdicts": len(verdicts),
    "verdict_counts": dict(counts),
    "inbox_matches_local_bytes": True,
    "hook_submitted_once": True,
    "live_store_edited_by_validation": False,
}
(root / "VALIDATION.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
