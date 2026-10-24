#!/usr/bin/env python3
"""Exact facet enumeration for the F_2^2 XOR three-marginal polytope.

Atoms are (u,v,w) with u,v,w in F_2^2 and w=u xor v.  We use nine
independent marginal coordinates by dropping state 3 in each of the three
four-state marginals.  Every facet is found by exhaustive exact enumeration
of the 9-vertex affine bases that could span an 8-dimensional facet.
"""
from itertools import combinations
from fractions import Fraction
from math import gcd
from functools import reduce

# Sixteen atoms, nine independent marginal coordinates.
V = []
for u in range(4):
    for v in range(4):
        w = u ^ v
        y = []
        for s in (u, v, w):
            y.extend(1 if s == i else 0 for i in range(3))
        V.append(tuple(y))


def rank_q(rows):
    A = [[Fraction(x) for x in row] for row in rows]
    if not A:
        return 0
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if A[i][c]), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        q = A[r][c]
        A[r] = [x / q for x in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                q = A[i][c]
                A[i] = [A[i][j] - q * A[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def primitive_null(rows):
    """Return primitive integer nullvector of 9x10 rank-9 matrix, else None."""
    A = [[Fraction(x) for x in row] for row in rows]
    m, n = len(A), len(A[0])
    piv, r = [], 0
    for c in range(n):
        p = next((i for i in range(r, m) if A[i][c]), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        q = A[r][c]
        A[r] = [x / q for x in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                q = A[i][c]
                A[i] = [A[i][j] - q * A[r][j] for j in range(n)]
        piv.append(c)
        r += 1
        if r == m:
            break
    if r != 9:
        return None
    free = [c for c in range(n) if c not in piv]
    if len(free) != 1:
        return None
    f = free[0]
    x = [Fraction(0) for _ in range(n)]
    x[f] = 1
    for i, c in enumerate(piv):
        x[c] = -A[i][f]

    def lcm(a, b):
        return a * b // gcd(a, b)

    L = 1
    for q in x:
        L = lcm(L, q.denominator)
    z = [int(q * L) for q in x]
    g = reduce(gcd, (abs(t) for t in z if t), 0)
    z = [t // g for t in z]
    for t in z:
        if t:
            if t < 0:
                z = [-s for s in z]
            break
    return tuple(z)


def canonical_supporting(z):
    vals = [sum(z[j] * V[i][j] for j in range(9)) + z[9] for i in range(16)]
    if all(t >= 0 for t in vals):
        return z
    if all(t <= 0 for t in vals):
        return tuple(-t for t in z)
    return None


def lin_prob(block, states):
    """Affine form for probability of 'states' in one four-state marginal.
    Returns (coeff[9], const), after state 3 is eliminated.
    """
    coeff = [0] * 9
    const = 0
    off = 3 * block
    for s in states:
        if s < 3:
            coeff[off + s] += 1
        else:
            const += 1
            for j in range(3):
                coeff[off + j] -= 1
    return coeff, const


def add_forms(*forms):
    c = [0] * 9
    k = 0
    for scale, (a, b) in forms:
        for j in range(9):
            c[j] += scale * a[j]
        k += scale * b
    return c, k


def primitive_ineq(coeff, const):
    z = list(coeff) + [const]
    g = reduce(gcd, (abs(t) for t in z if t), 0)
    z = [t // g for t in z]
    # Orientation is the literal >=0 orientation supplied by caller, do not flip.
    return tuple(z)

# Affine dimension check.
base = V[0]
diffs = [[V[i][j] - base[j] for j in range(9)] for i in range(1, 16)]
aff_dim = rank_q(diffs)
assert aff_dim == 9

# Exhaust all possible facet-supporting hyperplanes.
facets = set()
for S in combinations(range(16), 9):
    z = primitive_null([V[i] + (1,) for i in S])
    if z is None:
        continue
    z = canonical_supporting(z)
    if z is not None:
        facets.add(z)

# Expected twelve marginal-simplex facets.
expected = set()
for b in range(3):
    for s in range(4):
        a, k = lin_prob(b, {s})
        expected.add(primitive_ineq(a, k))  # probability >=0

# Expected twelve nontrivial character-parity facets.
# States are two-bit vectors encoded 0..3.  The three nonzero characters are
# ell_mask=1,2,3 with ell(s)=parity(mask & s).
def bitpar(n):
    return n.bit_count() & 1

for mask in (1, 2, 3):
    q = []
    for b in range(3):
        ones = {s for s in range(4) if bitpar(mask & s)}
        q.append(lin_prob(b, ones))
    # q_B+q_C-q_A >=0 and cyclic permutations
    expected.add(primitive_ineq(*add_forms((-1, q[0]), (1, q[1]), (1, q[2]))))
    expected.add(primitive_ineq(*add_forms((1, q[0]), (-1, q[1]), (1, q[2]))))
    expected.add(primitive_ineq(*add_forms((1, q[0]), (1, q[1]), (-1, q[2]))))
    # 2-q_A-q_B-q_C >=0
    c, k = add_forms((-1, q[0]), (-1, q[1]), (-1, q[2]))
    k += 2
    expected.add(primitive_ineq(c, k))

assert len(expected) == 24
assert facets == expected, (len(facets), len(expected), facets - expected, expected - facets)

# Every expected inequality is genuinely a facet: tight atoms affinely span dim 8.
for z in expected:
    tight = [V[i] for i in range(16)
             if sum(z[j] * V[i][j] for j in range(9)) + z[9] == 0]
    b = tight[0]
    d = [[row[j] - b[j] for j in range(9)] for row in tight[1:]]
    assert rank_q(d) == 8

print('F2^2 XOR three-marginal polytope')
print('atoms = 16')
print('affine_dimension = 9')
print('exact_facets = 24')
print('marginal_nonnegativity_facets = 12')
print('character_parity_facets = 12')
print('all facets independently tight-span dimension 8')
print('ALL_EXACT_CHECKS_PASS')
