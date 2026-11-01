"""Read-only validation of this packet and its explicitly allocated inbox copy."""
import json
from pathlib import Path

root=Path(__file__).resolve().parent
required=["STATUS.md","SOURCE_STATUS.json","ATTEMPT.md","CLAIMS.jsonl","REVIEW_PACKET.md","REPORT.md","INDEPENDENT_OBSTRUCTION.md","PAIRED_AUDIT.md","EDGES.jsonl","BUNDLE_STATE.json","recall_measurement.json","obstruction_measurement.json","patches/01_c0017_principal_spin.diff"]
assert all((root/name).is_file() for name in required)
assert (root/"STATUS.md").read_text(encoding="utf-8").splitlines()[0] in {"STATE: WORKING","STATE: NEEDS_REVIEW","STATE: BLOCKED","STATE: DONE"}
bundle=json.loads((root/"drafts/bundle_001.json").read_text(encoding="utf-8"))
keys={e["key"] for e in bundle["entries"]}
assert len(keys)==len(bundle["entries"])==6
for entry in bundle["entries"]:
    assert {"key","namespace","logical_name","kind","title","statement","proof_text","assumptions","domain","source"} <= entry.keys()
    assert entry["kind"] in {"definition","concept"}
    assert entry["proof_text"] is None
    assert entry["statement"] and isinstance(entry["assumptions"],list)
    assert entry["source"]["license"]=="owner-own-work"
    assert {"source_id","url","revision","license","excerpt"} <= entry["source"].keys()
allowed={"depends_on","defines","proves","refutes","generalizes","specializes","analogous_to","cites","semantic_association"}
graph={key:[] for key in keys}
for edge in bundle["relations"]:
    assert edge["kind"] in allowed and edge["from_key"] in keys
    if "to_key" in edge:
        assert edge["to_key"] in keys
        if edge["kind"]=="depends_on": graph[edge["from_key"]].append(edge["to_key"])
    else: assert edge["to_existing_logical"].startswith("math:")
def visit(key,active,done):
    assert key not in active, "Dependency cycle"
    if key in done: return
    for child in graph[key]: visit(child,active|{key},done)
    done.add(key)
done=set()
for key in keys: visit(key,set(),done)
claims=[json.loads(line) for line in (root/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
assert len(claims)==7 and len({r["id"] for r in claims})==7
for claim in claims:
    assert {"id","status","statement","assumptions","source","proof_or_counterexample","independent_reviewer","remaining_gap"} <= claim.keys()
    assert claim["status"] in {"conjecture","numerical evidence","sketch","proved special case","independently checked proof"}
state=json.loads((root/"BUNDLE_STATE.json").read_text(encoding="utf-8"))
assert state["submitted"] and not any(state[k] for k in ("reviewed","ingested","retrievable"))
assert Path(state["inbox_path"]).read_bytes()==(root/"drafts/bundle_001.json").read_bytes()
measurement=json.loads((root/"obstruction_measurement.json").read_text(encoding="utf-8"))
assert measurement["total_stencils_checked"]==849
assert measurement["hybrid_counterexample"]["actual_expectation_difference"]=="249851/250000"
assert measurement["hybrid_counterexample"]["correct_hybrid_bound"]=="249851/250000"
assert measurement["hybrid_counterexample"]["false_endpoint_only_bound"]=="14553/250000"
patch=(root/"patches/01_c0017_principal_spin.diff").read_text(encoding="utf-8")
assert patch.startswith("--- a/06_math_research/") and "+++ b/06_math_research/" in patch
before=json.loads((root/"extracts/attempt_C0017_before.json").read_text(encoding="utf-8"))
after=json.loads((root/"extracts/attempt_C0017_after.json").read_text(encoding="utf-8"))
assert "has spin sigma = 2/3" in before["result"] and "has spin sigma = 1/3" in after["result"]
assert all(after[key]==value for key,value in before.items() if key!="result")
print(json.dumps({"validation":"PASS","required_artifacts":len(required),"claims":len(claims),"entries":len(keys),"relations":len(bundle["relations"]),"no_theorem_promotions":True,"inbox_copy_matches":True,"source_patch_preserves_other_fields":True,"scope":"Structural/measurement checks only; mathematical referee review remains pending"},indent=2))
