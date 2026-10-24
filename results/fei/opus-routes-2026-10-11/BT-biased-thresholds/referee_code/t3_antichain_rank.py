"""Lemmas 4.3, 4.4, 4.5.

4.3 (paper lem:pivotal-antichain, KNOWN): for regular monotone T, on every fiber fixing coordinates outside
    U_i u {i}, supp(d_i) is an antichain of {0,1}^{U_i}.  Exhaustive n<=4.
4.4: product law with marginals r_j, m_j = min(r_j,1-r_j); every antichain A has
    nu(A) <= E c_{|F|} <= E (|F|+1)^{-1/2} <= (2 sum m_j)^{-1/2},  F ~ sum Bern(2 m_j),
    c_q = 2^{-q} binom(q, floor(q/2)); and nu(A) <= max(r_j, 1-r_j) for every j.  Exact rationals.
4.5: rank functional  F_i = E_{nu_i} ln^+(Lambda_i/(|B cap U_i|+1)) <= 3 + ln 4, nu_i(B) = P(B u {i})/I_i,
    plus the intermediate  E_{nu_i}(1-t)^kappa <= sqrt(2/(t Lambda_i)).
"""
import random
import time
from fractions import Fraction as Fr
from math import comb
import mpmath
from bfcore import *

mpmath.mp.dps = 30


def antichains(n):
    pts = list(range(1 << n))
    res = []
    for code in range(1 << (1 << n)):
        S = [y for y in pts if (code >> y) & 1]
        ok = True
        for a in S:
            for b in S:
                if a != b and (a & b) == a:  # a < b
                    ok = False
                    break
            if not ok:
                break
        if ok:
            res.append(S)
    return res


def cq(q):
    return Fr(comb(q, q // 2), 2 ** q)


def EcF(ms):
    """E c_{|F|}, F = sum Bern(2 m_j), exact."""
    dist = [Fr(1)]
    for m in ms:
        p = 2 * m
        new = [Fr(0)] * (len(dist) + 1)
        for k, v in enumerate(dist):
            new[k] += v * (1 - p)
            new[k + 1] += v * p
        dist = new
    return sum(dist[k] * cq(k) for k in range(len(dist))), dist


def lemma43(Tmono, n):
    order = regular_order(Tmono, n)
    if order is None:
        return None
    pos = {c: k for k, c in enumerate(order)}
    for i in range(n):
        U = [c for c in range(n) if pos[c] < pos[i]]
        R = [c for c in range(n) if c != i and pos[c] > pos[i]]
        d = pivotal(Tmono, n, i)
        for r in range(1 << len(R)):
            base = 0
            for b in range(len(R)):
                if (r >> b) & 1:
                    base |= 1 << R[b]
            supp = []
            for z in range(1 << len(U)):
                y = base
                for b in range(len(U)):
                    if (z >> b) & 1:
                        y |= 1 << U[b]
                if d[y] == 1:
                    supp.append(z)
            for a in supp:
                for b in supp:
                    if a != b and (a & b) == a:
                        return False
    return True


def rank_functional(T, qs, order):
    n = len(qs)
    P = spectrum([2 * t - 1 for t in T], qs)
    pos = {c: k for k, c in enumerate(order)}
    out = []
    for i in range(n):
        Umask = 0
        Lam = Fr(0)
        for c in range(n):
            if pos[c] < pos[i]:
                Umask |= 1 << c
                Lam += sig2(qs[c])
        Ii = sum(P[S] for S in range(1 << n) if (S >> i) & 1)
        if Ii == 0:
            continue
        Fi = mpmath.mpf(0)
        for S in range(1 << n):
            if (S >> i) & 1 and P[S] > 0:
                kap = popcount(S & Umask)
                if Lam > kap + 1:
                    Fi += mpq(P[S] / Ii) * mpmath.log(mpq(Lam / (kap + 1)))
        # intermediate noise inequality on a t-grid
        worst = mpmath.mpf(-1)
        if Lam > 0:
            for t in [Fr(1, 64), Fr(1, 16), Fr(1, 4), Fr(1, 2), Fr(1)]:
                lhs = sum(P[S] / Ii * (1 - t) ** popcount(S & Umask) for S in range(1 << n) if (S >> i) & 1)
                rhs = mpmath.sqrt(mpq(2 / (t * Lam)))
                worst = max(worst, mpq(lhs) - rhs)
        out.append((i, Fi, worst))
    return out


if __name__ == "__main__":
    random.seed(44)
    t0 = time.time()
    # ---- Lemma 4.3 exhaustive
    cnt = 0
    bad = 0
    for n in range(1, 5):
        for code in range(1 << (1 << n)):
            T = [(code >> y) & 1 for y in range(1 << n)]
            if not is_monotone(T, n):
                continue
            r = lemma43(T, n)
            if r is None:
                continue
            cnt += 1
            if not r:
                bad += 1
    print("Lemma 4.3: regular monotone functions n<=4 checked", cnt, "violations", bad)

    # ---- Lemma 4.4 exhaustive antichains n<=4
    worst_a = -1
    worst_b = -1
    worst_c = -1
    cases = 0
    for n in range(1, 5):
        ACs = antichains(n)
        if n == 4:
            print("antichains in {0,1}^4:", len(ACs))
        for A in ACs:
            for rep in range(30):
                rs = [random.choice([Fr(random.randint(1, 999), 1000), Fr(1, 10 ** 6), Fr(1, 2)]) for _ in range(n)]
                w = mu_weights(rs)
                nuA = sum(w[y] for y in A)
                ms = [min(r, 1 - r) for r in rs]
                E_c, dist = EcF(ms)
                cases += 1
                # (a) nu(A) <= E c_F  (exact)
                worst_a = max(worst_a, float(nuA - E_c))
                # (b) nu(A)^2 <= 1/(2 sum m)  (exact)
                sm = sum(ms)
                worst_b = max(worst_b, float(nuA * nuA * 2 * sm - 1))
                # (c) nu(A) <= max(r_j, 1-r_j)
                worst_c = max(worst_c, float(nuA - min(max(r, 1 - r) for r in rs)))
    print("Lemma 4.4 exhaustive n<=4:", cases, "cases; max nu-Ec:", worst_a, "; max nu^2*2sum(m)-1:", worst_b,
          "; max nu - min_j max(r_j,1-r_j):", worst_c, "(all must be <= 0)")
    # adversarial: layers of {0,1}^m under product laws (exact DP)
    worst_layer = -1.0
    for trial in range(400):
        m = random.randint(2, 30)
        rs = [Fr(random.randint(1, 999), 1000) if random.random() < 0.7 else Fr(1, 2) for _ in range(m)]
        dist = [Fr(1)]
        for r in rs:
            new = [Fr(0)] * (len(dist) + 1)
            for k, v in enumerate(dist):
                new[k] += v * (1 - r)
                new[k + 1] += v * r
            dist = new
        best = max(dist)
        ms = [min(r, 1 - r) for r in rs]
        E_c, _ = EcF(ms)
        worst_layer = max(worst_layer, float(best - E_c), float(best * best * 2 * sum(ms) - 1))
    print("Lemma 4.4 on layers (antichains) m<=30, 400 random product laws: max violation", worst_layer)
    print("time", round(time.time() - t0, 1))

    # ---- Lemma 4.5: rank functional on thresholds n<=12 (exact spectra, mp logs)
    L0 = 3 + mpmath.log(4)
    maxF = mpmath.mpf(0)
    maxW = mpmath.mpf(-10)
    arg = None
    for trial in range(220):
        n = random.randint(5, 11)
        kind = random.choice(["sym", "rand", "geo", "two"])
        if kind == "sym":
            w = [1] * n
        elif kind == "rand":
            w = [random.randint(1, 9) for _ in range(n)]
        elif kind == "geo":
            w = [2 ** (n - j) for j in range(n)]
        else:
            k = random.randint(1, n - 1)
            w = [random.randint(2, 6)] * k + [1] * (n - k)
        w.sort(reverse=True)
        theta = random.randint(1, sum(w))
        T = threshold_table(w, theta)
        mode = random.choice(["half", "rand", "skew"])
        if mode == "half":
            qs = [Fr(1, 2)] * n
        elif mode == "rand":
            qs = [Fr(random.randint(1, 99), 100) for _ in range(n)]
        else:
            qs = [Fr(random.choice([1, 5, 50, 95, 99]), 100) for _ in range(n)]
        order = list(range(n))  # weights sorted decreasingly => desirability order
        for (i, Fi, worst) in rank_functional(T, qs, order):
            if Fi > maxF:
                maxF = Fi
                arg = (w, theta, [str(q) for q in qs], i)
            maxW = max(maxW, worst)
    print("Lemma 4.5: max rank functional", mpmath.nstr(maxF, 6), "(bound 3+ln4 =", mpmath.nstr(L0, 6), ") at", arg)
    print("Lemma 4.5 intermediate: max [E(1-t)^kappa - sqrt(2/(t Lambda))] =", mpmath.nstr(maxW, 6), "(must be <= 0)")
    print("time", round(time.time() - t0, 1))
