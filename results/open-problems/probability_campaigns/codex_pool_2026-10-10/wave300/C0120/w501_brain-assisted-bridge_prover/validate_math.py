import json
import math
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parent
started = time.monotonic()

def simpson(fun, left, right, panels):
    assert panels % 2 == 0 and panels <= 4000
    step = (right-left)/panels
    return (step/3)*(fun(left)+fun(right)+sum((4 if k%2 else 2)*fun(left+k*step) for k in range(1,panels)))

# Actual source model at n=2: M=g_0+max(g_1,g_2).
# max(g_1,g_2)=(g_1+g_2+|g_1-g_2|)/2 gives Var(M)=2-1/pi.
# Coupled signs have correlation e^-t, so h(t)=3/2+asin(e^-t)/pi.
# The substitution u=sin(theta) avoids an endpoint square-root singularity.
exact_variance = 2-1/math.pi
integrated_overlap = 1.5+simpson(lambda theta: theta*math.cos(theta), 0, math.pi/2, 1000)/math.pi
error = abs(integrated_overlap-exact_variance)
assert error < 1e-11, error
n2_certificate = 1+simpson(lambda u: 2**(-(1-u)/(1+u)),0,1,2000)
assert n2_certificate > exact_variance+1e-4
checks = []
for n in (2,10,100,1000):
    log_n = math.log(n)
    for t in (0, n**-0.5, 0.1, 1.0, 3.0):
        a = math.tanh(t/2)
        uniform_envelope = sum(k**-a for k in range(1,n+1))
        lower = n**(1-a)
        assert uniform_envelope+1e-10 >= lower
        concentrated_envelope = float(n)
        assert concentrated_envelope+1e-10 >= uniform_envelope
        checks.append({"n":n,"t":t,"uniform_envelope":uniform_envelope,"lower":lower})
    # Independently integrate the scalar lower-bound envelope in u=e^-t.
    integral = n*simpson(lambda u: math.exp(-log_n*(1-u)/(1+u)),0,1,2000)
    assert integral+1e-9 >= (n-1)/log_n
    checks.append({"n":n,"integrated_scalar_envelope":integral,"certified_lower":(n-1)/log_n})
elapsed = time.monotonic()-started
assert elapsed < 30, elapsed
receipt = {"schema":"w501-math-check-v1","elapsed_seconds":elapsed,"n2_exact_variance":exact_variance,
           "n2_integrated_overlap":integrated_overlap,"n2_absolute_error":error,"envelope_cases":len(checks),
           "n2_hypercontractive_certificate":n2_certificate,"n2_certificate_minus_actual_variance":n2_certificate-exact_variance,
           "checks":checks,"passed":True,"is_proof_of_parent_problem":False,"formal_check":False}
(ROOT/"math_check_receipt.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in receipt.items() if k!="checks"}))
