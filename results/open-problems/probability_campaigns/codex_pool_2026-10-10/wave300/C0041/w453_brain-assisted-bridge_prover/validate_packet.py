"""Required structural/packaging checks; not a mathematical proof verifier."""
import importlib.util
import json
import sys
from pathlib import Path

sys.dont_write_bytecode=True
root=Path(__file__).resolve().parent
bundle=json.loads(root.joinpath("bundle_001.json").read_text(encoding="utf-8"))
states=json.loads(root.joinpath("BUNDLE_STATES.json").read_text(encoding="utf-8"))
assert root.joinpath("bundle_001.json").read_bytes()==Path(states["draft_path"]).read_bytes()
assert states["submitted"] and not states["ingested"] and not states["retrievable"]
entries={e["key"]:e for e in bundle["entries"]}
graph={k:[] for k in entries}
allowed={"depends_on","defines","proves","refutes","generalizes","specializes","analogous_to","cites","semantic_association"}
for relation in bundle["relations"]:
    assert relation["kind"] in allowed
    assert relation["from_key"] in entries
    if "to_key" in relation:
        assert relation["to_key"] in entries
        if relation["kind"]=="depends_on":
            graph[relation["from_key"]].append(relation["to_key"])
    else:
        assert relation["to_existing_logical"].startswith("math:")
seen=set()
visiting=set()
def visit(key):
    assert key not in visiting,"dependency cycle"
    if key in seen:return
    visiting.add(key)
    for dependency in graph[key]:visit(dependency)
    visiting.remove(key)
    seen.add(key)
for key in entries:visit(key)
for e in entries.values():
    assert e["source"]["license"].startswith("owner-own-work")
    assert e["proof_text"] if e["kind"] in {"lemma","theorem"} else e["proof_text"] is None
assert "alpha^(-1)" in entries["lem-clock"]["statement"]
assert "lambda>log(1/kappa)" in entries["lem-mean"]["statement"]
claims=[json.loads(line) for line in root.joinpath("CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line]
assert len({r["id"] for r in claims})==len(claims)
for claim in claims:
    assert claim["status"] in {"conjecture","numerical evidence","sketch","proved special case","independently checked proof"}
    assert all(field in claim for field in ("statement","assumptions","source","proof_or_counterexample","independent_reviewer","remaining_gap"))
hook=json.loads(root.joinpath("HOOK_PROPOSALS.jsonl").read_text(encoding="utf-8"))
assert len(hook["text"])<=300 and hook["fire_when"] and hook["silent_when"]
spec=importlib.util.spec_from_file_location("candidate_lookup_copy",root/"copies/candidate_lookup.py")
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
actual=module.lookup_candidate("~/math-brain-build/local/population/brain.sqlite3","C0041")
expected=json.loads(root.joinpath("candidate_lookup_measurement.json").read_text(encoding="utf-8"))["repaired"]["rows"]
assert [list(row) for row in actual]==expected
for name in ("patches/01_candidate_lookup.diff","patches/02_math_hook_proposal.diff"):
    patch=root.joinpath(name).read_text(encoding="utf-8")
    assert patch.startswith("--- a/C:/") and "\n+++ b/C:/" in patch
assert json.loads(root.joinpath("range_clock_checks.json").read_text(encoding="utf-8"))["failed"]==0
assert json.loads(root.joinpath("countermodel_checks.json").read_text(encoding="utf-8"))["failed"]==0
result={"command":"python -B -X utf8 validate_packet.py","passed":True,"entries":len(entries),"relations":len(bundle["relations"]),"claims":len(claims),"checks":["worker/inbox bundle equality","allowed kinds and owner source tags","acyclic dependencies","conditional alpha normalization and strict exponent present","claims schema and unique IDs","hook schema and text limit","actual copied prototype target lookup","named live-path diff headers","exact-run zero-failure receipts"],"limits":"Structural validation only; independent mathematical review and integration/retrieval remain pending."}
root.joinpath("packet_validation.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result))
