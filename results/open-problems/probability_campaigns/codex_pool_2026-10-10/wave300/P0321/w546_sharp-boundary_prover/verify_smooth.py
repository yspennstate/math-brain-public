"""Check L05 by direct Gaussian quadrature and independent Fourier coefficients."""
import os
for name in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS","NUMEXPR_NUM_THREADS"):
    os.environ[name]="1"
import json
import math
from pathlib import Path
import time
root=Path(__file__).resolve().parent
gate=json.loads((root/"COMPUTE_GATE_SMOOTH.json").read_text(encoding="utf-8-sig"))
wall,cpu=time.monotonic(),time.process_time()
from scipy.integrate import quad
from scipy.special import j0,j1,jv
def budget():
    if time.monotonic()-wall>gate["max_wall_seconds"] or time.process_time()-cpu>gate["max_cpu_seconds"]:
        raise RuntimeError("fresh smooth-check compute gate exceeded")
budget()
m,A=6,1/12
z=m*A
c0_direct=quad(lambda t:math.cos(t+z*math.sin(t)),0,2*math.pi,epsabs=1e-12)[0]/(2*math.pi)
c0_exact=-j1(z)
assert abs(c0_direct-c0_exact)<1e-12
rows=[]
for v in (0.1,1.0,10.0):
    budget()
    sigma=math.sqrt(v)
    # Uniform angular integration has the independent Bessel addition identity;
    # this integral is over the Gaussian increment, not over Fourier harmonics.
    direct=2*quad(lambda delta: math.cos(m*delta)*j0(2*z*math.sin(m*delta/2))*math.exp(-delta*delta/(2*v))/math.sqrt(2*math.pi*v),0,10*sigma,epsabs=1e-12,epsrel=1e-12,limit=400)[0]
    series=sum(float(jv(n-1,z))**2*math.exp(-m*m*n*n*v/2) for n in range(-20,21))
    exact_variance=v+A*A*(1-math.exp(-m*m*v/2))
    gaussian_prediction_same_variance=math.exp(-m*m*exact_variance/2)
    rows.append({"gaussian_increment_variance":v,"smooth_increment_variance":exact_variance,"variance_change":exact_variance-v,"sixfold_direct_integral":direct,"sixfold_fourier_series":series,"gaussian_prediction_using_smooth_variance":gaussian_prediction_same_variance,"direct_minus_series":direct-series,"actual_to_gaussian_prediction":direct/gaussian_prediction_same_variance})
    assert abs(direct-series)<2e-11
    assert direct>=c0_exact*c0_exact-2e-11
    budget()
assert abs(rows[-1]["sixfold_direct_integral"]-c0_exact*c0_exact)<2e-11
result={"status":"PASS","claim_id":"P0321-w546-L05","command":"python -X utf8 verify_smooth.py","gate":gate,"cpu_seconds":time.process_time()-cpu,"wall_seconds":time.monotonic()-wall,"smooth_map_derivative_lower_bound":1-m*A,"variance_error_bound":A*A,"orientational_plateau":c0_exact*c0_exact,"coefficient_direct_error":abs(c0_direct-c0_exact),"correlation_max_direct_series_error":max(abs(r["direct_minus_series"]) for r in rows),"rows":rows,"scope":"auxiliary counterexample only; not a microscopic Gibbs phase or formal check"}
(root/"VERIFICATION_SMOOTH.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
print(json.dumps({k:v for k,v in result.items() if k not in ("rows","gate")},indent=2))
