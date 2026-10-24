"""Tiny surrogate checks behind a fresh cached local compute gate; not a Riesz experiment or proof audit."""
from datetime import datetime, timezone
import json
import math
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parents[1]
state_path = Path("~/.claude/compute/compute_state.json")
now = time.time()
try:
    state = json.loads(state_path.read_text(encoding="utf-8-sig"))
    age = now - state_path.stat().st_mtime
    status = state.get("status")
    allowed = 0 <= age <= 60 and status in ("ok", "warn")
    receipt = {"read_at_utc": datetime.now(timezone.utc).isoformat(), "source": str(state_path), "age_s": age, "status": status, "allowed_tiny_cpu_checks": allowed, "reasons": state.get("reasons", []), "maximum_checks": 20, "gpu": False}
except (OSError, ValueError) as error:
    allowed = False
    receipt = {"read_at_utc": datetime.now(timezone.utc).isoformat(), "allowed_tiny_cpu_checks": False, "reason": str(error), "maximum_checks": 20, "gpu": False}
(ROOT / "evidence" / "compute_gate.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
if not allowed:
    result = {"state": "not_run_gate_denied", "checks_run": 0, "gate": "evidence/compute_gate.json", "mathematical_proof": False}
    (ROOT / "evidence" / "pressure_checks.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result))
    raise SystemExit(75)

start = time.process_time()
checks = []
def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)

def logsumexp(values):
    top = max(values)
    return top + math.log(sum(math.exp(value-top) for value in values))

def response(beta, n, h, a, c=None):
    values = (-a, a) if c is None else (-a, 0.0, a)
    log_weights = (0.0, 0.0) if c is None else (0.0, c*n, 0.0)
    tilted = [w+beta*h*n*x for w, x in zip(log_weights, values)]
    log_z = logsumexp(tilted)
    p = (log_z-logsumexp(log_weights))/(beta*n)
    m = sum(x*math.exp(w-log_z) for x,w in zip(values,tilted))
    return p, m

beta, a = 1.7, 0.6
for n in (10_000, 100_000):
    p, m = response(beta,n,0.07,a)
    check(f"coherent pressure cusp n={n}", abs(p-a*0.07)<=math.log(2)/(beta*n)+1e-12)
    check(f"volume first response n={n}", abs(m-a)<1e-10)
    check(f"finite zero-field symmetry n={n}", response(beta,n,0.0,a)[1]==0.0)
n=1_000_000
check("field removed too fast loses response", abs(response(beta,n,1/n**2,a)[1])<1e-5)
check("slower diagonal preserves response", abs(response(beta,n,1/math.sqrt(n),a)[1]-a)<1e-10)
beta,c,a,n=2.0,0.4,0.7,1000
check("rare ordered branch has no small-field response", abs(response(beta,n,0.1,a,c)[1])<1e-50)
check("rare ordered branch orders above nonzero field threshold", abs(response(beta,n,0.5,a,c)[1]-a)<1e-10)
for h in (0.0,0.1,0.5,-0.5):
    p,_=response(beta,n,h,a,c)
    check(f"C4 limiting pressure h={h}", abs(p-max(a*abs(h)-c/beta,0))<=math.log(3)/(beta*n)+1e-12)
result={"state":"passed","checks_run":len(checks),"checks":checks,"cpu_s":time.process_time()-start,"gate":"evidence/compute_gate.json","mathematical_proof":False,"scope":"Finite probability surrogates for limit order and conditional-branch failure; no Riesz simulation"}
(ROOT/"evidence"/"pressure_checks.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
print(json.dumps(result))
