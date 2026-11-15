"""Numerical cross-checks of explicit proof constants, not a proof substitute."""
import json
import math
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
x = .01
direct = sum((2*n+1)**2 * x**n for n in range(4, 100))
# Successive terms have ratio <= x*(11/9)^2, for n>=4.
upper = 81*x**4 / (1 - x*(11/9)**2)
assert direct <= upper < 1e-6
rows = []
for d in (2, 3, 5):
    vd = math.pi**(d/2) / math.gamma(d/2+1)
    for fraction in (.1, .5, .9):
        alpha = fraction / 2**d
        q = alpha * 2**d
        kappa = (1+q)/(2*q)
        rd = 2*alpha / (vd*(1-q))
        mu = 2**d*vd*rd
        lhs = mu/q-1
        rhs = kappa*mu
        assert abs(lhs-rhs) < 1e-10
        assert kappa > 1
        H = kappa*math.log(kappa)-kappa+1
        assert H > 0
        rows.append({"d":d,"alpha":alpha,"r_power_d_min":rd,"mu":mu,
                     "kappa":kappa,"H":H,"threshold_identity_error":lhs-rhs})
out = {"contour_sum_direct":direct,"contour_sum_geometric_upper":upper,
       "Chernoff_threshold_cases":rows,"status":"passed"}
(ROOT / "data" / "proof_constant_checks.json").write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k != 'Chernoff_threshold_cases'}, indent=2))
