"""Finite checks of examples, not a substitute for independent proof review."""
import json
import math
import pathlib
import time

root = pathlib.Path(__file__).resolve().parent
started = time.perf_counter()
a, cutoff, distance = 0.25, 1e8, 1e9
effective = (1+distance**2)**(-a/2)
microscopic = effective*math.exp(-(distance/cutoff)**2)
additive_bound = cutoff**(-a)
assert abs(effective-microscopic) <= additive_bound
assert microscopic < 0.5*effective

def laplace0(v):
    return math.exp(-v)*math.cosh(v/2)

def laplace1(v):
    return math.exp(-v)*(0.5+0.5*math.cosh(v/math.sqrt(2)))

delta_bound = math.exp(-1.5)/98304
alpha_bound = math.exp(-3)/(4*98304**2)
rows = []
for u, v in [(0,0), (0.1,0.2), (0.5,0.5), (1/3,2/3), (0.9,0.9)]:
    areas = [u*v, u*(1-v), (1-u)*v, (1-u)*(1-v)]
    assert math.isclose(sum(areas), 1)
    q0 = math.prod(laplace0(s) for s in areas)
    q1 = math.prod(laplace1(s) for s in areas)
    assert q1-q0 >= delta_bound
    assert (q1-q0)**2/4 >= alpha_bound
    rows.append({"grid_phase": [u,v], "conditional_void_probability_0": q0,
                 "conditional_void_probability_1": q1,
                 "conditional_regime_variance": (q1-q0)**2/4})
out = {"gate": "compute_gate.json", "command": "python -X utf8 check_math_examples.py", "seconds": time.perf_counter()-started,
       "fixed_additive_counterexample": {"a": a, "cutoff_R": cutoff, "distance_r": distance,
                                         "A": effective, "B": microscopic, "uniform_additive_bound": additive_bound,
                                         "relative_ratio_B_over_A": microscopic/effective,
                                         "algebraic_lower_transfer_fails": True},
       "cox_example": {"analytic_uniform_void_gap_lower_bound": delta_bound,
                       "analytic_alpha_lower_bound": alpha_bound,
                       "finite_phase_checks": rows},
       "checks_passed": 6, "proof_status": "finite sanity checks only; independent mathematical referee pending"}
(root/"math_checks.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
print(json.dumps(out))
