from fractions import Fraction
from collections import deque


def petersen_adjacency():
    # vertices 0..4 outer cycle; 5..9 inner star; spokes i--(5+i)
    n = 10
    A = [[0] * n for _ in range(n)]

    def add(u, v):
        A[u][v] = A[v][u] = 1

    for i in range(5):
        add(i, (i + 1) % 5)
        add(i, 5 + i)
    for i in range(5):
        add(5 + i, 5 + ((i + 2) % 5))
    return A


def mm(A, B):
    n = len(A)
    m = len(B)
    k = len(B[0])
    return [
        [sum(A[i][j] * B[j][ell] for j in range(m)) for ell in range(k)]
        for i in range(n)
    ]


def square_by_distance(A):
    n = len(A)
    S = [[0] * n for _ in range(n)]
    for s in range(n):
        dist = [None] * n
        dist[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            if dist[u] == 2:
                continue
            for v, a in enumerate(A[u]):
                if a and dist[v] is None:
                    dist[v] = dist[u] + 1
                    q.append(v)
        for v in range(n):
            if v != s and dist[v] in (1, 2):
                S[s][v] = 1
    return S


A = petersen_adjacency()
n = len(A)
d = sum(A[0])
assert d == 3 and all(sum(row) == d for row in A)
A2 = mm(A, A)
S_formula = [
    [A2[i][j] + A[i][j] - (d if i == j else 0) for j in range(n)]
    for i in range(n)
]
S_dist = square_by_distance(A)
assert S_formula == S_dist
assert all(S_formula[i][i] == 0 for i in range(n))
assert all(x in (0, 1) for row in S_formula for x in row)
assert all(sum(row) == d * d for row in S_formula)

print("Petersen square identity: PASS")
print("base_degree =", d, "square_degree =", d * d)

for d in range(3, 13):
    # Exact radial jump counts on the square of the d-regular tree, away from levels 0,1.
    counts = {-2: 1, -1: 1, 0: d - 2, 1: d - 1, 2: (d - 1) ** 2}
    assert sum(counts.values()) == d * d

    mean = sum(Fraction(k * multiplicity, d * d) for k, multiplicity in counts.items())
    target = Fraction((d - 2) * (2 * d + 1), d * d)
    assert mean == target

    second = sum(
        Fraction(k * k * multiplicity, d * d)
        for k, multiplicity in counts.items()
    )
    target2 = Fraction(4 * d * d - 7 * d + 8, d * d)
    assert second == target2

    # If lambda is a normalized base eigenvalue, the square-walk eigenvalue is
    # q(lambda)=lambda^2+lambda/d-1/d.  Check the exact gap factorization on a grid.
    for num in range(-d, d + 1):
        lam = Fraction(num, d)
        qlam = lam * lam + lam / Fraction(d, 1) - Fraction(1, d)
        lhs = 1 - qlam
        rhs = (1 - lam) * (1 + lam + Fraction(1, d))
        assert lhs == rhs

    # The output branching base d^2-1 strictly exceeds the maximal base-distance-two
    # growth base (d-1)^2.  This is the singleton obstruction to output LRE.
    assert (d - 1) ** 2 < d * d - 1

    print(
        f"d={d}: radial_mean={mean}, compound_second={second}, "
        f"branch_ratio={Fraction((d - 1) ** 2, d * d - 1)}"
    )

# Concrete LPS degree d=6 application.
d = 6
v = Fraction((d - 2) * (2 * d + 1), d * d)
assert v == Fraction(13, 9)
print("LPS d=6 square: degree=36 speed=13/9 center=(9/13) log_5 n")
print("P26_T08_GRAPH_SQUARE_TRANSFER_EXACT_PASS")
