"""Record received mathematical verdicts without re-auditing or promoting the live store."""
from datetime import datetime, timezone
import json
from pathlib import Path

root=Path(__file__).resolve().parents[1]
verdict_path=Path("~/brain_workers/w539/review/W537_VERDICTS.jsonl")
verdicts=[json.loads(line) for line in verdict_path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
by_claim={row["peer_claim"]:row for row in verdicts}
claims=[json.loads(line) for line in (root/"CLAIMS.jsonl").read_text(encoding="utf-8-sig").splitlines() if line.strip()]
for claim in claims:
    row=by_claim[claim["id"]]
    assert row["reviewer"]=="w539" and row["verdict"].startswith("KEEP")
    claim["independent_reviewer"]={"assigned":"w539","status":"scoped_keep","verdict":row["verdict"],"evidence":str(verdict_path),"served_model_gate":"UNKNOWN"}
    claim["additional_review"]={"reviewer":"w538","verdict":"KEEP under written assumptions","evidence":"~/brain_workers/w538/PAIRED_AUDIT.md","independence_note":"C5 separate derivation followed reading the paired proof; no blind-check claim"}
    claim["remaining_gap"]=row["unresolved_gap"]
    claim["status"]="independently checked proof"
    if claim["id"]=="w537-C3":
        claim["assumptions"].append("C is a bounded fundamental cell, such as a parallelepiped")
        claim["exact_statement"]=claim["exact_statement"].replace("tiled by K_N cells C","tiled by K_N bounded fundamental cells C")
(root/"CLAIMS.jsonl").write_text("".join(json.dumps(row,ensure_ascii=False)+"\n" for row in claims),encoding="utf-8")
(root/"review/SCOPED_KEEP_RECEIPTS.jsonl").write_text("".join(json.dumps(row,ensure_ascii=False)+"\n" for row in verdicts),encoding="utf-8")
attempt=(root/"ATTEMPT.md").read_text(encoding="utf-8")
attempt=attempt.replace("Mathematical review pending with w539.","w539 independently kept C1-C5 within their stated assumptions; received verdicts are in review/SCOPED_KEEP_RECEIPTS.jsonl. Different-model evidence and integration gates remain pending.",1)
attempt=attempt.replace("Let finite tori be tiled by K_N fundamental cells C+gamma", "Let finite tori be tiled by K_N bounded fundamental cells C+gamma",1)
(root/"ATTEMPT.md").write_text(attempt,encoding="utf-8")
source=json.loads((root/"SOURCE_STATUS.json").read_text(encoding="utf-8-sig"))
source["review_status"]="w539 KEEP C1-C5 under stated hypotheses; no complete target proof"
source["mathematical_review_receipt"]=str(verdict_path)
source["different_model_evidence"]="UNKNOWN"
(root/"SOURCE_STATUS.json").write_text(json.dumps(source,indent=2),encoding="utf-8")
state=json.loads((root/"BUNDLE_STATUS.json").read_text(encoding="utf-8"))
assert state["submitted"]
state.update({"reviewed":True,"review_scope":"Author proofs C1-C5 kept by w539; not an independent audit of every bundle edge or served-model gate","review_state":"scoped mathematical KEEP; source/model/edge integration gates pending","review_receipt":str(verdict_path),"bundle_edge_audit_completed":False,"different_model_gate":"UNKNOWN","ingested":False,"retrievable":False,"submitted_payload_note":"Concept-only draft was submitted before receipt registration; no submitted artifact overwritten."})
(root/"BUNDLE_STATUS.json").write_text(json.dumps(state,indent=2),encoding="utf-8")
report=(root/"REPORT.md").read_text(encoding="utf-8")
report=report.replace("Saved five proved-special-case claims, their author proofs", "Saved five independently kept special-case claims and their author proofs",1)
report=report.replace("Independent review is pending with w539;", "w539 independently kept C1-C5 under their stated assumptions; w538 also kept the reductions. Referee receipts are in review/SCOPED_KEEP_RECEIPTS.jsonl. Source/model/edge integration gates remain pending;",1)
report=report.replace("The proposed repair is limited to P0309,", "Risks: the two hardcoded titles can drift; the SQLite progress bound does not bound OS I/O stalls. The proposed repair is limited to P0309,",1)
report=report.replace("NEXT: w539 audits C1-C5, especially C5's circular tail bound; the next proof step is to establish a full-law Bragg lower bound or subexponential crystalline Fourier-event mass for the specified 3D Riesz model.", "NEXT: For s=1, compare the unrestricted neutral periodic Coulomb partition function with a fixed nonzero Fourier-response sector and prove its log-probability cost is o(N) at a fixed finite beta.")
report+="\nSubmitted concept-only draft: ~/math-brain-inbox/w537/bundle_001.json. Submitted=true; mathematical claims reviewed=true; bundle-edge/model gates pending; ingested=false; new draft retrievable=false. C3's bounded-cell hypothesis is now explicit in ATTEMPT.md and CLAIMS.jsonl and was already explicit in the submitted standalone card.\n"
(root/"REPORT.md").write_text(report,encoding="utf-8")
(root/"review/FINAL_HANDOFF.md").write_text("P0309 parent unproved, current openness UNKNOWN. w539 kept C1-C5 under explicit assumptions; exact receipts: review/SCOPED_KEEP_RECEIPTS.jsonl. Main distinct result: full-law circular Bragg liminf >=b^2 implies pressure right slope >=b. No unrestricted Riesz moment bound or full-rank crystal identification is supplied. Submitted concept draft: ~/math-brain-inbox/w537/bundle_001.json. Optional manual read-only repair: patches/01_p0309_target_lookup.diff, measured 2/2 exact cards in 0.068 s on one replay versus 0/3 topical general-recall hits in 51.943 s; scopes differ. No live recall change or ingestion. Served-model evidence UNKNOWN for author/referee. Numerical surrogate checks denied by fresh process_critical gate; 0 ran. Local hook drafts: HOOK_PROPOSALS.jsonl for authorized filing.\nNEXT: For s=1, prove o(N) probability cost of a nonzero Fourier-response sector under the unrestricted neutral periodic Coulomb Gibbs law at fixed finite beta.\n",encoding="utf-8")
print(json.dumps({"scoped_keep_claims":len(claims),"referee":"w539","submitted":state["submitted"],"ingested":False,"retrievable":False,"parent_proved":False}))
