"""Exact rational finite-graph checks, under the adjacent fresh COMPUTE_GATE.json."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import time

ROOT = Path(__file__).resolve().parent
START = time.monotonic()
EDGES = [(x, x ^ (1 << k)) for x in range(8) for k in range(3) if x < (x ^ (1 << k))]

def check(spin_weights, site_weights, label):
    n = len(site_weights)
    z = sum(spin_weights.values())
    moments = {}
    for mask in range(1 << n):
        moments[mask] = F(sum(value * (-1 if (state & mask).bit_count() % 2 else 1)
                              for state, value in spin_weights.items()), z)
    def moment(sites):
        mask = 0
        for x in sites:
            mask ^= 1 << x
        return moments[mask]
    g = [[moment((x, y)) for y in range(n)] for x in range(n)]
    h = [sum(site_weights[y] * g[x][y] for y in range(n)) for x in range(n)]
    v = sum(site_weights[x] * h[x] for x in range(n))
    assert v > 0
    q = [site_weights[x] * h[x] / v for x in range(n)]
    assert sum(q) == 1 and min(q) >= 0
    repeated = F(0)
    distinct = F(0)
    all_fourth = F(0)
    for a, b, c, d in product(range(n), repeat=4):
        u = moment((a,b,c,d)) - g[a][b]*g[c][d] - g[a][c]*g[b][d] - g[a][d]*g[b][c]
        assert u <= 0
        factor = site_weights[a] * site_weights[b] * site_weights[c] * site_weights[d]
        all_fourth += factor * moment((a,b,c,d))
        if len({a,b,c,d}) < 4:
            repeated -= factor * u
        else:
            distinct -= factor * u
    aa = sum(site_weights[x]**2 * h[x]**2 for x in range(n))
    bb = sum(site_weights[x]**2 * site_weights[y]**2 * g[x][y]**2
             for x in range(n) for y in range(n))
    cc = sum(site_weights[x]**3 * h[x] for x in range(n))
    ee = sum(w**4 for w in site_weights)
    formula = 12*aa - 6*bb - 16*cc + 12*ee
    assert repeated == formula
    bound = 12*sum(x*x for x in q)
    assert 0 <= repeated/v**2 <= bound
    assert repeated + distinct == 3*v*v - all_fourth
    direct2 = sum(value * sum(site_weights[x] * (-1 if state & (1 << x) else 1)
                             for x in range(n))**2 for state,value in spin_weights.items()) / F(z)
    direct4 = sum(value * sum(site_weights[x] * (-1 if state & (1 << x) else 1)
                             for x in range(n))**4 for state,value in spin_weights.items()) / F(z)
    assert direct2 == v and direct4 == all_fourth
    if len(set(site_weights)) == 1:
        assert repeated/v**2 <= F(12,n)
    return {"case":label,"configurations":len(spin_weights),"ordered_quadruples":n**4,
            "variance_exact":str(v),"contact_ratio_exact":str(repeated/v**2),
            "contact_ratio":float(repeated/v**2),"distinct_ratio":float(distinct/v**2),
            "total_ratio":float((repeated+distinct)/v**2),"bound":float(bound),
            "formula_error_exact":"0","full_moment_error_exact":"0"}

cases = []
for r in (1,2,4):
    sw = {state:r**sum(bool(state & (1 << x)) == bool(state & (1 << y))
                       for x,y in EDGES) for state in range(256)}
    for w,label in (([1]*8,"uniform"),([1,2,0,1,3,0,1,2],"inhomogeneous"),
                    ([1,0,0,0,0,0,0,0],"localized")):
        cases.append(check(sw,w,f"cube-r={r}-{label}"))
cases.append(check({0:1,255:1},[1]*8,"fully-locked-zero-temperature-limit"))
elapsed = time.monotonic()-START
result = {"gate":"COMPUTE_GATE.json","method":"stdlib Fraction, exhaustive finite cube; integer Boltzmann weights r^aligned, beta=log(r)/2",
          "cases":cases,"checks_passed":len(cases),"seconds":elapsed,
          "theorem_proof":False,"maximum_configurations_per_case":256,
          "maximum_ordered_quadruples_per_case":4096}
(ROOT/"measurements.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"checks_passed":len(cases),"seconds":elapsed,"cases":cases},indent=2))
