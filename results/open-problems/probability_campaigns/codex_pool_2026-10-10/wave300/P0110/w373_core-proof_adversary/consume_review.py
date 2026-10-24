"""Consume the named referee's recorded verdicts; do not re-audit a review."""
from pathlib import Path
import difflib
import hashlib
import json

root=Path(__file__).resolve().parent
review_path=Path("~/brain_workers/w374/REVIEW_PACKET.md")
data=review_path.read_bytes()
review=data.decode("utf-8-sig")
kept={
    "S1.w373.001":"| w373 `CLAIMS.jsonl`, `S1.w373.001` | KEEP |",
    "S1.w373.002":"| w373 `INDEPENDENT.md`, rare-event family | KEEP |",
    "S1.w373.003":"| w373 `ATTEMPT.md`, geodesic-selection example | KEEP |",
    "S1.w373.004":"| w372 `S1.w372.L1-short`; w373 small-endpoint obstruction | KEEP |",
    "S1.w373.005":"| w372 `S1.w372.CEX`; w373 high-probability agreement example | KEEP |",
    "S1.w373.007":"| w372 `S1.w372.L2` | KEEP |"
}
for cid,anchor in kept.items():
    if anchor not in review:
        raise RuntimeError("Missing exact referee row: "+cid)
if "| w372 `S1.w372.L4` | KEEP conditional |" not in review:
    raise RuntimeError("Missing localization verdict")
receipt={"reviewer":"w374","verdict_file":str(review_path),"sha256":hashlib.sha256(data).hexdigest(),
         "hash_is_proof":False,"consumed_keeps":list(kept),"still_pending":["S1.w373.006","S1.w373.008"],
         "scope":"Consumed explicit referee mathematical reproductions and KEEP rows; no review of a review. Full P0110 input remains unproved.",
         "verdict_rows":[line for line in review.splitlines() if any(anchor in line for anchor in kept.values()) or "| w372 `S1.w372.L4` | KEEP conditional |" in line]}
(root/"REFEREE_RECEIPT.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding="utf-8")
rows=[json.loads(x) for x in (root/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
for row in rows:
    if row["claim_id"] in kept:
        row["reviewed"]=True
        row["independent_reviewer"]="w374; explicit KEEP in ~/brain_workers/w374/REVIEW_PACKET.md"
        row["referee_receipt"]="REFEREE_RECEIPT.json"
        if row["claim_id"]!="S1.w373.001":
            row["status"]="independently checked proof"
        if row["claim_id"]=="S1.w373.001":
            row["remaining_gap"]="Target and definitions recovered. Current October 2026 openness remains UNKNOWN; no exhaustive status claim."
        elif row["claim_id"]=="S1.w373.007":
            row["remaining_gap"]="w374 independently kept the same L2/L4 reductions. Actual Uniform[1,2] mean gap and global exponent matching remain unproved."
        else:
            row["remaining_gap"]=row["remaining_gap"].replace("Independent check pending. ","")
(root/"CLAIMS.jsonl").write_text("".join(json.dumps(r,ensure_ascii=False)+"\n" for r in rows),encoding="utf-8")

bundle=json.loads((root/"bundle_001.json").read_text(encoding="utf-8"))
for i,e in enumerate(bundle["entries"]):
    if i<4:
        e["statement"]=e["statement"].replace("DRAFT audit concept; independent mathematical review pending. ","DRAFT audit concept; scoped argument independently checked by w374 (KEEP). ",1)
        e["source"]["revision"]="argument-checked-by-w374-2026-10-10-concept-draft"
    bundle["relations"][i]["rationale"]="From: '"+rows[i+1]["statement"]+"'. Target: 'Exhibit a nondegenerate iid undirected FPP law with well-defined fluctuation and wandering exponents satisfying chi=2xi-1.' This scoped observation guards an inference on a sufficient proof route; it neither proves nor refutes the target."
bundle_text=json.dumps(bundle,ensure_ascii=False,indent=2)+"\n"
(root/"bundle_001.json").write_text(bundle_text,encoding="utf-8")
live="~/math-brain-inbox/w373/bundle_001.json"
(root/"patches"/"01_p0110_draft_bundle.diff").write_text("".join(difflib.unified_diff([],bundle_text.splitlines(keepends=True),fromfile="a/"+live,tofile="b/"+live)),encoding="utf-8")

source=json.loads((root/"SOURCE_STATUS.json").read_text(encoding="utf-8"))
source["sources"][2]["locator"]="Section 4.3, equation (4.19), Question 22, printed p.88 / PDF p.89 in v2; existence and definition are part of the problem."
source["independent_review"]={"reviewer":"w374","state":"partial-keeps","kept_claims":list(kept),"pending_claims":receipt["still_pending"],"receipt":"REFEREE_RECEIPT.json"}
source["prior_work_checks"].append({"path":"~/Open problem project/solved_register.md","scope":"Targeted P0110/FPP/KPZ/first-passage search found no matching target; no whole-register certification claimed."})
source["canonical_repository_check"]={"path":"~/math-research-brain","scope":"Located src/math_brain/store.py SQLiteStore implementation; no sqlite/db artifact found under this repository. Queried the explicitly named live population store read-only for the exact P0110 card; receipt store_target_receipt.json. No complete canonical solved-work audit claimed."}
(root/"SOURCE_STATUS.json").write_text(json.dumps(source,ensure_ascii=False,indent=2),encoding="utf-8")

replacements={
 "REPORT.md":[
   ("Eight claim rows and the frozen proof audit are in this folder.","Eight claim rows and the frozen proof audit are in this folder. Six rows have explicit referee KEEP evidence; the norm countermodel and the sufficient-route reduction row remain pending."),
   ("The new concepts are not independently checked yet and have not been ingested.","Four of five concept arguments have explicit independent KEEP verdicts from w374; the norm countermodel remains pending. None has been submitted or ingested by this worker."),
   ("Exact checks also show","All 25 scoped checks passed. Exact checks also show")],
 "REVIEW_PACKET.md":[
   ("eight result rows; independent checks remain pending. A sketch label records the absence of independent certification even where a complete analytic argument is written.","eight result rows; six have consumed w374 KEEP verdicts and two remain pending. REFEREE_RECEIPT.json records the exact verdict rows; remaining sketch labels preserve the absence of independent certification."),
   ("Return KEEP/FIX/DROP per claim.","Return KEEP/FIX/DROP for the two remaining rows; preserve the six explicit prior KEEP verdicts in REFEREE_RECEIPT.json.")],
 "ATTEMPT.md":[
   ("Named independent reviewer: w374, pending.","Named independent reviewer: w374. REFEREE_RECEIPT.json records KEEP verdicts for the four scoped probability/endpoint obstructions and the paired L2/L4 reductions. The norm countermodel and the sufficient-route reduction row remain pending."),
   ("NEXT: Check w372's cylinder comparison for unconditional deterministic-domain independence and an L2 localization error small relative to sqrt(Var T), then request w374's verdict on these four obstructions.","NEXT: Obtain w374's decisions on the norm countermodel and sufficient-route reduction; the next proof input is a positive quantitative mean gap for the actual iid law, with an L2 localization error small relative to sqrt(Var T).")],
 "INDEPENDENT.md":[("Independent referee: w374, pending. No mathematical result here is independently checked yet.","Independent referee: w374, KEEP for the rare-event argument; exact verdict retained in REFEREE_RECEIPT.json. This is an abstract counterexample to an inference, not an iid FPP law.")],
 "PAIRED_AUDIT.md":[("Independent referee w374 remains responsible for a separate check.","w374 subsequently supplied independent KEEP verdicts for the same paired L2/L4 reductions; see REFEREE_RECEIPT.json. The geometry countermodel remains pending.")]
}
for filename,changes in replacements.items():
    path=root/filename
    text=path.read_text(encoding="utf-8")
    for before,after in changes:
        text=text.replace(before,after)
    path.write_text(text,encoding="utf-8")
print(json.dumps({"kept":list(kept),"pending":receipt["still_pending"],"concept_arguments_kept":4,"submitted":False,"ingested":False},indent=2))
