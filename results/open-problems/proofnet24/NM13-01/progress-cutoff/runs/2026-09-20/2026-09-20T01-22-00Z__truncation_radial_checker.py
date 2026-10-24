from fractions import Fraction


def complete_graph(n):
    return {i: [j for j in range(n) if j != i] for i in range(n)}


def complete_bipartite(a, b):
    G = {i: [] for i in range(a + b)}
    for i in range(a):
        for j in range(a, a + b):
            G[i].append(j)
            G[j].append(i)
    return G


def truncation(G):
    d = len(next(iter(G.values())))
    arcs = [(x, y) for x in G for y in G[x]]
    idx = {a: i for i, a in enumerate(arcs)}
    N = len(arcs)
    Q = [[Fraction(0) for _ in range(N)] for _ in range(N)]
    for a, (x, y) in enumerate(arcs):
        # Matching/flip edge.
        Q[a][idx[(y, x)]] += Fraction(1, d)
        # Clique edges inside the tail fiber.
        for z in G[x]:
            if z != y:
                Q[a][idx[(x, z)]] += Fraction(1, d)
    return arcs, idx, Q


def verify(G, name):
    n = len(G)
    d = len(next(iter(G.values())))
    arcs, idx, Q = truncation(G)
    N = len(arcs)
    assert N == n * d
    assert all(sum(row) == 1 for row in Q)

    # An exact rational test vector for the Dirichlet decomposition.
    f = [Fraction(((7 * i + 3 * i * i) % 17) - 8) for i in range(N)]
    g = {}
    for x in G:
        g[x] = sum(f[idx[(x, y)]] for y in G[x]) / d
    h = [f[i] - g[x] for i, (x, y) in enumerate(arcs)]
    assert all(sum(h[idx[(x, y)]] for y in G[x]) == 0 for x in G)

    mean_f = sum(f) / N
    var_f = sum((u - mean_f) ** 2 for u in f) / N
    mean_g = sum(g.values(), Fraction(0)) / n
    var_g = sum((u - mean_g) ** 2 for u in g.values()) / n
    v_fiber = sum(u * u for u in h) / N
    assert var_f == var_g + v_fiber

    E_full = Fraction(0)
    E_internal = Fraction(0)
    E_flip = Fraction(0)
    for i, (x, y) in enumerate(arcs):
        for j, p in enumerate(Q[i]):
            if not p:
                continue
            term = Fraction(1, 2 * N) * p * (f[i] - f[j]) ** 2
            E_full += term
            if arcs[j] == (y, x):
                E_flip += term
            else:
                E_internal += term
    assert E_full == E_internal + E_flip
    assert E_internal == v_fiber

    # Dirichlet energy of the tail average on the d-regular base.
    E_base = Fraction(0)
    for x in G:
        for y in G[x]:
            E_base += Fraction(1, 2 * n * d) * (g[x] - g[y]) ** 2
    assert E_base <= 2 * d * E_flip + 4 * v_fiber
    assert E_base <= 2 * d * E_full

    # Universal-truncation radial two-state chain away from the root.
    v = Fraction(d - 2, d * (d + 2))
    gp = Fraction(2, d + 2)
    gm = Fraction(0)
    m_plus = Fraction(1, d)
    m_minus = -Fraction(1, d)
    E_g_plus = Fraction(d - 2, d) * gp + Fraction(2, d) * gm
    E_g_minus = gp
    assert gp - E_g_plus == m_plus - v
    assert gm - E_g_minus == m_minus - v

    pi_plus = Fraction(d, d + 2)
    pi_minus = Fraction(2, d + 2)
    assert pi_plus * m_plus + pi_minus * m_minus == v

    # Exact return probability from radius 1, inward-oriented state.
    z = Fraction(1, d - 1)
    B_over_A = Fraction(2 * (d - 1), d)
    assert (d - 1) * z * z - d * z + 1 == 0
    return_probability = B_over_A * z
    assert return_probability == Fraction(2, d)

    # Root defect in the corrected radial martingale.
    b0 = Fraction(2, d * (d + 2))
    root_defect = (
        Fraction(1, d)
        - v
        + (Fraction(d - 1, d) * gp + Fraction(1, d) * gm - gp)
    )
    assert root_defect == b0

    print(f"{name}: PASS")
    print(f"  n={n}, d={d}, truncation vertices={N}, degree={d}")
    print("  Var(f)=Var(tail-average)+V_fiber: PASS")
    print(f"  internal Dirichlet = V_fiber = {E_internal}")
    print("  E_base(g) <= 2d E_flip + 4 V_fiber <= 2d E_trunc: PASS")
    print(f"  radial speed v*={v}, inverse speed={1 / v}")
    print(f"  Poisson corrector g(+)=2/(d+2)={gp}, g(-)=0: PASS")
    print(f"  return probability from (r=1,-)={return_probability}")
    print(f"  root martingale defect b0={b0}")


verify(complete_graph(4), "Tr(K4)")
verify(complete_bipartite(3, 3), "Tr(K3,3)")
print("ALL_EXACT_CHECKS_PASS")
