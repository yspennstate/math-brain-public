"""Independent recheck of the ordered-cone coefficient certificate for Phi' >= 0 (an agent, 11 Nov 2026).

No sympy: integer polynomials as dicts {exponent tuple: int}. Written from the statement, not from the prover's script.

Claim checked. x in R^n, sum x = 0, x_1 >= x_2 >= ... >= x_n, x_1 + x_n >= 0 (so a = x_1 is the coordinate of
largest modulus). With T = sum x^2, P = sum x^3, Q = sum x^4 (not normalised),
    H = K * Nh + 2 (n-3) (n(n-1) a^2 - T) * Dh,
    K  = (n^2 - 6n + 6) T^2 + 2 n Q,
    Nh = n(n-1) (T^2 - Q + 2 a P - 2 a^2 T) + T^2,
    Dh = n Q T - T^3 - n P^2,
is the degree-8 homogenisation of Phi' = K N + 2n(n-3)(n(n-1)S^2 - 1) D. If x = sum_k z_k rho_k with z_k >= 0 over
the extreme rays rho_k of the cone and every coefficient of H as a polynomial in z is >= 0, then H >= 0 on the cone.

Rays. The cone {sum = 0, ordered} is simplicial with rays r_j = (n-j repeated j times, -j repeated n-j times),
j = 1..n-1, and x = sum_j (x_j - x_{j+1})/n * r_j. The functional x_1 + x_n equals n - 2j on r_j. Cutting a
simplicial cone with the half-space x_1 + x_n >= 0 gives the rays r_j with n - 2j >= 0 and, for each pair
(i, j) with n - 2i > 0 > n - 2j, the point (2j - n) r_i + (n - 2i) r_j of the two-face spanned by r_i, r_j.
The script also checks this ray list numerically: random points of the cone are decomposed by linear programming-free
means (explicit formula below) and H(x) is compared with the polynomial in z.
"""
import sys
import time
import random
from fractions import Fraction


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
    for m1, v1 in p.items():
        for m2, v2 in q.items():
            m = tuple(a + b for a, b in zip(m1, m2))
            r[m] = r.get(m, 0) + v1 * v2
    return {m: v for m, v in r.items() if v}


def pscale(p, c):
    return {m: c * v for m, v in p.items()} if c else {}


def rays(n):
    r = {j: [n - j] * j + [-j] * (n - j) for j in range(1, n)}
    out, lab = [], []
    for j in range(1, n):
        if n - 2 * j >= 0:
            out.append(r[j]); lab.append((j,))
    for i in range(1, n):
        for j in range(1, n):
            if n - 2 * i > 0 and n - 2 * j < 0:
                out.append([(2 * j - n) * u + (n - 2 * i) * v for u, v in zip(r[i], r[j])]); lab.append((i, j))
    return out, lab


def H_poly(n, R):
    k = len(R)
    def unit(t):
        return tuple(1 if s == t else 0 for s in range(k))
    X = []
    for c in range(n):
        X.append({unit(t): R[t][c] for t in range(k) if R[t][c]})
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
    return padd(pmul(K, Nh), pmul(W, Dh), 2 * (n - 3))


def H_num(n, x):
    T = sum(v * v for v in x); P = sum(v ** 3 for v in x); Q = sum(v ** 4 for v in x); a = x[0]
    K = (n * n - 6 * n + 6) * T * T + 2 * n * Q
    Nh = n * (n - 1) * (T * T - Q + 2 * a * P - 2 * a * a * T) + T * T
    Dh = n * Q * T - T ** 3 - n * P * P
    return K * Nh + 2 * (n - 3) * (n * (n - 1) * a * a - T) * Dh


def peval(p, z):
    s = Fraction(0)
    for m, v in p.items():
        t = Fraction(v)
        for e, zz in zip(m, z):
            if e:
                t *= zz ** e
        s += t
    return s


def main():
    ns = [int(a) for a in sys.argv[1:]] or [5, 6, 7]
    rnd = random.Random(20261111)
    for n in ns:
        t0 = time.monotonic()
        R, lab = rays(n)
        # every ray lies in the cone
        for r in R:
            assert sum(r) == 0 and all(r[c] >= r[c + 1] for c in range(n - 1)) and r[0] + r[-1] >= 0, r
        Hp = H_poly(n, R)
        neg = [(m, v) for m, v in Hp.items() if v < 0]
        degs = {sum(m) for m in Hp}
        # identity check: polynomial in z against direct evaluation at x = sum z_k rho_k, exact rationals
        bad = 0
        for _ in range(6):
            z = [Fraction(rnd.randint(0, 9), rnd.randint(1, 7)) for _ in R]
            x = [sum(zk * r[c] for zk, r in zip(z, R)) for c in range(n)]
            if peval(Hp, z) != H_num(n, x):
                bad += 1
        # the pure powers z_k^8: value of H on each ray (zero at star and edge only)
        pure = []
        for t, l in enumerate(lab):
            m = tuple(8 if s == t else 0 for s in range(len(R)))
            pure.append((l, Hp.get(m, 0)))
        zero_rays = [l for l, v in pure if v == 0]
        print(f"n={n} rays={len(R)} terms={len(Hp)} degrees={sorted(degs)} negative={len(neg)} "
              f"identity_mismatch={bad} zero_on_rays={zero_rays} min_coeff={min(Hp.values())} "
              f"seconds={time.monotonic() - t0:.1f}", flush=True)
        if neg:
            print("  first negative terms:", neg[:5], flush=True)


if __name__ == "__main__":
    main()
