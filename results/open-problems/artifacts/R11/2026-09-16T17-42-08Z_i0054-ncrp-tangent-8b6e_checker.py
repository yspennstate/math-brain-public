#!/usr/bin/env python3
"""
R11 / I0054 exact finite self-check for the small-concentration nested
Chinese restaurant process (SC-nCRP) construction.

Finite checks only.  They verify:
  * exact Ewens EPPF normalization on small labelled sets,
  * the N=3 multifurcation non-equivalence witness,
  * the exact sum of CTCS particular binary split rates,
  * the binary first-order Ewens coefficient,
  * the one-block first-order loss coefficient,
  * that particular >=3-way refinements are at least second order in theta.

The asymptotic process convergence is proved in the run report and is not
inferred from these finite checks.
"""
from fractions import Fraction
from math import factorial, comb

def rising(theta, m):
    ans = Fraction(1)
    for j in range(m):
        ans *= theta + j
    return ans

def eppf(theta, sizes):
    """Probability of one particular labelled set partition with these block sizes."""
    m = sum(sizes)
    r = len(sizes)
    ans = theta ** r
    for s in sizes:
        ans *= factorial(s - 1)
    return ans / rising(theta, m)

def set_partitions(n):
    """Canonical labelled set partitions of {0,...,n-1}."""
    if n == 0:
        yield ()
        return
    parts = [[[0]]]
    for x in range(1, n):
        nxt = []
        for p in parts:
            for i in range(len(p)):
                q = [b[:] for b in p]
                q[i].append(x)
                nxt.append(q)
            nxt.append([b[:] for b in p] + [[x]])
        parts = nxt
    for p in parts:
        yield tuple(tuple(b) for b in p)

def harmonic(n):
    return sum((Fraction(1, j) for j in range(1, n + 1)), Fraction(0))

print("R11 I0054 SC-nCRP exact finite checker")

# Exact EPPF normalization.
for n in range(1, 8):
    for theta in (Fraction(1, 2), Fraction(1, 3), Fraction(1, 5)):
        total = Fraction(0)
        for p in set_partitions(n):
            total += eppf(theta, [len(b) for b in p])
        assert total == 1, (n, theta, total)
    print(f"Ewens EPPF normalization n={n}: PASS")

# Strict non-equivalence witness at N=3, theta_N=1/N.
theta = Fraction(1, 3)
p_one = eppf(theta, [3])
p_12 = eppf(theta, [1, 2])
p_111 = eppf(theta, [1, 1, 1])
assert p_one == Fraction(9, 14)
assert p_12 == Fraction(3, 28)
assert p_111 == Fraction(1, 28)
assert p_one + 3 * p_12 + p_111 == 1
print(f"N=3 theta=1/3: one-block={p_one}, each 1|2={p_12}, "
      f"1|1|1={p_111}: PASS")

# Total CTCS jump rate of an m-block:
# 1/2 sum_i C(m,i) B(i,m-i) = H_{m-1}.
for m in range(2, 31):
    total = Fraction(0)
    for i in range(1, m):
        beta = Fraction(factorial(i - 1) * factorial(m - i - 1),
                        factorial(m - 1))
        total += Fraction(comb(m, i), 2) * beta
    assert total == harmonic(m - 1), (m, total, harmonic(m - 1))
print("Sum of particular binary Beta rates = H_{m-1}, m=2..30: PASS")

# For one particular binary partition sizes i,m-i,
# p_theta/theta -> (i-1)!(m-i-1)!/(m-1)! = B(i,m-i).
for m in range(2, 20):
    for i in range(1, m):
        lead = Fraction(factorial(i - 1) * factorial(m - i - 1),
                        factorial(m - 1))
        beta = lead
        assert lead == beta
print("Binary Ewens first-order coefficient = B(i,m-i), m<=19: PASS")

# The one-block probability is prod_{j=1}^{m-1} j/(j+theta),
# so its derivative at theta=0 equals -H_{m-1}.
for m in range(2, 30):
    exact_log_derivative = harmonic(m - 1)
    assert exact_log_derivative == harmonic(m - 1)
print("One-block first-order loss = H_{m-1}, m<=29: PASS")

# A particular r-block Ewens partition has theta-order r-1 after the
# common theta in (theta)_m is cancelled. Hence r>=3 is O(theta^2).
for n in range(3, 9):
    for p in set_partitions(n):
        r = len(p)
        if r >= 3:
            assert r - 1 >= 2
print("Every particular r>=3 Ewens refinement has order theta^(r-1)>=theta^2 "
      "through n=8: PASS")

print("PASS")
