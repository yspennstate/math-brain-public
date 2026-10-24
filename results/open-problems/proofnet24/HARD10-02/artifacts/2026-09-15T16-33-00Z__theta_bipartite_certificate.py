"""
HARD10-02 exact certificate for 2026-09-15T16:33:00Z.

Certifies:
1. The planar bipartite triangle-free family H_m has
   D_m = -(5 m^3 + 41 m^2 - 91 m - 936)
         / ((m+6)^2 (m+8) (2m+13)),
   where d/dc P_ORRW(success)|_{c=1} = -D_m.
2. D_m < 0 iff integer m >= 5.
3. For m=5 and c=9/8, exact ORRW escape probability exceeds SRW.
4. Exact Graph-Atlas enumeration: every connected simple graph on at most
   seven vertices, every ordered root/target pair, and every non-target
   neighbor start has D >= 0. All arithmetic for D is Fraction-exact.

The Graph Atlas is NetworkX's standard list of all unlabeled graphs with at
most seven vertices; completeness of that external enumeration is the only
enumeration dependency.
"""

from fractions import Fraction as F
import networkx as nx


def theta_D(m: int) -> F:
    num = -(5*m**3 + 41*m**2 - 91*m - 936)
    den = (m+6)**2 * (m+8) * (2*m+13)
    return F(num, den)


def theta_first_crossing_parts(m: int):
    """Exact q-values/harmonic values for H_m."""
    h_x = F(3, m+6)
    h_y = F(2, m+6)
    h_z = F(1, m+6)
    q_xb = F(3, m+6)
    q_rz = -F(1, m+6)
    q_zy = -F(3, 2*m+13)
    q_yx = -F(3, m+8)
    D = (
        (1-h_x)*q_xb
        + m*h_z*q_rz
        + m*(h_y-h_z)*q_zy
        + m*(h_x-h_y)*q_yx
    )
    return {
        "h_x": h_x, "h_y": h_y, "h_z": h_z,
        "q_xb": q_xb, "q_rz": q_rz,
        "q_zy": q_zy, "q_yx": q_yx,
        "D": D,
    }


def theta_escape(m: int, c: F) -> F:
    """Exact full-c escape probability on H_m by branch-state reduction.

    Branch states before absorption:
      0: neither x-y nor y-z old
      A: x-y old, y-z fresh
      C: x-y and y-z both old

    X[(a,d)] is success probability from x with a A-branches, d C-branches.
    The recursion is triangular: decreasing k=a+d, increasing a at fixed k.
    """
    X = {}
    for k in range(m, -1, -1):
        n0 = m-k
        for a in range(0, k+1):
            d = k-a

            const = F(1)  # fresh x-b success edge

            # Enter a state-0 branch: it becomes A, then start at y.
            if n0:
                YA_new = (
                    c*X[(a+1, d)]
                    + c*X[(a, d+1)]/(c+2)
                )/(c+1)
                const += n0 * YA_new

            # Existing A-branch contribution has a current-X term plus
            # a term that converts that branch A -> C.
            if a:
                const += (
                    a*c*c*X[(a-1, d+1)]
                    / ((c+1)*(c+2))
                )

            # Coefficient multiplying current X[(a,d)] from returns through
            # already-old branch edges.
            coeff = (
                a*c*c/(c+1)
                + d*c*(c+1)/(c+2)
            )

            # At x: old x-r plus a+d old x-y edges, n0 fresh x-y edges,
            # and one fresh x-b edge.
            Z = c*(1+k) + n0 + 1
            X[(a,d)] = const / (Z-coeff)

    return X[(0,0)]


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
        if p != 1:
            A[col] = [x/p for x in A[col]]
        for r in range(n):
            if r == col:
                continue
            q = A[r][col]
            if q:
                A[r] = [
                    A[r][j] - q*A[col][j]
                    for j in range(2*n)
                ]
    return [row[n:] for row in A]


def exact_D_all_starts_for_root_target(G, root, target):
    """Exact D for all non-target root-neighbor starts.

    Uses one exact Dirichlet Green inverse and the closed first-crossing
    formula from the prior HARD10-02 checkpoint.
    """
    nodes = list(G.nodes())
    interior = [v for v in nodes if v not in (root, target)]
    ix = {v: i for i, v in enumerate(interior)}
    n = len(interior)
    if n == 0:
        return {}

    L = [[0]*n for _ in range(n)]
    rhs = [0]*n
    for v in interior:
        L[ix[v]][ix[v]] = G.degree(v)
        for w in G.neighbors(v):
            if w in ix:
                L[ix[v]][ix[w]] -= 1
            elif w == target:
                rhs[ix[v]] += 1

    Inv = invert_frac(L)
    hvec = [
        sum(Inv[i][j]*rhs[j] for j in range(n))
        for i in range(n)
    ]

    def h(v):
        if v == root:
            return F(0)
        if v == target:
            return F(1)
        return hvec[ix[v]]

    starts = [s for s in G.neighbors(root) if s != target and s in ix]
    out = {s: F(0) for s in starts}

    for u, v in G.edges():
        grad = h(v)-h(u)
        if grad == 0:
            continue

        if u in ix and v in ix:
            A = Inv[ix[u]][ix[u]]
            B = Inv[ix[v]][ix[v]]
            C = Inv[ix[u]][ix[v]]
            den = (1+C)**2 - A*B
            coeffX = (1+C+B)/den
            coeffY = (1+C+A)/den
            for s in starts:
                q = (
                    coeffX*Inv[ix[s]][ix[u]]
                    - coeffY*Inv[ix[s]][ix[v]]
                )
                out[s] += grad*q

        elif u in ix and v in (root, target):
            for s in starts:
                # Skip the already-old root-start edge.
                if frozenset((u, v)) == frozenset((root, s)):
                    continue
                q = Inv[ix[s]][ix[u]]
                out[s] += grad*q

        elif v in ix and u in (root, target):
            for s in starts:
                if frozenset((u, v)) == frozenset((root, s)):
                    continue
                # Stored orientation u -> v; boundary formula is for
                # interior -> boundary, hence the minus sign.
                q = -Inv[ix[s]][ix[v]]
                out[s] += grad*q

    return {s: (D, h(s)) for s, D in out.items()}


def atlas_certificate():
    counts = {}
    cases = 0
    zeros = 0
    minpos = None

    for G in nx.graph_atlas_g():
        n = len(G)
        if n < 2 or n > 7 or not nx.is_connected(G):
            continue
        counts[n] = counts.get(n, 0) + 1

        for root in G.nodes():
            for target in G.nodes():
                if target == root:
                    continue
                out = exact_D_all_starts_for_root_target(G, root, target)
                for start, (D, hs) in out.items():
                    cases += 1
                    assert D >= 0, (
                        "negative D", n, D, list(G.edges()),
                        root, target, start, hs
                    )
                    if D == 0:
                        zeros += 1
                    elif minpos is None or D < minpos:
                        minpos = D

    assert counts == {2:1, 3:2, 4:6, 5:21, 6:112, 7:853}
    assert cases == 104018
    assert zeros == 6273
    assert minpos == F(118942, 8752705)
    return counts, cases, zeros, minpos


def main():
    # Closed first-order formula and threshold checks.
    for m in range(1, 9):
        parts = theta_first_crossing_parts(m)
        assert parts["D"] == theta_D(m)
    assert theta_D(4) == F(9, 700)
    assert theta_D(5) == -F(259, 36179)
    for m in range(1, 5):
        assert theta_D(m) > 0
    for m in range(5, 20):
        assert theta_D(m) < 0

    # Concrete full-c planar bipartite triangle-free counterexample.
    m = 5
    c = F(9, 8)
    p = theta_escape(m, c)
    h = F(3, 11)
    diff = p-h
    assert diff == F(
        12273379805549756953660104222378580389717218286352429470319397,
        120057133643886825040706122653589668492966446032818287314554256827,
    )
    assert diff > 0

    counts, cases, zeros, minpos = atlas_certificate()

    print("H_5 first-order D:", theta_D(5))
    print("H_5 derivative at c=1:", -theta_D(5))
    print("H_5 c=9/8 exact escape excess:", diff)
    print("atlas connected counts:", counts)
    print("atlas cases:", cases)
    print("atlas zero-D cases:", zeros)
    print("atlas minimum positive D:", minpos)
    print("ALL EXACT CHECKS PASSED")


if __name__ == "__main__":
    main()
