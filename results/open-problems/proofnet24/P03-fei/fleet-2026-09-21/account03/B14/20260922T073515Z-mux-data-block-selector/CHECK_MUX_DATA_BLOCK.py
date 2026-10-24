#!/usr/bin/env python3
"""Regression check for the exact MUX data-block selector identities.

This is not the proof.  It independently samples interior product biases and
checks the algebraic identities used in REPORT.md for the physical block
T={D0,D1}.  Only Python's standard library is used.
"""
import math
import random

LN2 = math.log(2.0)

def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -(x*math.log(x)+(1.0-x)*math.log(1.0-x))/LN2

def entropy(ps):
    return -sum(p*math.log(p)/LN2 for p in ps if p > 0.0)

def V(x):
    return 4.0*x*(1.0-x)

# A generic symmetric boundary-normalized test potential.
def gamma(x):
    y = x*(1.0-x)
    return 0.7*y + 0.2*y*y

def trial(t, q0, q1):
    a = 1.0-t
    d = q0+q1-2.0*q0*q1
    r = a*q0+t*q1
    Vt, V0, V1 = V(t), V(q0), V(q1)

    # Exact six nonzero biased-Walsh squared masses of the one-bit MUX.
    weights = [
        (1.0-2.0*r)**2,
        Vt*(q1-q0)**2,
        a*a*V0,
        t*t*V1,
        t*a*V0,
        t*a*V1,
    ]
    Hparent = entropy(weights)

    it0 = V0*a
    it1 = V1*t
    itA = Vt*d

    # Closed form from the two-data-bit block entropy cocycle.
    C = (d*h2(Vt) + h2(q0)+h2(it0) + h2(q1)+h2(it1)
         - Hparent)

    # Data-layer subset K has only empty, {D0}, {D1}; never {D0,D1}.
    HK = entropy([1.0-it0-it1, it0, it1])
    TC = h2(it0)+h2(it1)-HK
    TC_lower = it0*it1/LN2

    B = lambda x: gamma(x)+h2(V(x))
    Ddirect = d*B(t)+a*B(q0)+t*B(q1)-gamma(r)-Hparent
    Rblock = (d*gamma(t)-gamma(r)
              + a*B(q0)+t*B(q1)
              - h2(q0)-h2(it0)-h2(q1)-h2(it1))

    I = itA+it0+it1
    W = I/4.0-r*(1.0-r)
    Wclosed = t*a*(V0+V1)/4.0
    return weights, C, TC, TC_lower, Ddirect, Rblock, W, Wclosed

def main():
    random.seed(20260922)
    n = 200000
    max_weight_sum_error = 0.0
    max_defect_cocycle_error = 0.0
    max_W_closed_error = 0.0
    min_C_minus_TC = float("inf")
    min_TC_minus_lower = float("inf")

    for _ in range(n):
        t, q0, q1 = random.random(), random.random(), random.random()
        weights, C, TC, lower, D, R, W, Wclosed = trial(t,q0,q1)
        max_weight_sum_error = max(max_weight_sum_error,
                                   abs(sum(weights)-1.0))
        max_defect_cocycle_error = max(max_defect_cocycle_error,
                                       abs(D-(R+C)))
        max_W_closed_error = max(max_W_closed_error, abs(W-Wclosed))
        min_C_minus_TC = min(min_C_minus_TC, C-TC)
        min_TC_minus_lower = min(min_TC_minus_lower, TC-lower)

    print("samples =", n)
    print("max_weight_sum_error =", f"{max_weight_sum_error:.3e}")
    print("max_defect_cocycle_error =", f"{max_defect_cocycle_error:.3e}")
    print("max_W_closed_error =", f"{max_W_closed_error:.3e}")
    print("min_C_minus_TC =", f"{min_C_minus_TC:.12e}")
    print("min_TC_minus_ab_over_ln2 =", f"{min_TC_minus_lower:.12e}")

    assert max_weight_sum_error < 1e-12
    assert max_defect_cocycle_error < 1e-12
    assert max_W_closed_error < 1e-12
    assert min_C_minus_TC > -1e-12
    assert min_TC_minus_lower > -1e-12
    print("PASS")

if __name__ == "__main__":
    main()
