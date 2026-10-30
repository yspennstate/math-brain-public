from fractions import Fraction
from itertools import combinations, permutations


def cadd(z, w):
    return (z[0] + w[0], z[1] + w[1])


def cmul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def perm_from_string(s):
    return tuple(int(ch) - 1 for ch in s)


def perm_sign(p):
    inv = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return -1 if inv % 2 else 1


# ---------------------------------------------------------------------------
# 1. Exact Gaussian-integer refutation of the Drury upper-facet candidate.
# ---------------------------------------------------------------------------
A = [(-76, 69), (12, 8), (0, -143), (0, -1)]
B = [(-13, 85), (49, 4), (-140, 117), (40, -16)]


def vertex(p):
    z = (1, 0)
    for i, j in enumerate(p):
        z = cmul(z, cadd(A[i], B[j]))
    return z


vertices = {p: vertex(p) for p in permutations(range(4))}
assert len(set(vertices.values())) == 24
assert len(set(z[0] for z in vertices.values())) == 24
max_perm = max(vertices, key=lambda p: vertices[p][0])
M = vertices[max_perm][0]
assert max_perm == perm_from_string("4321")
assert M == 44569469

needed = ["2134", "3214", "1432", "4321"]
three_u = sum(vertices[perm_from_string(s)][0] for s in needed)
three_u -= vertices[perm_from_string("1234")][0]
assert three_u == 135459685
upper_facet_violation_numerator = three_u - 3 * M
assert upper_facet_violation_numerator == 1751278
assert upper_facet_violation_numerator > 0


# ---------------------------------------------------------------------------
# 2. Exact symbolic check of all one-use spanning-tree Givens words in n=4.
# Polynomials use six variables (c0,s0,c1,s1,c2,s2) and integer coefficients.
# ---------------------------------------------------------------------------
ZERO_MON = (0,) * 6


def pone():
    return {ZERO_MON: 1}


def pvar(k):
    e = [0] * 6
    e[k] = 1
    return {tuple(e): 1}


def padd(x, y):
    z = dict(x)
    for m, a in y.items():
        z[m] = z.get(m, 0) + a
        if z[m] == 0:
            del z[m]
    return z


def pneg(x):
    return {m: -a for m, a in x.items()}


def pmul(x, y):
    z = {}
    for m, a in x.items():
        for n, b in y.items():
            q = tuple(m[i] + n[i] for i in range(6))
            z[q] = z.get(q, 0) + a * b
    return {m: a for m, a in z.items() if a}


def pscale(x, a):
    return {m: a * b for m, b in x.items() if a * b}


def psum(items):
    z = {}
    for x in items:
        z = padd(z, x)
    return z


def real_givens_word(edges):
    U = [[{} for _ in range(4)] for _ in range(4)]
    one = pone()
    for i in range(4):
        U[i][i] = one
    for k, (u, v) in enumerate(edges):
        c = pvar(2 * k)
        s = pvar(2 * k + 1)
        old_u = [U[i][u] for i in range(4)]
        old_v = [U[i][v] for i in range(4)]
        # Right multiplication by [[c,-s],[s,c]].
        for i in range(4):
            U[i][u] = padd(pmul(old_u[i], c), pmul(old_v[i], s))
            U[i][v] = padd(pmul(old_v[i], c), pneg(pmul(old_u[i], s)))
    return U


def mu_poly(U, p):
    z = pone()
    for i, j in enumerate(p):
        z = pmul(z, U[i][j])
    return pscale(z, perm_sign(p))


def is_tree(E):
    if len(E) != 3:
        return False
    adj = {i: set() for i in range(4)}
    for u, v in E:
        adj[u].add(v)
        adj[v].add(u)
    seen = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen) == 4


all_edges = list(combinations(range(4), 2))
trees = [E for E in combinations(all_edges, 3) if is_tree(E)]
assert len(trees) == 16

target_sum = pone()
for k in range(3):
    c = pvar(2 * k)
    s = pvar(2 * k + 1)
    target_sum = pmul(target_sum, padd(pmul(c, c), pmul(s, s)))

word_count = 0
nonzero_term_count = 0
for T in trees:
    for order in permutations(T):
        word_count += 1
        U = real_givens_word(order)
        mus = [mu_poly(U, p) for p in permutations(range(4))]
        nonzero = [q for q in mus if q]
        assert len(nonzero) == 8
        for q in nonzero:
            assert len(q) == 1
            (mon, coeff), = q.items()
            assert coeff == 1
            assert all(e % 2 == 0 for e in mon)
        assert psum(mus) == target_sum
        nonzero_term_count += len(nonzero)

assert word_count == 96
assert nonzero_term_count == 768


# ---------------------------------------------------------------------------
# 3. Exact four-edge cycle: positivity of mu can fail immediately.
# ---------------------------------------------------------------------------
def rational_givens_word(edges, c=Fraction(3, 5), s=Fraction(4, 5)):
    U = [[Fraction(int(i == j)) for j in range(4)] for i in range(4)]
    for u, v in edges:
        old_u = [U[i][u] for i in range(4)]
        old_v = [U[i][v] for i in range(4)]
        for i in range(4):
            U[i][u] = c * old_u[i] + s * old_v[i]
            U[i][v] = c * old_v[i] - s * old_u[i]
    return U


cycle_edges = [(0, 1), (1, 2), (2, 3), (0, 3)]
U_cycle = rational_givens_word(cycle_edges)
cycle_mu = {}
for p in permutations(range(4)):
    z = Fraction(perm_sign(p), 1)
    for i, j in enumerate(p):
        z *= U_cycle[i][j]
    cycle_mu[p] = z

assert sum(cycle_mu.values(), Fraction(0, 1)) == 1
cycle_min = min(cycle_mu.values())
assert cycle_min == Fraction(-186624, 9765625)
assert cycle_min < 0

print("UPPER_FACET_MAX", M, "PERM", "".join(str(i + 1) for i in max_perm))
print("THREE_U", three_u)
print("UPPER_FACET_VIOLATION", upper_facet_violation_numerator,
      "=> u(F)-M = 1751278/3")
print("FOREST_GIVENS_TREE_WORDS", word_count)
print("FOREST_GIVENS_NONZERO_MU_TERMS", nonzero_term_count)
print("FOUR_CYCLE_MIN_MU", cycle_min)
print("PASS")
