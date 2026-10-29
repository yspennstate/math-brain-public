"""Independent check of T084-C015/C016 (complete-graph forests).

Method, chosen to differ from the proof: no Lagrange substitution, no Hermite
recurrence for the counts. The vertex-degree polynomial H(z) at a vertex v is
computed directly by the exponential formula over the components of F - v:
a component on k vertices is one of k^(k-2) trees with k-1 edges, either
unattached (weight 1) or attached to v at one of its k vertices (weight k t z).
Then Z = H(1), E = H'(1)/N, L = H''(1)/(N(N-1)) by exchangeability at v, and D
from the edge-count derivative t E' - E = 2(n-2) L + h D/2 (also brute forced).
Small n: every edge subset of K_n enumerated with union-find.
"""
import itertools, json, sys
from fractions import Fraction
import sympy as sp

t, z = sp.symbols("t z")


def H_direct(n):
    N = n - 1
    x = sp.symbols("x")
    s = sum(sp.Integer(k) ** (k - 2) * t ** (k - 1) * (1 + k * t * z) * x ** k / sp.factorial(k)
            for k in range(1, N + 1))
    ser = sp.series(sp.exp(s), x, 0, N + 1).removeO()
    return sp.expand(sp.factorial(N) * ser.coeff(x, N))


def quantities(n):
    N, h = n - 1, (n - 2) * (n - 3)
    H = H_direct(n)
    Z = sp.expand(H.subs(z, 1))
    E = sp.expand(sp.diff(H, z).subs(z, 1) / N)
    L = sp.expand(sp.diff(H, z, 2).subs(z, 1) / (N * (N - 1)))
    D = sp.expand(2 * (t * sp.diff(E, t) - E - 2 * (n - 2) * L) / h)
    return H, Z, E, L, D


def brute(n):
    V = range(n)
    edges = list(itertools.combinations(V, 2))
    e01, e02, e23 = edges.index((0, 1)), edges.index((0, 2)), edges.index((2, 3))
    Zc, Ec, Lc, Dc = [0] * n, [0] * n, [0] * n, [0] * n
    for mask in range(1 << len(edges)):
        par = list(V)

        def f(a):
            while par[a] != a:
                par[a] = par[par[a]]
                a = par[a]
            return a
        ok, k = True, 0
        for i, (a, b) in enumerate(edges):
            if mask >> i & 1:
                ra, rb = f(a), f(b)
                if ra == rb:
                    ok = False
                    break
                par[ra] = rb
                k += 1
        if not ok:
            continue
        Zc[k] += 1
        if mask >> e01 & 1:
            Ec[k] += 1
            if mask >> e02 & 1:
                Lc[k] += 1
            if mask >> e23 & 1:
                Dc[k] += 1
    pol = lambda c: sp.expand(sum(ci * t ** i for i, ci in enumerate(c)))
    return pol(Zc), pol(Ec), pol(Lc), pol(Dc)


def P_list(n, a0, b0):
    P = [sp.Integer(1), b0]
    for k in range(2, n + 1):
        P.append(sp.expand(b0 * P[-1] - a0 * (k - 1) * P[-2]))
    return P


out = {"brute": {}, "formulas": {}, "riccati": {}, "series": {}, "largeT": {}}
for n in range(4, 8):
    _, Z, E, L, D = quantities(n)
    bZ, bE, bL, bD = brute(n)
    out["brute"][n] = all(sp.expand(p - q) == 0 for p, q in ((Z, bZ), (E, bE), (L, bL), (D, bD)))
    print("brute", n, out["brute"][n], flush=True)

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 16
for n in range(4, NMAX + 1):
    H, Z, E, L, D = quantities(n)
    N, h, M = n - 1, (n - 2) * (n - 3), n * (n - 1) // 2
    a0 = 1 / t
    b0 = n + a0
    P = P_list(n, a0, b0)
    Q = lambda k: P[k] - k * P[k - 1]
    f1 = [t ** (n - 1) * Q(n - 1), t ** (n - 1) * Q(n - 2), t ** (n - 1) * Q(n - 3),
          t ** (n - 1) * (P[n - 3] - (n - 4) * P[n - 4])]
    ok1 = all(sp.simplify(sp.expand(fx - q)) == 0 for fx, q in zip(f1, (Z, E, L, D)))
    # C015 (4): H(z) = t^N Q_N(N + a + z, a)
    Pz = P_list(N, a0, N + a0 + z)
    okH = sp.simplify(sp.expand(t ** N * (Pz[N] - N * Pz[N - 1]) - H)) == 0
    rho = E / Z
    ok4 = sp.simplify(L / Z - ((2 + n * t) * rho - 2 * t) / (n - 2)) == 0
    ok5 = sp.simplify(D / Z - (1 - 2 * (n - 4) * t + (-1 / t + 2 * n - 9 + n * (n - 4) * t) * rho) / h) == 0
    ok7 = sp.expand(t * sp.diff(Z, t) - M * E) == 0
    lhs = 2 * t ** 2 * sp.diff(rho, t)
    rhs = t - 2 * n * t ** 2 + ((2 * n + 1) * t - 1 + n ** 2 * t ** 2) * rho - n * (n - 1) * t * rho ** 2
    ok8 = sp.simplify(sp.together(lhs - rhs)) == 0
    out["formulas"][n] = [ok1, okH, ok4, ok5, ok7]
    out["riccati"][n] = ok8
    # (11), (12): small t
    adj = sp.series(sp.expand(E ** 2 - Z * L), t, 0, 4).removeO()
    dis = sp.series(sp.expand(E ** 2 - Z * D), t, 0, 5).removeO()
    rs = sp.series(rho, t, 0, 4).removeO()
    delta, a_, b_ = t * h, t - 2 * (n - 4) * t ** 2, -1 + (2 * n - 9) * t + n * (n - 4) * t ** 2
    fexpr = delta * rho ** 2 - b_ * rho - a_
    lim0 = sp.limit(fexpr / t ** 5, t, 0)
    out["series"][n] = [sp.expand(adj - t ** 3) == 0, sp.expand(dis - 2 * t ** 4) == 0,
                        sp.expand(rs - (t - t ** 2 + (3 - n) * t ** 3)) == 0, sp.simplify(lim0 - 2 * h) == 0]
    liminf = sp.limit(fexpr, t, sp.oo)
    r_inf = sp.limit(rho, t, sp.oo)
    r1 = sp.limit((rho - r_inf) * t, t, sp.oo)
    out["largeT"][n] = [sp.simplify(r_inf - sp.Rational(2, n)) == 0, sp.simplify(r1 + sp.Rational(n + 6, n ** 3)) == 0,
                        sp.simplify(liminf - sp.Rational(4 * h, n ** 4)) == 0]
    print(n, out["formulas"][n], ok8, out["series"][n], out["largeT"][n], flush=True)

json.dump({k: {str(a): b for a, b in v.items()} for k, v in out.items()},
          open(r"(local file)", "w"), default=str, indent=1)
print("ALL", all(all(v if isinstance(v, bool) else all(v) for v in d.values()) for d in out.values()))
