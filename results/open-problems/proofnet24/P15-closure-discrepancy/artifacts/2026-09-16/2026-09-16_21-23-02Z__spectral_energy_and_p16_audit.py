from fractions import Fraction
from itertools import product


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def mt(A):
    return [list(row) for row in zip(*A)]


# P15 finite noncommuting critical-noise witness.
a = Fraction(1, 2)
C1 = [[0, a], [a, 0]]
C2 = [[a, 0], [0, -a]]
comm = msub(mm(C1, C2), mm(C2, C1))
agg = madd(mm(mt(C1), C1), mm(mt(C2), C2))
assert comm != [[0, 0], [0, 0]]
assert agg == [[Fraction(1, 2), 0], [0, Fraction(1, 2)]]
beta2 = Fraction(1, 2)
p = 4
assert (p - 1) * beta2 < 2
bellman_mult = Fraction(p - 1, 2) * beta2
assert bellman_mult == Fraction(3, 4)


# Independent exact audit of P16-D5-SERIAL-POTENTIAL-20.
T = [(aa, b, c) for aa, b, c in product(range(1, 5), repeat=3)
     if aa + c <= 5 and aa + b + c >= 6]
assert len(T) == 30

P = {
    (1, 1): Fraction(3, 4),
    (1, 2): Fraction(1, 4),
    (1, 3): Fraction(1, 12),
    (1, 4): Fraction(3, 4),
}
Q = {
    (1, 1): Fraction(15, 32),
    (2, 1): Fraction(1, 16),
    (3, 1): Fraction(7, 96),
    (4, 1): Fraction(3, 16),
    (4, 2): Fraction(1, 16),
    (4, 3): Fraction(1, 48),
}


def pv(D, key):
    return D.get(key, Fraction(0))


zero_edges = []
for aa, b, c in T:
    base_lhs = Fraction(1, b * c) - Fraction(b, 4)
    base_rhs = pv(P, (b, c)) - pv(P, (aa, b))
    assert base_lhs <= base_rhs
    if base_lhs == base_rhs:
        zero_edges.append(((aa, b), (b, c)))

    q_lhs = (Fraction(1, b * c) - Fraction(b, 4)
             + Fraction(15, 32) * (b - 2))
    q_rhs = pv(Q, (b, c)) - pv(Q, (aa, b))
    assert q_lhs <= q_rhs

assert len(zero_edges) == 7

adj = {}
for u, v in zero_edges:
    adj.setdefault(u, []).append(v)
nodes = set(adj) | {v for _, v in zero_edges}
cycles = set()


def canon(cyc):
    rots = [tuple(cyc[i:] + cyc[:i]) for i in range(len(cyc))]
    return min(rots)


for start in nodes:
    def dfs(cur, path, seen):
        for nxt in adj.get(cur, []):
            if nxt == start:
                cycles.add(canon(path))
            elif nxt not in seen and len(path) < len(nodes):
                dfs(nxt, path + [nxt], seen | {nxt})

    dfs(start, [start], {start})

assert cycles == {((1, 1), (1, 4), (4, 1))}


def stats(word):
    ell = len(word)
    S = sum(word)
    R = sum(Fraction(1, word[i] * word[(i + 1) % ell])
            for i in range(ell))
    D = Fraction(ell, S)
    delta = Fraction(1, 2) - D
    C = Fraction(S, 1) / R
    internal_degrees = [
        5 - word[(i - 1) % ell] - word[(i + 1) % ell]
        for i in range(ell)
    ]
    return S, R, D, delta, C, internal_degrees


s114 = stats([1, 1, 4])
s1144 = stats([1, 1, 4, 4])
assert s114[:5] == (6, Fraction(3, 2), Fraction(1, 2),
                    Fraction(0), Fraction(4))
assert s114[5] == [0, 0, 3]
assert s1144[:5] == (10, Fraction(25, 16), Fraction(2, 5),
                     Fraction(1, 10), Fraction(32, 5))
assert s1144[5] == [0, 0, 0, 0]
assert Fraction(s1144[0], 4) - s1144[1] == \
       Fraction(15, 32) * (s1144[0] - 2 * 4)

print("P15 I0066 spectral-energy + P16 independent exact audit")
print("C1C2-C2C1 =", comm)
print("C1^T C1 + C2^T C2 =", agg)
print("beta^2 =", beta2)
print("p =", p,
      ", (p-1)beta^2 =", (p - 1) * beta2,
      ", Bellman multiplier =", bellman_mult,
      sep="")
print("P16 admissible relaxed triples =", len(T))
print("P16 base zero-slack edges =", len(zero_edges))
print("P16 zero-slack directed cycles =", sorted(cycles))
print("P16 word 1,1,4 stats =", s114)
print("P16 word 1,1,4,4 stats =", s1144)
print("ALL_EXACT_CHECKS_PASSED")
