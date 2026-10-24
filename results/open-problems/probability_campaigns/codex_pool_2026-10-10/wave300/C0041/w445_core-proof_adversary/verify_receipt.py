"""Read-only verification of this worker's saved checks, draft and review receipts."""
from fractions import Fraction
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
checks = json.loads((root / "CHECK_RESULTS.json").read_text(encoding="utf-8"))
bundle = json.loads((root / "DRAFT_BUNDLE.json").read_text(encoding="utf-8"))
status = json.loads((root / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
assert checks["exact_arithmetic_passed"] == sum(checks["groups"].values()) == 144
assert checks["hook_semantic_controls_passed"] == 2
assert len(bundle["entries"]) == checks["draft_schema_entries"] == 7
assert len(bundle["relations"]) == checks["draft_relations"] == 5
keys = {entry["key"] for entry in bundle["entries"]}
assert len(keys) == 7
for entry in bundle["entries"]:
    assert entry["kind"] == "concept" and entry["proof_text"] is None
    assert entry["source"]["license"].startswith("owner-own-work")
    assert entry["statement"] and entry["assumptions"]
for relation in bundle["relations"]:
    assert relation["from_key"] in keys and relation["to_key"] in keys
    assert relation["kind"] in {"refutes", "semantic_association"}
assert status["current_openness"] == "UNKNOWN"
assert status["submitted"] and not any(status[k] for k in ("reviewed", "ingested", "retrievable"))
assert not status["formal_check"]["performed"]
assert json.loads(Path(status["draft_path"]).read_text(encoding="utf-8")) == bundle
for name, expected in json.loads((root / "EVIDENCE_HASHES.json").read_text(encoding="utf-8"))["sha256"].items():
    assert hashlib.sha256((root / name).read_bytes()).hexdigest() == expected, name
claims = [json.loads(line) for line in (root / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
assert len({claim["claim_id"] for claim in claims}) == len(claims) == 6
for claim in claims:
    assert all(k in claim for k in ("statement", "assumptions", "source", "proof_or_counterexample", "independent_reviewer", "remaining_gap", "status"))
    assert claim["status"] in {"conjecture", "numerical evidence", "sketch", "proved special case", "independently checked proof"}
assert 1-Fraction(63, 64)**64 > Fraction(1, 2)
assert checks["q_one_quarter_truncated_mean"] == {"K0": 4, "K16": 28}
print(json.dumps({"receipt_verification":"PASS", "saved_exact_controls":144,
                  "hook_semantic_controls":2, "draft_concepts":7, "relations":5,
                  "unique_claims":6, "full_target_proved":False,
                  "independent_review":"pending", "draft_path":status["draft_path"]}, indent=2))
