#!/usr/bin/env python3
"""Standard-library checker for B16 signed Gibbs phase residual theorem.

This does not prove FEI.  It checks the closed formulas and exhausts balanced
truth tables for k=3,4 at two fixed rational tilts.
"""
import itertools, math

C = 6.521851214
X = 2.0 ** (-C)
LN2 = math.log(2.0)


def fwht(vals):
    a = [float(v) for v in vals]
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                u, v = a[j], a[j+h]
                a[j], a[j+h] = u+v, u-v
        h *= 2
    return [v/n for v in a]


def phase_credit(k, lam, t):
    y = X ** (1.0-lam)
    A = (1.0+y)**k - 1.0
    bracket = 1.0 - (2.0**(t-1))*((1.0+y)**(k-t)-1.0)
    L = (y**(t/2.0)/A) * max(0.0, bracket)
    P = L*L/(4.0*LN2)
    return y, A, L, P


def kl2(p, q):
    ans = 0.0
    for a,b in zip(p,q):
        if a > 0.0:
            ans += a*math.log2(a/b)
    return ans


def exhaustive(k, lam, t):
    y,A,L,P = phase_credit(k,lam,t)
    rho = [0.0]*(1<<k)
    for s in range(1,1<<k):
        rho[s] = y**(s.bit_count())/A
    count = 0
    min_slack = float("inf")
    for neg in itertools.combinations(range(1<<k), 1<<(k-1)):
        f = [1.0]*(1<<k)
        for z in neg:
            f[z] = -1.0
        ah = fwht(f)
        assert abs(ah[0]) < 1e-12
        w = [v*v for v in ah]
        D = kl2(w[1:], rho[1:])
        min_slack = min(min_slack, D-P)
        count += 1
    return count, min_slack, y, A, L, P


def main():
    # Universal complement-pair formula: t=k has no outside-block subtraction.
    for k in range(2,12):
        for lam in (-0.5, 0.0, 0.25, 0.5, 5.0/6.0):
            y,A,L,P = phase_credit(k,lam,k)
            target = y**(k/2.0)/A
            assert abs(L-target) <= 1e-13*max(1.0,abs(target))
            assert abs(P-y**k/(4.0*LN2*A*A)) <= 1e-13*max(1.0,abs(P))

    c3, s3, y3, A3, L3, P3 = exhaustive(3, 5.0/6.0, 3)
    c4, s4, y4, A4, L4, P4 = exhaustive(4, 4.0/5.0, 4)
    assert c3 == 70 and c4 == 12870
    assert s3 >= -1e-12 and s4 >= -1e-12

    lam = 5.0/6.0
    scalar3 = math.log2(A3/X)/(lam*C)
    signed3 = (math.log2(A3/X)-P3)/(lam*C)
    assert signed3 < scalar3

    print("PASS")
    print("k3_count =", c3)
    print("k3_y = %.17g" % y3)
    print("k3_A = %.17g" % A3)
    print("k3_L = %.17g" % L3)
    print("k3_phase_credit = %.17g" % P3)
    print("k3_min_exhaustive_DminusP = %.17g" % s3)
    print("k3_scalar_threshold_same_lambda = %.17g" % scalar3)
    print("k3_signed_threshold_same_lambda = %.17g" % signed3)
    print("k3_threshold_gain = %.17g" % (scalar3-signed3))
    print("k4_count =", c4)
    print("k4_phase_credit = %.17g" % P4)
    print("k4_min_exhaustive_DminusP = %.17g" % s4)


if __name__ == "__main__":
    main()
