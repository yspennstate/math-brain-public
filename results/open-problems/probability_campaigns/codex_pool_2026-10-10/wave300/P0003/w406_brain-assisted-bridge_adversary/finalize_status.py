"""Validate artifact structure and write the exact restart/review state without a BOM."""
import json
import pathlib

root=pathlib.Path(__file__).resolve().parent
required=["STATUS.md","SOURCE_STATUS.json","ATTEMPT.md","CLAIMS.jsonl","REPORT.md","REVIEW_PACKET.md","INDEPENDENT_OBSTRUCTION.md","ENSEMBLE_GAP.md","AUDIT_w405.md","EDGES.jsonl","BOUNDED_REPAIR.json","BUNDLE_STATUS.json","recall_evidence.json","bridge_retrieval.json","narrow_source_lookup.json","compute_gate_receipt.json","compute_gate_receipt_first.json","verify_cycle_modes.py","run_bounded_checks.py","patches/01_p0003_bridge_requirements.diff","drafts/bundle_001.json"]
for name in required:
    assert (root/name).is_file() and (root/name).stat().st_size>0, name
claims=[json.loads(line) for line in (root/"CLAIMS.jsonl").read_text(encoding="utf-8-sig").splitlines() if line.strip()]
assert len(claims)==7 and len({c["id"] for c in claims})==7
for claim in claims:
    assert all(key in claim for key in ("statement","assumptions","source","proof_or_counterexample","independent_reviewer","remaining_gap","status")),claim["id"]
bundle=json.loads((root/"drafts/bundle_001.json").read_text(encoding="utf-8"))
assert bundle["spec"]=="mathbrain-draft-v1" and len(bundle["entries"])==5 and len(bundle["relations"])==4
keys={entry["key"] for entry in bundle["entries"]}
for entry in bundle["entries"]:
    assert entry["kind"] in ("concept","definition") and entry["proof_text"] is None
for relation in bundle["relations"]:
    assert relation["from_key"] in keys
    assert relation["to_key"] in keys if "to_key" in relation else bool(relation.get("to_existing_logical"))
gate=json.loads((root/"compute_gate_receipt.json").read_text(encoding="utf-8"))
validation={"required_artifacts_present":len(required),"claims_parse_and_required_fields":len(claims),"draft_entries":5,"draft_relations":4,"structural_validation":"passed","mathematical_independent_review":"pending w407","exact_checker":"passed" if gate.get("checker_status")=="passed" else "not run; held by fresh gate","formal_kernel_receipt":False,"scope":"Artifact/schema validation only; not mathematical proof or an integrator receipt"}
(root/"VALIDATION.json").write_text(json.dumps(validation,indent=2)+"\n",encoding="utf-8")
path=root/"STATUS.md"
lines=path.read_text(encoding="utf-8-sig").splitlines()
assert lines[0] in ("STATE: WORKING","STATE: NEEDS_REVIEW"),lines[0]
lines[0]="STATE: NEEDS_REVIEW"
lines[1]="NEXT: Independently verify the cycle-space proof and C6 ensemble counterexample in REVIEW_PACKET.md, then specify the required fixed-n length/endpoint-conditioning transfer."
for message in (
    "2026-10-10: Submitted five DRAFT entries/four exact edges and one unactivated hook; seven claim rows, source status, report, review packet and proposed metadata diff complete. Artifact/schema validation passed; independent review/ingestion/retrievability unconfirmed.",
    "2026-10-10 STUCK: Exact checker held by two fresh physical-headroom gates (2996 MB then 2782 MB <4096 MB); runnable checker and receipts retained, algebraic proof/audit completed. No numerical pass or formal proof receipt claimed. Both direct referee messages failed (w407 unregistered); durable worker-folder handoff is ready.",
):
    if message not in lines: lines.append(message)
path.write_text("\n".join(lines)+"\n",encoding="utf-8")
assert path.read_bytes().splitlines()[0]==b"STATE: NEEDS_REVIEW"
assert path.read_text(encoding="utf-8").splitlines()[1].startswith("NEXT: ")
print(json.dumps({"state":"NEEDS_REVIEW","validation":validation}))
