#!/usr/bin/env python3
"""Reproduce B12 branch-information calibration numbers.

No external packages are required. The seed constants are the lower endpoints
recorded in the owner-directed FEI sprint report; this script does not re-audit
the external seed.
"""
from decimal import Decimal, getcontext
import math

getcontext().prec = 70

SEED_H_LO = Decimal("6.776605309005978082519790221891882314787235038")
SEED_I = Decimal(261) / Decimal(128)
LN2 = Decimal(2).ln()


def log2_decimal_integer(n: int) -> Decimal:
    return Decimal(n).ln() / LN2


def seed_branch_lower(r: int):
    i = SEED_I
    limit = SEED_H_LO / (i - 1)
    I_r = i ** r
    H_over_I = limit * (Decimal(1) - i ** (-r))
    N_r = 18 ** r
    # C_br = H-J and J <= H(K) <= log2(N+1).
    penalty = log2_decimal_integer(N_r + 1) / I_r
    return I_r, H_over_I, penalty, H_over_I - penalty


def majority_branch_ratio(n: int):
    assert n >= 3 and n % 2 == 1
    m = (n - 1) // 2
    logA = math.lgamma(2*m + 1) - 2*math.lgamma(m + 1) - 2*m*math.log(2.0)
    A = math.exp(logA)
    I = n * A
    cbr = 0.0
    total = 0.0
    for r in range(m + 1):
        k = 2*r + 1
        logW = (
            2*logA + math.log(2*m + 1) - math.log(2*r + 1)
            + 2*(math.lgamma(m + 1)-math.lgamma(r + 1)-math.lgamma(m-r + 1))
            - (math.lgamma(2*m + 1)-math.lgamma(2*r + 1)-math.lgamma(2*m-2*r + 1))
        )
        W = math.exp(logW)
        total += W
        logC = (math.lgamma(n+1)-math.lgamma(k+1)-math.lgamma(n-k+1))/math.log(2.0)
        cbr += W * logC
    return I, total, cbr / I


if __name__ == "__main__":
    print("seed_limit_H_over_I =", SEED_H_LO / (SEED_I - 1))
    print("r  I_r  H_r/I_r  H(K)/I upper  C_br/I lower")
    for r in (1,2,3,4,5,7,10,15,20):
        vals = seed_branch_lower(r)
        print(r, *(str(v) for v in vals))
    print()
    print("majority n  I  mass_sum  C_br/I")
    for n in (13,151,251,501,1001,5001,10001):
        I, mass, ratio = majority_branch_ratio(n)
        print(n, f"{I:.15g}", f"{mass:.15g}", f"{ratio:.15g}")
    print("2 log2(e) =", 2.0 / math.log(2.0))
