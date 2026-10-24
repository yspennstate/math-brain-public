"""Bounded exact arithmetic and finite geometry controls; no sampling/training."""

import itertools
import json
import time
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path

from block_bridge_guard import assess_block_bridge

ROOT = Path(__file__).resolve().parent
import psutil
fresh_memory = psutil.virtual_memory()
fresh_gate = {"checked_at": datetime.now(timezone.utc).isoformat(),
              "policy": "Existing compute_sense permits short light work while forbidding model-heavy/GPU launches; deterministic arithmetic only.",
              "cpu_percent": psutil.cpu_percent(interval=0.05),
              "available_memory_mb": fresh_memory.available // (1024*1024),
              "workers": 1, "uses_gpu": False, "model_loads": 0,
              "bounded_work": "12 small window geometries; 256 truth tables on three bits; exact integer controls."}
(ROOT / "COMPUTE_GATE.json").write_text(json.dumps(fresh_gate, indent=2), encoding="utf-8")
start = time.perf_counter()
checks = 0


def require(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def evaluate(delta, r, **kwargs):
    defaults = dict(sigma_field_independence_verified=True, finite_bit_count=100, compatibility_verified=True)
    defaults.update(kwargs)
    return assess_block_bridge(delta, r, **defaults)


# Independently enumerate windows to verify the exchangeability formula's sets.
for d in range(1, 5):
    for length in range(1, 4):
        origins = [(0,) * d]
        for index in range(d):
            for sign in (-1, 1):
                center = [0] * d
                center[index] = sign
                origins.append(tuple(center))
        windows = []
        for center in origins:
            windows.append({tuple(a+b for a, b in zip(center, offset))
                            for offset in itertools.product(range(-length, length+1), repeat=d)})
        common = set.intersection(*windows)
        union = set.union(*windows)
        side = 2*length+1
        require(len(common) == (side-2)**d, f"intersection d={d}, L={length}")
        require(len(union) == side**(d-1)*(side+2*d), f"union d={d}, L={length}")

# Exact closed-form counterexamples, not Monte Carlo or an observed brain rule.
counterexamples = []
for length in (1000, 10000, 100000):
    d = 3
    side = 2*length+1
    good = Fraction((side-2)**d, side**(d-1)*(side+2*d))
    r = 2*length+2
    unguarded_inference = good >= Fraction(99, 100)
    decision = evaluate(1-good, r)
    require(unguarded_inference, "control must trigger the unguarded high-density inference")
    require(decision.status == "ABSTAIN", "range-aware guard must withhold the false percolation certificate")
    counterexamples.append({"d": d, "L": length, "good_density_exact": str(good), "good_density": float(good),
                            "range": r, "all_components_finite": True, "component_size_upper_bound": side**d,
                            "unguarded_false_positive": unguarded_inference,
                            "guard_status": decision.status, "criterion_exponent": decision.exponent})

positive_controls = []
for r in (0, 1, 2):
    exponent = 6*(r+1)**2
    bound = Fraction(1, 2**(exponent+1))
    decision = evaluate(bound, r)
    require(decision.status == "SUFFICIENT_CONDITIONAL_BRIDGE", "strict-margin control")
    require(evaluate(Fraction(1, 2**exponent), r).status == "ABSTAIN", "equality cannot support parameter lowering")
    require(evaluate(Fraction(1, 2**exponent)+Fraction(1, 2**(exponent+10)), r).status == "ABSTAIN", "just above threshold")
    positive_controls.append({"r": r, "bad_bound": str(bound), "status": decision.status})

# Numerical corner cases and missing hypotheses must not silently pass.
require(evaluate(Fraction(1, 2**4000), 1).status == "SUFFICIENT_CONDITIONAL_BRIDGE", "no float underflow")
require(evaluate(Fraction(1, 1000), 10**9).status == "ABSTAIN", "huge ranges must not allocate huge powers")
require(evaluate(Fraction(0), 0, sigma_field_independence_verified=False).status == "ABSTAIN", "missing sigma-field proof")
require(evaluate(Fraction(0), 0, compatibility_verified=False).status == "ABSTAIN", "missing compatibility proof")
require(evaluate(Fraction(0), None).status == "ABSTAIN", "missing range")
require(evaluate(None, 0).status == "ABSTAIN", "missing marginal")
require(evaluate(Fraction(0), 0, finite_bit_count=None).status == "ABSTAIN", "missing finite bit count")
require(evaluate(Fraction(0), 0).status == "SUFFICIENT_CONDITIONAL_BRIDGE", "zero bad probability")

# Exhaust all event truth tables on three bits; coupling bound covers nonmonotone events.
states = list(itertools.product((0, 1), repeat=3))
p = Fraction(1, 3)
pp = Fraction(2, 3)
coupling_bound = 1-(1-abs(p-pp))**3
for table in range(2**len(states)):
    probabilities = []
    for parameter in (p, pp):
        total = Fraction(0)
        for index, state in enumerate(states):
            if table & (1 << index):
                ones = sum(state)
                total += parameter**ones * (1-parameter)**(3-ones)
        probabilities.append(total)
    require(abs(probabilities[0]-probabilities[1]) <= coupling_bound, "finite-event coupling oracle")

measurements = {"command": "python -X utf8 verify_bridge.py", "checks": checks, "elapsed_seconds": time.perf_counter()-start,
                "fresh_compute_gate": fresh_gate,
                "counterexamples": counterexamples, "positive_controls": positive_controls,
                "unguarded_false_certificates": sum(row["unguarded_false_positive"] for row in counterexamples),
                "guarded_false_certificates": sum(row["guard_status"] != "ABSTAIN" for row in counterexamples),
                "scope": "Constructed deterministic reasoning controls, not a live retrieval benchmark, general recall gain, or proof of C0023."}
(ROOT / "MEASUREMENTS.json").write_text(json.dumps(measurements, indent=2), encoding="utf-8")
print(json.dumps(measurements, indent=2))
