"""Exact check of A2-L3k (Lemma 3 with k spectral addresses): for a product row g_T of a Boolean f with k address
coordinates, kappa = min |ghat| = nu 2^{1-k-r} with nu integer, prod q_i | nu, nu' = nu / prod q_i,
w = nu'^2 4^{1-k-r} prod (p_i^2+q_i^2) and  L + H(q) = 2(k-1) - 2 log2 nu' + sum_i Ft(p_i, q_i).
Random Boolean f with k = 1..4 addresses and |C| = 1..3; every product row with w > 0 is tested exactly.
Also confirms the identity FAILS for k = 0 as literally stated (nu not an integer), i.e. it needs k >= 1."""
import random
from fractions import Fraction
from math import isqrt, gcd
import numpy as np
from refk2 import walsh_int, LogLin, rows_of
from ref_rows import h_loglin

random.seed(7)
tested = 0
fails = 0
for k in (0, 1, 2, 3, 4):
    for m in (1, 2, 3):
        n = k + m
        if n > 9:
            continue
        for trial in range(300 if k > 0 else 50):
            f = [random.choice((1, -1)) for _ in range(1 << n)]
            if random.random() < 0.5:   # sparse variants hit more product rows
                f = [1] * (1 << n)
                for _ in range(random.randint(1, 3)):
                    f[random.randrange(1 << n)] = -1
            W = walsh_int(np.array(f, dtype=np.int64))
            A = tuple(range(k))
            rows, C = rows_of(W, n, A)
            for t, V in rows.items():
                a = [v * v for v in V]
                Z = sum(a)
                if Z == 0:
                    continue
                al = [Fraction(sum(a[u] for u in range(1 << m) if (u >> i) & 1), Z) for i in range(m)]
                prod_ok = all(Fraction(a[u], Z) == np.prod([al[i] if (u >> i) & 1 else 1 - al[i] for i in range(m)])
                              for u in range(1 << m))
                if not prod_ok:
                    continue
                R = [i for i in range(m) if 0 < al[i] < 1]
                r = len(R)
                pairs = []
                for i in R:
                    mi = min(al[i], 1 - al[i]); k2 = (1 - mi) / mi
                    p, q = isqrt(k2.numerator), isqrt(k2.denominator)
                    assert p * p == k2.numerator and q * q == k2.denominator
                    pairs.append((p, q))
                kappa = Fraction(min(abs(v) for v in V if v), 2 ** n)
                nu = kappa * 2 ** (r + k - 1) if k >= 1 else kappa * Fraction(2) ** (r - 1)
                tested += 1
                if nu.denominator != 1:
                    fails += 1
                    if k >= 1:
                        print("FAIL nu not integer", k, m, f)
                    continue
                nu = nu.numerator
                pq = 1
                for (p, q) in pairs:
                    pq *= q
                assert nu % pq == 0
                nup = nu // pq
                PS = 1
                for (p, q) in pairs:
                    PS *= p * p + q * q
                w = Fraction(Z, 4 ** n)
                assert w == Fraction(nup * nup * PS, 1) * Fraction(4) ** (1 - k - r), ("weight", k, m)
                lhs = LogLin()
                for v in V:
                    if v:
                        pp = Fraction(v * v, 4 ** n)
                        lhs.q0 += pp * 2 * n
                        lhs.add_log2_int(-2 * pp, abs(v))
                lhs = LogLin().add(lhs, 1 / w)
                rhs = LogLin(Fraction(2 * (k - 1)))
                rhs.add_log2_int(-2, nup)
                for (p, q) in pairs:
                    rhs.q0 += 2
                    rhs.add_log2_int(-1, p * p + q * q)
                    rhs.add(h_loglin(p, q))
                d = LogLin().add(lhs).add(rhs, -1).clean()
                assert d.q0 == 0 and not d.ql, ("identity", k, m)
print("product rows tested:", tested, " rows where nu is not an integer:", fails, "(all of them have k = 0)")
