"""Independent rigorous re-derivation of the scenario-B certificate (NOTES.md 5.6) by a different method.

The route bounds sup_L 2^{-L} (Eeven_t(L) - mu) by subdividing L into thousands of interval pieces.  Here the
same envelope is maximised in closed form instead: for each j, T_j(L) = 2 kappa (1-j) - Gmin((rmin+2-L-2j)_+, 2j)
is piecewise linear in L with at most three pieces (slopes GB, GA, 0), so on each piece the target is
phi(L) = 2^{-L} (A + B L) with B > 0, whose maximum on [La, Lb] is at clamp(1/ln2 - A/B, La, Lb).
Everything is evaluated in mpmath interval arithmetic (outward rounding), so the final bounds are rigorous.

Odd rows (e odd only) are enumerated from scratch over every coprime odd-odd pair (p > q), every odd nu',
every multiset with at most rho unfair pairs and N = nu'^2 prod (p^2+q^2)/2 <= 2^{rho+2} - 3.

Also re-derives every numeric constant of NOTES.md Sections 3 (Lemma E) and 5 with intervals."""
import sys, json
from math import gcd
from mpmath import iv, mpf, mp

iv.dps = 50
mp.dps = 50
LN2 = iv.log(2)


def log2(x):
    return iv.log(x) / LN2


def h(t):
    t = iv.mpf(t)
    return -(t * log2(t) + (1 - t) * log2(1 - t))


def I(x):
    return iv.mpf(x)


C = I(16) / 3 - I(3) / 2 * log2(I(3))
KAP = C / 2 - 1
DEL = 2 - C / 2
PSI = log2(1 + I(2) ** (-C))          # max_t h(t) - c t
SA = log2(I(5)) - 1


def G(p, q):
    S = p * p + q * q
    return KAP * (log2(I(S)) - 2) + C * I(q * q) / S - h(I(q * q) / S)


GA = G(2, 1) / SA
L10 = log2(I(10))
GB = (KAP * (L10 - 2) - PSI) / (L10 - 1)
A_ = DEL + GB
K0 = 2 * KAP - 2 * GB


def ub(x):
    return mpf(x.b)


def lb(x):
    return mpf(x.a)


def phi_sup(Acoef, Bcoef, La, Lb):
    """rigorous upper bound of sup_{L in [La,Lb]} 2^{-L} (A + B L), B > 0 (intervals A, B; numbers La <= Lb)"""
    La = I(La); Lb = I(Lb)
    Ls = 1 / LN2 - Acoef / Bcoef
    f = lambda L: I(2) ** (-L) * (Acoef + Bcoef * L)
    if ub(Ls) < lb(La):
        return ub(f(La))
    if lb(Ls) > ub(Lb):
        return ub(f(Lb))
    # critical point may lie inside: global maximum value 2^{-L*} B / ln 2 bounds the sup
    return max(ub(I(2) ** (-Ls) * Bcoef / LN2), ub(f(La)), ub(f(Lb)))


def even_sup(t, mu, rmin, Lmin, Lmax):
    """sup over L in [Lmin, Lmax] and j >= 1 of 2^{-L} (Eeven_t(L) - mu)"""
    best = mpf("-inf")
    j = 1
    while True:
        b1 = rmin + 2 - 2 * j - 2 * j * SA      # X = 2 j SA
        b2 = I(rmin + 2 - 2 * j)                 # X = 0
        # piece 1: L <= b1 (only where meaningful): T = 2kap(1-j) - GA 2j SA - GB (rmin+2-2j-2jSA - L)
        A1 = DEL * 0 + 2 * KAP * (1 - j) - GA * 2 * j * SA - GB * (rmin + 2 - 2 * j - 2 * j * SA) - C * t - mu
        B1 = DEL + GB
        A2 = 2 * KAP * (1 - j) - GA * (rmin + 2 - 2 * j) - C * t - mu
        B2 = DEL + GA
        A3 = 2 * KAP * (1 - j) - C * t - mu
        B3 = DEL
        pieces = []
        # the piece boundaries are intervals; use outward boundaries so every L is covered by some piece
        # piece 1 on [Lmin, min(Lmax, ub(b1))]
        if lb(Lmin) <= ub(b1):
            pieces.append((A1, B1, lb(Lmin), min(ub(Lmax), ub(b1))))
        # piece 2 on [max(Lmin, lb(b1)), min(Lmax, ub(b2))]
        lo2 = max(lb(Lmin), lb(b1)); hi2 = min(ub(Lmax), ub(b2))
        if lo2 <= hi2:
            pieces.append((A2, B2, lo2, hi2))
        # piece 3 on [max(Lmin, lb(b2)), Lmax]
        lo3 = max(lb(Lmin), lb(b2))
        if lo3 <= ub(Lmax):
            pieces.append((A3, B3, lo3, ub(Lmax)))
        for (Ac, Bc, La, Lb) in pieces:
            v = phi_sup(Ac, Bc, La, Lb)
            if v > best:
                best = v
        # stop once T_j is constant (= 2kap(1-j)) on the whole range: then larger j only lower it
        if ub(b2) <= lb(Lmin):
            break
        j += 1
        assert j < 100
    return best


def odd_rows(rho):
    """all odd rows: (N, nu', list of pairs) with u <= rho odd-odd coprime unfair pairs, N <= 2^{rho+2}-3"""
    NMAX = 2 ** (rho + 2) - 3
    pairs = []
    p = 3
    while (p * p + 1) // 2 <= NMAX:
        for q in range(1, p, 2):
            if gcd(p, q) == 1 and (p * p + q * q) // 2 <= NMAX:
                pairs.append((p, q))
        p += 2
    out = []

    def rec(start, prodn, chosen):
        nu = 1
        while prodn * nu * nu <= NMAX:
            out.append((prodn * nu * nu, nu, list(chosen)))
            nu += 2
        if len(chosen) == rho:
            return
        for k in range(start, len(pairs)):
            pp, qq = pairs[k]
            nn = (pp * pp + qq * qq) // 2
            if prodn * nn > NMAX:
                continue
            chosen.append((pp, qq))
            rec(k, prodn * nn, chosen)
            chosen.pop()

    rec(0, 1, [])
    return out, pairs


def odd_sup(t, mu, rho):
    best = mpf("-inf")
    rows, _ = odd_rows(rho)
    for (N, nu, prs) in rows:
        w = I(N) / 2 ** (rho + 2)
        L = rho + 2 - log2(I(N))
        eb = DEL * L + 2 * KAP * (1 - log2(I(nu)))
        for (p, q) in prs:
            eb = eb - G(p, q)
        eb = eb - C * t
        v = ub(w * (eb - mu))
        if v > best:
            best = v
    return best, len(rows)


def bound(rho, e_odd, mu):
    emin = 1 if e_odd else 2
    lo = I(emin) / 2 ** (rho + 2)
    Lmin = -log2(1 - 3 * lo)
    Lmax = -log2(lo)
    rmin = rho + 1 if e_odd else rho
    mu = I(mu)
    M = []
    nodd = 0
    for t in (0, 1, 2):
        v = even_sup(t, mu, rmin, Lmin, Lmax)
        if e_odd:
            vo, nodd = odd_sup(t, mu, rho)
            v = max(v, vo)
        M.append(v)
    tot = mu + I(M[0]) + 2 * I(M[1]) + I(M[2])
    return ub(tot), [float(x) for x in M], nodd


def best_mu(rho, e_odd, lo=-4.0, hi=0.0, it=60):
    """golden-section search on the convex function mu -> bound (float guide only; the final bound is rigorous)"""
    import math
    g = (math.sqrt(5) - 1) / 2
    a, b = lo, hi
    f = lambda m_: float(bound(rho, e_odd, mpf(m_))[0])
    x1 = b - g * (b - a); x2 = a + g * (b - a)
    f1, f2 = f(x1), f(x2)
    for _ in range(it):
        if f1 < f2:
            b, x2, f2 = x2, x1, f1
            x1 = b - g * (b - a); f1 = f(x1)
        else:
            a, x1, f1 = x1, x2, f2
            x2 = a + g * (b - a); f2 = f(x2)
    return (a + b) / 2


if __name__ == "__main__":
    out = {}
    print("c* =", C, "\nkappa =", KAP, "\ndelta =", DEL, "\npsi =", PSI, "\nSA =", SA, "\nGA =", GA, "\nGB =", GB,
          "\na =", A_, "\nK0 =", K0)
    for rho in (2, 3, 4, 5):
        for e_odd in (True, False):
            m_ = best_mu(rho, e_odd, it=40)
            # round mu to a short decimal and certify there
            mu_r = mpf(round(m_, 4))
            tot, M, nodd = bound(rho, e_odd, mu_r)
            # also certify at the route's mu values
            print(f"rho={rho} e {'odd ' if e_odd else 'even'}: best mu ~ {m_:.5f}; certified bound at mu={float(mu_r):.4f}:"
                  f" {float(tot):+.6f}  (M0,M1,M2)={tuple(round(x,6) for x in M)}  odd rows enumerated={nodd}", flush=True)
            out[f"rho{rho}_{'odd' if e_odd else 'even'}"] = dict(mu=float(mu_r), bound=float(tot), M=M, n_odd_rows=nodd)
    route_mu = {(2, True): "-1.7668", (2, False): "-1.7058", (3, True): "-1.4779", (3, False): "-1.4921"}
    for (rho, e_odd), mu in route_mu.items():
        tot, M, nodd = bound(rho, e_odd, mpf(mu))
        print(f"at the route's mu: rho={rho} e {'odd ' if e_odd else 'even'} mu={mu}: certified {float(tot):+.6f}", flush=True)
        out[f"route_mu_rho{rho}_{'odd' if e_odd else 'even'}"] = dict(mu=float(mpf(mu)), bound=float(tot))
    json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "ref_certificate.json", "w", encoding="utf-8"), indent=1)
