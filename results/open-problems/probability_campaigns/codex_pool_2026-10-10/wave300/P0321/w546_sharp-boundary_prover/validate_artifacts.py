"""Read-only draft consistency checks, with a local validation receipt."""
import json
import re
from pathlib import Path
from datetime import datetime, timezone
root=Path(__file__).resolve().parent
bundle=json.loads((root/"DRAFT_BUNDLE.json").read_text(encoding="utf-8"))
inbox=Path("~/math-brain-inbox/w546/bundle_001.json")
assert inbox.exists(), "If coordinator moved the draft, inspect its receipt; never recreate it"
assert bundle==json.loads(inbox.read_text(encoding="utf-8"))
claims=[json.loads(line) for line in (root/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
assert len(claims)==5 and len({c["claim_id"] for c in claims})==5
required_claim={"claim_id","exact_statement","assumptions","source","proof_or_counterexample","independent_reviewer","remaining_gap","status"}
for claim in claims:
    assert required_claim<=claim.keys() and claim["remaining_gap"]
    assert claim["status"] in {"conjecture","numerical evidence","sketch","proved special case","independently checked proof"}
    assert (root/claim["source"]["artifact"]).exists()
for filename in ("STATUS.md","SOURCE_STATUS.json","ATTEMPT.md","REPORT.md","REVIEW_PACKET.md","BRAIN_STATE.json"):
    assert (root/filename).exists()
for filename in ("VERIFICATION.json","VERIFICATION_SMOOTH.json"):
    assert json.loads((root/filename).read_text())["status"]=="PASS"
keys={entry["key"] for entry in bundle["entries"]}
assert len(keys)==len(bundle["entries"])==5
for entry in bundle["entries"]:
    assert entry["kind"] in {"concept","definition"} and entry["proof_text"] is None
    assert entry["source"]["license"].startswith("owner-own-work")
    assert re.fullmatch(r"[a-z][a-z0-9]*(?:\.[a-z][a-z0-9]*)*",entry["namespace"])
    assert re.fullmatch(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*",entry["logical_name"])
    assert entry["statement"] and entry["assumptions"]
graph={key:[] for key in keys}
allowed={"depends_on","defines","proves","refutes","generalizes","specializes","analogous_to","cites","semantic_association"}
for relation in bundle["relations"]:
    assert relation["from_key"] in keys and relation["kind"] in allowed
    assert relation["rationale"]
    if "to_key" in relation:
        assert relation["to_key"] in keys
    else:
        assert relation["to_existing_logical"]=="math:probability.core:open-problem-p0321-existence-of-a-hexatic-phase-for-two-dimensional-riesz-gases"
    if relation["kind"]=="depends_on":
        graph[relation["from_key"]].append(relation["to_key"])
active,done=set(),set()
def visit(key):
    assert key not in active, "dependency cycle"
    if key in done: return
    active.add(key)
    for child in graph[key]: visit(child)
    active.remove(key); done.add(key)
for key in keys: visit(key)
hook=json.loads((root/"HOOK_PROPOSAL.jsonl").read_text())
assert len(hook["text"])<=300 and hook["fire_when"] and hook["silent_when"] and hook["evidence"]
receipt={"status":"PASS","checked_at":datetime.now(timezone.utc).isoformat(),"command":"python -X utf8 validate_artifacts.py","claim_rows":len(claims),"draft_entries":len(keys),"supported_relations":len(bundle["relations"]),"dependency_dag":"PASS","worker_and_inbox_drafts_equal":True,"numerical_receipts":"both PASS","scope":"format, evidence paths, and draft consistency; not a mathematical referee verdict"}
(root/"VALIDATION_RECEIPT.json").write_text(json.dumps(receipt,indent=2),encoding="utf-8")
print(json.dumps(receipt,indent=2))
