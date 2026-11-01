"""Static packet checks and a fresh gate for optional tiny arithmetic checks.

No live mutation or proof-status promotion; no model loads or SQLite writes.
"""
import ast
import json
import time
from datetime import datetime
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
started = time.perf_counter()
bundle = json.loads((ROOT/"bundle_001.json").read_text(encoding="utf-8"))
allowed_kinds = {"definition","lemma","theorem","concept"}
allowed_relations = {"depends_on","defines","proves","refutes","generalizes","specializes","analogous_to","cites","semantic_association"}
keys = {e["key"] for e in bundle["entries"]}
assert len(keys) == len(bundle["entries"])
for e in bundle["entries"]:
    assert e["kind"] in allowed_kinds and e["statement"] and e["assumptions"]
    assert e["source"]["license"].startswith("owner-own-work")
    if e["kind"] in {"lemma","theorem"}:
        assert e["proof_text"] and len(e["proof_text"]) > 40
    else:
        assert e["proof_text"] is None
deps = {k:[] for k in keys}
for r in bundle["relations"]:
    assert r["kind"] in allowed_relations and r["from_key"] in keys and r["rationale"]
    if "to_key" in r:
        assert r["to_key"] in keys
        if r["kind"] == "depends_on":
            deps[r["from_key"]].append(r["to_key"])
    else:
        assert r["to_existing_logical"].startswith("math:")


def visit(node, stack):
    assert node not in stack, "dependency cycle"
    for target in deps[node]:
        visit(target, stack | {node})


for key in keys:
    visit(key, set())
claims = [json.loads(line) for line in (ROOT/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line]
assert {c["id"] for c in claims} == {f"w477-L{i:03}" for i in range(1,8)}
for c in claims:
    assert c["status"] in {"conjecture","numerical evidence","sketch","proved special case","independently checked proof"}
    assert c["proof"] and c["independent_reviewer"] and c["remaining_gap"]
    assert not c["novelty_claim"]
source = json.loads((ROOT/"SOURCE_STATUS.json").read_text(encoding="utf-8"))
assert source["current_openness"] == "UNKNOWN" and not source["formal_check"]["performed"]
hook = json.loads((ROOT/"HOOK_PROPOSAL.jsonl").read_text(encoding="utf-8"))
assert len(hook["text"]) <= 300 and hook["fire_when"] and hook["silent_when"] and hook["evidence"]
for name in ("targeted_math_id_lookup.py","store_lookup.py","build_packet.py"):
    ast.parse((ROOT/name).read_text(encoding="utf-8"), filename=name)

lookup = json.loads((ROOT/"STORE_LOOKUP.json").read_text(encoding="utf-8"))
assert lookup["read_only"] and lookup["exact_problem_hits"] == 1
old = lookup["rows"][0]["body"]
new = next(e["statement"] for e in bundle["entries"] if e["key"] == "source-target")
atoms = {"subcritical_regime":"0<beta<beta_c", "susceptibility_definition":"chi=",
         "correlation_length_definition":"xi=", "coupling_normalization":"chi^2 xi^3", "source_sign":"<=0"}
old_checks = {k: token in old for k,token in atoms.items()}
new_checks = {k: token in new for k,token in atoms.items()}
assert not any(old_checks.values()) and all(new_checks.values())

gate_path = Path("~/.claude/compute/compute_state.json")
gate = {"path":str(gate_path),"optional_arithmetic_allowed":False}
try:
    state = json.loads(gate_path.read_text(encoding="utf-8-sig"))
    ts = datetime.fromisoformat(state["ts"])
    if ts.tzinfo is None:
        ts = ts.astimezone()
    age = (datetime.now().astimezone()-ts).total_seconds()
    gate.update({"ts":state["ts"],"age_seconds":age,"status":state.get("status"),
                 "mode":state.get("mode"),"reasons":state.get("reasons",[]),
                 "cpu_pct":state.get("cpu_pct"),"mem_avail_mb":state.get("mem_avail_mb"),
                 "commit_used_pct":state.get("commit_used_pct"),"hung_windows":state.get("hung_windows")})
    gate["optional_arithmetic_allowed"] = (
        -5 <= age <= 120 and state.get("status") == "ok"
        and state.get("mode") in {"owner_present_polite","owner_away_open","open"}
        and not state.get("reasons") and not state.get("hung_windows")
        and isinstance(state.get("cpu_pct"),(int,float)) and state["cpu_pct"] < 90
        and isinstance(state.get("mem_avail_mb"),(int,float)) and state["mem_avail_mb"] > 8192
        and isinstance(state.get("commit_used_pct"),(int,float)) and state["commit_used_pct"] < 85
    )
except (OSError, ValueError, KeyError, TypeError) as exc:
    gate["error"] = str(exc)[:300]

arithmetic = {"status":"HELD_BY_FRESH_COMPUTE_GATE", "rows":[]}
if gate["optional_arithmetic_allowed"]:
    arithmetic["status"] = "PASS_EXACT_ARITHMETIC_ONLY"
    for K in (2,4,16,64):
        N=K**3
        r=Fraction(1,K)
        small=2*r*(1-r)+(1-r)**2/N
        mean=Fraction(K)+small
        second=Fraction(K**4)+small
        probability=2*r-r*r+(1-r)**2/N
        q=r+(1-r)/N
        assert N*q*q == mean
        assert N*q*q+N*(N-1)*r*r == second
        assert mean*mean/second <= probability
        arithmetic["rows"].append({"K":K,"mean":str(mean),"second":str(second),
                                   "hit_probability":str(probability),"Q":str(second/(mean*mean))})

result = {
    "static_packet_validation":"PASS", "entries":len(bundle["entries"]),
    "relations":len(bundle["relations"]),"claims":len(claims),
    "retrieval_failure":{"command":"python -X utf8 ~/.claude/dreaming/brain.py recall 'C0052 3D Ising nontriviality random current proof mistakes' -n 3",
                         "timeout_seconds":60,"returned_hits":0,"outcome":"TimeoutExpired"},
    "mention_only_fallback":{"command":"python -X utf8 targeted_math_fallback.py C0052 --limit 3 --timeout 10",
                             "seconds":9.150454000104219,"related_hits":1,"exact_problem_hits":0,
                             "returned_logical_id":"math:probability.statmech:attempt-c0051-improved-two-point-function-bounds-for-the-critical-three-dimensional"},
    "bounded_exact_lookup":{"command":"python -X utf8 store_lookup.py","seconds":lookup["seconds"],
                            "exact_problem_hits":lookup["exact_problem_hits"],
                            "logical_id":lookup["rows"][0]["metadata"]["logical_id"],
                            "truth_status_preserved":lookup["rows"][0]["metadata"]["truth_status"]},
    "source_scope_checklist":{"before":old_checks,"staged_after":new_checks,
                              "before_score":sum(old_checks.values()),"staged_after_score":sum(new_checks.values()),
                              "interpretation":"Five source-recording atoms, not five independent math proofs; the draft is not ingested."},
    "compute_gate":gate,"optional_arithmetic":arithmetic,
    "seconds":time.perf_counter()-started,
    "limits":"No formal proof verification, Ising simulation, local theorem promotion, model/account attestation, or global retrieval change."}
(ROOT/"MEASUREMENTS.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"static_packet_validation":"PASS","entries":len(bundle["entries"]),
                  "relations":len(bundle["relations"]),"claims":len(claims),
                  "source_checklist":"0/5 -> 5/5 (staged)","exact_lookup_seconds":lookup["seconds"],
                  "optional_arithmetic":arithmetic["status"],"gate_mode":gate.get("mode")},indent=2))
