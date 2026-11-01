"""Offline validation of the worker's draft; no live store or integration call."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
local=ROOT/"bundle_001.json"
remote=Path("~/math-brain-inbox/w388/bundle_001.json")
original=local.read_text(encoding="utf-8")
bundle=json.loads(original)
allowed={"key","namespace","logical_name","kind","title","statement","proof_text","assumptions","domain","source"}
# Normalize only this worker's own draft to the exact documented fields.
# Compare the remote draft first, so a later coordinator/peer edit is never overwritten.
needs_normalization=any(set(e)-allowed for e in bundle["entries"])
if needs_normalization:
    if remote.read_text(encoding="utf-8") != original:
        raise RuntimeError("owned draft differs from local source; preserve it and ask reviewer")
    for e in bundle["entries"]:
        for key in list(e):
            if key not in allowed:
                e.pop(key)
    normalized=json.dumps(bundle,indent=2,ensure_ascii=False)
    local.write_text(normalized,encoding="utf-8")
    part=remote.with_suffix(".schema.part")
    assert part.parent.resolve()==Path("~/math-brain-inbox/w388").resolve()
    if part.exists():
        raise RuntimeError("normalization staging file exists; preserve it")
    part.write_text(normalized,encoding="utf-8")
    part.replace(remote)

assert bundle["spec"]=="mathbrain-draft-v1" and bundle["author_agent"]=="w388"
assert 0<len(bundle["entries"])<=200
keys={e["key"] for e in bundle["entries"]}
assert len(keys)==len(bundle["entries"])
entry_checks=0
for e in bundle["entries"]:
    assert set(e)==allowed
    assert e["kind"]=="concept" and e["proof_text"] is None
    assert e["statement"] and e["assumptions"] and e["source"]["license"].startswith("owner-own-work")
    assert e["logical_name"]==e["logical_name"].lower() and " " not in e["logical_name"]
    assert {"source_id","url","revision","license","excerpt"}==set(e["source"])
    entry_checks+=1
existing=json.loads((ROOT/"store_target_rows.json").read_text(encoding="utf-8"))
existing_logical={json.loads(x["metadata_json"])["logical_id"] for x in existing}
relation_kinds={"depends_on","defines","proves","refutes","generalizes","specializes","analogous_to","cites","semantic_association"}
for rel in bundle["relations"]:
    assert rel["from_key"] in keys and rel["kind"] in relation_kinds and rel["rationale"]
    assert ("to_key" in rel)!=("to_existing_logical" in rel)
    if "to_key" in rel:
        assert rel["to_key"] in keys
    else:
        assert rel["to_existing_logical"] in existing_logical
assert not any(rel["kind"]=="depends_on" for rel in bundle["relations"])
claims=[json.loads(line) for line in (ROOT/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
assert len({c["claim_id"] for c in claims})==len(claims)
claim_fields={"claim_id","exact_statement","assumptions","source","proof_or_counterexample","independent_reviewer","remaining_gap","status"}
statuses={"conjecture","numerical evidence","sketch","proved special case","independently checked proof"}
for c in claims:
    assert claim_fields<=set(c) and c["status"] in statuses
assert "impossible" in next(c for c in claims if c["claim_id"].endswith("C03"))["exact_statement"]
source=json.loads((ROOT/"SOURCE_STATUS.json").read_text(encoding="utf-8"))
assert source["current_openness"]=="UNKNOWN" and source["novelty_claim"] is False
assert local.read_bytes()==remote.read_bytes()
edge_rows=[json.loads(line) for line in (ROOT/"EDGE_EVIDENCE.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
assert len(edge_rows)==len(bundle["relations"]) and all(x["quote_from"] and x["quote_to"] for x in edge_rows)
hook=json.loads((ROOT/"HOOK_PROPOSAL.jsonl").read_text(encoding="utf-8"))
assert len(hook["text"])<=300 and hook["fire_when"] and hook["silent_when"] and hook["evidence"]
metrics=json.loads((ROOT/"MEASUREMENTS.json").read_text(encoding="utf-8"))
assert len(metrics["cases"])==10 and metrics["bounded_localization_pair_checks"]==168
assert metrics["posterior_product_checks"]==36 and metrics["output_measurable_selector_checks"]==9
result={"command":"python -X utf8 validate_packet.py","verdict":"PASS","claim_rows":len(claims),
    "concept_entries":entry_checks,"relations":len(bundle["relations"]),"supporting_end_pairs":len(edge_rows),
    "all_entries_remain_concepts":True,"live_store_write":False,"integrator_invoked":False,
    "schema_normalization_needed":needs_normalization,"source_current_openness":"UNKNOWN"}
(ROOT/"VALIDATION.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
print(json.dumps(result))
