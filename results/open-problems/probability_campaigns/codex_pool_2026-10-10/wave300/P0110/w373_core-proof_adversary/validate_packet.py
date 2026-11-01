"""Local schema and artifact consistency checks; never integrates or writes a store."""
from pathlib import Path
import json

root=Path(__file__).resolve().parent
bundle=json.loads((root/"bundle_001.json").read_text(encoding="utf-8"))
rows=[json.loads(x) for x in (root/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
hook=json.loads((root/"hook_proposal.jsonl").read_text(encoding="utf-8"))
report={"command":"python -X utf8 ~/brain_workers/w373/validate_packet.py","checks":[]}
def verify(name,ok):
    report["checks"].append({"check":name,"passed":bool(ok)})
    if not ok:
        raise AssertionError(name)
verify("required_worker_artifacts",all((root/f).is_file() for f in ("STATUS.md","SOURCE_STATUS.json","ATTEMPT.md","CLAIMS.jsonl","REPORT.md","REVIEW_PACKET.md","PAIRED_AUDIT.md")))
verify("draft_spec",bundle["spec"]=="mathbrain-draft-v1" and bundle["author_agent"]=="w373" and len(bundle["entries"])<=200)
keys={e["key"] for e in bundle["entries"]}
verify("unique_entry_keys",len(keys)==len(bundle["entries"]))
verify("concepts_not_unchecked_theorems",all(e["kind"]=="concept" and e["proof_text"] is None and e["statement"].startswith("DRAFT audit concept;") for e in bundle["entries"]))
required={"key","namespace","logical_name","kind","title","statement","proof_text","assumptions","domain","source"}
verify("required_entry_fields",all(required<=e.keys() for e in bundle["entries"]))
verify("accepted_owner_source_tag",all(e["source"]["license"].startswith("owner-own-work") for e in bundle["entries"]))
stored=json.loads((root/"store_target_receipt.json").read_text(encoding="utf-8"))
logical_ids={json.loads(row["metadata_json"])["logical_id"] for row in stored["rows"]}
allowed={"depends_on","defines","proves","refutes","generalizes","specializes","analogous_to","cites","semantic_association"}
verify("relation_ends_and_kinds",all(r["from_key"] in keys and r["kind"] in allowed and r["to_existing_logical"] in logical_ids for r in bundle["relations"]))
verify("unique_claim_rows",len({r["claim_id"] for r in rows})==len(rows))
verify("all_claims_record_scope_and_review",all(all(k in r for k in ("statement","assumptions","source","proof_or_counterexample","independent_reviewer","remaining_gap","status","submitted","reviewed","ingested","retrievable")) for r in rows))
verify("hook_text_budget",len(hook["text"])<=300)
verify("hook_controls_and_evidence",bool(hook["fire_when"] and hook["silent_when"] and hook["evidence"]))
for filename,expected in (("01_p0110_draft_bundle.diff","~/math-brain-inbox/w373/bundle_001.json"),("02_fpp_scope_hook.diff","~/primary_directive/hooks1000/proposals/math-w373.jsonl")):
    data=(root/"patches"/filename).read_text(encoding="utf-8")
    verify("live_headers_"+filename,data.startswith("--- a/"+expected+"\n+++ b/"+expected+"\n"))
verify("current_openness_not_overclaimed",json.loads((root/"SOURCE_STATUS.json").read_text(encoding="utf-8"))["current_openness"]=="UNKNOWN")
report.update({"passed":len(report["checks"]),"total":len(report["checks"]),"draft_entries":len(keys),"claims":len(rows),"mathematical_proof":False,"independently_kept_claims":sum(bool(r["reviewed"]) for r in rows),"pending_claims":[r["claim_id"] for r in rows if not r["reviewed"]]})
(root/"packet_validation.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
print(json.dumps(report,indent=2))
