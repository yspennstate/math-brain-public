"""(LCR) of NOTES section 7, tested exactly; and a structured family aimed at breaking it.

(LCR):  sum_{k>=1} W_k ln(1/W_k)  <=  sum_k sum_i W_k pi_i^(k) ln^+(4 pi_i^(k)/sigma_i^2)  +  C I,
pi_i^(k) = (sum_{|S|=k, S contains i} P(S)) / W_k.   The route conjectures an absolute C for weighted thresholds.

Candidate breaker ("anti-diagonal tribes"): n = 2m, weights w_i = i, theta = n+1, so the minimal 2-sets are the
pairs i+j >= n+1; biases q_i = b r^(i-1) make every anti-diagonal pair {i, n+1-i} equally likely
(q_i q_{n+1-i} = b^2 r^(n-1)) and every other minimal set lighter by a factor r (pairs) or b/r (triples).
The level-2 spectral sample is then (nearly) uniform over m disjoint pairs, each coordinate has inclusion
probability ~1/m, and the per-coordinate credit overcharges the choice of the pair by ln m.
Heuristic prediction: excess/I ~ (1/2) ln m - ln 2.
"""
import sys
import time
from fractions import Fraction as Fr
import mpmath
from bfcore import *

mpmath.mp.dps = 40


def lcr_data(T, qs):
    n = len(qs)
    P = spectrum([2 * t - 1 for t in T], qs)
    V, I, D, J = metrics_exact(P)
    lhs = mpmath.mpf(0)
    cred = mpmath.mpf(0)
    for k in range(1, n + 1):
        sets = [S for S in range(1 << n) if popcount(S) == k and P[S] != 0]
        Wk = sum(P[S] for S in sets)
        if Wk == 0:
            continue
        lhs += mpq(Wk) * mpmath.log(mpq(1 / Wk))
        for i in range(n):
            mass = sum(P[S] for S in sets if (S >> i) & 1)
            if mass == 0:
                continue
            pik = mass / Wk
            arg = 4 * pik / sig2(qs[i])
            if arg > 1:
                cred += mpq(mass) * mpmath.log(mpq(arg))
    # global credit (CR) for comparison
    gcred = mpmath.mpf(0)
    for i in range(n):
        Ii = sum(P[S] for S in range(1 << n) if (S >> i) & 1)
        if Ii == 0:
            continue
        arg = 4 * (Ii / sig2(qs[i])) / V
        if arg > 1:
            gcred += mpq(Ii) * mpmath.log(mpq(arg))
    vlv = mpq(V) * mpmath.log(mpq(1 / V))
    E = corrected_entropy(P, qs)
    return dict(lcr=(lhs - cred) / mpq(I), cr=(vlv - gcred) / mpq(I), ratio=E / mpmath.log(2) / mpq(D),
                EI=E / mpq(I), P=P, I=I, V=V)


def antidiag(m, r, b):
    n = 2 * m
    T = threshold_table(list(range(1, n + 1)), n + 1)
    qs = [b * r ** i for i in range(n)]
    return T, qs


if __name__ == "__main__":
    t0 = time.time()
    print("control: route's T_s family (route reports LCR excess/I = -0.77, -0.73 for s = 4, 8)")
    for s in [4, 8]:
        x = Fr(1, s)
        p = x / 50
        a = p ** s
        ph = a * (1 - x) / (x + a * (1 - x))
        T = [1 if (s * (y & 1) + popcount(y >> 1)) >= s else 0 for y in range(1 << (s + 1))]
        d = lcr_data(T, [ph] + [p] * s)
        print("  s=%d  LCR excess/I = %s   CR excess/I = %s" % (s, mpmath.nstr(d["lcr"], 6), mpmath.nstr(d["cr"], 6)))
    print("anti-diagonal tribes thresholds, exact full spectra")
    for m in range(2, 8):
        n = 2 * m
        r = Fr(1, n * n)
        b = r / (n * n)
        T, qs = antidiag(m, r, b)
        d = lcr_data(T, qs)
        pred = mpmath.log(m) / 2 - mpmath.log(2)
        print("  m=%d n=%2d  LCR excess/I = %s  (heuristic (ln m)/2 - ln 2 = %s)  CR excess/I = %s  H+/Delta = %s  t=%.0fs"
              % (m, n, mpmath.nstr(d["lcr"], 8), mpmath.nstr(pred, 6), mpmath.nstr(d["cr"], 8),
                 mpmath.nstr(d["ratio"], 6), time.time() - t0))
        sys.stdout.flush()
