"""Structural/reproducibility checks only; does not certify mathematics."""
import ast
import hashlib
import json
from pathlib import Path

root=Path(__file__).resolve().parent
required=["STATUS.md","SOURCE_STATUS.json","ATTEMPT.md","CLAIMS.jsonl","REPORT.md","REVIEW_PACKET.md","BRAIN_COMPARISON.md","AUDIT_W561.md","draft_bundle_001.json","EDGE_AUDIT.jsonl","BUNDLE_RECEIPT.json","MODEL_PROVENANCE.json"]
for name in required:assert (root/name).is_file(),name
claims=[json.loads(line)for line in (root/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines()if line.strip()]
assert len(claims)==len({row["claim_id"]for row in claims})==5
for claim in claims:
    assert all(field in claim for field in ("statement","assumptions","source","proof_or_counterexample","independent_reviewer","remaining_gap","status"))
for measurement in ("fallback_measurement.json","overlap_measurement.json","pivotal_measurement.json"):
    assert json.loads((root/measurement).read_text(encoding="utf-8"))["all_checks_passed"]
bundle=json.loads((root/"draft_bundle_001.json").read_text(encoding="utf-8"))
assert len(bundle["entries"])==4 and len(bundle["relations"])==5
assert all(e["kind"]=="concept"and e["proof_text"]is None for e in bundle["entries"])
edges=[json.loads(line)for line in (root/"EDGE_AUDIT.jsonl").read_text(encoding="utf-8").splitlines()if line.strip()]
assert len(edges)==5 and all(e["from_quote"]and e["to_quote"]for e in edges)
receipt=json.loads((root/"BUNDLE_RECEIPT.json").read_text(encoding="utf-8"))
assert receipt["submitted"] and not receipt["ingested"]and not receipt["retrievable"]and not receipt["live_store_changed"]
assert Path(receipt["submitted_path"]).read_bytes()==(root/"draft_bundle_001.json").read_bytes()
for name,digest in json.loads((root/"ARTIFACT_HASHES.json").read_text(encoding="utf-8")).items():
    assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,name
source=root/"proposed/math_brain/target_fallback.py"
ast.parse(source.read_text(encoding="utf-8"))
patch=(root/"patches/01_candidate_target_fallback.diff").read_text(encoding="utf-8")
assert patch.startswith("--- a/~/math-brain-build/src/math_brain/target_fallback.py\n+++ b/~/math-brain-build/src/math_brain/target_fallback.py\n")
assert not Path("~/math-brain-build/src/math_brain/target_fallback.py").exists(),"Review required: proposed destination now exists"
assert json.loads((root/"SOURCE_STATUS.json").read_text(encoding="utf-8"))["current_openness"]=="UNKNOWN"
assert json.loads((root/"MODEL_PROVENANCE.json").read_text(encoding="utf-8"))["served_model"]=="UNKNOWN"
result={"all_checks_passed":True,"claim_rows":len(claims),"scoped_audit_rows":1,"draft_concepts":len(bundle["entries"]),"supported_relations":len(edges),"inbox_matches_local":True,"live_module_absent":True,"scope":"Structural, evidence hash and prior measured-check validation; not mathematical proof, integration or serving validation."}
(root/"PACKET_VALIDATION.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
