"""Cone coefficient certificate with packed monomials (an agent, 11 Nov 2026).

Same statement as cone_recheck.py; a monomial z^e is the integer sum_k e_k 16^k (every e_k <= 8, total degree 8, so
products of monomials are sums of the codes with no carry). About a fifth of the memory of the tuple version.
Checks itself against cone_recheck.py's counts when run with n = 5 or 6, and against direct evaluation of H at
random rational points of the cone.
"""
import random
import resource
import sys
import time
from fractions import Fraction

from cone_recheck import H_num, rays


def padd(p, q, c=1):
    r = dict(p)
    for m, v in q.items():
        w = r.get(m, 0) + c * v
        if w:
            r[m] = w
        elif m in r:
            del r[m]
    return r


def pmul(p, q):
    r = {}
    if len(p) > len(q):
        p, q = q, p
    get = r.get
    for m1, v1 in p.items():
        for m2, v2 in q.items():
            m = m1 + m2
            r[m] = get(m, 0) + v1 * v2
    return {m: v for m, v in r.items() if v}


def pscale(p, c):
    return {m: c * v for m, v in p.items()} if c else {}


def H_poly(n, R):
    k = len(R)
    X = [{16 ** t: R[t][c] for t in range(k) if R[t][c]} for c in range(n)]
    T, P, Q = {}, {}, {}
    for xc in X:
        x2 = pmul(xc, xc); x3 = pmul(x2, xc); x4 = pmul(x2, x2)
        T = padd(T, x2); P = padd(P, x3); Q = padd(Q, x4)
    a = X[0]
    a2 = pmul(a, a)
    T2 = pmul(T, T)
    K = padd(pscale(T2, n * n - 6 * n + 6), Q, 2 * n)
    inner = padd(padd(padd(T2, Q, -1), pmul(a, P), 2), pmul(a2, T), -2)
    Nh = padd(pscale(inner, n * (n - 1)), T2)
    Dh = padd(padd(pscale(pmul(Q, T), n), pmul(T2, T), -1), pmul(P, P), -n)
    W = padd(pscale(a2, n * (n - 1)), T, -1)
    del inner, x2, x3, x4
    A = pmul(K, Nh)
    del K, Nh
    B = pmul(W, Dh)
    del W, Dh
    for m, v in B.items():                       # A += 2(n-3) B in place
        w = A.get(m, 0) + 2 * (n - 3) * v
        if w:
            A[m] = w
        elif m in A:
            del A[m]
    return A


def peval(p, z):
    k = len(z)
    s = Fraction(0)
    pw = [[zz ** e for e in range(9)] for zz in z]
    for m, v in p.items():
        t = Fraction(v)
        for i in range(k):
            e = (m >> (4 * i)) & 15
            if e:
                t *= pw[i][e]
        s += t
    return s


def main():
    ns = [int(a) for a in sys.argv[1:]] or [5, 6]
    known = {5: 1277, 6: 2991, 7: 75561, 8: 125947, 9: 2220039}
    rnd = random.Random(20261112)
    for n in ns:
        t0 = time.monotonic()
        R, lab = rays(n)
        k = len(R)
        Hp = H_poly(n, R)
        neg = [(m, v) for m, v in Hp.items() if v < 0]
        degs = {sum((m >> (4 * i)) & 15 for i in range(k)) for m in list(Hp)[:2000]}
        bad = 0
        for _ in range(3):
            z = [Fraction(rnd.randint(0, 5), rnd.randint(1, 3)) for _ in R]
            x = [sum(zk * r[c] for zk, r in zip(z, R)) for c in range(n)]
            if peval(Hp, z) != H_num(n, x):
                bad += 1
        zero_rays = [l for t, l in enumerate(lab) if Hp.get(8 * 16 ** t, 0) == 0]
        ok = "" if n not in known else (" count_matches_tuple_version" if known[n] == len(Hp) else " COUNT MISMATCH")
        rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        print(f"n={n} rays={k} terms={len(Hp)} degrees={sorted(degs)} negative={len(neg)} identity_mismatch={bad} "
              f"zero_on_rays={zero_rays} min_coeff={min(Hp.values())}{ok} maxrss={rss} seconds={time.monotonic() - t0:.1f}",
              flush=True)
        if neg:
            neg.sort(key=lambda mv: mv[1])
            show = [([(m >> (4 * i)) & 15 for i in range(k)], v) for m, v in neg[:6]]
            print(f"  negative terms {len(neg)}; most negative: {show}", flush=True)
            print("  ray labels:", lab, flush=True)


if __name__ == "__main__":
    main()
