"""Validate this small draft locally; optionally publish only to the named inbox."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re

parser = argparse.ArgumentParser()
parser.add_argument("--submit", action="store_true")
args = parser.parse_args()
ROOT = Path(__file__).resolve().parent
draft_path = ROOT / "drafts" / "bundle_001.json"
draft = json.loads(draft_path.read_text(encoding="utf-8"))
assert draft["spec"] == "mathbrain-draft-v1" and draft["author_agent"] == "w433"
assert 0 < len(draft["entries"]) <= 200
keys = set()
names = set()
required = {"key", "namespace", "logical_name", "kind", "title", "statement", "proof_text", "assumptions", "domain", "source"}
for entry in draft["entries"]:
    assert required <= entry.keys()
    assert entry["key"] not in keys
    keys.add(entry["key"])
    name = (entry["namespace"], entry["logical_name"])
    assert name not in names
    names.add(name)
    assert re.fullmatch(r"[a-z][a-z0-9-]*(\.[a-z][a-z0-9-]*)+", entry["namespace"])
    assert re.fullmatch(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*", entry["logical_name"])
    assert entry["kind"] == "concept" and entry["proof_text"] is None
    assert entry["title"].startswith("DRAFT:")
    assert "referee review pending" in entry["statement"]
    assert isinstance(entry["assumptions"], list) and entry["assumptions"]
    source = entry["source"]
    assert {"source_id", "url", "revision", "license", "excerpt"} <= source.keys()
    assert source["license"].startswith("owner-own-work")
    assert source["url"].startswith("file:///~/brain_workers/w433/")
allowed = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
dependencies = {key: [] for key in keys}
for relation in draft["relations"]:
    assert relation["from_key"] in keys and relation["to_key"] in keys
    assert relation["kind"] in allowed and relation["rationale"]
    if relation["kind"] == "depends_on":
        dependencies[relation["from_key"]].append(relation["to_key"])
def walk(key, active, finished):
    assert key not in active
    if key in finished:
        return
    for next_key in dependencies[key]:
        walk(next_key, active | {key}, finished)
    finished.add(key)
finished = set()
for key in keys:
    walk(key, set(), finished)
claims = [json.loads(line) for line in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
assert len(claims) == len({claim["id"] for claim in claims}) == 8
statuses = {"conjecture", "numerical evidence", "sketch", "proved special case", "independently checked proof"}
for claim in claims:
    assert {"exact_statement", "assumptions", "source", "proof_or_counterexample", "independent_reviewer", "remaining_gap", "status"} <= claim.keys()
    assert claim["status"] in statuses and claim["remaining_gap"]
measurements = json.loads((ROOT / "MEASUREMENTS.json").read_text(encoding="utf-8"))
assert measurements["status"] == "PASS" and measurements["enumerated_states_total"] == 626
formal = json.loads((ROOT / "FORMAL_CHECK_RECEIPT.json").read_text(encoding="utf-8"))
assert not formal["mathematical_proof_certified"] and formal["kernel_verification"] == "NOT_RUN"
hook = json.loads((ROOT / "HOOK_PROPOSAL.jsonl").read_text(encoding="utf-8"))
assert len(hook["text"]) <= 300 and hook["fire_when"] and hook["silent_when"] and hook["evidence"]
receipt = {
    "status": "PASS", "validator_scope": "local draft structure and evidence consistency only, not mathematics or live integrator acceptance",
    "command": "python -X utf8 ~/brain_workers/w433/validate_and_submit.py" + (" --submit" if args.submit else ""),
    "entries": len(draft["entries"]), "relations": len(draft["relations"]), "claim_rows": len(claims),
    "all_entries_concepts": True, "theorem_promotions": 0, "dependency_graph_acyclic": True,
    "relation_ends_present": True, "exact_controls_pass": True,
    "submitted": False
}
if args.submit:
    delivery = json.loads((ROOT / "BRAIN_DELIVERY_STATUS.json").read_text(encoding="utf-8"))
    assert delivery["claim_id"] == "clm-619fd2ede2"
    inbox = Path("~/math-brain-inbox/w433").resolve()
    destination = inbox / "bundle_001.json"
    part = inbox / "bundle_001.part"
    assert destination.parent.resolve() == inbox and part.parent.resolve() == inbox
    inbox.mkdir(exist_ok=True)
    if destination.exists():
        assert json.loads(destination.read_text(encoding="utf-8")) == draft, "Existing inbox artifact differs; do not overwrite."
        receipt["atomic_write"] = "existing identical file; no replacement"
    else:
        assert not part.exists(), "Existing partial artifact; inspect rather than overwrite."
        part.write_text(json.dumps(draft, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        assert json.loads(part.read_text(encoding="utf-8")) == draft
        part.rename(destination)
        receipt["atomic_write"] = ".part completed and renamed to .json"
    receipt["submitted"] = True
    receipt["destination"] = str(destination)
    receipt["submitted_at_utc"] = datetime.now(timezone.utc).isoformat()
    delivery.update({
        "submitted": True, "submitted_path": str(destination), "submitted_at_utc": receipt["submitted_at_utc"],
        "reviewed": "PENDING: w434 independent check", "ingested": "NOT_VERIFIED: coordinator receipt absent",
        "retrievable": "NOT_VERIFIED: no store query confirming these entries",
        "notes": "Source/hash and local structural checks do not certify mathematics. Submission is separate from review, ingestion and retrieval."
    })
    (ROOT / "BRAIN_DELIVERY_STATUS.json").write_text(json.dumps(delivery, indent=2) + "\n", encoding="utf-8")
(ROOT / "DRAFT_VALIDATION.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, indent=2))
