"""Tiny exact rational checks, not a numerical proof of C0041."""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path
from time import perf_counter

ROOT = Path(__file__).resolve().parent
START = perf_counter()
MAX_CASES = 1000
MAX_SECONDS = 5.0
cases = 0

def gate():
    global cases
    cases += 1
    if cases > MAX_CASES or perf_counter() - START > MAX_SECONDS:
        raise RuntimeError("Arithmetic resource gate exceeded; no result certified")

def solve(matrix, rhs):
    """Exact Gaussian elimination, independent of the geometric-series formula."""
    aug = [list(row) + [value] for row, value in zip(matrix, rhs)]
    for col in range(len(rhs)):
        pivot = next(i for i in range(col, len(rhs)) if aug[i][col])
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [v / scale for v in aug[col]]
        for row in range(len(rhs)):
            if row != col:
                factor = aug[row][col]
                aug[row] = [x - factor * y for x, y in zip(aug[row], aug[col])]
    return [row[-1] for row in aug]

theta = F(51, 100)
rows = {"+": (F(9,20), F(1,20), F(1,4), F(1,4)),
        "-": (F(1,20), F(9,20), F(1,4), F(1,4))}
law = {"+": theta, "-": 1-theta}
num = F(0)
den = F(0)
details = []
for s, t in product(rows, repeat=2):
    gate()
    p0, py = rows[s], rows[t]
    assert sum(p0) == sum(py) == 1 and min(p0 + py) == F(1,20)
    # U={0,-e1}; killed transition matrix in that order.
    matrix = [[F(1), -p0[1]], [-py[0], F(1)]]
    visits = solve(matrix, [F(1), F(0)])
    g = visits[0]
    assert g == 1 / (1-p0[1]*py[0])
    # Compute the no-return exit vector without using the Green formula.
    q = (F(1), 1-py[0], F(1), F(1))
    assert g * sum(p*qv for p,qv in zip(p0,q)) == 1
    mass = law[s] * law[t]
    drift = p0[0]-p0[1]
    num += mass*g*drift
    den += mass*g
    details.append({"types": s+t, "mass": str(mass), "green": str(g), "drift": str(drift)})
mean = sum(law[s]*(rows[s][0]-rows[s][1]) for s in rows)
weighted = num/den
assert mean == F(1,125) and weighted < 0

# Reflected two-site domain U={0,+e1} must reverse the occupation preference.
mirror_num = F(0)
mirror_den = F(0)
for s,t in product(rows, repeat=2):
    gate()
    p0,py = rows[s],rows[t]
    g = solve([[F(1),-p0[0]],[-py[1],F(1)]],[F(1),F(0)])[0]
    mirror_num += law[s]*law[t]*g*(p0[0]-p0[1])
    mirror_den += law[s]*law[t]*g
assert mirror_num/mirror_den > 0

# Exact threshold polynomial for the same two-site domain and general theta.
def threshold_polynomial(th):
    return 31280*th*th + 223282*th - 127281

for th in (F(1,2),F(51,100),F(53,100),F(531,1000),F(1)):
    gate()
    numerator = F(2,5)*400*((2*th-1)/391+th*(1-th)*(F(1,399)-F(1,319)))
    assert numerator == 160*threshold_polynomial(th)/49766871
assert threshold_polynomial(F(53,100)) < 0 < threshold_polynomial(F(531,1000))

# Check L3 over all 80 nonzero q vectors in {0,1,2}^4 and 12 laws.
a = F(1,4)
worst_ratio = None
generic_to_binary = []
for b in (F(1,20), F(1,10), F(1,5)):
    for th in (F(1,100), F(1,10), F(1,2), F(1)):
        p0 = (a,a,a,a)
        pp = (a+b,a-b,a,a)
        binary_bound = 2*b*th/(1+(1-th)*b/a)
        generic_bound = (a-b)*(2*b*th)/(1-3*(a-b))
        assert binary_bound >= generic_bound > 0
        generic_to_binary.append(float(binary_bound/generic_bound))
        for q in product(range(3), repeat=4):
            if not any(q):
                continue
            gate()
            d0 = sum(p*qv for p,qv in zip(p0,q))
            dp = sum(p*qv for p,qv in zip(pp,q))
            ratio = (th*2*b/dp)/((1-th)/d0+th/dp)
            formula = 2*b*th/(th+(1-th)*dp/d0)
            assert ratio == formula and ratio >= binary_bound
            assert ratio >= generic_bound
            if q == (1,0,0,0):
                assert ratio == binary_bound  # relaxed-q sharpness only
            worst_ratio = min(worst_ratio or ratio/binary_bound, ratio/binary_bound)

selected_b, selected_theta = F(1,5), F(1,10)
selected_generic = (a-selected_b)*(2*selected_b*selected_theta)/(1-3*(a-selected_b))
selected_binary = 2*selected_b*selected_theta/(1+(1-selected_theta)*selected_b/a)
receipt = {
    "status": "PASS", "command": "python -X utf8 ~/brain_workers/w450/verify_exact.py",
    "fresh_arithmetic_gate": {"max_cases": MAX_CASES,"max_seconds":MAX_SECONDS,"one_process":True,"network":False},
    "cases": cases, "wall_seconds": perf_counter()-START,
    "counterexample": {"dimension":2,"ellipticity": "1/20", "positive_type_probability":str(theta),
        "mean_one_step_drift":str(mean),"weighted_numerator":str(num),"weighted_denominator":str(den),
        "kalikow_drift":str(weighted),"kalikow_drift_decimal":float(weighted),"site_cases":details,
        "reflected_domain_drift":str(mirror_num/mirror_den),
        "threshold_polynomial":"31280*theta^2+223282*theta-127281",
        "unique_zero_bracket":["53/100","531/1000"]},
    "rare_bias_bound": {"grid_cases":960,"minimum_checked_ratio_to_bound":str(worst_ratio),
        "selected_b":str(selected_b),"selected_theta":str(selected_theta),
        "generic_bound":str(selected_generic),"binary_bound":str(selected_binary),
        "improvement_factor":str(selected_binary/selected_generic)},
    "limits": "Exact finite arithmetic confirms the displayed example and sampled formulas. General inequalities are proved in ATTEMPT.md; no simulation or formal check of C0041 was performed."
}
ROOT.joinpath("exact_receipt.json").write_text(json.dumps(receipt, indent=2)+"\n",encoding="utf-8")
print(json.dumps(receipt, indent=2))
