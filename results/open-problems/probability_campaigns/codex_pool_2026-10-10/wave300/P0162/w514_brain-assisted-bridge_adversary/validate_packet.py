"""Local artifact validation only; not a mathematical or formal-proof verifier."""
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def read(name):
    return json.loads((ROOT/name).read_text(encoding="utf-8"))

def jsonl(name):
    return [json.loads(row) for row in (ROOT/name).read_text(encoding="utf-8").splitlines() if row.strip()]

def main():
    bundle=read("brain_bundle/bundle_001.json")
    assert bundle["spec"]=="mathbrain-draft-v1" and bundle["author_agent"]=="w514"
    entries=bundle["entries"]
    assert 0<len(entries)<=200
    bykey={e["key"]:e for e in entries}
    assert len(bykey)==len(entries)
    assert len({e["logical_name"] for e in entries})==len(entries)
    for e in entries:
        assert e["kind"] in ("definition","concept")
        assert e["proof_text"] is None
        assert e["statement"] and e["assumptions"]
        assert e["source"]["license"].startswith("owner-own-work")
        assert e["source"]["source_id"] and e["source"]["revision"]
        if e["kind"]=="concept":
            assert "DRAFT" in e["statement"] or "REFUTED ROUTE" in e["statement"]
            assert "independent check" in e["statement"]
    allowed={"depends_on","defines","proves","refutes","generalizes","specializes","analogous_to","cites","semantic_association"}
    deps={k:[] for k in bykey}
    for r in bundle["relations"]:
        assert r["kind"] in allowed and r["from_key"] in bykey and r["to_key"] in bykey
        if r["kind"]=="depends_on":
            deps[r["from_key"]].append(r["to_key"])
    def walk(key,path):
        assert key not in path,"dependency cycle"
        for target in deps[key]:
            walk(target,path|{key})
    for key in deps:
        walk(key,set())
    edges=jsonl("EXACT_EDGES.jsonl")
    assert len(edges)==len(bundle["relations"])
    for edge,r in zip(edges,bundle["relations"]):
        assert edge["from_quote"]==bykey[r["from_key"]]["statement"]
        assert edge["to_quote"]==bykey[r["to_key"]]["statement"]
        assert edge["kind"]==r["kind"] and edge["reviewer"]=="w515"
    claims=jsonl("CLAIMS.jsonl")
    required={"id","exact_statement","assumptions","source","independent_reviewer","remaining_gap","status"}
    for claim in claims:
        assert required<=claim.keys()
        assert claim.get("proof") or claim.get("counterexample")
        assert claim["status"] in ("conjecture","numerical evidence","sketch","proved special case","independently checked proof")
        assert claim["review_state"]=="unreviewed"
        assert claim["status"]!="independently checked proof"
    state=read("BUNDLE_STATE.json")
    assert state["prepared"] and all(not state[k] for k in ("submitted","reviewed","ingested","retrievable"))
    source=read("SOURCE_STATUS.json")
    assert source["current_openness"]=="UNKNOWN" and source["formal_check"] is None
    diagnostic=read("RETRIEVAL_FAILURE.json")
    assert diagnostic["before_selected_status_visible"]==0
    assert diagnostic["after_selected_status_visible"]==3
    assert all(row["status"]=="unverified" for row in diagnostic["after_statuses"])
    patch=(ROOT/"patches/01_p0162_bridge_bundle.diff").read_text(encoding="utf-8")
    assert patch.startswith("--- a/~/math-brain-inbox/w514/bundle_001.json\n+++ b/~/math-brain-inbox/w514/bundle_001.json\n")
    added="".join(row[1:] for row in patch.splitlines(keepends=True) if row.startswith("+") and not row.startswith("+++"))
    assert added==(ROOT/"brain_bundle/bundle_001.json").read_text(encoding="utf-8")
    hook=jsonl("proposals/math-w514.jsonl")[0]
    assert len(hook["text"])<=300
    cue=re.compile(hook["cue"])
    assert cue.search(hook["fire_when"])
    assert not cue.search(hook["silent_when"])
    audits=jsonl("AUDIT_W513.jsonl")
    assert len(audits)==6 and all(row["verdict"]=="KEEP" for row in audits)
    assert all(row["exact_statement_reviewed"] and row["assumptions_reviewed"] for row in audits)
    correction=read("NODE_CORRECTION.json")
    assert correction["state"]=="DRAFT; not applied"
    assert correction["source_quote"]=="delta = max_i Inf_i"
    checks=read("adversary_checks.json")
    assert checks["seconds"]<checks["gate"]["max_wall_seconds"]
    assert checks["delta_counterexample"]["rho0"]>checks["delta_counterexample"]["wrong_input_bias_ceiling"]
    assert source["paired_access"]["proof_available_at_later_read"]
    assert source["paired_access"]["audited_claims"]==6
    receipt={"scope":"artifact/schema/quote/gate consistency only; not proof verification","claims":len(claims),
             "draft_entries":len(entries),"exact_edges":len(edges),"dependency_graph_acyclic":True,
             "drafts_not_promoted":True,"hook_fire_control":True,"hook_silent_control":True,
             "status_display_coverage_before":"0/3","status_display_coverage_after":"3/3",
             "peer_KEEP_verdicts":len(audits),"source_correction":"DRAFT; not applied","result":"PASS"}
    (ROOT/"packet_validation.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(receipt))

if __name__=="__main__":
    main()
