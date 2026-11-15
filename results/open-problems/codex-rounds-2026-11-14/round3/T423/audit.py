"""Small algebra and normalization checks; not a proof of SPDE uniqueness."""

from fractions import Fraction as F
from itertools import product
import math
import os
from pathlib import Path
import re


def integrated_abs(z, left, right):
    """Exact integral of |z-a| da by splitting at its kink."""
    cuts = sorted({left, right} | ({z} if left < z < right else set()))
    total = F(0)
    for a, b in zip(cuts, cuts[1:]):
        if (a + b) / 2 <= z:
            total += z * (b - a) - (b * b - a * a) / 2
        else:
            total += (b * b - a * a) / 2 - z * (b - a)
    return total


assert os.environ.get("OMP_NUM_THREADS") == "1"
print("OMP_NUM_THREADS=1; inherited nice=", os.getpriority(os.PRIO_PROCESS, 0))

# Independently integrate the Tanaka-level average, using exact rationals.
occupation_cases = 0
for eps in [F(1, 5), F(1), F(3)]:
    for j in range(-30, 31):
        z = F(j, 7)
        average = (integrated_abs(z, -eps, eps)
                   - integrated_abs(F(0), -eps, eps)) / (2 * eps)
        formula = z * z / (2 * eps) if abs(z) <= eps else abs(z) - eps / 2
        assert average == formula
        assert 0 <= abs(z) - average <= eps / 2
        occupation_cases += 1
print(f"Tanaka average and epsilon/2 error: {occupation_cases} exact rational cases")

# Compare direct weighted squared norms with the covariance expansion.
energy_cases = 0
for a, b, c, d in product([F(0), F(1, 2), F(2)], repeat=4):
    U, V, C = a*a + b*b, c*c + d*d, a*c + b*d
    for p, q in [(F(1), F(1)), (F(1, 3), F(2, 5))]:
        direct = (p*a-q*c)**2 + (p*b-q*d)**2
        expanded = p*p*U + q*q*V - 2*p*q*C
        assert direct == expanded >= 0
        energy_cases += 1
print(f"Weighted energy versus covariance expansion: {energy_cases} exact cases")

# Fréchet endpoints for two Bernoulli variables with the same mean.
for j in range(101):
    p = F(j, 100)
    for joint in [max(F(0), 2*p-1), p]:
        delta = 2*p - 2*joint
        assert 0 <= delta <= 2*min(p, 1-p)
print("Bernoulli disagreement bound: 202 exact endpoint cases")

q = math.log(2) / 3
coefficient = math.exp(-q) - 2*math.exp(-4*q)
assert abs(coefficient) < 1e-15
assert (1 - 2)**2 == 1
print(f"Noncoercivity test: weighted coefficient={coefficient:.3g}; A=1")

# A normalization check for the factor 2 in the survival tail.
t, mass = 3.0, 2.0
for horizon in [100.0, 10000.0, 1000000.0]:
    scaled = horizon * (-math.expm1(-2*mass/(horizon-t)))
    assert 0 <= scaled <= 4*mass
    print(f"Tail check: T={horizon:g}, T*(1-exp(-2S/(T-t)))={scaled:.10f}")
assert abs(scaled - 2*mass) < 1e-5
print("Tail normalization target: 2S=4")

proof = Path("PROOF.md").read_text()
report = Path("REPORT.md").read_text()
for left, right in [(r"\[", r"\]"), (r"\(", r"\)")]:
    assert proof.count(left) == proof.count(right)
labels = re.findall(r"\\tag\{([^}]+)\}", proof)
assert len(labels) == len(set(labels))
assert set(labels) == {str(j) for j in range(1, 22)}
assert report.splitlines()[0].startswith("VERDICT: PARTIAL ")
assert not Path("SOLVED_ELSEWHERE.md").exists()
print("Document checks: balanced math delimiters; labels 1..21; partial verdict")
for name in ["PROOF.md", "REPORT.md", "LOG.md", "audit.py"]:
    body = Path(name).read_text()
    print(f"{name}: {len(body.splitlines())} lines, {len(body.encode())} bytes")
