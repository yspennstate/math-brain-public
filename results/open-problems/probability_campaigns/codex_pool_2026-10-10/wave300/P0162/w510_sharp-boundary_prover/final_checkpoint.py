"""Save the independently reported verdict and finish the author handoff."""
import json
from pathlib import Path

root=Path(__file__).resolve().parent
audit="~/brain_workers/w511/AUDIT_W510.md"
claims=[]
for line in (root/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines():
    claim=json.loads(line)
    claim["status"]="independently checked proof"
    claim["scope"]="special case or counterexample to a stronger auxiliary bridge; not unrestricted FEI"
    claim["independent_reviewer"]={"agent":"w511","state":"KEEP","evidence":audit,"reported_at":"2026-10-10 05:35 UTC","account_separation":"not certified"}
    claim["primary_referee"]={"agent":"w512","state":"pending"}
    claim["remaining_gap"]=claim["remaining_gap"].replace("independent review pending","primary referee review pending")
    claims.append(claim)
(root/"CLAIMS.jsonl").write_text("".join(json.dumps(c,ensure_ascii=False)+"\n" for c in claims),encoding="utf-8")
states=json.loads((root/"BUNDLE_STATES.json").read_text(encoding="utf-8"))
states["reviewed"]={"state":"one independent mathematical KEEP; required further review pending","primary_referee":"w512","primary_referee_state":"pending","adversary":"w511","adversary_verdict":"KEEP C001-C004","adversary_evidence":audit,"two_account_keeps":"not certified"}
states["author_proof_only"]=False
(root/"BUNDLE_STATES.json").write_text(json.dumps(states,indent=2)+"\n",encoding="utf-8")
source=json.loads((root/"SOURCE_STATUS.json").read_text(encoding="utf-8"))
source["integration_state"]="DRAFT submitted; one independent KEEP from w511; w512 pending; ingestion and retrieval unverified"
source["independent_audit"]={"agent":"w511","verdict":"KEEP C001-C004","evidence":audit,"scope":"mathematical review of affine and entropy-boundary proofs; not a full FEI result"}
(root/"SOURCE_STATUS.json").write_text(json.dumps(source,indent=2)+"\n",encoding="utf-8")
verification=json.loads((root/"FINAL_VERIFICATION_STATE.json").read_text(encoding="utf-8"))
verification["mathematical_status"]="C001-C004 independently kept by w511; primary referee pending"
(root/"FINAL_VERIFICATION_STATE.json").write_text(json.dumps(verification,indent=2)+"\n",encoding="utf-8")
delivery=json.loads((root/"REVIEW_DELIVERY.json").read_text(encoding="utf-8"))
review_note="\nIndependent mathematical verdict received at 2026-10-10 05:35 UTC: w511 KEEP C001-C004, including fixed-r equality, r=0/1, conditioning mass, and spectral dependence. Evidence: "+audit+". This is one independent verdict; account separation and the required further keep are not certified. Referee routing receipt: "+delivery["state"]+".\n"
for name in ("ATTEMPT.md","REVIEW_PACKET.md"):
    with (root/name).open("a",encoding="utf-8") as f:
        f.write(review_note)
with (root/"REPORT.md").open("a",encoding="utf-8") as f:
    f.write(review_note+"\nProgress event logged through the expressly requested pd_progress.py --event command (no email). The normalization hook remains prepared locally for reviewer submission.\n")
for name in ("SOURCE_STATUS.json","BUNDLE_STATES.json","FINAL_VERIFICATION_STATE.json","DRAFT_BUNDLE.json"):
    json.loads((root/name).read_text(encoding="utf-8"))
required=["STATUS.md","SOURCE_STATUS.json","ATTEMPT.md","CLAIMS.jsonl","REVIEW_PACKET.md","REPORT.md","MEASUREMENTS.json","FINAL_VERIFICATION_STATE.json","DRAFT_BUNDLE.json","BUNDLE_STATES.json"]
assert all((root/name).is_file() for name in required)
with (root/"SOURCE_ROWS.jsonl").open("a",encoding="utf-8") as f:
    f.write(json.dumps({"row_id":"S1.P0162.w510.audit.001","type":"independent_mathematical_verdict","claims":[c["claim_id"] for c in claims],"verdict":"KEEP","reviewer":"w511","evidence":audit,"source_quote":"KEEP your affine C001-C004, including fixed-r equality, r=0/1, conditioning mass and dependent spectral coordinates","scope":"one independently reported mathematical verdict; no full FEI solution or two-account certification"})+"\n")
status="STATE: NEEDS_REVIEW\nNEXT: w512 audits the fixed-codimension equality and variance factor in C001-C004; rerun bounded verification when the corrected memory gate permits it.\n\n2026-10-10: Author task complete: exact target and prior digest, four boundary proofs, measurement receipts, and six-entry/five-relation DRAFT saved. Initial 182 exact checks passed in 0.438023 seconds with zero discrepancies; initial gate omission corrected; repeat DENIED at 92.1999% commit and 2.082 GB physical headroom. No further experiments run.\n2026-10-10: Statement delivered first to w511; w511 independently kept C001-C004 in AUDIT_W510.md. w512 mathematical review remains pending. Referee delivery: "+delivery["state"]+"; receipt REVIEW_DELIVERY.json.\n2026-10-10: DRAFT submitted at ~/math-brain-inbox/w510/bundle_001.json after exclusive output claim. No integrator run; ingestion/retrieval unverified; two-account keeps not certified. Progress event logged. Hook proposal prepared locally under worker write restrictions. General FEI remains unproved and current openness UNKNOWN; next research gap is a variance-weighted block spectral-entropy budget beyond affine spectra.\n"
(root/"STATUS.md").write_text(status,encoding="utf-8")
print(json.dumps({"state":"NEEDS_REVIEW","claims":len(claims),"w511_verdict":"KEEP","w512_review":"pending","referee_delivery":delivery["state"],"draft_entries":states["entries"],"draft_relations":states["relations"],"corrected_gate_rerun":"pending"}))
