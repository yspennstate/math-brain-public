"""BT-11 (evidence) reproduction and the same Gibbs bounds on the anti-diagonal family.

Gibbs bound with level-k product reference theta_k and EXACT normalizer Z_k = e_k(theta_k):
   B = sum_k [ W_k ln(Z_k / W_k) + sum_{|S|=k} P(S) sum_{i in S} ln(sigma_i^2 / theta_k(i)) ]  >=  E.
 paper-type:  theta_k(i) = max(sigma_i^2 min(1,(k/Lam_i)^a), 4 pi_i),      pi_i = I_i / V
 level-dep.:  theta_k(i) = max(sigma_i^2 min(1,(k/Lam_i)^a), 4 pi_i^(k))
a = 6/5, Lam_i = sum of sigma_j^2 over coordinates of larger weight (the desirability order).
"""
import sys
import time
from fractions import Fraction as Fr
import mpmath
from bfcore import *

mpmath.mp.dps = 40
A = mpmath.mpf(6) / 5


def esym(vals, k):
    e = [mpmath.mpf(1)] + [mpmath.mpf(0)] * k
    for v in vals:
        for j in range(k, 0, -1):
            e[j] += v * e[j - 1]
    return e[k]


def gibbs(T, qs, weights):
    n = len(qs)
    P = spectrum([2 * t - 1 for t in T], qs)
    V, I, D, J = metrics_exact(P)
    E = corrected_entropy(P, qs)
    sig = [mpq(sig2(q)) for q in qs]
    order = sorted(range(n), key=lambda i: -weights[i])
    Lam = [mpmath.mpf(0)] * n
    acc = mpmath.mpf(0)
    for i in order:
        Lam[i] = acc
        acc += sig[i]
    Ii = [sum(P[S] for S in range(1 << n) if (S >> i) & 1) for i in range(n)]
    pi = [mpq(Ii[i] / V) for i in range(n)]
    out = {}
    for kind in ("paper", "level"):
        B = mpmath.mpf(0)
        for k in range(1, n + 1):
            sets = [S for S in range(1 << n) if popcount(S) == k and P[S]]
            if not sets:
                continue
            Wk = sum(P[S] for S in sets)
            if kind == "paper":
                ref = pi
            else:
                ref = [mpq(sum(P[S] for S in sets if (S >> i) & 1) / Wk) for i in range(n)]
            th = []
            for i in range(n):
                rk = sig[i] * (min(mpmath.mpf(1), (k / Lam[i]) ** A) if Lam[i] > 0 else 1)
                th.append(max(rk, 4 * ref[i]))
            Zk = esym(th, k)
            cost = mpmath.mpf(0)
            for S in sets:
                c = mpmath.mpf(0)
                for i in range(n):
                    if (S >> i) & 1:
                        c += mpmath.log(sig[i] / th[i])
                cost += mpq(P[S]) * c
            B += mpq(Wk) * mpmath.log(Zk / mpq(Wk)) + cost
        out[kind] = B / mpq(I)
    out["E"] = E / mpq(I)
    return out


if __name__ == "__main__":
    t0 = time.time()
    print("T_s family (route reports E/I 0.622, 0.662, 0.674; paper-type exact-Z 1.351, 1.286, 1.238; level-dep 0.631, 0.671, 0.683)")
    for s in [4, 8, 12]:
        x = Fr(1, s)
        p = x / 50
        a = p ** s
        ph = a * (1 - x) / (x + a * (1 - x))
        T = [1 if (s * (y & 1) + popcount(y >> 1)) >= s else 0 for y in range(1 << (s + 1))]
        g = gibbs(T, [ph] + [p] * s, [s] + [1] * s)
        print("  s=%2d  E/I=%s  paper-type B/I=%s  level-dep B/I=%s  t=%.0fs" % (
            s, mpmath.nstr(g["E"], 5), mpmath.nstr(g["paper"], 5), mpmath.nstr(g["level"], 5), time.time() - t0))
        sys.stdout.flush()
    print("anti-diagonal family: T = 1[sum i y_i >= n+1], q_i = r^(i+2), r = 1/(4m^2)")
    for m in range(2, 7):
        n = 2 * m
        r = Fr(1, 4 * m * m)
        T = threshold_table(list(range(1, n + 1)), n + 1)
        qs = [r ** (i + 3) for i in range(n)]
        g = gibbs(T, qs, list(range(1, n + 1)))
        print("  m=%d  E/I=%s  paper-type B/I=%s  level-dep B/I=%s   (1/2)ln(2m-1) = %s  t=%.0fs" % (
            m, mpmath.nstr(g["E"], 5), mpmath.nstr(g["paper"], 5), mpmath.nstr(g["level"], 5),
            mpmath.nstr(mpmath.log(2 * m - 1) / 2, 5), time.time() - t0))
        sys.stdout.flush()
