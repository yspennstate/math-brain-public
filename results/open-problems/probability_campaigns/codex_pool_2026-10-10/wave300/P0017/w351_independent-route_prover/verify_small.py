"""Reproducible mathematical checks; numerical mode fails closed at the live gate."""
import argparse
import ast
from datetime import datetime, timezone
from fractions import Fraction as F
import json
import math
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parent
STATE = Path("~/.claude/compute/compute_state.json")

def artifact_checks():
    rows = [json.loads(line) for line in (ROOT / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    required = {"id", "statement", "assumptions", "source", "proof", "independent_reviewer", "remaining_gap", "status"}
    allowed = {"conjecture", "numerical evidence", "sketch", "proved special case", "independently checked proof"}
    for row in rows:
        assert required <= row.keys(), row["id"]
        assert row["status"] in allowed
        assert row["proof"] and row["assumptions"]
        assert not row.get("novelty_claim")
    assert len({row["id"] for row in rows}) == len(rows)
    for name in ("SOURCE_STATUS.json", "RECALL_RECEIPT.json", "COMPUTE_GATE.json"):
        json.loads((ROOT / name).read_text(encoding="utf-8-sig"))
    for name in ("verify_small.py", "build_bundle.py", "recall_bounded.py"):
        ast.parse((ROOT / name).read_text(encoding="utf-8"), filename=name)
    result = {"status":"passed", "claim_rows":len(rows), "independently_checked_rows":sum(row["status"] == "independently checked proof" for row in rows), "math_proof_certification":False, "python_sources_parsed":3}
    if (ROOT / "bundle_001.json").exists():
        bundle = json.loads((ROOT / "bundle_001.json").read_text(encoding="utf-8"))
        keys = {e["key"] for e in bundle["entries"]}
        assert len(keys) == len(bundle["entries"])
        kinds = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
        for entry in bundle["entries"]:
            assert entry["kind"] in {"definition", "concept"}
            assert entry["proof_text"] is None
            assert entry["source"]["license"].startswith("owner-own-work")
        for relation in bundle["relations"]:
            assert relation["from_key"] in keys and relation["kind"] in kinds
            assert relation.get("to_key") in keys or relation.get("to_existing_logical", "").startswith("math:")
            assert relation["rationale"]
        result.update(draft_entries=len(bundle["entries"]), relations=len(bundle["relations"]))
    (ROOT / "ARTIFACT_CHECKS.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    return result

def numerical_checks():
    state = json.loads(STATE.read_text(encoding="utf-8"))
    age = time.time() - STATE.stat().st_mtime
    reason_text = " ".join(map(str, state.get("reasons", []))).lower()
    telemetry = [state.get(k) for k in ("cpu_pct", "mem_avail_mb", "commit_avail_mb", "commit_used_pct", "hung_windows")]
    missing = not all(isinstance(value, (int,float)) and math.isfinite(value) for value in telemetry)
    held = (not 0 <= age <= 120 or state.get("status") != "ok" or "critical" in reason_text
            or state.get("mode") not in {"owner_present_polite", "owner_away_open", "open"} or missing)
    if not missing:
        held = held or state["cpu_pct"] >= 95 or state["mem_avail_mb"] <= 8192 or state["commit_avail_mb"] <= 16384 or state["commit_used_pct"] >= 85 or state["hung_windows"] > 0
    receipt = {"checked_at":datetime.now(timezone.utc).isoformat(), "source":str(STATE), "age_seconds":age, "governor_status":state.get("status"), "mode":state.get("mode"), "reasons":state.get("reasons"), "status":"HELD" if held else "admitted", "gpu":False, "threads":1, "models":False, "cpu_budget_seconds":3}
    (ROOT / "NUMERICAL_GATE.json").write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
    if held:
        print(json.dumps(receipt))
        return 75
    started = time.process_time()
    def budget():
        if time.process_time() - started > 3:
            raise TimeoutError("small-check CPU budget exceeded")
    # Independent finite-probability saturation check for the projection lemma.
    r = F(1,2)
    outcomes = [(u,v,(1+r*u*v)/4) for u in (-1,1) for v in (-1,1)]
    variance = sum(p*(u+v)**2 for u,v,p in outcomes)
    conditional_sum = F(0)
    for which in (0,1):
        for value in (-1,1):
            selected = [(u,v,p) for u,v,p in outcomes if (u,v)[which] == value]
            mass = sum(p for u,v,p in selected)
            mean = sum(p*(u+v) for u,v,p in selected)/mass
            conditional_sum += sum(p*((u+v)-mean)**2 for u,v,p in selected)
    assert variance == conditional_sum/(1-r) == 3
    assert variance > conditional_sum
    # Direct barycentric covariance, without using the simplified covariance formula.
    covariance_cells = 0
    for N in (3,5,9):
        for i in range(N):
            for j in range(N):
                value = sum((F(int(i==k))-F(1,N))*(F(int(j==l))-F(1,N))*F(1+int(k==l),N*(N+1))*N*(N+1) for k in range(N) for l in range(N))
                assert value == F(int(i==j))-F(1,N)
                covariance_cells += 1
            budget()
    def simpson(fn, lo, hi, count=400):
        h = (hi-lo)/count
        return h/3*(fn(lo)+fn(hi)+sum((4 if i%2 else 2)*fn(lo+i*h) for i in range(1,count)))
    beta_moment_errors = []
    for n in (2,3,8):
        for k in (2,4):
            measured = simpson(lambda s: n*(n-1)*s**(k+1)*(1-s)**(n-2), 0,1)
            exact = math.prod(range(2,2+k))/math.prod(range(n+1,n+1+k))
            beta_moment_errors.append(abs(measured-exact))
    assert max(beta_moment_errors) < 2e-8
    # An explicit C1 bump in the n=2 projected interval, with full transverse energy.
    def amplitude(s):
        z=(s-.9)/.05
        return 16*z*z*(1-z)*(1-z)
    def amplitude_prime(s):
        z=(s-.9)/.05
        return 32*z*(1-z)*(1-2*z)/.05
    L2=24.
    A=simpson(lambda s:2*s*amplitude(s)**2,.9,.95)
    D=simpson(lambda s:2*amplitude(s)**2/s,.9,.95)
    directional_ratio=L2/math.pi**2*A/D
    average_slice_constant=12/math.pi**2
    assert directional_ratio > average_slice_constant
    transverse=simpson(lambda s:2*s*simpson(lambda u:(amplitude_prime(s)*math.sin(math.pi*u)-amplitude(s)*math.pi*u/s*math.cos(math.pi*u))**2,-.5,.5,160),.9,.95,200)/18
    full_ratio=(A/2)/(math.pi**2*D/(2*L2)+transverse)
    assert 0 < full_ratio < directional_ratio
    budget()
    scaling=[]
    for n in (2,3,8,32,128,1000):
        N=n+1
        scaling.append({"n":n,"worst_slice_over_average":str(F(N*(N+1),6)),"nonlinear_correlation_lower_bound_squared":str(F((N-2)*(7*N+9),3*(N-1)*(5*N+6))),"mass_S_gt_half":str(F(n+1,2**n))})
    result={"status":"passed", "cpu_seconds":time.process_time()-started,"projection_tight_variance":str(variance),"incorrect_independence_bound":str(conditional_sum),"exact_covariance_cells":covariance_cells,"maximum_beta_moment_error":max(beta_moment_errors),"n2_directional_ratio":directional_ratio,"n2_incorrect_average_bound":average_slice_constant,"n2_full_gradient_ratio":full_ratio,"scaling":scaling,"proof_certification":False}
    (ROOT / "NUMERICAL_RESULTS.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result))
    return 0

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--numerical",action="store_true")
    args=parser.parse_args()
    if args.numerical:
        raise SystemExit(numerical_checks())
    print(json.dumps(artifact_checks()))
