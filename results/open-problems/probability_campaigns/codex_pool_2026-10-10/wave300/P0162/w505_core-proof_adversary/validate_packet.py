"""Validate final packet structure and the narrow sign correction; no shared writes."""
import json
import re
import time
from fractions import Fraction
from pathlib import Path
from verify_obstruction import family_values, split, walsh

root=Path(__file__).resolve().parent
started=time.monotonic()
statuses={"conjecture","numerical evidence","sketch","proved special case","independently checked proof"}
claims=[json.loads(s) for s in (root/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if s.strip()]
assert len({c["claim_id"] for c in claims})==len(claims)
assert all(c["status"] in statuses for c in claims)
assert all({"statement","assumptions","source","proof_or_counterexample","independent_reviewer","remaining_gap","status"} <= set(c) for c in claims)
review=json.loads((root/"INDEPENDENT_REVIEW.json").read_text(encoding="utf-8"))
assert review["receipt"]["verdict"]=="KEEP"
assert next(c for c in claims if c["claim_id"]=="w505-C003")["status"]=="independently checked proof"
checked=[c for c in claims if c["status"]=="independently checked proof"]
assert {c["claim_id"] for c in checked}=={"w505-C001","w505-C002","w505-C003","w505-C004","w505-C005"}
assert next(c for c in claims if c["claim_id"]=="w505-C006")["status"]=="conjecture"
update=json.loads((root/"INDEPENDENT_REVIEW_UPDATE.json").read_text(encoding="utf-8"))
assert len(update["receipts"])==6 and all(r["verdict"]=="KEEP" for r in update["receipts"])
bundle=json.loads((root/"DRAFT_BUNDLE_REVIEWED.json").read_text(encoding="utf-8"))
assert bundle["spec"]=="mathbrain-draft-v1" and bundle["author_agent"]=="w505"
assert len(bundle["entries"])==4 and len(bundle["relations"])==5
keys={e["key"] for e in bundle["entries"]}
required={"key","namespace","logical_name","kind","title","statement","proof_text","assumptions","domain","source"}
licenses=("cc-by-sa","cc-by","cc0","apache-2.0","gfdl","public-domain","mit","arxiv-nonexclusive","owner-own-work")
for e in bundle["entries"]:
    assert required <= set(e)
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*",e["logical_name"])
    assert e["source"]["license"].lower().startswith(licenses)
    if e["kind"] in {"lemma","theorem"}:
        assert e["proof_text"] and len(e["proof_text"])>100
        assert e["key"]=="coordinate-obstruction"
    else:
        assert e["kind"] in {"definition","concept"} and e["proof_text"] is None
allowed={"depends_on","defines","proves","refutes","generalizes","specializes","analogous_to","cites","semantic_association"}
known_targets={"math:probability.core:open-problem-p0162-fourier-entropy-versus-total-influence","math:probability.core:attempt-p0162-fourier-entropy-versus-total-influence"}
for r in bundle["relations"]:
    assert r["from_key"] in keys and r["kind"] in allowed
    assert (r.get("to_key") in keys) != (r.get("to_existing_logical") in known_targets)
state=json.loads((root/"BUNDLE_STATE.json").read_text(encoding="utf-8"))
assert state["submitted"] and state["live_store_written"] is False
assert json.loads(Path(state["latest_inbox_path"]).read_text(encoding="utf-8"))==bundle
assert state["ingestion_receipt"] is None and state["retrieval_receipt"] is None
assert state["promotion_hold"] and state["different_model_review_gate"]=="UNKNOWN"
assert next(e for e in bundle["entries"] if e["key"]=="missing-coordinate-input")["kind"]=="concept"
edges=[json.loads(s) for s in (root/"EDGE_EVIDENCE.jsonl").read_text(encoding="utf-8").splitlines() if s]
assert len(edges)==2 and all(e["from_statement_quote"] and e["to_statement_quote"] for e in edges)
hook=json.loads((root/"hook_proposals.jsonl").read_text(encoding="utf-8").strip())
assert len(hook["text"])<=300 and hook["fire_when"] and hook["silent_when"] and hook["evidence"]
# Fresh finite check gate: 20 seconds, only the four-point exceptional restriction.
_,_,full=family_values(1)
restriction=split(full,0)[0]
coeffs=walsh(restriction)
assert coeffs==[Fraction(1,2),Fraction(-1,2),Fraction(1,2),Fraction(1,2)]
assert time.monotonic()-started<20
source=json.loads((root/"SOURCE_STATUS.json").read_text(encoding="utf-8"))
assert source["primary_statement_verified"] and source["current_openness"]=="UNKNOWN"
audit=json.loads((root/"PEER_AUDIT.json").read_text(encoding="utf-8"))
assert "FIX" in audit["verdict"] and "KEEP" in audit["verdict"]
assert (root/audit["patch"]).read_text(encoding="utf-8").startswith("--- a/~/brain_workers/w504/PROOF.md")
result={"passed":True,"claims":len(claims),"independently_kept_claims":len(checked),"bundle_entries":4,"bundle_relations":5,"quoted_relation_rows":2,"signed_boundary_control":"+1/2,-1/2,+1/2,+1/2 confirmed from exact Walsh transform","seconds":time.monotonic()-started,"scope":"Packet/schema validation plus a finite sign check; not a mathematical proof or model/live integration receipt."}
(root/"PACKET_VALIDATION.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
metrics=json.loads((root/"measurements.json").read_text(encoding="utf-8"))
report=f'''# w505 P0162 report

Found an explicit Boolean counterexample to a universal restriction-deficit bound for every coordinate. Referee w506 independently re-derived it and filed KEEP, receipt P0162-REVIEW-W505-004. This is a check of a proof input; full FEI and the suitable-coordinate premise remain unproved. Current global openness is UNKNOWN; no novelty claim is made.

The exact statement and original source pointer are recovered in SOURCE_STATUS.json: O'Donnell, arXiv:1204.6447, printed p.5. The original P0162 card and its failed singleton-spectrum attempt were retrieved read-only; relevant owner FEI memories and two recent primary papers were checked for scope.

For F_m(u,v,y)=(-1)^(u dot v)-(1-y)1{{u=v=0}}, I_y=2^(-2m) and Delta_y/I_y>=log_2((2^m-1)^2+1). The measured ratio rises from 4.8676687468 at m=1 to 20.3280154117 at m=8. The entire displayed family also has H/I<=2, now explicitly kept by w506. C001-C005 have separate scoped KEEPs in INDEPENDENT_REVIEW_UPDATE.json. C006 retains status conjecture: only the conditional induction was checked. The remaining hardest input is a uniform suitable-coordinate bound when every influence is below 1/16.

w504's core proof was audited after the independent derivation was saved. Its exact entropy identity, conditional reduction, and base-coordinate family bound check out. The audit found two wrong literal control-block signs; the correct nonzero coefficients are -2t,+2t,+2t. w504's current proof has the corrected phase and w506 records a corrected draft. The historical patch remains audit evidence; do not reapply it to corrected text.

Validation commands:

- python -X utf8 -B ~/brain_workers/w505/verify_obstruction.py --gate cpu20s-n9
- python -X utf8 -B ~/brain_workers/w505/validate_packet.py

The final mathematical check passed in {metrics['seconds']:.6f}s within its fresh 20-second gate: four exact family truth tables, 276 Boolean functions through dimension three, independent direct character sums for m<=3, and the base-coordinate formula on 20 restrictions. Packet validation passed with {len(claims)} result rows, four entries, five relations, and two relation rows quoting both supporting ends. No formal proof-assistant check was claimed.

The latest DRAFT is {state['latest_inbox_path']}. It has one independently kept lemma, one definition, and two concepts. The earlier drafts are retained; the coordinator should validate this latest revision. Submitted, scoped mathematical review, full-bundle review, ingestion, and retrieval states are separate in BUNDLE_STATE.json. No ingestion or retrieval receipt is available.

Apply: codex-01a12190 validates bundle_003.json and the scoped referee receipts; live promotion waits for the corresponding model-review gates. MODEL_EVIDENCE.json records author and referee served models as UNKNOWN, because no response-side evidence was supplied. INTEGRATION_HANDOFF.json provides exact artifact paths and file SHA-256 hashes. Hashes establish identity only. No peer/live proof or math store was changed; no services or agents were started. Global hook/progress requests remain staged in the worker folder.

Main risk: promoting the family result or conditional reduction to a universal theorem, or treating a finite numerical run or source hash as a proof. The peer packet leaves the missing input explicit. The staged hook targets that precise quantifier mistake.

NEXT: Attempt the positive-influence suitable-coordinate inequality for arbitrary Boolean spectra with max_i Inf_i<1/16; retain the unproved input label.
'''
(root/"REPORT.md").write_text(report,encoding="utf-8")
print(json.dumps(result))
