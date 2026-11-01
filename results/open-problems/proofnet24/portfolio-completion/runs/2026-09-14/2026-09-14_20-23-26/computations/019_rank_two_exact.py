"""Exact, deterministic checks for agents/019.md; standard library only.

No random search and no numerical eigenvalue certificates are used.
The proof in the report does not depend on this computation.
"""
from fractions import Fraction as F
from itertools import combinations
from collections import deque
import json


def identity(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def transpose(A):
    return [list(row) for row in zip(*A)]


def matmul(A, B):
    return [[sum(x * y for x, y in zip(row, col))
             for col in zip(*B)] for row in A]


def add(A, B):
    return [[x + y for x, y in zip(a, b)] for a, b in zip(A, B)]


def scale(A, t):
    return [[t * x for x in row] for row in A]


def outer(u):
    return [[x * y for y in u] for x in u]


def determinant(A):
    A = [row[:] for row in A]
    d = F(1)
    for j in range(len(A)):
        pivot = next((i for i in range(j, len(A)) if A[i][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            A[j], A[pivot] = A[pivot], A[j]
            d = -d
        a = A[j][j]
        d *= a
        for i in range(j + 1, len(A)):
            ratio = A[i][j] / a
            for k in range(j + 1, len(A)):
                A[i][k] -= ratio * A[j][k]
    return d


def principal(A, mask):
    ix = [i for i in range(len(A)) if mask >> i & 1]
    return [[A[i][j] for j in ix] for i in ix]


def mobius(f, n):
    c = f[:]
    for i in range(n):
        for mask in range(1 << n):
            if mask >> i & 1:
                c[mask] -= c[mask ^ (1 << i)]
    return c


def expectation_polynomial(A, c):
    return sum(c[s] * determinant(principal(A, s))
               for s in range(len(c)) if c[s])


def mixed(A, c, U, V):
    # Each variable is affine since its update has rank one, so this is exact.
    return (expectation_polynomial(add(add(A, U), V), c)
            - expectation_polynomial(add(A, U), c)
            - expectation_polynomial(add(A, V), c)
            + expectation_polynomial(A, c))


def projection(columns, n):
    out = [[F(0) for _ in range(n)] for _ in range(n)]
    for col in columns:
        out = add(out, outer(col))
    return out


def supermodular_differences(f, n):
    out = []
    for i, j in combinations(range(n), 2):
        for s in range(1 << n):
            if not (s >> i & 1 or s >> j & 1):
                out.append(f[s | 1 << i | 1 << j] + f[s]
                           - f[s | 1 << i] - f[s | 1 << j])
    return out


def exact_rank_one_coupling(pairlaw, triplelaw):
    # Rational augmenting-path flow on the pair/triple inclusion graph.
    source, sink = ("source", 0), ("sink", 0)
    caps, adj = {}, {}

    def edge(a, b, capacity):
        caps[a, b] = capacity
        caps[b, a] = F(0)
        adj.setdefault(a, []).append(b)
        adj.setdefault(b, []).append(a)

    for p, mass in pairlaw.items():
        edge(source, ("pair", p), mass)
    for t, mass in triplelaw.items():
        edge(("triple", t), sink, mass)
    for p in pairlaw:
        for t in triplelaw:
            if p & t == p:
                edge(("pair", p), ("triple", t), F(1))
    original = caps.copy()
    value = F(0)
    while True:
        parent = {source: None}
        queue = deque([source])
        while queue and sink not in parent:
            a = queue.popleft()
            for b in adj[a]:
                if b not in parent and caps[a, b] > 0:
                    parent[b] = a
                    queue.append(b)
        if sink not in parent:
            break
        path, b = [], sink
        while parent[b] is not None:
            a = parent[b]
            path.append((a, b))
            b = a
        amount = min(caps[e] for e in path)
        for a, b in path:
            caps[a, b] -= amount
            caps[b, a] += amount
        value += amount
    assert value == 1
    coupling = {
        (p, t): original[("pair", p), ("triple", t)]
        - caps[("pair", p), ("triple", t)]
        for p in pairlaw for t in triplelaw if p & t == p
    }
    for p, mass in pairlaw.items():
        assert sum(x for (pp, _), x in coupling.items() if pp == p) == mass
    for t, mass in triplelaw.items():
        assert sum(x for (_, tt), x in coupling.items() if tt == t) == mass
    return {key: mass for key, mass in coupling.items() if mass}


def main():
    n = 5
    I = identity(n)
    a = list(map(F, [1, 2, 3, 4, 5]))
    Q = add(I, scale(outer(a), -F(2, 55)))
    assert matmul(transpose(Q), Q) == I
    cols = transpose(Q)
    u, v = cols[:2]
    U, V = outer(u), outer(v)
    B = [[F(0) for _ in range(n)] for _ in range(n)]
    diagonal = [F(1, 3), F(2, 3), F(1, 5), F(2, 5), F(3, 5)]
    for i, x in enumerate(diagonal):
        B[i][i] = x
    B[0][2] = B[2][0] = F(1, 100)
    B[1][3] = B[3][1] = F(1, 80)
    # Exact strict-contraction certificate: symmetric Gershgorin intervals.
    intervals = []
    for i in range(n):
        radius = sum(abs(B[i][j]) for j in range(n) if j != i)
        lo, hi = B[i][i] - radius, B[i][i] + radius
        assert 0 < lo <= hi < 1
        intervals.append([str(lo), str(hi)])
    K = matmul(matmul(Q, B), transpose(Q))
    C = [[F(0) for _ in range(n)] for _ in range(n)]
    for j in range(2, n):
        C = add(C, scale(outer(cols[j]), diagonal[j]))
    weights = [1, 1, 2, 3, 4]
    f = [F(max(0, sum(weights[i] for i in range(n) if s >> i & 1) - 4) ** 2)
         for s in range(1 << n)]
    assert min(supermodular_differences(f, n)) >= 0
    c = mobius(f, n)
    fc = [f[((1 << n) - 1) ^ s] for s in range(1 << n)]
    cc = mobius(fc, n)
    qK, qC = mixed(K, c, U, V), mixed(C, c, U, V)
    assert qK == qC
    spectral_sum, endpoint_output, coupling_count = F(0), [], 0
    for mask in range(1 << (n - 2)):
        selected = [j for j in range(2, n) if mask >> (j - 2) & 1]
        remaining = [j for j in range(2, n) if j not in selected]
        P = projection([cols[j] for j in selected], n)
        value = mixed(P, c, U, V)
        weight = F(1)
        for j in range(2, n):
            weight *= diagonal[j] if j in selected else 1 - diagonal[j]
        spectral_sum += weight * value
        # Complement plus compression reduces every n=5 vertex to rank <= 1.
        reduced_cols, reduced_c = selected, c
        if len(selected) >= 2:
            reduced_cols, reduced_c = remaining, cc
            P_reduced = projection([cols[j] for j in reduced_cols], n)
            assert value == mixed(P_reduced, reduced_c, U, V)
        pair_projection = add(U, V)
        pairlaw = {s: determinant(principal(pair_projection, s))
                   for s in range(1 << n) if s.bit_count() == 2}
        if reduced_cols:
            triple_projection = add(pair_projection, outer(cols[reduced_cols[0]]))
            triplelaw = {s: determinant(principal(triple_projection, s))
                         for s in range(1 << n) if s.bit_count() == 3}
            coupling = exact_rank_one_coupling(pairlaw, triplelaw)
            assert all(reduced_c[p] + reduced_c[t] >= 0 for p, t in coupling)
            certificate = sum(mass * (reduced_c[p] + reduced_c[t])
                              for (p, t), mass in coupling.items())
            coupling_count += 1
        else:
            certificate = sum(mass * reduced_c[p] for p, mass in pairlaw.items())
        assert certificate == value and value >= 0
        endpoint_output.append({"subset_mask": mask, "rank": len(selected),
                                "weight": str(weight), "mixed": str(value)})
    assert qK == spectral_sum
    output = {
        "dimension": n,
        "arithmetic": "fractions.Fraction throughout",
        "basis": "Q = I - (2/55) aa^T, a=(1,2,3,4,5)",
        "B_diagonal": [str(x) for x in diagonal],
        "B_extra_entries": {"02=20": "1/100", "13=31": "1/80"},
        "strict_contraction_Gershgorin_intervals": intervals,
        "f": "max(0, sum_{i in S}(1,1,2,3,4)_i - 4)^2",
        "negative_Mobius_coefficients": {str(s): str(x) for s, x in enumerate(c) if x < 0},
        "mixed_derivative_exact": str(qK),
        "mixed_derivative_decimal": float(qK),
        "compression_identity": True,
        "spectral_interpolation_identity": True,
        "complement_identities": True,
        "exact_monotone_couplings_checked": coupling_count,
        "projection_endpoints": endpoint_output,
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
