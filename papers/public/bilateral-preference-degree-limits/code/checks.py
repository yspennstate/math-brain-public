"""Checks for "Degree fluctuations in bilateral preference random graphs".

Run:  python checks.py > checks_output.txt      (under a minute on a laptop)

Every check prints PASS or FAIL with the numbers behind it; the last line counts them.
Model: LK(n,k). Scores U_ij iid Unif(0,1) on the edges of K_n, each vertex proposes to the k
vertices with the smallest scores, an edge is kept when both ends propose. D is the root degree
and H = k - D. Section numbers refer to the paper.
"""
import itertools
import math
import sys
from fractions import Fraction as Fr

import numpy as np
from scipy import integrate, optimize, special, stats

RESULTS = []


def report(name, ok, detail=""):
    RESULTS.append((name, bool(ok)))
    print(("PASS  " if ok else "FAIL  ") + name + (("  [" + detail + "]") if detail else ""))
    sys.stdout.flush()


# ---------------------------------------------------------------- exact polynomials over Q
def p_trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def p_add(a, b):
    m = max(len(a), len(b))
    return p_trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(m)])


def p_scale(a, c):
    return p_trim([c * x for x in a])


def p_sub(a, b):
    return p_add(a, p_scale(b, -1))


def p_mul(a, b):
    out = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[i + j] += x * y
    return p_trim(out)


def p_antider(a):
    """Integral from 0 to x."""
    return p_trim([Fr(0)] + [c / (i + 1) for i, c in enumerate(a)])


def p_divx(a, m):
    """Exact division by x^m."""
    assert all(c == 0 for c in a[:m]), "not divisible by x^m"
    return a[m:] or [Fr(0)]


def p_int01(a):
    return sum((c / (i + 1) for i, c in enumerate(a)), Fr(0))


def p_eval(a, x):
    return sum((c * x ** i for i, c in enumerate(a)), Fr(0))


def mono_beta(a, b):
    """x^a (1-x)^b."""
    out = [Fr(0)] * (a + b + 1)
    for i in range(b + 1):
        out[a + i] = Fr(math.comb(b, i) * (-1) ** i)
    return out


def beta_cdf(a, b):
    """Regularized incomplete beta I_x(a,b) for integers a, b >= 1."""
    N = a + b - 1
    out = [Fr(0)]
    for j in range(a, N + 1):
        out = p_add(out, p_scale(mono_beta(j, N - j), math.comb(N, j)))
    return out


def beta_pdf(a, b):
    B = Fr(math.factorial(a - 1) * math.factorial(b - 1), math.factorial(a + b - 1))
    return p_scale(mono_beta(a - 1, b - 1), 1 / B)


def exact_structure(n, k):
    """Exact E H and Var H for 1 <= k <= n-2 from Section 2 (eq. (2.2), Lemmas 2.2 and 2.3):
    X ~ Beta(k+1, n-k-1), T ~ Beta(k, n-k-1), q(x) = F_T(x) - k F_X(x)/((n-1)x),
    Var H = E[k q(1-q)] + k(k-1) E[Var_W p_X(W)] + k^2 Var q(X),
    Var_W p_X(W) = Var_W [F_T(x) - F_T(W)]_+ / ((n-2)x)^2.
    Also returns whether E_W p_X(W) = q(X) holds identically."""
    FT = beta_cdf(k, n - k - 1)
    FX = beta_cdf(k + 1, n - k - 1)
    fX = beta_pdf(k + 1, n - k - 1)
    q = p_sub(FT, p_scale(p_divx(FX, 1), Fr(k, n - 1)))
    G1 = p_antider(FT)
    G2 = p_antider(p_mul(FT, FT))
    xFT = p_mul([Fr(0), Fr(1)], FT)
    first = p_sub(xFT, G1)                                            # int_0^x (F_T(x) - F_T(w)) dw
    second = p_add(p_sub(p_mul(xFT, FT), p_scale(p_mul(FT, G1), 2)), G2)
    V = p_sub(second, p_mul(first, first))                            # Var_W [F_T(x) - F_T(W)]_+
    cov = p_scale(p_divx(V, 2), Fr(1, (n - 2) ** 2))
    Eq = p_int01(p_mul(q, fX))
    Eq2 = p_int01(p_mul(p_mul(q, q), fX))
    Ecov = p_int01(p_mul(cov, fX))
    EH = k * Eq
    VarH = k * (Eq - Eq2) + k * (k - 1) * Ecov + k * k * (Eq2 - Eq * Eq)
    bX = p_divx(p_antider(beta_cdf(k, n - k - 2)), 1) if k <= n - 3 else [Fr(0)]
    mean_ok = p_sub(p_add(bX, p_scale(p_divx(first, 1), Fr(1, n - 2))), q) == [0]
    return {"EH": EH, "VarH": VarH, "mean_ok": mean_ok, "V": V, "FT": FT}


# ---------------------------------------------------------------- enumeration of every score order
def enumerate_root(n):
    """Exact joint law over all (C(n,2))! orders of the scores. Returns, for each budget b in 1..n-2,
    a Counter-like array of H_b = b - D_b and of I_b - D_b (I_b = in-proposals of the root)."""
    edges = list(itertools.combinations(range(n), 2))
    E = len(edges)
    inc = [[e for e, (a, c) in enumerate(edges) if v in (a, c)] for v in range(n)]
    pos = [{e: i for i, e in enumerate(inc[v])} for v in range(n)]
    root_edges = [(e, edges[e][1]) for e in inc[0]]                      # (edge, other end)
    hist_H = {b: np.zeros(n, dtype=np.int64) for b in range(1, n - 1)}
    hist_ID = {b: np.zeros(2 * n, dtype=np.int64) for b in range(1, n - 1)}
    sum_D = {b: 0 for b in range(1, n - 1)}
    sum_D2 = {b: 0 for b in range(1, n - 1)}
    total = 0
    for first in range(E):
        rest = [x for x in range(E) if x != first]
        perms = np.array(list(itertools.permutations(rest)), dtype=np.int16)
        S = np.concatenate([np.full((perms.shape[0], 1), first, dtype=np.int16), perms], axis=1)
        total += S.shape[0]
        rank = []
        for v in range(n):
            sub = S[:, inc[v]]
            rank.append(np.argsort(np.argsort(sub, axis=1, kind="stable"), axis=1, kind="stable"))
        for b in range(1, n - 1):
            D = np.zeros(S.shape[0], dtype=np.int64)
            I = np.zeros(S.shape[0], dtype=np.int64)
            for e, j in root_edges:
                mine = rank[0][:, pos[0][e]] < b
                theirs = rank[j][:, pos[j][e]] < b
                D += mine & theirs
                I += theirs
            hist_H[b] += np.bincount(b - D, minlength=n)[:n]
            hist_ID[b] += np.bincount(I - D + n, minlength=2 * n)[:2 * n]   # shifted, I - D >= 0 anyway
            sum_D[b] += int(D.sum())
            sum_D2[b] += int((D * D).sum())
    return total, hist_H, hist_ID, sum_D, sum_D2


# ---------------------------------------------------------------- fixed r = n-1-k limit (Section 4)
def mu_sum(r):
    """(4.3): mu_r = sum_{l<r} (r-l) E[e^{-A} A^l]/l!, A ~ Gamma(r,1)."""
    return sum(Fr((r - l) * math.factorial(r - 1 + l), math.factorial(l) * math.factorial(r - 1) * 2 ** (r + l))
               for l in range(r))


def mu_closed(r):
    return Fr(r * math.comb(2 * r, r), 4 ** r)


def c_ds(k):
    """Constant of Dabirian-Subramanian Theorem 7: lim E H at fixed k."""
    return Fr((2 * k - 1) * math.comb(2 * k - 2, k - 1), 2 ** (2 * k - 1))


def M2(r):
    """(4.4): E Lambda_r(A_r)^2."""
    s = sum(Fr((r - l) * (r - m) * math.factorial(r + l + m - 1), math.factorial(l) * math.factorial(m) * 3 ** (r + l + m))
            for l in range(r) for m in range(r))
    return s / math.factorial(r - 1)


def fact_moment_limit(r, j):
    """E[Lambda_r(A_r)^j], the j-th factorial moment of the fixed-r limit."""
    P = [Fr(r - l, math.factorial(l)) for l in range(r)]
    Pj = [Fr(1)]
    for _ in range(j):
        Pj = p_mul(Pj, P)
    return sum((c * Fr(math.factorial(r - 1 + N), math.factorial(r - 1) * (j + 1) ** (r + N)) for N, c in enumerate(Pj)), Fr(0))


# ---------------------------------------------------------------- floating point version of exact_structure
def float_structure(n, k):
    aT, bT, aX, bX = k, n - k - 1, k + 1, n - k - 1
    FT = lambda x: special.betainc(aT, bT, x)
    FX = lambda x: special.betainc(aX, bX, x)
    fX = lambda x: stats.beta.pdf(x, aX, bX)
    q = lambda x: FT(x) - k / ((n - 1) * x) * FX(x)
    # closed forms: scipy's beta.std loses all accuracy for parameters near 1e8
    mX, sX = aX / (aX + bX), math.sqrt(aX * bX / ((aX + bX) ** 2 * (aX + bX + 1)))
    mT, sT = aT / (aT + bT), math.sqrt(aT * bT / ((aT + bT) ** 2 * (aT + bT + 1)))
    lo, hi = max(mX - 16 * sX, 1e-300), min(mX + 16 * sX, 1.0)
    tlo = max(mT - 16 * sT, 0.0)

    def G2(x):
        if x <= tlo:
            return 0.0
        return integrate.quad(lambda w: FT(w) ** 2, tlo, x, limit=200, epsabs=0, epsrel=1e-12)[0]

    def V(x):
        f = FT(x)
        first = k / (n - 1) * FX(x)                                  # x F_T(x) - int_0^x F_T
        G1 = x * f - first
        second = x * f * f - 2 * f * G1 + G2(x)
        return second - first * first

    opts = dict(limit=400, epsabs=0, epsrel=1e-12, points=[mX])
    Eq = integrate.quad(lambda x: q(x) * fX(x), lo, hi, **opts)[0]
    Eq2 = integrate.quad(lambda x: q(x) ** 2 * fX(x), lo, hi, **opts)[0]
    Ecov = integrate.quad(lambda x: V(x) / ((n - 2) * x) ** 2 * fX(x), lo, hi, **opts)[0]
    EH = k * Eq
    VarH = k * (Eq - Eq2) + k * (k - 1) * Ecov + k * k * (Eq2 - Eq * Eq)
    return EH, VarH


def g(z):
    return stats.norm.pdf(z) + z * stats.norm.cdf(z)


def main():
    print("Checks for the root degree of LK(n,k). Exact arithmetic in Fractions unless stated.")
    print()

    # ---- A. exact finite-n structure against enumeration of every score order
    print("A. Section 2: exact E H and Var H against every order of the scores")
    for n in (4, 5):
        total, hist_H, hist_ID, sum_D, sum_D2 = enumerate_root(n)
        assert total == math.factorial(n * (n - 1) // 2)
        for k in range(1, n - 1):
            ED = Fr(sum_D[k], total)
            VD = Fr(sum_D2[k], total) - ED * ED
            ex = exact_structure(n, k)
            report(f"n={n} k={k}: E H and Var H from the variance identity equal the enumeration ({total} orders)",
                   ex["EH"] == k - ED and ex["VarH"] == VD, f"E D={ED}, Var D={VD}")
            report(f"n={n} k={k}: E_W p_X(W) = q(X) identically (Lemma 2.2 kernel)", ex["mean_ok"])
            r = n - 1 - k
            law_H = hist_H[k]
            law_ID = hist_ID[r][n:n + n]
            report(f"n={n}: law of H at budget k={k} equals law of I-D at budget r={r} (complement duality)",
                   np.array_equal(law_H, law_ID), "counts " + ",".join(str(int(c)) for c in law_H))
    anchors = [  # exact reference values from an independent program
        (4, 2, "D", Fr(8, 5), Fr(28, 75)),
        (10, 8, "H", Fr(8, 17), Fr(454, 867)),
    ]
    for n, k, kind, m, v in anchors:
        ex = exact_structure(n, k)
        mean = ex["EH"] if kind == "H" else k - ex["EH"]
        report(f"n={n} k={k}: E {kind} = {m}, Var = {v} (reference value)", mean == m and ex["VarH"] == v)
    n7 = {1: Fr(30, 121), 2: Fr(241676, 495495), 3: Fr(243059, 385385), 4: Fr(63920, 99099), 5: Fr(178, 363)}
    report("n=7: Var D for k=1..5 equals the reference values",
           all(exact_structure(7, k)["VarH"] == v for k, v in n7.items()))
    deltas = {(1, 5): Fr(3, 7), (1, 10): Fr(8, 17), (1, 20): Fr(18, 37), (2, 5): Fr(18, 35), (2, 10): Fr(56, 85),
              (2, 20): Fr(918, 1295), (3, 5): Fr(3, 7), (3, 10): Fr(168, 221), (3, 20): Fr(2448, 2849)}
    report("E H at r=1,2,3 and n=5,10,20 equals the reference values",
           all(exact_structure(n, n - 1 - r)["EH"] == d for (r, n), d in deltas.items()))
    report("E H(n,1) = (n-2)/(2n-3) for n=3..30",
           all(exact_structure(n, 1)["EH"] == Fr(n - 2, 2 * n - 3) for n in range(3, 31)))
    ok = True
    for n in range(4, 25):
        eh = {k: exact_structure(n, k)["EH"] for k in range(1, n - 1)}
        ok &= all(eh[k] == eh[n - 1 - k] for k in eh)
    report("E H(n,k) = E H(n,n-1-k) for every 4 <= n <= 24 and 1 <= k <= n-2 (mean duality)", ok)
    ok = True
    for n in range(3, 25):
        for k in range(1, n - 1):
            FT = beta_cdf(k, n - k - 1)
            ok &= exact_structure(n, k)["EH"] == (n - 1) * p_int01(p_sub(FT, p_mul(FT, FT)))
    report("E H(n,k) = (n-1) int_0^1 F_T (1 - F_T), T ~ Beta(k, n-1-k), for every 3 <= n <= 24 and 1 <= k <= n-2", ok)
    worst = Fr(0)
    for n, k in ((8, 3), (12, 5), (16, 4), (20, 15)):
        ex = exact_structure(n, k)
        for j in range(1, 16):
            x = Fr(j, 16)
            Vx, Fx = p_eval(ex["V"], x), p_eval(ex["FT"], x)
            worst = max(worst, Vx - Fx * Fx / 4)
    report("Lemma 2.2: Var_W [F_T(x) - F_T(W)]_+ <= F_T(x)^2/4 on a grid (Popoviciu)", worst <= 0,
           f"max excess {float(worst):.3e}")
    print()

    # ---- B. Monte Carlo of the graph itself at n=12
    print("B. Monte Carlo of LK(12,k), 200000 graphs each, root degree against the exact formula")
    rng = np.random.default_rng(20261014)
    n = 12
    edges = list(itertools.combinations(range(n), 2))
    inc = [[e for e, (a, c) in enumerate(edges) if v in (a, c)] for v in range(n)]
    for k in (4, 8):
        Ds = []
        for _ in range(10):
            U = rng.random((20000, len(edges)))
            rank = [np.argsort(np.argsort(U[:, inc[v]], axis=1), axis=1) for v in range(n)]
            D = np.zeros(U.shape[0], dtype=np.int64)
            for c, e in enumerate(inc[0]):
                j = edges[e][1]
                D += (rank[0][:, c] < k) & (rank[j][:, inc[j].index(e)] < k)
            Ds.append(D)
        D = np.concatenate(Ds)
        ex = exact_structure(n, k)
        ED, VD = float(k - ex["EH"]), float(ex["VarH"])
        z_mean = (D.mean() - ED) / math.sqrt(VD / D.size)
        m4 = np.mean((D - D.mean()) ** 4)
        z_var = (D.var() - VD) / math.sqrt((m4 - VD ** 2) / D.size)
        report(f"n=12 k={k}: simulated E D and Var D agree with the exact values (|z| < 4)",
               abs(z_mean) < 4 and abs(z_var) < 4,
               f"exact {ED:.6f}, {VD:.6f}; simulated {D.mean():.6f}, {D.var():.6f}; z {z_mean:.2f}, {z_var:.2f}")
    print()

    # ---- C. fixed r: the limit law of Section 4
    print("C. Section 4: constants of the fixed-r limit")
    report("mu_r: (4.3) sum = r C(2r,r)/4^r = Dabirian-Subramanian c_r for r = 1..60",
           all(mu_sum(r) == mu_closed(r) == c_ds(r) for r in range(1, 61)))
    report("mu_r = 1/B(1/2, r) in floating point for r = 1..60",
           all(abs(float(mu_closed(r)) * special.beta(0.5, r) - 1) < 1e-12 for r in range(1, 61)))
    nu = {r: mu_closed(r) + M2(r) - mu_closed(r) ** 2 for r in (1, 2, 3)}
    report("r=1: mu=1/2, M2=1/3, nu=7/12, endpoint^2 = mu^2/nu = 3/7",
           mu_closed(1) == Fr(1, 2) and M2(1) == Fr(1, 3) and nu[1] == Fr(7, 12) and mu_closed(1) ** 2 / nu[1] == Fr(3, 7))
    report("r=2: mu=3/4, M2=22/27, nu=433/432, endpoint^2 = 243/433",
           mu_closed(2) == Fr(3, 4) and M2(2) == Fr(22, 27) and nu[2] == Fr(433, 432) and mu_closed(2) ** 2 / nu[2] == Fr(243, 433))
    report("endpoints sqrt(3/7) = 0.654654 and sqrt(243/433) = 0.749133 differ",
           abs(math.sqrt(3 / 7) - 0.654654) < 1e-6 and abs(math.sqrt(243 / 433) - 0.749133) < 1e-6,
           f"{math.sqrt(3 / 7):.7f}, {math.sqrt(243 / 433):.7f}")
    reference = {1: [Fr(1, 2), Fr(1, 3), Fr(1, 4), Fr(1, 5)],
               2: [Fr(3, 4), Fr(22, 27), Fr(133, 128), Fr(4536, 3125)],
               3: [Fr(15, 16), Fr(323, 243), Fr(74193, 32768), Fr(8379549, 1953125)]}
    report("factorial moments E[Lambda_r(A_r)^j], j=1..4, r=1..3, equal the reference values",
           all([fact_moment_limit(r, j) for j in range(1, 5)] == v for r, v in reference.items()))
    report("factorial moment j=2 equals M2 from (4.4), r=1..12", all(fact_moment_limit(r, 2) == M2(r) for r in range(1, 13)))

    def p_r(y, r):
        return stats.poisson.cdf(r - 1, y)

    ok, worst = True, 0.0
    for r in range(1, 7):
        Lam_num = lambda a: integrate.quad(lambda y: p_r(y, r), a, np.inf, limit=200)[0]
        Lam_cf = lambda a: math.exp(-a) * sum((r - l) * a ** l / math.factorial(l) for l in range(r))
        for a in (0.0, 0.5, 1.0, 2.5, 5.0, 10.0):
            worst = max(worst, abs(Lam_num(a) - Lam_cf(a)))
        fA = lambda a: stats.gamma.pdf(a, r)
        mu_num = integrate.quad(lambda a: Lam_cf(a) * fA(a), 0, np.inf, limit=200)[0]
        m2_num = integrate.quad(lambda a: Lam_cf(a) ** 2 * fA(a), 0, np.inf, limit=200)[0]
        ok &= abs(mu_num - float(mu_closed(r))) < 1e-10 and abs(m2_num - float(M2(r))) < 1e-10
    report("(4.1) Lambda_r(a) = int_a^inf p_r = e^{-a} sum (r-l) a^l/l!, and mu_r, M2 by quadrature, r=1..6",
           ok and worst < 1e-9, f"max |Lambda diff| {worst:.1e}")
    report("standardized Gamma(r) excess kurtosis = 6/r (fourth moment 3 + 6/r), r=1..50",
           all(abs(float(stats.gamma.stats(r, moments="k")) - 6 / r) < 1e-12 for r in range(1, 51)))
    print("   fixed r, exact finite n: E H and Var H approach mu_r and nu_r")
    for r in (1, 2, 3):
        rows, prev = [], None
        mono = True
        for n in (10, 20, 40, 80):
            ex = exact_structure(n, n - 1 - r)
            dm, dv = abs(float(ex["EH"] - mu_closed(r))), abs(float(ex["VarH"] - nu[r]))
            rows.append(f"n={n}: E H={float(ex['EH']):.6f} Var={float(ex['VarH']):.6f}")
            if prev is not None and not (dm < prev[0] and dv < prev[1]):
                mono = False
            prev = (dm, dv)
        print("   r=%d (mu=%.6f nu=%.6f): " % (r, float(mu_closed(r)), float(nu[r])) + "; ".join(rows))
        report(f"r={r}: distances to (mu_r, nu_r) shrink along n = 10, 20, 40, 80", mono,
               f"at n=80: {prev[0]:.2e}, {prev[1]:.2e}")
    for r in (1, 2):
        n = 20000
        EH, VH = float_structure(n, n - 1 - r)
        report(f"r={r}, n={n} (floating point): E H, Var H within 2e-3 of mu_r, nu_r",
               abs(EH - float(mu_closed(r))) < 2e-3 and abs(VH - float(nu[r])) < 2e-3, f"{EH:.6f}, {VH:.6f}")
    print()

    # ---- D. k and n-k to infinity: Theorem 2.1
    print("D. Theorem 2.1: E H / s_n -> 1/sqrt(pi), Var H / s_n^2 -> v")
    m = 1 / math.sqrt(math.pi)
    v = 1 / 3 + (math.sqrt(3) - 2) / (2 * math.pi)
    Eg = integrate.quad(lambda z: g(z) * stats.norm.pdf(z), -np.inf, np.inf)[0]
    Eg2 = integrate.quad(lambda z: g(z) ** 2 * stats.norm.pdf(z), -np.inf, np.inf)[0]
    report("E g(Z) = 1/sqrt(pi)", abs(Eg - m) < 1e-12, f"{Eg:.15f}")
    report("E g(Z)^2 = 1/3 + sqrt(3)/(2 pi)", abs(Eg2 - (1 / 3 + math.sqrt(3) / (2 * math.pi))) < 1e-12, f"{Eg2:.15f}")
    report("v = 1/3 + (sqrt(3)-2)/(2 pi) = 0.290687...", abs(Eg2 - Eg ** 2 - v) < 1e-12 and abs(v - 0.290687) < 1e-6,
           f"{v:.9f}")
    report("upper endpoint of L_inf: m/sqrt(v) = 1.04643", abs(m / math.sqrt(v) - 1.046433) < 1e-6, f"{m / math.sqrt(v):.6f}")
    for n, k in ((40, 20), (80, 30)):
        ex = exact_structure(n, k)
        EH, VH = float_structure(n, k)
        report(f"floating-point integrals agree with the exact rationals at n={n}, k={k}",
               abs(EH / float(ex["EH"]) - 1) < 1e-9 and abs(VH / float(ex["VarH"]) - 1) < 1e-9,
               f"{EH:.12f} vs {float(ex['EH']):.12f}; {VH:.12f} vs {float(ex['VarH']):.12f}")
    regimes = {"k=n/2": (lambda n: n // 2, (10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6)),
               "k=n/10": (lambda n: n // 10, (10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6)),
               "k=sqrt(n)": (lambda n: math.isqrt(n), (10 ** 2, 10 ** 4, 10 ** 6, 10 ** 8))}
    for name, (kf, ns) in regimes.items():
        prev, rows, mono = None, [], True
        for n in ns:
            k = kf(n)
            s2 = k * (n - k) / n
            EH, VH = float_structure(n, k)
            a, b = EH / math.sqrt(s2), VH / s2
            d = (abs(a - m), abs(b - v))
            rows.append(f"n=1e{round(math.log10(n))}: {a:.6f}, {b:.6f} (s_n*dist {math.sqrt(s2) * d[0]:.3f}, {math.sqrt(s2) * d[1]:.3f})")
            if prev is not None and not (d[0] < prev[0] and d[1] < prev[1]):
                mono = False
            prev = d
        print(f"   {name}: E H/s_n, Var H/s_n^2 = " + "; ".join(rows))
        report(f"{name}: both ratios move monotonically toward (0.564190, 0.290687), within 1e-2 at the largest n",
               mono and max(prev) < 1e-2, f"distances at the largest n: {prev[0]:.1e}, {prev[1]:.1e}")
    bad = 0
    for n in (20, 50, 100, 200, 500, 1000, 2000):
        for k in range(1, n - 1):
            p = stats.binom.sf(k, n - 1, k / (2 * n))
            if p > math.exp(-(math.log(2) - 0.5) * k) * (1 + 1e-12):
                bad += 1
    report("Lemma 2.4: P(X < k/(2n)) = P(Bin(n-1, k/(2n)) >= k+1) <= exp(-(log 2 - 1/2) k), all k, 7 values of n", bad == 0)
    worst = 0.0
    for a in (2, 5, 30, 300, 3000):
        for b in (2, 7, 40, 500, 5000):
            formula = 6 * ((a - b) ** 2 * (a + b + 1) - a * b * (a + b + 2)) / (a * b * (a + b + 2) * (a + b + 3))
            worst = max(worst, abs(formula - float(stats.beta.stats(a, b, moments="k"))))
    report("Beta excess kurtosis formula used for uniform integrability agrees with scipy", worst < 1e-10, f"{worst:.1e}")
    print()

    # ---- E. the law L_inf of Section 3
    print("E. Section 3: distribution function and density of L_inf")
    xmax = m / math.sqrt(v)

    def yx(x):
        target = m - math.sqrt(v) * x
        return optimize.brentq(lambda y: g(y) - target, -40, 40, xtol=1e-14, rtol=1e-14)

    dens = lambda x: math.sqrt(v) * stats.norm.pdf(yx(x)) / stats.norm.cdf(yx(x))
    pts = [xmax - 1e-2, xmax - 1e-4]
    tot = integrate.quad(dens, -12, xmax - 1e-12, limit=400, points=pts)[0]
    mean = integrate.quad(lambda x: x * dens(x), -12, xmax - 1e-12, limit=400, points=pts)[0]
    sec = integrate.quad(lambda x: x * x * dens(x), -12, xmax - 1e-12, limit=400, points=pts)[0]
    report("(3.2) density integrates to 1, mean 0, variance 1", abs(tot - 1) < 1e-6 and abs(mean) < 1e-6 and abs(sec - 1) < 1e-6,
           f"{tot:.8f}, {mean:.2e}, {sec:.8f}")
    zs = np.random.default_rng(7).standard_normal(2_000_000)
    L = (m - g(zs)) / math.sqrt(v)
    worst = max(abs(np.mean(L <= x) - (1 - stats.norm.cdf(yx(x)))) for x in (-2.0, -1.0, 0.0, 0.5, 0.9, 1.04))
    report("(3.1) P(L_inf <= x) = 1 - Phi(y_x) against 2e6 normal draws", worst < 2e-3, f"max diff {worst:.1e}")
    print()

    npass = sum(ok for _, ok in RESULTS)
    print(f"{npass} of {len(RESULTS)} checks passed" + ("" if npass == len(RESULTS) else "  <-- FAILURES ABOVE"))


if __name__ == "__main__":
    main()
