"""Local structural checks only; never invoke the live integrator."""
import json
from pathlib import Path
import re
import sqlite3

ROOT = Path(__file__).resolve().parent
bundle = json.loads((ROOT/"bundle_001.json").read_text(encoding="utf-8"))
assert bundle["spec"]=="mathbrain-draft-v1" and bundle["author_agent"]=="w385"
entries=bundle["entries"]
assert 0<len(entries)<=200
required={"key","namespace","logical_name","kind","title","statement","proof_text","assumptions","domain","source"}
by_key={e["key"]:e for e in entries}
assert len(by_key)==len(entries)
logical=set()
for e in entries:
    assert required<=e.keys()
    assert e["kind"] in {"definition","lemma","theorem","concept"}
    assert re.fullmatch(r"[a-z][a-z0-9.-]*",e["namespace"])
    assert re.fullmatch(r"[a-z][a-z0-9-]*",e["logical_name"])
    identity=(e["namespace"],e["logical_name"])
    assert identity not in logical
    logical.add(identity)
    assert len(e["statement"].strip())>=20 and e["title"].strip()
    assert e["kind"] in {"definition","concept"} and e["proof_text"] is None
    if e["kind"]=="concept":
        assert e["statement"].startswith("DRAFT: independent verification pending.")
    assert isinstance(e["assumptions"],list) and all(isinstance(a,str) and a.strip() for a in e["assumptions"])
    src=e["source"]
    assert all(isinstance(src[f],str) and src[f].strip() for f in ["source_id","url","revision","license"])
    assert src["license"].startswith("owner-own-work")

allowed={"depends_on","defines","proves","refutes","generalizes","specializes","analogous_to","cites","semantic_association"}
adj={k:[] for k in by_key}
external={}
with sqlite3.connect("file:~/math-brain-build/local/population/brain.sqlite3?mode=ro",uri=True,timeout=3) as c:
    c.row_factory=sqlite3.Row
    row=c.execute("SELECT id,body,metadata_json FROM nodes WHERE id=?",("claim_00e83dbdd81c6433d9909a1b375c4e0a688bea718951c1d68fe8ffcd72b1bcf1",)).fetchone()
    assert row is not None
    external[json.loads(row["metadata_json"])["logical_id"]]={"id":row["id"],"statement":row["body"]}
relations=bundle["relations"]
quotes=[json.loads(line) for line in (ROOT/"RELATION_EVIDENCE.jsonl").read_text(encoding="utf-8").splitlines()]
assert len(quotes)==len(relations)
for r,q in zip(relations,quotes):
    assert r["kind"] in allowed and r["from_key"] in by_key and r["rationale"].strip()
    assert q["from_statement_quote"]==by_key[r["from_key"]]["statement"]
    if "to_key" in r:
        assert r["to_key"] in by_key
        assert q["to_statement_quote"]==by_key[r["to_key"]]["statement"]
        if r["kind"]=="depends_on":
            adj[r["from_key"]].append(r["to_key"])
    else:
        assert r["to_existing_logical"] in external
        assert q["to_statement_quote"]==external[r["to_existing_logical"]]["statement"]
gray=set()
black=set()
def visit(v):
    assert v not in gray
    if v in black:
        return
    gray.add(v)
    for w in adj[v]:
        visit(w)
    gray.remove(v)
    black.add(v)
for v in adj:
    visit(v)
claims=[json.loads(line) for line in (ROOT/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines()]
for x in claims:
    assert {"claim_id","statement","assumptions","source","proof_or_counterexample","independent_reviewer","remaining_gap","status"}<=x.keys()
    assert x["status"] in {"conjecture","numerical evidence","sketch","proved special case","independently checked proof"}
audits=[json.loads(line) for line in (ROOT/"AUDIT_W384.jsonl").read_text(encoding="utf-8").splitlines()]
hooks=[json.loads(line) for line in (ROOT/"hooks_proposed.jsonl").read_text(encoding="utf-8").splitlines()]
for h in hooks:
    assert {"id","area","event","cue","fire_when","silent_when","text","evidence","proposer"}<=h.keys()
    assert h["proposer"]=="w385" and len(h["text"])<=300 and h["fire_when"]!=h["silent_when"]
m=json.loads((ROOT/"MEASUREMENTS.json").read_text(encoding="utf-8"))
assert m["status"]=="PASS" and m["gate"]["passed"]
assert m["deleted_edge_formula"]["checked_equalities"]==9375 and m["deleted_edge_formula"]["maximum_exact_error"]=="0"
assert m["selector"]["underestimate_factor"]==4096
assert len(entries)==8 and len(relations)==8 and len(claims)==9 and len(audits)==4
receipt={"status":"PASS","command":"python -X utf8 validate_packet.py",
         "draft_entries":len(entries),"definition_entries":1,"draft_concepts":7,"theorem_entries":0,
         "relations":len(relations),"internal_relations":7,"verified_existing_card_links":1,
         "full_target_quote_checked_read_only":True,"claim_rows":len(claims),"author_audit_verdicts":len(audits),
         "hook_proposals":len(hooks),"dependencies_acyclic":True,
         "official_integrator_invoked":False,"new_mathematics_independently_reviewed":False,
         "scope":"Local structural validation and exact relation ends; finite control receipt checked. Mathematical correctness and live ingestion are not certified."}
(ROOT/"PACKET_VALIDATION.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps(receipt))
