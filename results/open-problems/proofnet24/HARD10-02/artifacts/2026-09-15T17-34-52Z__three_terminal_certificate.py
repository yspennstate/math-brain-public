"""HARD10-02 exact certificate for the 2026-09-15T17:34:52Z report.

Checks with fractions.Fraction on the planar bipartite H_5 graph:
  1. G(v,v)=xi(v)+R_AB*h(v)*(1-h(v));
  2. R_vA=G(v,v)+R_AB*h(v)^2 and the B analogue;
  3. the prior first-crossing/current identity;
  4. the new edge identity
       -beta*d = Delta_xi*d + R_AB*(1-hu-hv)*d^2;
  5. the full source/current/xi/bulk decomposition of D;
  6. the known exact H_5 value D=-259/36179.

No floating-point arithmetic is used.
"""

from fractions import Fraction as F


def invert_frac(M):
    n = len(M)
    A = [
        [F(M[i][j]) for j in range(n)]
        + [F(int(i == j)) for j in range(n)]
        for i in range(n)
    ]
    for col in range(n):
        piv = next(r for r in range(col, n) if A[r][col])
        if piv != col:
            A[col], A[piv] = A[piv], A[col]
        p = A[col][col]
        A[col] = [x / p for x in A[col]]
        for r in range(n):
            if r == col:
                continue
            q = A[r][col]
            if q:
                A[r] = [
                    A[r][j] - q * A[col][j]
                    for j in range(2 * n)
                ]
    return [row[n:] for row in A]


def solve_frac(A, b):
    inv = invert_frac(A)
    return [
        sum(inv[i][j] * F(b[j]) for j in range(len(b)))
        for i in range(len(b))
    ]


def effective_resistance(nodes, edges, a, b):
    rem = [v for v in nodes if v != b]
    ix = {v: i for i, v in enumerate(rem)}
    L = [[F(0) for _ in rem] for __ in rem]
    for u, v in edges:
        if u != b:
            L[ix[u]][ix[u]] += 1
        if v != b:
            L[ix[v]][ix[v]] += 1
        if u != b and v != b:
            L[ix[u]][ix[v]] -= 1
            L[ix[v]][ix[u]] -= 1
    rhs = [F(0) for _ in rem]
    rhs[ix[a]] = 1
    phi = solve_frac(L, rhs)
    return phi[ix[a]]


def dirichlet_data(nodes, edges, root, target):
    interior = [v for v in nodes if v not in (root, target)]
    ix = {v: i for i, v in enumerate(interior)}
    n = len(interior)
    L = [[F(0) for _ in interior] for __ in interior]
    rhs = [F(0) for _ in interior]

    for u, v in edges:
        if u in ix:
            L[ix[u]][ix[u]] += 1
        if v in ix:
            L[ix[v]][ix[v]] += 1
        if u in ix and v in ix:
            L[ix[u]][ix[v]] -= 1
            L[ix[v]][ix[u]] -= 1
        if u in ix and v == target:
            rhs[ix[u]] += 1
        if v in ix and u == target:
            rhs[ix[v]] += 1

    G = invert_frac(L)
    hvec = [
        sum(G[i][j] * rhs[j] for j in range(n))
        for i in range(n)
    ]

    def h(v):
        if v == root:
            return F(0)
        if v == target:
            return F(1)
        return hvec[ix[v]]

    return interior, ix, G, h


def H_m(m=5):
    nodes = ["r", "x", "b"]
    edges = [("r", "x"), ("x", "b")]
    for i in range(m):
        z = f"z{i}"
        y = f"y{i}"
        nodes += [z, y]
        edges += [("r", z), (z, y), (y, "x")]
    return nodes, edges


def exact_H5_certificate():
    nodes, edges = H_m(5)
    root, target, start = "r", "b", "x"
    interior, ix, G, h = dirichlet_data(nodes, edges, root, target)

    R = effective_resistance(nodes, edges, root, target)
    xi = {}

    for v in interior:
        RvA = effective_resistance(nodes, edges, v, root)
        RvB = effective_resistance(nodes, edges, v, target)
        xi[v] = (RvA + RvB - R) / 2

        assert xi[v] >= 0
        assert (
            G[ix[v]][ix[v]]
            == xi[v] + R * h(v) * (1 - h(v))
        )
        assert (
            RvA == G[ix[v]][ix[v]] + R * h(v) ** 2
        )
        assert (
            RvB == G[ix[v]][ix[v]] + R * (1 - h(v)) ** 2
        )

    initial = frozenset((root, start))
    D = F(0)
    source = h(start) * G[ix[start]][ix[start]]
    correction = F(0)
    current_term = F(0)
    xi_term = F(0)
    bulk_term = F(0)

    for u, v in edges:
        if frozenset((u, v)) == initial:
            continue
        d = h(v) - h(u)

        if u in ix and v in ix:
            A = G[ix[u]][ix[u]]
            B = G[ix[v]][ix[v]]
            C = G[ix[u]][ix[v]]
            X = G[ix[start]][ix[u]]
            Y = G[ix[start]][ix[v]]
            den = (1 + C) ** 2 - A * B

            q = ((1 + C + B) * X - (1 + C + A) * Y) / den
            r = ((1 + C - B) * X + (1 + C - A) * Y) / den
            j = X - Y
            gamma = A + B - 2 * C
            beta = A - B

            assert q - j == (gamma * j - beta * r) / (2 - gamma)

            D += d * q
            correction += d * (q - j)

            dxi = xi[v] - xi[u]
            assert (
                -beta * d
                == dxi * d + R * (1 - h(u) - h(v)) * d * d
            )

            current_term += gamma * d * j / (2 - gamma)
            xi_term += r * dxi * d / (2 - gamma)
            bulk_term += (
                R * r * (1 - h(u) - h(v)) * d * d
                / (2 - gamma)
            )

        else:
            # Fresh boundary edges have q=j exactly.
            if u in ix and v in (root, target):
                q = G[ix[start]][ix[u]]
            elif v in ix and u in (root, target):
                q = -G[ix[start]][ix[v]]
            else:
                continue
            D += d * q

    assert D == source + correction
    assert correction == current_term + xi_term + bulk_term
    assert D == -F(259, 36179)

    return {
        "R_AB": R,
        "D": D,
        "source": source,
        "current": current_term,
        "xi": xi_term,
        "bulk": bulk_term,
    }


if __name__ == "__main__":
    out = exact_H5_certificate()
    print("EXACT THREE-TERMINAL CERTIFICATE PASSED")
    for key, value in out.items():
        print(key, value)
    print("ALL EXACT CHECKS PASSED")
