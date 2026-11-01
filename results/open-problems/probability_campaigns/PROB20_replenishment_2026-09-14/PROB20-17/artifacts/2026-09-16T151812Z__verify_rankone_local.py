#!/usr/bin/env python3
"""Exact self-check for PROB20-17 local rank-one analysis.

All acceptance decisions use fractions.Fraction only.

Family:
  u_x(eps) = ((1-(eps*x)^2)/(1+(eps*x)^2),
              2 eps*x/(1+(eps*x)^2))
  A_x = u_x u_x^T.

For equal-scale rank-one PSD matrices, every word norm is the product of
absolute consecutive Gram entries. The script:
  1) verifies, over every x-subset of {-4,...,4}, n=4,...,8 and m=4,...,n,
     the exact z=eps^2 derivative formula
       d/dz (WOR/WR)|_{z=0} = -4 (m-1) Var(x)/(n-1);
  2) searches the same geometries at eps in {1/20,1/50,1/100,1/200}
     using exact rational arithmetic and asserts WOR/WR <= 1.

This is a finite corroborative certificate for the report's analytic theorem;
it is not an exhaustive search of PSD matrices.
"""

from fractions import Fraction
from itertools import combinations

POOL = tuple(range(-4, 5))
DENOMS = (20, 50, 100, 200)
NMAX = 8


def gram_halfangle(xs, eps):
    g = []
    for x in xs:
        tx = eps * x
        row = []
        for y in xs:
            ty = eps * y
            num = 1 - tx * tx - ty * ty + 4 * tx * ty + tx * tx * ty * ty
            den = (1 + tx * tx) * (1 + ty * ty)
            row.append(abs(num / den))
        g.append(row)
    return g


def wr_avg(g, m):
    n = len(g)
    # total weight of all length-m walks = 1^T G^(m-1) 1
    v = [Fraction(1) for _ in range(n)]
    for _ in range(m - 1):
        v = [sum(v[i] * g[i][j] for i in range(n)) for j in range(n)]
    return sum(v, Fraction(0)) / Fraction(n**m)


def wor_avg(g, m):
    n = len(g)
    # subset DP for all ordered simple paths of length m
    cur = {(1 << i, i): Fraction(1) for i in range(n)}
    for _ in range(1, m):
        nxt = {}
        for (mask, last), val in cur.items():
            for j in range(n):
                if (mask >> j) & 1:
                    continue
                key = (mask | (1 << j), j)
                nxt[key] = nxt.get(key, Fraction(0)) + val * g[last][j]
        cur = nxt
    total = sum(cur.values(), Fraction(0))
    falling = 1
    for r in range(m):
        falling *= n - r
    return total / Fraction(falling)


def ratio_exact(xs, m, eps):
    g = gram_halfangle(xs, eps)
    wr = wr_avg(g, m)
    wor = wor_avg(g, m)
    assert wr > 0
    return wor / wr, wor, wr


def population_variance(xs):
    n = len(xs)
    mean = Fraction(sum(xs), n)
    return sum((Fraction(x) - mean) ** 2 for x in xs) / n


def direct_ratio_derivative_z(xs, m):
    # For the half-angle family, g_ij(z) = 1 - 2(x_i-x_j)^2 z + O(z^2).
    n = len(xs)
    s = sum(Fraction(-2 * (x - y) ** 2) for x in xs for y in xs)
    wr_d = Fraction(m - 1, n * n) * s
    wor_d = Fraction(m - 1, n * (n - 1)) * s  # diagonal derivatives vanish
    # Since WOR(0)=WR(0)=1, derivative of ratio is WOR_d-WR_d.
    return wor_d - wr_d


def predicted_ratio_derivative_z(xs, m):
    n = len(xs)
    return -Fraction(4 * (m - 1), n - 1) * population_variance(xs)


def main():
    derivative_checks = 0
    for n in range(4, NMAX + 1):
        for xs in combinations(POOL, n):
            for m in range(4, n + 1):
                got = direct_ratio_derivative_z(xs, m)
                want = predicted_ratio_derivative_z(xs, m)
                assert got == want, (xs, m, got, want)
                assert got < 0  # xs are distinct, hence variance > 0
                derivative_checks += 1

    search_instances = 0
    best = None
    best_offdiag = None
    for q in DENOMS:
        eps = Fraction(1, q)
        for n in range(4, NMAX + 1):
            for xs in combinations(POOL, n):
                for m in range(4, n + 1):
                    ratio, wor, wr = ratio_exact(xs, m, eps)
                    assert ratio <= 1, (q, xs, m, ratio)
                    rec = (ratio, xs, n, m, q, wor, wr)
                    if best is None or ratio > best[0]:
                        best = rec
                    if m < n and (best_offdiag is None or ratio > best_offdiag[0]):
                        best_offdiag = rec
                    search_instances += 1

    ratio, xs, n, m, q, wor, wr = best
    ro, xso, no, mo, qo, woro, wro = best_offdiag

    print("ALL ASSERTIONS PASSED")
    print(f"derivative_checks={derivative_checks}")
    print(f"exact_search_instances={search_instances}")
    print("pool=-4,-3,-2,-1,0,1,2,3,4")
    print("eps_denominators=20,50,100,200")
    print("best_overall:")
    print(f"  n={n} m={m} eps=1/{q} xs={xs}")
    print(f"  WOR/WR={ratio}")
    print(f"  decimal={float(ratio):.16f}")
    print("best_genuinely_m_less_than_n:")
    print(f"  n={no} m={mo} eps=1/{qo} xs={xso}")
    print(f"  WOR/WR={ro}")
    print(f"  decimal={float(ro):.16f}")
    ex = (-4, -3, -2, -1, 0)
    ex_m = 4
    print("example_local_coefficient:")
    print(f"  xs={ex} n=5 m=4 Var={population_variance(ex)}")
    print(f"  d_dz_ratio_at_0={predicted_ratio_derivative_z(ex, ex_m)}")


if __name__ == "__main__":
    main()
