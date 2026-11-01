"""Structural validation is read-only; numerical controls run only on a fresh normal gate.

No formal checker or ingestion is invoked. All outputs stay in w517.
"""
from pathlib import Path
import datetime as dt
import importlib.util
import json
import math
import sys
import time

sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent
result={"checked_utc":dt.datetime.now(dt.timezone.utc).isoformat(),"formal_proof_check":False,"trusted_axioms_receipt":None}
tool_path=Path("~/math-brain-build/tools/integrate_drafts.py")
spec=importlib.util.spec_from_file_location("w517_validation_only",tool_path)
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
payload,errors=module.parse_draft(ROOT/"bundle_001.json")
assert not errors,errors
rows=[json.loads(line) for line in (ROOT/"CLAIMS.jsonl").read_text(encoding="utf-8").splitlines()]
required={"statement","assumptions","source","proof_or_counterexample","independent_reviewer","remaining_gap","status"}
assert all(required<=set(r) for r in rows)
assert all(r["status"] in {"conjecture","numerical evidence","sketch","proved special case","independently checked proof"} for r in rows)
assert len({r["id"] for r in rows})==len(rows)
assert all(e["kind"]=="concept" and e["proof_text"] is None and "DRAFT" in e["statement"] for e in payload["entries"])
result["structural"]={"integrator_parse_errors":errors,"claim_rows":len(rows),"concept_drafts":len(payload["entries"]),"relations":len(payload["relations"]),"pending_review":True}
gate_path=Path("~/.claude/compute/compute_state.json")
gate={"checked_utc":dt.datetime.now(dt.timezone.utc).isoformat()}
try:
    state=json.loads(gate_path.read_text(encoding="utf-8-sig"))
    age=time.time()-gate_path.stat().st_mtime
    gate.update(age_seconds=round(age,3),mode=state.get("mode"),cpu_pct=state.get("cpu_pct"))
    allowed=0<=age<=60 and state.get("mode")=="normal"
except (OSError,ValueError) as exc:
    gate.update(error=str(exc)); allowed=False
gate["allows_numerical_controls"]=allowed
result["fresh_gate"]=gate
if allowed:
    started=time.perf_counter()
    def simpson(fun,a,b,count=6000):
        h=(b-a)/count
        return h/3*(fun(a)+fun(b)+4*sum(fun(a+i*h) for i in range(1,count,2))+2*sum(fun(a+i*h) for i in range(2,count,2)))
    phi=lambda x:math.exp(-x*x/2)/math.sqrt(2*math.pi)
    normal_abs=2*simpson(lambda t:t*phi(t),0,10)
    assert abs(normal_abs-math.sqrt(2/math.pi))<2e-10
    result["O1_control"]={"xi":0.5,"v":1,"rho":0,"fixed_edge_prediction":0,"selected_log_mean_by_absolute_difference_quadrature":-0.5*normal_abs/math.sqrt(2),"closed_form":-0.5/math.sqrt(math.pi)}
    xi=0.5; b0=1/(xi*math.sqrt(math.pi)); lip=b0*math.exp(-0.5)/(math.sqrt(2)*xi)
    switching=[]
    for beta in (1,2,4,8,16,32,64):
        kernel=lambda u:math.exp(-abs(u))/(1+math.exp(-abs(u)))**2
        got=simpson(lambda u:kernel(u)*b0*math.exp(-u*u/(4*xi*xi*beta*beta)),-24,24)
        bound=2*math.log(2)*lip/beta+(4*beta+2*b0)*math.exp(-beta)
        assert abs(got-b0)<=bound+3e-8
        switching.append({"beta":beta,"beta_E_B":got,"limit":b0,"NT_error_bound":bound})
    result["NT_controls"]=switching
    def inverse_normal(p):
        low,high=-20.,0.
        for _ in range(80):
            mid=(low+high)/2
            if 0.5*math.erfc(-mid/math.sqrt(2))<p:low=mid
            else:high=mid
        return (low+high)/2
    medians=[]
    for n in (4,16,64,256):
        m=2**n
        p=-math.expm1(-math.log(2)/m)
        z=inverse_normal(p)
        got=-xi*z/math.sqrt(n)
        medians.append({"n":n,"independent_median_exponent":got,"common_median_exponent":0,"limiting_independent_exponent":xi*math.sqrt(2*math.log(2))})
    assert all(x["independent_median_exponent"]>0 for x in medians)
    assert medians[-1]["independent_median_exponent"]>medians[0]["independent_median_exponent"]
    result["O2_controls"]=medians
    # Independent integral of the competitive event, rather than the closed-form tail.
    p_competitive=simpson(lambda x:phi(x)*(0.5*math.erfc(x/math.sqrt(2))),-10,10)
    assert abs(p_competitive-0.5)<2e-9
    result["three_route_control"]={"xi":1,"M":0,"competitive_event_probability_by_integral":p_competitive,"isolated_pair_limit":2/math.sqrt(2*math.pi),"full_pair_limit":2/math.sqrt(2*math.pi)*p_competitive}
    q=5/math.sqrt(6); gamma=4/(q+math.sqrt(q*q-4)); dimension=gamma*math.sqrt(6)
    assert abs(dimension-4)<1e-12
    result["anchor_dimension_control"]=dimension
    result["numerical_seconds"]=time.perf_counter()-started
    result["numerical_status"]="passed bounded deterministic controls; not a proof of the limit or of LQG"
else:
    result["numerical_status"]="deferred: fresh gate does not permit numerical controls; no experiment run"
(ROOT/"VALIDATION.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
