"""Record late review and paired audit; finish the already validated handoff."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
source_path=ROOT/"SOURCE_STATUS.json"
source=json.loads(source_path.read_text(encoding="utf-8"))
source["brain_and_review"]["paired_prover"]="w387 arrived during final validation; statement-only packet and ATTEMPT.md L1-L4/G1 read after independent lock. PEER_VERDICTS.jsonl supplies four KEEP verdicts and an entropy-margin note."
source["brain_and_review"]["review_receipts"]["w389"]="C01,C02,C04,C05,C06 KEEP; C03 FIX accepted. C06 symbolic rederivation announced at05:16 UTC as R07."
source_path.write_text(json.dumps(source,indent=2),encoding="utf-8")
claim_path=ROOT/"CLAIMS.jsonl"
claims=[json.loads(x) for x in claim_path.read_text(encoding="utf-8").splitlines() if x.strip()]
for c in claims:
    if c["claim_id"].endswith("C06"):
        c["status"]="independently checked proof"
        c["review_status"]="KEEP by w389, R07; symbolic rederivation announced05:16 UTC. Not a main-theorem or formal-check receipt."
        c["independent_reviewer"]="w389; P0117-w389-R07 in REVIEWS.jsonl"
        c["remaining_gap"]="No gap in the posterior law under exact output-only conditioning; geometric inputs and the September manuscript's full theorem remain uncertified."
claim_path.write_text("\n".join(json.dumps(c,ensure_ascii=False) for c in claims)+"\n",encoding="utf-8")

# Keep the submitted concept's narrow-review statement current, preserving all mathematical scope.
local=ROOT/"bundle_001.json"
remote=Path("~/math-brain-inbox/w388/bundle_001.json")
old=local.read_text(encoding="utf-8")
bundle=json.loads(old)
for e in bundle["entries"]:
    if e["key"]=="posterior":
        e["statement"]=e["statement"].replace("DRAFT separately derived narrow check; w389 review pending.","DRAFT narrow sublemma independently checked by w389; validating-coordinator review remains required.")
new=json.dumps(bundle,indent=2,ensure_ascii=False)
assert remote.read_text(encoding="utf-8")==old, "preserve any changed/moved coordinator draft"
local.write_text(new,encoding="utf-8")
part=remote.with_suffix(".review.part")
assert not part.exists()
assert part.parent.resolve()==Path("~/math-brain-inbox/w388").resolve()
part.write_text(new,encoding="utf-8")
part.replace(remote)
by_key={x["key"]:x for x in bundle["entries"]}
edges_path=ROOT/"EDGE_EVIDENCE.jsonl"
edges=[json.loads(x) for x in edges_path.read_text(encoding="utf-8").splitlines() if x.strip()]
for e in edges:
    e["quote_from"]=by_key[e["from_key"]]["statement"]
    if "to_key" in e:
        e["quote_to"]=by_key[e["to_key"]]["statement"]
edges_path.write_text("\n".join(json.dumps(e,ensure_ascii=False) for e in edges)+"\n",encoding="utf-8")
states_path=ROOT/"BUNDLE_STATES.json"
states=json.loads(states_path.read_text(encoding="utf-8"))
states["review_detail"]="w389 KEEP on C01,C02,C04,C05,C06; C03 FIX accepted; C07 awaits w392; bundle relations/coordinator review pending"
states["paired_audit"]="w388 independently kept w387 L1-L4 and refined G1; PEER_VERDICTS.jsonl"
states_path.write_text(json.dumps(states,indent=2),encoding="utf-8")

report=ROOT/"REPORT.md"
text=report.read_text(encoding="utf-8")
text=text.replace("and awaits the narrow C06 review.","and has now received the narrow C06 KEEP from w389 (R07).")
text=text.replace("NEXT: w389 check C06 and w392 check w389's shell-floor correction; certify", "NEXT: w392 check w389's shell-floor correction; certify")
text += "\nAdditional paired-audit controls: `python -X utf8 check_peer_shortcuts.py` checked256 square worlds, obtaining fixed-route pattern1/256 versus selected-route pattern0, and five entropy examples whose unions remain1/2 despite a pointwise strict logarithmic gap. With L=6,D=421,eta=1/268435456, the explicit shortcut exponent is c=1.4747784265244686e-12; this does not dominate unrestricted lattice-path entropy. The separate controls used0.015625 seconds CPU.\n"
report.write_text(text,encoding="utf-8")
posterior=ROOT/"POSTERIOR_CHECK.md"
text=posterior.read_text(encoding="utf-8").replace("Independent reviewer w389 has not yet checked this new derivation.","Independent reviewer w389 has now kept this derivation after symbolic rederivation (R07, announced05:16 UTC).")
posterior.write_text(text,encoding="utf-8")
audit=ROOT/"AUDIT.md"
text=audit.read_text(encoding="utf-8").replace("C01,C02,C04,C05 received independent KEEP verdicts", "C01,C02,C04,C05,C06 received independent KEEP verdicts")
text=text.replace("NEXT: w389 check C06; w392 check", "NEXT: w392 check")
audit.write_text(text,encoding="utf-8")
index=ROOT/"review_packet/INDEX.md"
text=index.read_text(encoding="utf-8").replace("C01,C02,C04,C05 KEEP; C03 FIX accepted.","C01,C02,C04,C05,C06 KEEP (C06 is R07); C03 FIX accepted.")
text=text.replace("New C06 review and the designated w392 check on w389's new correction are pending.","The designated w392 check on w389's new correction and the coordinator's bundle/relation reviews are pending.")
text=text.replace("NEXT: check C06 and the shell-floor correction, then assess", "NEXT: check the shell-floor correction, then assess")
index.write_text(text,encoding="utf-8")
print(json.dumps({"own_independent_keeps":5,"peer_result_keeps":4,"accepted_fixes":1,"submitted_concepts":8,"relations":8,"main_status":"UNKNOWN"}))
