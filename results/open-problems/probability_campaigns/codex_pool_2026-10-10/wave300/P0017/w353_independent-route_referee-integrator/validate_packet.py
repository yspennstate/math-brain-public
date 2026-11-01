"""Read-only structural check for the local P0017 handoff."""
from __future__ import annotations

import json
import re
from pathlib import Path

root = Path(__file__).resolve().parent
claims = [json.loads(line) for line in (root / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
assert len({row["id"] for row in claims}) == len(claims)
required_claim = {"id", "target", "statement", "assumptions", "source", "proof_or_counterexample", "independent_reviewer", "remaining_gap", "status", "verdict"}
assert all(required_claim <= row.keys() and row["target"] == "P0017" for row in claims)

status = json.loads((root / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
measure = json.loads((root / "MEASUREMENTS.json").read_text(encoding="utf-8"))
bundle = json.loads((root / "bundle_001.json").read_text(encoding="utf-8"))
assert status["current_openness"] == "UNKNOWN"
assert not any(paper["full_proof_independently_checked"] for paper in status["primary_literature"])
assert measure["fresh_host_gate_passed"] and measure["accepted"]
assert bundle["spec"] == "mathbrain-draft-v1" and bundle["author_agent"] == "w353"
entries = bundle["entries"]
keys = {entry["key"] for entry in entries}
assert len(keys) == len(entries) and len(entries) <= 200
required_entry = {"key", "namespace", "logical_name", "kind", "title", "statement", "proof_text", "assumptions", "domain", "source"}
required_source = {"source_id", "url", "revision", "license", "excerpt"}
identifier = re.compile(r"[a-z0-9][a-z0-9._/-]{0,255}\Z")
for entry in entries:
    assert required_entry <= entry.keys()
    assert required_source <= entry["source"].keys()
    assert identifier.fullmatch(entry["namespace"]) and identifier.fullmatch(entry["logical_name"])
    assert entry["kind"] == "concept" and entry["proof_text"] is None
    assert all(isinstance(entry["source"][name], str) and entry["source"][name].strip() for name in ("source_id", "url", "revision", "license"))
    assert entry["source"]["license"].startswith(("arxiv-nonexclusive", "owner-own-work"))
for relation in bundle["relations"]:
    assert relation["from_key"] in keys
    assert relation["kind"] in {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
    assert ("to_key" in relation) != ("to_existing_logical" in relation)
    if "to_key" in relation:
        assert relation["to_key"] in keys
print(json.dumps({"claims":len(claims),"draft_entries":len(entries),"draft_relations":len(bundle["relations"]),"current_openness":status["current_openness"],"measurement_gate":measure["gate"]["decision"],"max_quadrature_relative_error":measure["max_peer_relative_error"]}))
