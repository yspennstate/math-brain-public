#!/usr/bin/env python3
from fractions import Fraction
from math import factorial
from decimal import Decimal, getcontext

getcontext().prec = 50

def exp_lower_integer(R: int, N: int) -> Fraction:
    """Exact lower bound sum_{n=0}^N R^n/n! < exp(R)."""
    term = Fraction(1, 1)
    s = term
    for n in range(1, N + 1):
        term *= Fraction(R, n)
        s += term
    return s

def gamma_positive_part_poly(k: int, R: int) -> Fraction:
    """P with psi_k(R)=exp(-R) P for integer-shape Gamma(k,1)."""
    return sum((Fraction((k-r) * (R ** r), factorial(r)) for r in range(k)), Fraction(0,1))

def psi_upper(k: int, R: int, N: int = 180) -> Fraction:
    # exp(-R) < 1 / sum_{n=0}^N R^n/n!
    return gamma_positive_part_poly(k, R) / exp_lower_integer(R, N)

def dec(x: Fraction) -> Decimal:
    return Decimal(x.numerator) / Decimal(x.denominator)

# The exact coefficient identity behind the positive-part formula:
# int_R^infty P(Gamma(k,1)>t) dt
# = exp(-R) sum_{m=0}^{k-1} sum_{r=0}^m R^r/r!
# = exp(-R) sum_{r=0}^{k-1} (k-r) R^r/r!.
for k in range(1, 21):
    lhs_counts = [sum(1 for m in range(k) if m >= r) for r in range(k)]
    rhs_counts = [k-r for r in range(k)]
    assert lhs_counts == rhs_counts

M = 49
checks = [
    # q, k=2q, R, exact rational target for M psi_k(R)
    (4, 8, 35, Fraction(1, 1_500_000)),
    (6, 12, 40, Fraction(1, 200_000)),
    (8, 16, 50, Fraction(1, 2_000_000)),
    (10, 20, 57, Fraction(1, 2_000_000)),
]
print("PROB10-10 exact source-domination tail certificate")
print("Taylor exp lower truncation N = 180")
for q,k,R,target in checks:
    assert k == 2*q
    up = M * psi_upper(k,R,180)
    ok = up < target
    print(f"q={q} k={k} R={R}")
    print(f"  exact_upper_decimal = {dec(up)}")
    print(f"  target_decimal      = {dec(target)}")
    print(f"  exact_comparison    = {ok}")
    assert ok

# Source-facing L=4 Bellman threshold and a safe reserve after q=4,R=35 pruning.
lambda_star = Fraction(3002823, 1250000)
safe_eps = Fraction(1, 1_500_000)
reserved = lambda_star - safe_eps
assert reserved == Fraction(18016933, 7500000)
assert reserved + safe_eps == lambda_star
print("lambda_star =", dec(lambda_star))
print("safe_q4_R35_pruning_budget <", dec(safe_eps))
print("sufficient_pruned_lambda <=", dec(reserved), "=", f"{reserved.numerator}/{reserved.denominator}")

# Deterministic samplewise negation of zero-loss deletion, with equality in the delay bound.
# Sources a and i; activation y_a=0, y_i=35.
# A chosen a->i path has realized cost 36, and i->o has cost 1.
# A separate a->o route costs 100.
# Full system reaches o at min(100,35+1)=36.
# After deleting i, it reaches o at min(100,36+1)=37.
# epsilon_i=(0+36-35)_+=1, so loss is positive and equals epsilon_i.
y_a = Fraction(0)
y_i = Fraction(35)
a_i = Fraction(36)
i_o = Fraction(1)
a_o = Fraction(100)
full = min(a_o, y_i+i_o)
pruned = min(a_o, y_a+a_i+i_o)
eps = max(Fraction(0), y_a+a_i-y_i)
assert full == 36 and pruned == 37 and eps == 1
assert pruned-full == eps
print("ZERO_LOSS_DELETION_FALSE = True")
print("TOY_DELAY_BOUND_ATTAINED = True")
print("ALL_EXACT_CHECKS_PASS = True")
