"""Local structural validation; never presented as a mathematical audit."""
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parent
bundle=json.loads((ROOT/"drafts/bundle_001.json").read_text(encoding="utf-8"))
assert bundle["spec"]=="mathbrain-draft-v1" and bundle["author_agent"]=="w399"
required={"key","namespace","logical_name","kind","title","statement","proof_text","assumptions","domain","source"}
keys=set()
for e in bundle["entries"]:
    assert required<=set(e)
    assert e["key"] not in keys
    keys.add(e["key"])
    assert e["kind"] in {"definition","concept"}
    assert e["proof_text"] is None and e["statement"] and e["assumptions"]
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*",e["logical_name"])
    assert e["source"]["license"].startswith("owner-own-work")
    assert e["source"]["revision"].endswith("pending-w401")
allowed={"depends_on","defines","proves","refutes","generalizes","specializes","analogous_to","cites","semantic_association"}
adj={k:[] for k in keys}
for rel in bundle["relations"]:
    assert rel["kind"] in allowed and rel["from_key"] in keys and rel["to_key"] in keys
    if rel["kind"]=="depends_on":
        adj[rel["from_key"]].append(rel["to_key"])
def visit(node, stack):
    assert node not in stack
    for nxt in adj[node]:
        visit(nxt,stack|{node})
for key in keys:
    visit(key,set())
rel_rows=[json.loads(line) for line in (ROOT/"RELATION_EVIDENCE.jsonl").read_text(encoding="utf-8").splitlines()]
assert len(rel_rows)==len(bundle["relations"])
bykey={e["key"]:e for e in bundle["entries"]}
for row in rel_rows:
    assert row["from_statement"]==bykey[row["from_key"]]["statement"]
    assert row["to_statement"]==bykey[row["to_key"]]["statement"]
claims=[json.loads(line) for line in (ROOT/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines()]
assert {"w399-P0003-L3","w399-P0003-L4","w399-P0003-L5","w399-P0003-G1"}<={c["claim_id"] for c in claims}
for c in claims:
    assert c["status"] in {"conjecture","numerical evidence","sketch","proved special case","independently checked proof"}
    assert c["statement"] and c["source"] and c["independent_reviewer"] and "remaining_gap" in c
    if c["status"]=="independently checked proof":
        assert c["review_evidence"]["reviewer"]=="w401"
        assert c["review_evidence"]["verdict"]=="KEEP" and c["review_scope_only"]
        assert c["review_evidence"]["scope"] and c["review_evidence"]["reproduction"]
for filename in ["MEASUREMENTS.json","MEASUREMENTS_THREE_PROBE.json"]:
    m=json.loads((ROOT/filename).read_text(encoding="utf-8"))
    assert m["passed"] and m["formal_checker"] is None and m["elapsed_seconds"]<45
source=json.loads((ROOT/"SOURCE_STATUS.json").read_text(encoding="utf-8"))
assert source["current_openness"]=="UNKNOWN" and source["full_target_proved"] is False
assert len(source["original_target"]["source_quote"].split())<=25
assert source["working_target"]["transfer_to_original_fixed_n_target"]=="UNPROVED"
hook=json.loads((ROOT/"HOOK_PROPOSAL.jsonl").read_text(encoding="utf-8"))
assert len(hook["text"])<=300
controls=json.loads((ROOT/"HOOK_CONTROLS.json").read_text(encoding="utf-8"))
assert controls["fire"]["matched"] and not controls["silent"]["matched"]
patch=(ROOT/"patches/01_w399_three_probe_draft.diff").read_text(encoding="utf-8").splitlines()
added="\n".join(line[1:] for line in patch if line.startswith("+") and not line.startswith("+++"))+"\n"
assert added==(ROOT/"drafts/bundle_001.json").read_text(encoding="utf-8")
result={"passed":True,"validation_type":"structure only; not independent mathematical review","draft_entries":len(keys),"draft_relations":len(bundle["relations"]),"claim_rows":len(claims),"theorem_entries":0,"relation_ends_quoted":True,"depends_on_acyclic":True,"owner_own_work_tag":True,"hook_fire_control":True,"hook_silent_control":True,"creation_diff_payload_matches":True,"formal_checker":None}
(ROOT/"VALIDATION.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
