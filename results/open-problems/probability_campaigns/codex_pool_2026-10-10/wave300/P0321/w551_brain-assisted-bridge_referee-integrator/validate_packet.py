"""Validate draft structure and saved referee rows without mutating the store."""
import json
from pathlib import Path
import re

HERE = Path(__file__).parent
BUNDLE_DIR = Path("~/math-brain-inbox/w551")
BUNDLE = BUNDLE_DIR / "bundle_001.json"
if not BUNDLE.exists():
    BUNDLE = BUNDLE_DIR / "bundle_001.part"
data = json.loads(BUNDLE.read_text(encoding="utf-8"))
assert data["spec"] == "mathbrain-draft-v1"
assert data["author_agent"] == "w551"
assert 0 < len(data["entries"]) <= 200
keys = set()
for entry in data["entries"]:
    assert entry["key"] not in keys
    keys.add(entry["key"])
    assert re.fullmatch(r"[a-z]+(?:\.[a-z]+)+", entry["namespace"])
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", entry["logical_name"])
    assert entry["kind"] in {"definition", "lemma", "theorem", "concept"}
    assert entry["statement"] and entry["title"] and isinstance(entry["assumptions"], list)
    if entry["kind"] in {"lemma", "theorem"}:
        assert entry["proof_text"]
    else:
        assert entry["proof_text"] is None
    source = entry["source"]
    assert all(source[k] for k in ("source_id", "url", "revision", "license"))
    assert source["license"].startswith(("owner-own-work", "arxiv-nonexclusive"))
for relation in data["relations"]:
    assert relation["from_key"] in keys
    assert (relation.get("to_key") in keys) ^ bool(relation.get("to_existing_logical"))
    assert relation["kind"] in {"depends_on", "defines", "proves", "refutes", "generalizes",
                                "specializes", "analogous_to", "cites", "semantic_association"}
    assert relation["rationale"]
claims = [json.loads(line) for line in (HERE / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line]
assert len({c["id"] for c in claims}) == len(claims)
for claim in claims:
    assert all(k in claim for k in ("statement", "assumptions", "source", "proof_or_counterexample",
                                    "independent_reviewer", "remaining_gap", "status"))
assert json.loads((HERE / "SOURCE_STATUS.json").read_text(encoding="utf-8"))["current_openness"] == "UNKNOWN"
result = {"bundle_json_valid": True, "entries": len(data["entries"]),
          "relations": len(data["relations"]), "claim_rows_valid": len(claims),
          "source_current_openness": "UNKNOWN", "live_store_mutated": False}
(HERE / "VALIDATION.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps(result))
