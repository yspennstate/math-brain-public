"""Standalone interval certificate for the chain theorem (every AND/OR chain has H <= 4 I).

Checks Phi_K(s) = 2 E(s) + sum_{k<K} 2^-k psi(T^k s) > 0 for every s in [1/2, 1), K = 8, where
    eps(p) = 4p^2 + (2/ln2)[g(p) + g(1-p)] - g(|1-2p|)/ln2,   g(x) = x^2 ln x  (g(0) = 0),
    E(s)   = sum_{l>=0} 2^l eps(2^-l s),   psi(u) = eps(2 min(u, 1-u)),   T u = 2u mod 1.
Only mpmath interval arithmetic (outward rounding) is used.  [1/2,1) is cut into 2^(M-1) dyadic intervals of width
2^-M; on each, every quantity is enclosed:
  * eps on P = [p0,p1] with p1 < 0.05 (the terms l >= 5 of E) from the series
        eps(p) = p^2 (4 - 3/ln2 + 2 log2 p) + (2/ln2) sum_{n>=3} (2^n - 2) p^n / (n(n-1)(n-2)),
    whose first part is decreasing and second part increasing on (0, 0.05] (checked analytically in REPORT),
    with the series truncated at n = 25 and the tail bounded by (2/ln2)(2p)^26/(26*25*24*(1-2p));
  * eps on other intervals from g, using that g is decreasing on [0, e^-1/2] and increasing on [e^-1/2, 1];
  * the tail l >= L of E is bounded by sum_{l>=L} 2^-l (2 l + 4) (valid since 2^l |eps(2^-l s)| <= 2^-l (2l+4)
    for 2^-l s <= 2^-L, L >= 6; see REPORT);
  * T^k maps each dyadic cell of width 2^-M (k < M) onto a cell of width 2^(k-M) without wrapping.
Output: the smallest certified lower bound of Phi_K over all cells.
"""
import sys
from mpmath import iv, mp, mpf

iv.prec = 120
mp.prec = 120
LN2 = iv.log(iv.mpf(2))
EMH = iv.exp(iv.mpf(-0.5))          # e^-1/2 as an interval


def g_point(x):
    x = iv.mpf(x)
    if x == 0:
        return iv.mpf(0)
    return x * x * iv.log(x)


def g_int(a, b):
    """Enclosure of g(x) = x^2 ln x on [a, b], 0 <= a <= b <= 1 (a, b are mpf numbers)."""
    ga, gb = g_point(a), g_point(b)
    lo_candidates = [ga.a, gb.a]
    hi = max(ga.b, gb.b)
    c = mpf(EMH.a)  # below the true e^-1/2
    if a <= mpf(EMH.b) and b >= c:
        # the minimum -1/(2e) is attained inside
        lo_candidates.append((-1 / (2 * iv.e)).a)
    return iv.mpf([min(lo_candidates), hi])


C0 = iv.mpf(4) - 3 / LN2


def series_part(p, N=25):
    s = iv.mpf(0)
    pn = p * p
    for n in range(3, N + 1):
        pn = pn * p
        s += (2 ** n - 2) * pn / (n * (n - 1) * (n - 2))
    return 2 * s / LN2


def series_tail_bound(p, N=25):
    q = 2 * p
    return 2 / LN2 * q ** (N + 1) / ((N + 1) * N * (N - 1) * (1 - q))


def eps_int(p0, p1):
    """Enclosure of eps on [p0, p1] subset of [0, 1] (p0, p1 mpf)."""
    if p1 < mpf("0.05"):
        # first part f1(p) = p^2 (C0 + 2 log2 p) decreasing, f1(0) = 0; second part f2 increasing, f2(0) = 0
        def f1(p):
            if p == 0:
                return iv.mpf(0)
            P = iv.mpf(p)
            return P * P * (C0 + 2 * iv.log(P) / LN2)
        def f2(p):
            if p == 0:
                return iv.mpf(0)
            P = iv.mpf(p)
            return series_part(P)
        lo = f1(p1).a + f2(p0).a
        P1 = iv.mpf(p1)
        hi = f1(p0).b + f2(p1).b + series_tail_bound(P1).b
        return iv.mpf([lo, hi])
    P = iv.mpf([p0, p1])
    q0, q1 = 1 - p1, 1 - p0
    if p1 <= mpf(1) / 2:
        r0, r1 = 1 - 2 * p1, 1 - 2 * p0
    elif p0 >= mpf(1) / 2:
        r0, r1 = 2 * p0 - 1, 2 * p1 - 1
    else:
        r0, r1 = mpf(0), max(1 - 2 * p0, 2 * p1 - 1)
    return 4 * P * P + (2 / LN2) * (g_int(p0, p1) + g_int(q0, q1)) - g_int(r0, r1) / LN2


def d_int(v0, v1):
    lo = min(min(v0, 1 - v0), min(v1, 1 - v1))
    if v0 <= mpf(1) / 2 <= v1:
        hi = mpf(1) / 2
    else:
        hi = max(min(v0, 1 - v0), min(v1, 1 - v1))
    return lo, hi


def Phi_cell(i, M, K, L=40):
    w = mpf(2) ** (-M)
    a = mpf(1) / 2 + i * w
    b = a + w
    E = iv.mpf(0)
    for l in range(L):
        sc = mpf(2) ** (-l)
        E += (2 ** l) * eps_int(a * sc, b * sc)
    tail = sum((mpf(2) ** (-l)) * (2 * l + 4) for l in range(L, L + 200))
    E += iv.mpf([-tail, tail])
    out = 2 * E
    num = (2 ** (M - 1)) + i   # a = num * 2^-M exactly
    for k in range(K):
        # T^k [a, b] = [frac(num 2^k / 2^M), + 2^(k-M)]
        top = (num << k) % (1 << M)
        v0 = mpf(top) / 2 ** M
        v1 = v0 + mpf(2) ** (k - M)
        d0, d1 = d_int(v0, v1)
        out += eps_int(2 * d0, 2 * d1) / (2 ** k)
    return out


def eps_neg_check(ncell=4096):
    """Certify eps(p) < 0 on (0, 1/2): series bound on (0, 1/64], cells on [1/64, 0.45], derivative > 0 on [0.45, 1/2]."""
    # (i) 0 < p <= 1/64: eps(p) <= p^2 (C0 + 2 log2 p) + (2/ln2) (8/6) p^3 / (1 - 2p) < 0 since the bracket
    #     C0 + 2 log2 p + (2/ln2)(4/3) p/(1-2p) <= C0 - 12 + 0.07 < 0.
    assert (C0 + 2 * iv.log(iv.mpf(1) / 64) / LN2 + 2 / LN2 * iv.mpf(4) / 3 * (iv.mpf(1) / 64) / (1 - iv.mpf(2) / 64)).b < 0
    # (ii) cells of [1/64, 0.45]
    lo, hi = mpf(1) / 64, mpf("0.45")
    worst = None
    for i in range(ncell):
        p0 = lo + (hi - lo) * i / ncell
        p1 = lo + (hi - lo) * (i + 1) / ncell
        v = eps_int(p0, p1)
        worst = v.b if worst is None else max(worst, v.b)
    assert worst < 0, worst
    # (iii) on [0.45, 1/2]: eps'(p) = 8p + (2/ln2)(g'(p) - g'(1-p)) + (2/ln2) g'(1-2p), g'(x) = x(2 ln x + 1);
    #       enclose each part on cells; eps' > 0 there and eps(1/2) = 0 give eps < 0 on [0.45, 1/2).
    def gp_int(a, b):
        # g'(x) = x(2 ln x + 1) is decreasing on [0, e^-3/2] and increasing after; g'(0) = 0
        def gp(x):
            X = iv.mpf(x)
            return iv.mpf(0) if x == 0 else X * (2 * iv.log(X) + 1)
        A, B = gp(a), gp(b)
        cands = [A.a, B.a]
        e32 = iv.exp(iv.mpf(-1.5))
        if a <= mpf(e32.b) and b >= mpf(e32.a):
            cands.append((-2 * e32).a)
        return iv.mpf([min(cands), max(A.b, B.b)])
    worstd = None
    m = 512
    for i in range(m):
        p0 = mpf("0.45") + mpf("0.05") * i / m
        p1 = mpf("0.45") + mpf("0.05") * (i + 1) / m
        v = 8 * iv.mpf([p0, p1]) + (2 / LN2) * (gp_int(p0, p1) - gp_int(1 - p1, 1 - p0)) + (2 / LN2) * gp_int(1 - 2 * p1, 1 - 2 * p0)
        worstd = v.a if worstd is None else min(worstd, v.a)
    assert worstd > 0, worstd
    return worst, worstd


def certify(M0, Mmax, K, thresh):
    """Adaptive: a cell at level M whose lower bound is below `thresh` is split, down to level Mmax."""
    stack = [(i, M0) for i in range(2 ** (M0 - 1))]
    worst, worst_cell, ncells = None, None, 0
    while stack:
        i, M = stack.pop()
        v = Phi_cell(i, M, K)
        ncells += 1
        if v.a < thresh and M < Mmax:
            stack.append((2 * i, M + 1)); stack.append((2 * i + 1, M + 1))
            continue
        if worst is None or v.a < worst:
            worst, worst_cell = v.a, (i, M)
        if ncells % 200 == 0:
            print("cells %d, pending %d, running min %.6f" % (ncells, len(stack), float(worst)), flush=True)
    return worst, worst_cell, ncells


if __name__ == "__main__":
    M0 = int(sys.argv[1]) if len(sys.argv) > 1 else 9
    Mmax = int(sys.argv[2]) if len(sys.argv) > 2 else 14
    K = int(sys.argv[3]) if len(sys.argv) > 3 else 8
    thresh = mpf(sys.argv[4]) if len(sys.argv) > 4 else mpf("0.02")
    assert K < M0, "need K < M so that T^k maps cells without wrapping"
    w1, w2 = eps_neg_check()
    print("eps < 0 on (0,1/2): max upper bound on cells of [1/64,0.45] = %s ; min lower bound of eps' on [0.45,1/2] = %s"
          % (mp.nstr(w1, 8), mp.nstr(w2, 8)), flush=True)
    worst, (i, M), n = certify(M0, Mmax, K, thresh)
    a = mpf(1) / 2 + i * mpf(2) ** (-M)
    print("K=%d, cells examined %d: certified min of Phi_K lower bounds = %s on cell [%s, %s] (level %d)"
          % (K, n, mp.nstr(worst, 10), mp.nstr(a, 12), mp.nstr(a + mpf(2) ** (-M), 12), M))
    print("CERTIFIED POSITIVE" if worst > 0 else "NOT CERTIFIED")
