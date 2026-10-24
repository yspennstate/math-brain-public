"""Local shape and safety checks, not a proof verifier."""
import json
from pathlib import Path

root=Path(__file__).resolve().parent
b=json.loads((root/"bundle_001.json").read_text(encoding="utf-8"))
required={"key","namespace","logical_name","kind","title","statement","proof_text","assumptions","domain","source"}
keys={e["key"] for e in b["entries"]}
assert len(keys)==len(b["entries"])<=200
assert b["spec"]=="mathbrain-draft-v1" and b["author_agent"]=="w478"
for e in b["entries"]:
    assert required<=e.keys()
    assert e["kind"]=="concept" and e["proof_text"] is None
    assert "DRAFT" in e["title"] and e["statement"]
    assert e["source"]["license"].startswith("owner-own-work")
graph={k:[] for k in keys}
allowed={"depends_on","defines","proves","refutes","generalizes","specializes","analogous_to","cites","semantic_association"}
for r in b["relations"]:
    assert r["from_key"] in keys and r["to_key"] in keys and r["kind"] in allowed
    if r["kind"]=="depends_on":
        graph[r["from_key"]].append(r["to_key"])
def visit(k,active,done):
    assert k not in active
    if k in done:
        return
    active.add(k)
    for target in graph[k]:
        visit(target,active,done)
    active.remove(k)
    done.add(k)
done=set()
for k in keys:
    visit(k,set(),done)
for line in (root/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines():
    c=json.loads(line)
    assert {"id","exact_statement","assumptions","source","proof_or_counterexample","independent_reviewer","remaining_gap","status"}<=c.keys()
print(json.dumps({"shape":"PASS","concepts":len(keys),"edges":len(b["relations"]),
 "dependency_cycles":0,"mathematical_proof_checked":False}))
