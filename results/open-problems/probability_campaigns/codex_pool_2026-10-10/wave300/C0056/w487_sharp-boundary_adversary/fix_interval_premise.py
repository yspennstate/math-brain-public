"""Apply w488's narrow FIX and prepare an immutable second draft version."""
import difflib
import hashlib
import json
from pathlib import Path

folder=Path(__file__).resolve().parent
attempt=(folder/"ATTEMPT.md").read_text(encoding="utf-8")
attempt=attempt.replace("In any fixed nonempty interval I compactly inside (-6,6)",
                        "In any fixed open interval I=(a,b) with -6<a<b<6")
attempt += "\n2026-10-10 referee FIX applied to S1.487.5: require a nondegenerate open energy interval I=(a,b), -6<a<b<6. A singleton is excluded; its grid count need not diverge. The existing numerical cases use I=(-1,1) and already satisfy this premise.\n"
(folder/"ATTEMPT.md").write_text(attempt,encoding="utf-8")
rows=[json.loads(line) for line in (folder/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
for row in rows:
    if row["row_id"]=="S1.487.5":
        row["assumptions"]=[a.replace("nonempty fixed energy interval compactly inside (-6,6)","fixed open interval I=(a,b) with -6<a<b<6") for a in row["assumptions"]]
        row["review_status"]="w488 FIX applied: explicitly nondegenerate open interval; final confirmation pending"
        row["independent_reviewer"]="w488 (narrow premise FIX received and applied; served-model identity UNKNOWN)"
        row["remaining_gap"]="Confirm revised nondegenerate-interval wording; zero-disorder periodic example does not refute positive-disorder C0056. Served-model gate unavailable."

bundle=json.loads((folder/"bundle_001.json").read_text(encoding="utf-8"))
bundle["bundle_slug"]="c0056-spectral-moment-boundary-20261010-v2"
for item in bundle["entries"]:
    if item["key"]=="goe":
        item["statement"]=item["statement"].replace("In any fixed nonempty interval compactly inside (-6,6)","In any fixed open interval I=(a,b) with -6<a<b<6")
        item["assumptions"]=[a.replace("fixed nonempty interval compactly inside (-6,6)","fixed open interval I=(a,b) with -6<a<b<6") for a in item["assumptions"]]
    item["source"]["revision"]="campaign-author-2026-10-10-v2-nondegenerate-interval-fix"
local=folder/"bundle_002.json"
local.write_text(json.dumps(bundle,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
bykey={e["key"]:e for e in bundle["entries"]}
for row in rows:
    if row.get("kind")=="draft_relation":
        rel=row["statement"]
        row["supporting_from_quote"]=bykey[rel["from_key"]]["statement"]
        if rel.get("to_key"):
            row["supporting_to_quote"]=bykey[rel["to_key"]]["statement"]
        row["source"]="bundle_002.json and STORE_MATCHES.jsonl for the external end"
(folder/"CLAIMS.jsonl").write_text("".join(json.dumps(r,ensure_ascii=False)+"\n" for r in rows),encoding="utf-8")
target="~/math-brain-inbox/w487/bundle_002.json"
patch="".join(difflib.unified_diff([],local.read_text(encoding="utf-8").splitlines(keepends=True),fromfile="a/"+target,tofile="b/"+target))
(folder/"patches"/"02_c0056_nondegenerate_interval_fix.diff").write_text(patch,encoding="utf-8")
report=(folder/"REPORT.md").read_text(encoding="utf-8")
report=report.replace("bundle_001.json (review diff: patches/01_c0056_boundary_draft.diff)","bundle_002.json (review diff: patches/02_c0056_nondegenerate_interval_fix.diff)")
report += "\nReferee correction applied: S1.487.5 now assumes a fixed open interval I=(a,b), -6<a<b<6, so the bulk count diverges; a singleton is excluded. The original submitted bundle_001.json is preserved and superseded by bundle_002.json. Existing numerical windows (-1,1) need no rerun. Four native KEEP receipts remain valid; the fifth row has FIX applied, awaiting confirmation.\n"
(folder/"REPORT.md").write_text(report,encoding="utf-8")
packet=(folder/"REVIEW_PACKET.md").read_text(encoding="utf-8")
packet += "\nReview revision v2: w488's S1.487.5 FIX is applied. The energy interval is explicitly I=(a,b), -6<a<b<6; no singleton is permitted. Confirm this premise correction and review bundle_002.json; bundle_001.json is preserved but superseded.\n"
(folder/"REVIEW_PACKET.md").write_text(packet,encoding="utf-8")
receipt=json.loads((folder/"REVIEW_RECEIPT.json").read_text(encoding="utf-8"))
refrows=[json.loads(line) for line in Path(r"~\brain_workers\w488\REVIEWS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
receipt["narrow_fix_receipts"]=[r for r in refrows if r.get("claim")=="S1.487.5"]
receipt["fix_application"]="Applied a fixed nondegenerate open interval I=(a,b), -6<a<b<6; v2 draft, no theorem promotion"
(folder/"REVIEW_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
status=(folder/"STATUS.md").read_text(encoding="utf-8")
status=status.replace("STATE: NEEDS_REVIEW","STATE: WORKING",1)
lines=status.splitlines(); lines[1]="NEXT: Publish v2 nondegenerate-interval FIX, route its exact hashes, then return to NEEDS_REVIEW."
(folder/"STATUS.md").write_text("\n".join(lines)+"\n2026-10-10: Received w488 FIX for S1.487.5; nonempty interval could mean singleton. Added explicit I=(a,b), -6<a<b<6 throughout the author proof, claim and v2 draft. Original submitted draft is preserved.\n",encoding="utf-8")
assert all("nonempty interval" not in e["statement"] for e in bundle["entries"] if e["key"]=="goe")
assert bykey["goe"]["assumptions"][-1]=="fixed open interval I=(a,b) with -6<a<b<6"
print(json.dumps({"fixed":"S1.487.5","draft":str(local),"entries":len(bundle["entries"]),"relations":len(bundle["relations"]),"prior_draft":"preserved, superseded"}))
