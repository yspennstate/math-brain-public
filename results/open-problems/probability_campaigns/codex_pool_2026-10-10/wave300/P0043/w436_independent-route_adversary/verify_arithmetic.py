"""Bounded exact checks of the two independent tree calculations; no simulation."""
from fractions import Fraction as F
from pathlib import Path
import json
import time

ROOT = Path(__file__).resolve().parent
started = time.perf_counter()
N = 4095
mean = F(1)
second = F(1)
reciprocal_sum = F(0)
for n in range(1, N + 1):
    children = 8 if n & (n - 1) == 0 else 2
    offspring_mean = F(children, 2)
    offspring_variance = F(children, 4)
    second = offspring_mean**2 * second + offspring_variance * mean
    mean *= offspring_mean
    reciprocal_sum += 1 / mean
    assert mean == 4**n.bit_length(), (n, "generation-size identity")
    assert second / mean**2 == 1 + reciprocal_sum / 2, (n, "conditional moment identity")
    assert 1 / (second / mean**2) >= F(4, 5), (n, "critical lower bound")
    assert mean <= 4 * n**2, (n, "subcritical polynomial prefactor")

# N is the endpoint of twelve full dyadic blocks. The omitted geometric tail
# is known exactly and is checked separately rather than truncated silently.
dyadic_tail = F(1, 2 * (N + 1))
assert reciprocal_sum + dyadic_tail == F(1, 2)
host_ray_energy = 1 + (reciprocal_sum + dyadic_tail) / 2
assert host_ray_energy == F(5, 4)

# Reproduce the OTHER author's square-block sum independently, including tail.
K = 24
square_sum = sum((F(2*k + 1, 2**k) for k in range(1, K + 1)), F(0))
square_tail = F(2*K + 5, 2**K)
assert square_sum + square_tail == 5
assert 1 + (square_sum + square_tail) / 2 == F(7, 2)

row = {
    "command": "python -X utf8 verify_arithmetic.py",
    "check_type": "deterministic exact rational arithmetic; not a proof of P0043",
    "generations_checked": N,
    "identities_per_generation": 4,
    "failed_assertions": 0,
    "dyadic_partial_reciprocal_sum": str(reciprocal_sum),
    "dyadic_omitted_tail": str(dyadic_tail),
    "dyadic_full_sum": "1/2",
    "dyadic_second_moment_upper_bound": "5/4",
    "dyadic_critical_survival_lower_bound": "4/5",
    "square_blocks_checked": K,
    "square_tail": str(square_tail),
    "square_full_sum": "5",
    "square_energy": "7/2",
    "elapsed_seconds": round(time.perf_counter() - started, 6),
}
(ROOT / "MEASUREMENTS.json").write_text(json.dumps(row, indent=2)+"\n", encoding="utf-8")
print(json.dumps(row, indent=2), flush=True)
