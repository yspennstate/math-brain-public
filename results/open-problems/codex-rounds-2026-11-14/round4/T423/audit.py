"""Algebra and scalar-coupling checks; no SPDE simulation or uniqueness claim."""

from fractions import Fraction as F
from itertools import product
import math
import os
from pathlib import Path
import re


assert os.environ.get("OMP_NUM_THREADS") == "1"
print("OMP_NUM_THREADS=1; inherited nice=", os.getpriority(os.PRIO_PROCESS, 0))

# Exact backward-ODE and rescaled-kernel arithmetic, independently of Ito.
cases = 0
for horizon, fraction, lam in product(
        [F(1), F(3), F(100)], [F(0), F(1, 3), F(1)],
        [F(1, 2), F(2), F(10)]):
    s = horizon * fraction
    theta = lam / horizon
    den = 1 + (horizon - s) * theta / 2
    b = theta / den
    b_prime = theta * theta / (2 * den * den)
    assert b_prime == b*b/2
    assert b == lam / (horizon + (horizon-s)*lam/2)
    assert 0 < horizon*b <= lam
    # Time derivative -b' x and Ito correction b^2 x/2 cancel.
    for mass in [F(0), F(1, 7), F(9)]:
        assert -b_prime*mass + b*b*mass/2 == 0
    # Two opposite +/- L/2 drifts, after subtracting, give b dL.
    assert -(-F(1, 2))*b - (-F(1, 2)*b) == b
    # Exact endpoint-Laplace exponent gap controls the uniform error.
    m = F(5, 3)
    low = 2*m/horizon*lam/(lam+2)
    high = 2*m/horizon
    assert 2*horizon*(high-low) == 8*m/(lam+2)
    cases += 1
print(f"Backward drift, kernel bound, Tanaka factor, error constant: {cases} exact cases")

# Independent recheck of the mass-difference covariance normalization.
cases = 0
for a, b, c, d in product([F(0), F(1, 2), F(3)], repeat=4):
    U, V, C = a*a+b*b, c*c+d*d, a*c+b*d
    assert (a-c)**2+(b-d)**2 == U+V-2*C
    cases += 1
print(f"Direct square-root discrepancy versus covariance expansion: {cases} exact cases")

# Uniform approximation: use a cancellation-resistant exponential difference.
cases = 0
for m, horizon, lam in product([0.0, 0.2, 3.0],
                              [0.01, 1.0, 1000.0], [0.2, 2.0, 30.0]):
    low = (2*m/horizon)*lam/(lam+2)
    gap = (2*m/horizon)*2/(lam+2)
    actual = 2*horizon*math.exp(-low)*(-math.expm1(-gap))
    bound = 8*m/(lam+2)
    assert -1e-14 <= actual <= bound + 1e-12
    cases += 1
print(f"Uniform extinction-approximation bound: {cases} numerical cases")

# U=X+Y, V=X+Z, independent Feller masses initially a,b,b.
# Direct extinction probabilities and a separate E|min| bound give
# tail coefficient 4b and ell=2b. These are not SPDE constructions.
for a, b in [(1.0, 0.0), (0.0, 1.0), (2.0, 0.5)]:
    target = 4*b
    values = []
    for horizon in [100.0, 10000.0, 1000000.0]:
        survival_b = -math.expm1(-2*b/horizon)
        delta = 2*math.exp(-2*(a+b)/horizon)*survival_b
        scaled = horizon*delta
        values.append(f"{scaled:.9f}")
        assert 0 <= scaled <= target + 1e-12
    assert abs(scaled-target) < 4e-5
    print(f"Scalar a={a:g}, b={b:g}: T*delta={', '.join(values)}; target={target:g}")

# Independent terminal-Laplace check, using elementary sandwich bounds.
# For Y,Z independent, B=1-exp(-theta Y), B'=1-exp(-theta Z):
# E|B-B'|=2 EB-2 E min(B,B'), with E min <= P(Z>0)*EB.
# The shared X multiplies the absolute difference by its Laplace transform.
for lam in [0.5, 2.0, 10.0]:
    horizon, a, b = 1000000.0, 2.0, 0.5
    laplace_x = math.exp(-a*lam/(horizon*(1+lam/2)))
    expected_B = -math.expm1(-b*lam/(horizon*(1+lam/2)))
    extinction_b = math.exp(-2*b/horizon)
    lower = 2*horizon*laplace_x*expected_B*extinction_b
    upper = 2*horizon*laplace_x*expected_B
    target = 4*b*lam/(lam+2)
    assert lower <= upper
    assert abs(lower-target) < 1e-5 and abs(upper-target) < 1e-5
    print(f"Finite lambda={lam:g}: scalar bounds [{lower:.9f}, {upper:.9f}], target={target:.9f}")

proof = Path("PROOF.md").read_text()
report = Path("REPORT.md").read_text()
for left, right in [(r"\[", r"\]"), (r"\(", r"\)")]:
    assert proof.count(left) == proof.count(right)
labels = re.findall(r"\\tag\{([^}]+)\}", proof)
assert len(labels) == len(set(labels))
assert set(labels) == {str(j) for j in range(1, 24)}
assert report.splitlines()[0] == "VERDICT: PARTIAL exact inverse-time extinction-disagreement coefficient"
assert not Path("SOLVED_ELSEWHERE.md").exists()
print("Documents: balanced delimiters, unique labels 1..23, partial verdict")
print("All checks passed; analytic SPDE conclusions depend on PROOF.md, not these checks.")
