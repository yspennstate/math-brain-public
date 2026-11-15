"""Exact check of the chain  n (n(n-1) a^2 - T) Psi_h >= H  on random rational points (an agent, 11 Nov 2026).

Homogeneous forms (T = sum x^2 not normalised, a = max x = coordinate of largest modulus):
    Psi_h = (n-4)(2 Q T - T^3) - 2 (n-3) P^2 + (n-1) K m,      K = (n^2-6n+6) T^2 + 2 n Q,   m = max_{i != j} x_i x_j
    M_h   = (T^2 - Q + 2 a P - a^2 T) / (n(n-1) a^2 - T)
    H     = K Nh + 2 (n-3)(n(n-1) a^2 - T) Dh   (as in cone_recheck.py)
Claims tested, all in exact rational arithmetic:
    (1) n(n-1) a^2 - T > 0;   (2) m >= M_h;   (3) n (n(n-1)a^2 - T) Psi_h - H = (n-1) n K (n(n-1)a^2 - T)(m - M_h) exactly;
    (4) hence Psi_h >= 0 whenever H >= 0.
Also: the decomposition of a random point of the cone into the listed extreme rays with nonnegative coefficients
(greedy transport), to test that the ray list generates the cone.
"""
import random
from fractions import Fraction as F


def rays(n):
    r = {j: [n - j] * j + [-j] * (n - j) for j in range(1, n)}
    return r


def forms(n, x):
    T = sum(v * v for v in x); P = sum(v ** 3 for v in x); Q = sum(v ** 4 for v in x); a = x[0]
    K = (n * n - 6 * n + 6) * T * T + 2 * n * Q
    m = max(x[i] * x[j] for i in range(n) for j in range(n) if i != j)
    W = n * (n - 1) * a * a - T
    Mh = (T * T - Q + 2 * a * P - a * a * T) / W
    Nh = n * (n - 1) * (T * T - Q + 2 * a * P - 2 * a * a * T) + T * T
    Dh = n * Q * T - T ** 3 - n * P * P
    H = K * Nh + 2 * (n - 3) * W * Dh
    Psi = (n - 4) * (2 * Q * T - T ** 3) - 2 * (n - 3) * P * P + (n - 1) * K * m
    return T, K, m, W, Mh, H, Psi


def decompose(n, x):
    """x in the cone -> nonnegative coefficients on r_j (n-2j >= 0) and on the mixed rays (i, j)."""
    r = rays(n)
    c = {j: (x[j - 1] - x[j]) / n for j in range(1, n)}          # x = sum c_j r_j, c_j >= 0
    pos = {i: c[i] * (n - 2 * i) for i in c if n - 2 * i > 0}     # mass on the inside
    neg = {j: c[j] * (2 * j - n) for j in c if n - 2 * j < 0}     # mass on the outside
    coef = {}
    for j, need in neg.items():
        for i in list(pos):
            if need == 0:
                break
            t = min(need, pos[i])
            if t > 0:
                # t units: uses t/(n-2i) of r_i and t/(2j-n) of r_j = t/((n-2i)(2j-n)) of the mixed ray
                coef[(i, j)] = coef.get((i, j), 0) + t / ((n - 2 * i) * (2 * j - n))
                pos[i] -= t; need -= t
        assert need == 0, "outside mass not covered: point not in the cone"
    for i in pos:
        coef[(i,)] = pos[i] / (n - 2 * i)
    for i in c:
        if n - 2 * i == 0:
            coef[(i,)] = c[i]
    y = [F(0)] * n
    for key, z in coef.items():
        assert z >= 0
        if len(key) == 1:
            v = r[key[0]]
        else:
            i, j = key
            v = [(2 * j - n) * u + (n - 2 * i) * w for u, w in zip(r[i], r[j])]
        y = [p + z * q for p, q in zip(y, v)]
    return y == list(x)


def main():
    rnd = random.Random(1111)
    for n in range(5, 13):
        worst_gap = None; minPsi = None; cnt = 0; dec_ok = 0; dec_try = 0
        for trial in range(4000):
            kind = trial % 4
            if kind == 0:
                x = [F(rnd.randint(-30, 30)) for _ in range(n)]
            elif kind == 1:
                x = [F(rnd.choice([-3, -1, 0, 0, 0, 1, 2])) for _ in range(n)]
            elif kind == 2:                                   # near the star
                x = [F(n - 1) * 50] + [F(-50 + rnd.randint(-3, 3)) for _ in range(n - 1)]
            else:                                             # near the edge
                x = [F(100), F(-100)] + [F(rnd.randint(-4, 4)) for _ in range(n - 2)]
            s = sum(x); x = [v - s / n for v in x]
            x.sort(reverse=True)
            if x[0] + x[-1] < 0:
                x = sorted([-v for v in x], reverse=True)
            if all(v == 0 for v in x):
                continue
            T, K, m, W, Mh, H, Psi = forms(n, x)
            assert W > 0
            assert m >= Mh, (n, x)
            lhs = n * W * Psi - H
            assert lhs == (n - 1) * n * K * W * (m - Mh), (n, x)
            assert lhs >= 0
            if trial < 400:
                dec_try += 1; dec_ok += decompose(n, x)
            cnt += 1
            g = float((m - Mh) / T)
            worst_gap = g if worst_gap is None else min(worst_gap, g)
            p = float(Psi / T ** 3)
            minPsi = p if minPsi is None else min(minPsi, p)
        print(f"n={n} points={cnt} all asserts passed; min (m - M)/T = {worst_gap:.3e}; min Psi (normalised) = {minPsi:.6f}; "
              f"ray decompositions exact: {dec_ok}/{dec_try}")


if __name__ == "__main__":
    main()
