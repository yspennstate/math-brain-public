"""Theorem 5.1, Corollary 5.2, Theorem 6.1 and its Case B ingredients.

A. Thm 5.1: E <= V ln(1/V) + A0 I,  A0 = 2 + ln 7 + (6/5)(3+ln 4), all regular monotone n<=4, many biases.
B. Cor 5.2: q_i in [delta,1-delta] => V ln(1/V) <= max(1.661, ln(1/delta)/(1-delta)) I.
C. Thm 6.1: E <= K_delta J, K_delta = max(2A_delta/(delta(1-delta)), 8A_delta+18.5).
D. Case B (iii)+(v): for ANY Boolean T and any coordinate 0 (no monotonicity needed for (ii)-(iii)):
     E_{>=2}(f) <= 4[(1-q0)E(U) + q0 E(V')] + 8.25[(1-q0)Var U + q0 Var V'],
     sum_{j!=0} I_j(f) = (1-q0) I(U) + q0 I(V')   (exact),
   U = 2u-1, u = T|y0=0;  V' = 2v-1, v = 1 - T|y0=1  (functions of the other coordinates).
   And (i) for monotone T: rho_j <= eps/(q_j(1-q_j)), eps = 1 - rho_0 (exact).
Logs: float64 from exact rationals (evidence); the exact parts are exact.
"""
import math
import random
import time
from fractions import Fraction as Fr
from bfcore import *

LN = math.log
A0 = 2 + LN(7) + 1.2 * (3 + LN(4))


def E_float(P, qs, ge2=False):
    s = 0.0
    for S in range(1, len(P)):
        if ge2 and popcount(S) < 2:
            continue
        p = P[S]
        if p:
            s += float(p) * LN(float(sigS2(S, qs) / p))
    return s


def vlnv(V):
    V = float(V)
    return V * LN(1 / V) if V > 0 else 0.0


def restrict(T, n, coord, val):
    """table of T with y_coord = val, as a function of the other coordinates (in increasing order)."""
    others = [c for c in range(n) if c != coord]
    tab = []
    for z in range(1 << (n - 1)):
        y = val << coord
        for b, c in enumerate(others):
            if (z >> b) & 1:
                y |= 1 << c
        tab.append(T[y])
    return tab, others


def caseB(T, qs, c0=0):
    n = len(qs)
    f = [2 * t - 1 for t in T]
    P = spectrum(f, qs)
    u, others = restrict(T, n, c0, 0)
    t1, _ = restrict(T, n, c0, 1)
    v = [1 - x for x in t1]
    qo = [qs[c] for c in others]
    PU = spectrum([2 * x - 1 for x in u], qo)
    PV = spectrum([2 * x - 1 for x in v], qo)
    VU, IU, _, _ = metrics_exact(PU)
    VV, IV, _, _ = metrics_exact(PV)
    q0 = qs[c0]
    lhs = E_float(P, qs, ge2=True)
    rhs = 4 * (float(1 - q0) * E_float(PU, qo) + float(q0) * E_float(PV, qo)) + 8.25 * float((1 - q0) * VU + q0 * VV)
    # (v) exact identity: sum_{j != 0} I_j(f) = sum_S |S minus {0}| P(S)
    Isum = Fr(0)
    for S in range(1 << n):
        Isum += popcount(S & ~(1 << c0)) * P[S]
    ident = (Isum == (1 - q0) * IU + q0 * IV)
    return lhs, rhs, ident


def rq(extreme):
    if extreme and random.random() < 0.3:
        return random.choice([Fr(1, 10 ** 6), Fr(10 ** 6 - 1, 10 ** 6), Fr(1, 1000), Fr(999, 1000)])
    return Fr(random.randint(1, 999), 1000)


if __name__ == "__main__":
    random.seed(45)
    t0 = time.time()
    # regular monotone functions n <= 4 with a desirability order
    regs = []
    for n in range(1, 5):
        for code in range(1 << (1 << n)):
            T = [(code >> y) & 1 for y in range(1 << n)]
            if is_monotone(T, n) and regular_order(T, n) is not None:
                regs.append((n, T))
    nonconst = [(n, T) for (n, T) in regs if 0 < sum(T) < len(T)]
    print("regular monotone nonconstant functions n<=4:", len(nonconst))

    # ---- A: Theorem 5.1
    worstA = -1e9
    maxratio = 0.0
    for (n, T) in nonconst:
        for rep in range(40):
            qs = [rq(True) for _ in range(n)]
            P = spectrum([2 * t - 1 for t in T], qs)
            V, I, D, J = metrics_exact(P)
            E = E_float(P, qs)
            val = (E - vlnv(V)) / float(I)
            maxratio = max(maxratio, val)
    print("A. Thm 5.1: max (E - V ln(1/V))/I over n<=4 =", round(maxratio, 4), " bound A0 =", round(A0, 4))

    # ---- B, C: floors
    for delta in [Fr(1, 2), Fr(1, 4), Fr(1, 10), Fr(1, 100), Fr(1, 1000)]:
        d = float(delta)
        bnd = max(1.661, LN(1 / d) / (1 - d))
        Ad = A0 + bnd
        Kd = max(2 * Ad / (d * (1 - d)), 8 * Ad + 18.5)
        mB = 0.0
        mC = 0.0
        for (n, T) in nonconst:
            for rep in range(15):
                qs = [random.choice([delta, 1 - delta, Fr(random.randint(int(1000 * d) if d > 0.001 else 1, 1000 - (int(1000 * d) if d > 0.001 else 1)), 1000)])
                      for _ in range(n)]
                qs = [min(max(q, delta), 1 - delta) for q in qs]
                P = spectrum([2 * t - 1 for t in T], qs)
                V, I, D, J = metrics_exact(P)
                mB = max(mB, vlnv(V) / float(I))
                if J > 0:
                    mC = max(mC, E_float(P, qs) / float(J))
        # adversarial for B: AND_k with all q = delta (tight case)
        andmax = 0.0
        for k in range(1, 13):
            qs = [delta] * k
            T = [1 if y == (1 << k) - 1 else 0 for y in range(1 << k)]
            P = spectrum([2 * t - 1 for t in T], qs)
            V, I, D, J = metrics_exact(P)
            andmax = max(andmax, vlnv(V) / float(I))
        print("B/C delta=%s: max V ln(1/V)/I = %.4f (AND_k at q=delta: %.4f), bound %.4f ; max E/J = %.3f, K_delta = %.1f"
              % (delta, mB, andmax, bnd, mC, Kd))

    # ---- D: Case B pieces, every Boolean function n <= 4, coordinate 0
    worstD = -1e9
    worst_ratio = 0.0
    idfail = 0
    cnt = 0
    for n in range(2, 5):
        for code in range(1 << (1 << n)):
            T = [(code >> y) & 1 for y in range(1 << n)]
            reps = 3 if n < 4 else 1
            for rep in range(reps):
                qs = [rq(True) for _ in range(n)]
                lhs, rhs, ident = caseB(T, qs, 0)
                cnt += 1
                if not ident:
                    idfail += 1
                worstD = max(worstD, lhs - rhs)
                if rhs > 0:
                    worst_ratio = max(worst_ratio, lhs / rhs)
                elif lhs > 1e-12:
                    worstD = max(worstD, lhs)
        print("  D n=%d done, cases %d, time %.0f" % (n, cnt, time.time() - t0))
    print("D. Case-B inequality, all Boolean T n<=4, pivot coordinate 0:", cnt, "cases; max (lhs-rhs) =", worstD,
          "; max lhs/rhs =", round(worst_ratio, 4), "; identity (v) failures:", idfail)

    # ---- (i) for monotone T, exact
    fi = 0
    ci = 0
    for (n, T) in regs:
        for c0 in range(n):
            for rep in range(5):
                qs = [rq(True) for _ in range(n)]
                w = mu_weights(qs)
                d0 = pivotal(T, n, c0)
                eps = 1 - sum(w[y] for y in range(1 << n) if d0[y] == 1)
                for j in range(n):
                    if j == c0:
                        continue
                    dj = pivotal(T, n, j)
                    rhoj = sum(w[y] for y in range(1 << n) if dj[y] == 1)
                    ci += 1
                    if rhoj > eps / (qs[j] * (1 - qs[j])):
                        fi += 1
    print("(i) rho_j <= eps/(q_j(1-q_j)) on regular monotone n<=4:", ci, "checks, failures", fi)
    print("time", round(time.time() - t0, 1))
