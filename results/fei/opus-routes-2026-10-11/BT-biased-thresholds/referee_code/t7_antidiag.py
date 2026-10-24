"""Anti-diagonal tribes thresholds: a weighted-threshold family that breaks (LCR) and every level-2 product reference.

T_m = 1[ sum_{i=1}^{n} i*y_i >= n+1 ],  n = 2m,  q_i = r^(i+2)  (so q_i q_{n+1-i} = r^(n+5) for every i).

Referee lemma (proved in REFEREE.md section 3): for monotone T, if every level-2 credit argument
4 pi_i^(2)/sigma_i^2 is >= 1, then
   LCR-excess  >=  W_2 [ 2 H(u) - H_2 - 4 ln 2 ]  -  R,
   u_i = M_{i,2}/(2 W_2),  H_2 = entropy of the level-2 set law,
   R = sum_i ln(1/(q_i(1-q_i))) (I_i - M_{i,2}),  M_{i,2} = sum_{|S|=2, S contains i} P(S).
And for ANY positive weights theta, the level-2 Gibbs bound has slack W_2 KL(nu_2 || Q_theta) with
   KL(nu_2 || Q_theta) >= nu_2(M) H(nu_2(.|M)) - h(nu_2(M)),   M = the m anti-diagonal pairs.

Part 1: exact full spectra (m <= 7): exact LCR excess, the lemma's bound, the numerically optimal product
        reference (inf over theta of KL, by convex minimization) against the analytic lower bound.
Part 2: structured computation for larger m: all level-1 and level-2 masses from exact generating functions
        (truncated at degree n), in mpmath interval arithmetic, giving a certified lower bound for LCR-excess/I.
"""
import math
import sys
import time
from fractions import Fraction as Fr
import mpmath
from mpmath import iv
from bfcore import *

mpmath.mp.dps = 40


# ---------------------------------------------------------------- Part 1 (exact full spectra)
def part1(m, r):
    n = 2 * m
    T = threshold_table(list(range(1, n + 1)), n + 1)
    qs = [r ** (i + 3) for i in range(n)]  # coordinate index i (0-based) has weight i+1 and bias r^((i+1)+2)
    P = spectrum([2 * t - 1 for t in T], qs)
    V, I, D, J = metrics_exact(P)
    # exact LCR excess
    lhs = mpmath.mpf(0)
    cred = mpmath.mpf(0)
    levels = {}
    for S in range(1, 1 << n):
        if P[S]:
            levels.setdefault(popcount(S), []).append(S)
    for k, sets in levels.items():
        Wk = sum(P[S] for S in sets)
        lhs += mpq(Wk) * mpmath.log(mpq(1 / Wk))
        for i in range(n):
            mass = sum(P[S] for S in sets if (S >> i) & 1)
            if mass:
                arg = 4 * mass / (Wk * sig2(qs[i]))
                if arg > 1:
                    cred += mpq(mass) * mpmath.log(mpq(arg))
    excess = (lhs - cred) / mpq(I)
    # lemma bound
    pairs = levels[2]
    W2 = sum(P[S] for S in pairs)
    M2 = [sum(P[S] for S in pairs if (S >> i) & 1) for i in range(n)]
    Ii = [sum(P[S] for S in range(1 << n) if (S >> i) & 1) for i in range(n)]
    cond = all(4 * M2[i] / (W2 * sig2(qs[i])) >= 1 for i in range(n) if M2[i])
    H2 = -sum(mpq(P[S] / W2) * mpmath.log(mpq(P[S] / W2)) for S in pairs)
    Hu = -sum(mpq(M2[i] / (2 * W2)) * mpmath.log(mpq(M2[i] / (2 * W2))) for i in range(n) if M2[i])
    R = sum(mpmath.log(mpq(1 / (qs[i] * (1 - qs[i])))) * mpq(Ii[i] - M2[i]) for i in range(n))
    lb = (mpq(W2) * (2 * Hu - H2 - 4 * mpmath.log(2)) - R) / mpq(I)
    # product-reference obstruction at level 2
    anti = [(1 << i) | (1 << (n - 1 - i)) for i in range(m)]
    nuM = sum(P[S] for S in anti) / W2
    HnuM = -sum(mpq(P[S] / (W2 * nuM)) * mpmath.log(mpq(P[S] / (W2 * nuM))) for S in anti)
    hb = -(mpq(nuM) * mpmath.log(mpq(nuM)) + (mpq(1 - nuM) * mpmath.log(mpq(1 - nuM)) if nuM < 1 else 0))
    kl_lb = mpq(nuM) * HnuM - hb
    # numerical inf over theta of KL(nu_2 || Q_theta): convex in x = log theta
    import numpy as np
    from scipy.optimize import minimize
    nu = [(S, float(P[S] / W2)) for S in pairs]
    Hnu = -sum(p * math.log(p) for _, p in nu if p > 0)
    idx = [[i for i in range(n) if (S >> i) & 1] for S, _ in nu]
    w = np.array([p for _, p in nu])
    A = np.array(idx)

    def F(x):
        th = np.exp(x - x.max())
        e2 = (th.sum() ** 2 - (th ** 2).sum()) / 2
        val = math.log(e2) + 2 * x.max() - float(w @ (x[A[:, 0]] + x[A[:, 1]]))
        # gradient
        s = th.sum()
        g = th * (s - th) / e2
        gl = np.zeros(n)
        np.add.at(gl, A[:, 0], w)
        np.add.at(gl, A[:, 1], w)
        return val, g - gl
    best = None
    for start in range(4):
        x0 = np.random.default_rng(start).normal(0, 1, n)
        res = minimize(F, x0, jac=True, method="L-BFGS-B")
        if best is None or res.fun < best:
            best = res.fun
    klinf = best - Hnu
    E = corrected_entropy(P, qs)
    return dict(excess=excess, lb=lb, cond=cond, klinf=klinf, kl_lb=kl_lb, ln2m1=math.log(2 * m - 1),
                ratio=E / mpmath.log(2) / mpq(D), EI=E / mpq(I), W2I=mpq(W2) / mpq(I), nuM=nuM)


# ---------------------------------------------------------------- Part 2 (structured, interval arithmetic)
def polymul_trunc(a, b, deg, zero):
    out = [zero] * (deg + 1)
    for i, x in enumerate(a):
        if i > deg:
            break
        for j, y in enumerate(b):
            if i + j > deg:
                break
            out[i + j] += x * y
    return out


def part2(m, rexp, dps=60):
    """q_i = r^(i+2), r = 2^-rexp; weights 1..n; threshold n+1.  Interval arithmetic throughout."""
    iv.dps = dps
    n = 2 * m
    deg = n
    one = iv.mpf(1)
    zero = iv.mpf(0)
    r = iv.mpf(2) ** (-rexp)
    q = [None] + [r ** (i + 2) for i in range(1, n + 1)]          # 1-based
    s2 = [None] + [4 * q[i] * (1 - q[i]) for i in range(1, n + 1)]
    L = [None] + [iv.log(1 / (q[i] * (1 - q[i]))) for i in range(1, n + 1)]
    def mulfac(a, i):
        """a(z) * (1 - q_i + q_i z^i), truncated at degree deg (a is a full-length list)."""
        out = [(one - q[i]) * a[k] for k in range(deg + 1)]
        for k in range(i, deg + 1):
            out[k] += q[i] * a[k - i]
        return out
    base = [one] + [zero] * deg
    pre = [base]
    for i in range(1, n + 1):
        pre.append(mulfac(pre[-1], i))
    suf = [None] * (n + 2)
    suf[n + 1] = base
    for i in range(n, 0, -1):
        suf[i] = mulfac(suf[i + 1], i)
    rho, M1 = {}, {}
    Fm = {}
    for i in range(1, n + 1):
        Fi = polymul_trunc(pre[i - 1], suf[i + 1], deg, zero)     # law of N_{-i} on [0, n]
        Fi = Fi + [zero] * (deg + 1 - len(Fi))
        Fm[i] = Fi
        rho[i] = sum(Fi[n + 1 - i: n + 1], zero)                  # pivotal iff n+1-i <= N_{-i} <= n
    P2 = {}
    for i in range(1, n + 1):
        Fi = Fm[i]
        for j in range(i + 1, n + 1):
            # deconvolve factor j from the law of N_{-i}:  a_k = (1-q_j) c_k + q_j c_{k-j}
            c = [zero] * (deg + 1)
            for k in range(deg + 1):
                v = Fi[k] - (q[j] * c[k - j] if k >= j else zero)
                c[k] = v / (1 - q[j])
            tot = sum(c, zero)

            def Dsum(u):
                return tot if u <= 0 else sum(c[u:], zero)
            G = (Dsum(n + 1 - i - j) - Dsum(n + 1 - i) - Dsum(n + 1 - j) + Dsum(n + 1)) / 2
            P2[(i, j)] = s2[i] * s2[j] * G * G
    W2 = sum(P2.values(), zero)
    M2 = {i: zero for i in range(1, n + 1)}
    for (i, j), p in P2.items():
        M2[i] += p
        M2[j] += p
    Ii = {i: s2[i] * rho[i] for i in range(1, n + 1)}
    I = sum(Ii.values(), zero)
    cond = all((4 * M2[i] / (W2 * s2[i])).a >= 1 for i in range(1, n + 1))
    H2 = zero
    straddle = 0
    for p in P2.values():
        x = p / W2
        if x.a > 0:
            H2 += x * iv.log(1 / x)
        elif x.b > 0:
            # enclosure of t ln(1/t) for t in [0, x.b] (x.b <= 1/e): [0, x.b ln(1/x.b)]
            straddle += 1
            ub = iv.mpf(x.b) * iv.log(1 / iv.mpf(x.b))
            H2 += iv.mpf([0, mpmath.mpf(ub.b)])
    Hu = zero
    for i in range(1, n + 1):
        x = M2[i] / (2 * W2)
        Hu -= x * iv.log(x)
    R = sum((L[i] * (Ii[i] - M2[i]) for i in range(1, n + 1)), zero)
    lb = (W2 * (2 * Hu - H2 - 4 * iv.log(2)) - R) / I
    nuM = sum((P2[(i, n + 1 - i)] for i in range(1, m + 1)), zero) / W2
    return dict(lb=lb, cond=cond, W2I=W2 / I, RW=R / W2, H2=H2, Hu=Hu, nuM=nuM, straddle=straddle)


def fmt(z):
    return "[%s, %s]" % (mpmath.nstr(mpmath.mpf(z.a), 7), mpmath.nstr(mpmath.mpf(z.b), 7))


if __name__ == "__main__":
    t0 = time.time()
    which = sys.argv[1] if len(sys.argv) > 1 else "both"
    if which in ("1", "both"):
        print("Part 1: exact full spectra, q_i = r^(i+2)")
        for m in range(2, 8):
            r = Fr(1, 4 * m * m)
            d = part1(m, r)
            print(" m=%d r=1/%d: LCR excess/I = %s ; lemma lower bound = %s (cond %s) ; heuristic (ln m)/2 - ln2 = %s"
                  % (m, 4 * m * m, mpmath.nstr(d["excess"], 7), mpmath.nstr(d["lb"], 7), d["cond"],
                     mpmath.nstr(mpmath.log(m) / 2 - mpmath.log(2), 6)))
            print("        inf_theta KL(nu2||Q_theta) = %.5f >= analytic bound %s ; ln(2m-1) = %.5f ; nu2(M) = %s ; W2/I = %s ; E/I = %s ; H+/Delta = %s  t=%.0fs"
                  % (d["klinf"], mpmath.nstr(d["kl_lb"], 6), d["ln2m1"], mpmath.nstr(mpq(d["nuM"]), 8),
                     mpmath.nstr(d["W2I"], 6), mpmath.nstr(d["EI"], 6), mpmath.nstr(d["ratio"], 6), time.time() - t0))
            sys.stdout.flush()
    if which in ("2", "both"):
        print("Part 2: structured interval computation, r = 2^-rexp")
        for (m, rexp) in [(4, 8), (7, 8), (16, 12), (32, 14), (64, 16)]:
            d = part2(m, rexp)
            print(" m=%3d r=2^-%d: certified LCR-excess/I >= %s  (cond %s; nu2(M) %s; W2/I %s; R/W2 %s) heuristic %s  t=%.0fs"
                  % (m, rexp, fmt(d["lb"]), d["cond"], fmt(d["nuM"]), fmt(d["W2I"]), fmt(d["RW"]),
                     mpmath.nstr(mpmath.log(m) / 2 - mpmath.log(2), 6), time.time() - t0))
            sys.stdout.flush()
