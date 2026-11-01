"""Exact finite controls for algebra; not a proof verifier or lattice experiment."""
from fractions import Fraction as F
import json
from pathlib import Path
from time import perf_counter

start = perf_counter()
checks = 0

def require(condition):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(f"control {checks} failed")

ratios = [F(n, 20) for n in range(1, 20)]
rates = [F(k) for k in (0, 1, 2, 4, 6, 8, 10)]
critical_zero = 0
noncritical_nonzero = 0
for u in ratios:
    log_derivative = F(2, 3) * (2*u-1) / (u*(1-u))
    for rate in rates:
        # Generator obtained directly from the quotient process and Ito correction.
        actual = 2*(1/u-u) + rate*(u-1) + rate*log_derivative*(1-u)**2/2
        target = (6-rate)*(1/u-u)/3
        require(actual == target)
        require((actual == 0) == (rate == 6))
        if rate == 6:
            critical_zero += 1
        else:
            noncritical_nonzero += 1

two_pair_forces_variance_six = 0
for x in range(1, 5):
    for y in range(x+1, 7):
        for z in range(y+1, 8):
            x, y, z = F(x), F(y), F(z)
            s12, s13 = 1/x+1/y, 1/x+1/z
            require(s12-s13 > 0)
            for rate in rates:
                drift = s12*(2-rate/3)
                # Enforce the first martingale; test what the second one requires.
                second_residual = drift-s13*(2-rate/3)
                require((second_residual == 0) == (rate == 6))
            two_pair_forces_variance_six += 1

counterexample_points = 0
for numerator in range(1, 21):
    y = F(numerator, 10)
    t = (4-y*y)/8
    x = y/2
    w = 3-3*y/2
    g1, g2 = 3-y, 3-y/2
    yp = -4/y
    require(F(0) <= t < F(1, 2))
    require(g1-w == x and g2-w == y)
    require(-yp == 2/x and -yp/2 == 2/y)
    require(x/y == F(1, 2))
    require(-3*yp/2 == 2*(1/x+1/y))
    counterexample_points += 1
u = F(1, 3)
third_initial_du = 2/F(9)*(1/u-u)+(u-1)/3*3
require(third_initial_du == F(-2, 27))

result = {
    "command": "python -X utf8 ~/brain_workers/w412/verify_cardy_algebra.py",
    "arithmetic": "fractions.Fraction, exact rational equalities",
    "checks": checks,
    "failures": 0,
    "critical_zero_drift_controls": critical_zero,
    "noncritical_nonzero_drift_controls": noncritical_nonzero,
    "ordered_mark_triples": two_pair_forces_variance_six,
    "counterexample_points": counterexample_points,
    "third_observable_initial_ratio_derivative": str(third_initial_du),
    "before": {"one_observable_premise": "admits one explicit non-Brownian driver"},
    "after": {"two_observable_premise": "rejects that driver; identities force variance six in every finite control"},
    "elapsed_seconds": perf_counter()-start,
    "scope": "Finite algebra controls only. No continuum probability theorem, square-lattice Cardy limit, formal proof, or independent review is certified."
}
Path(__file__).with_name("MEASUREMENTS.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result), flush=True)
