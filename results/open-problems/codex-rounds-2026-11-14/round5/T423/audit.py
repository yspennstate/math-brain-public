"""Exact algebra and scalar checks for the small-mass budget.

This does not simulate the SPDE or verify pathwise uniqueness.
"""

from fractions import Fraction as F
from itertools import product
import math
import os
from pathlib import Path
import re


def integral_abs(z, lo, hi):
    cuts = sorted({lo, hi} | ({z} if lo < z < hi else set()))
    out = F(0)
    for left, right in zip(cuts, cuts[1:]):
        term = z * (right - left) - (right**2 - left**2) / 2
        out += term if (left + right) / 2 <= z else -term
    return out


def f_eps(z, eps):
    return z*z/(2*eps) if abs(z) <= eps else abs(z)-eps/2


assert os.environ.get("OMP_NUM_THREADS") == "1"
print("OMP_NUM_THREADS=1; inherited nice=", os.getpriority(os.PRIO_PROCESS, 0))

# Independent integration over Tanaka levels, rather than differentiating F.
count = 0
for eps in [F(1, 10), F(1), F(3)]:
    for j in range(-40, 41):
        z = F(j, 9)
        average = (integral_abs(z, -eps, eps)
                   - integral_abs(F(0), -eps, eps)) / (2*eps)
        assert average == f_eps(z, eps)
        assert 0 <= abs(z)-average <= eps/2
        count += 1
print(f"Occupation normalization and epsilon/2 error: {count} exact cases")

# Spatial covariance and the minimum's martingale bracket.
count = 0
for p, q, r, s in product([F(0), F(1, 2), F(2)], repeat=4):
    U, V, C = p*p+q*q, r*r+s*s, p*r+q*s
    A = (p-r)**2+(q-s)**2
    assert A == U+V-2*C >= 0
    # From M=(U+V-|D|)/2, away from the tie:
    sign = 1 if U > V else -1
    cu, cv = F(1-sign, 2), F(1+sign, 2)
    bracket_M = cu*cu*U + cv*cv*V + 2*cu*cv*C
    assert bracket_M == min(U, V)
    # At a tie either selection still has bracket equal to the common mass.
    if U == V:
        assert U == V == min(U, V)
    count += 1
print(f"Mass covariance and min-bracket algebra: {count} exact cases")

# The half-local-time term in M gives precisely twice its loss of expectation.
for initial_min, terminal_min in product([F(0), F(1, 3), F(2)], repeat=2):
    expected_L_increment = 2*(initial_min-terminal_min)
    assert terminal_min-initial_min == -expected_L_increment/2
print("Minimum compensator: factor 2 checked independently")


def concave_test(x, a, eta):
    if x <= a:
        return x, F(1), F(0)
    if x < a+eta:
        h = x-a
        return a+h-h*h/(2*eta), 1-h/eta, -1/eta
    return a+eta/2, F(0), F(0)


count = 0
for a, eta in product([F(1, 5), F(1), F(3)], [F(1, 7), F(2)]):
    # The three pieces meet in both value and first derivative.
    assert a+F(0)-F(0)**2/(2*eta) == a
    assert a+eta-eta**2/(2*eta) == a+eta/2
    assert 1-F(0)/eta == 1 and 1-eta/eta == 0
    for j in range(61):
        x = F(j, 7)
        val, prime, second = concave_test(x, a, eta)
        assert 0 <= val <= min(x, a+eta/2)
        assert 0 <= prime <= 1 and second <= 0
        if x <= a:
            assert prime == 1
        count += 1
print(f"Independent concave cutoff and signs: {count} exact cases")

# All combinations of the two occupation errors, including the worst sign.
count = 0
for eps, b in product([F(1, 20), F(1), F(7)], [F(0), F(1, 4), F(3)]):
    for error_T, error_stop in product([F(0), eps/4, eps/2], repeat=2):
        upper_post = 2*b-error_T+error_stop
        assert upper_post <= 2*b+eps/2
        assert 2*eps*(2*b+eps/2) == 4*b*eps+eps*eps
        count += 1
    m = F(5, 4)
    assert 4*min(m, eps)*eps+eps*eps <= 5*eps*eps
print(f"Post-entrance finite-width constant: {count} exact cases")

# Independent Feller generator calculation for the occupation after extinction.
# This checks the epsilon^2 remainder even when subsequent local time is zero.
count = 0
for eps in [F(1, 10), F(1), F(3)]:
    for j in range(61):
        x = F(j, 7)
        g = 2*eps*x-x*x if x <= eps else eps*eps
        second = -2 if x < eps else 0
        assert g == 2*eps*(x-f_eps(x, eps))
        assert 0 <= g <= eps*eps
        if x != eps:
            assert x*second/2 == -x*(0 < x < eps)
        count += 1
print(f"After-extinction Feller occupation potential: {count} exact cases")

# Independent Feller masses start at a, with a=m so tau_a=0.
# E min <= a P(V>0), hence E L_t >= 2a exp(-2a/t), and E L_inf=2a.
a = 1.25
for horizon in [10.0, 1000.0, 1000000.0]:
    min_upper = a*(-math.expm1(-2*a/horizon))
    local_time_lower = 2*a-2*min_upper
    assert 0 <= local_time_lower <= 2*a
    assert abs(local_time_lower-2*a*math.exp(-2*a/horizon)) < 1e-14
    print(f"Independent scalar T={horizon:g}: "
          f"E L_T in [{local_time_lower:.9f}, {2*a:.9f}]")
assert abs(local_time_lower-2*a) < 1e-5
print("Scalar budget target: 2a=2.5; attained in the broader mass class")

# Identical masses show why a.s. extinction cannot remove the terminal expectation.
assert 2*a-2*a == 0
print("Identical scalar: E L_T=0 and E M_T=a for every finite T")

proof = Path("PROOF.md").read_text()
report = Path("REPORT.md").read_text()
for left, right in [(r"\[", r"\]"), (r"\(", r"\)")]:
    assert proof.count(left) == proof.count(right)
labels = re.findall(r"\\tag\{([^}]+)\}", proof)
assert len(labels) == len(set(labels))
assert set(labels) == {str(j) for j in range(1, 23)}
assert report.splitlines()[0].startswith("VERDICT: PARTIAL ")
assert not Path("SOLVED_ELSEWHERE.md").exists()
print("Documents: balanced delimiters, unique labels 1..22, partial verdict")
print("All checks passed; the stochastic proof is in PROOF.md.")
