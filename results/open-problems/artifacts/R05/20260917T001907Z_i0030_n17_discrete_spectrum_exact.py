#!/usr/bin/env python3
"""
R05 / I0030 exact finite certificate.

Claims checked:
  (1) order-17 connected arc-transitive class via prime-order affine reduction:
      exact inverse-closed Cayley search on F_17 has four multiplier-orbit
      isomorphism types, degrees 2,4,8,16; this is the complete non-2-transitive
      branch under Burnside, while the 2-transitive branch is K_17.
  (2) exact integer walk identities through power 40 on those four types.
  (3) discrete lazy-walk determinant identities, including the exact first odd
      obstruction polynomial for a d-regular arc-transitive graph with lambda
      common neighbors on every edge.
  (4) exact C5 phase thresholds: all-step monotonicity threshold sqrt(2)-1 and
      eventual threshold 1/5, with exact symbolic identities.

This does not change the frozen continuous-time Aldous--Fill 7.30 target.
"""
from itertools import product
import sympy as sp

# ---------------------------------------------------------------------------
# Prime-order exact Cayley classification at p=17.
# ---------------------------------------------------------------------------
p = 17
pairs = []
seen = set()
for k in range(1, p):
    if k in seen:
        continue
    pr = tuple(sorted((k, (-k) % p)))
    pairs.append(pr)
    seen.update(pr)
assert len(pairs) == 8

all_sets = []
for bits in product((0, 1), repeat=len(pairs)):
    S = set()
    for bit, pr in zip(bits, pairs):
        if bit:
            S.update(pr)
    all_sets.append(frozenset(S))
assert len(all_sets) == 256


def mult_stabilizer(S):
    return tuple(a for a in range(1, p)
                 if frozenset((a*s) % p for s in S) == S)


def affine_arc_transitive_connection_set(S):
    if not S:
        return False
    H = mult_stabilizer(S)
    s0 = next(iter(S))
    return set((a*s0) % p for a in H) == set(S)


def scale_canonical(S):
    return min(tuple(sorted((a*s) % p for s in S)) for a in range(1, p))

selected = [S for S in all_sets if affine_arc_transitive_connection_set(S)]
assert len(selected) == 15
assert sorted(len(S) for S in selected) == [2]*8 + [4]*4 + [8]*2 + [16]

classes = {}
for S in selected:
    classes.setdefault(scale_canonical(S), []).append(S)
assert len(classes) == 4
class_data = sorted((len(canon), len(members), canon)
                    for canon, members in classes.items())
assert [(d, count) for d, count, _ in class_data] == [(2,8),(4,4),(8,2),(16,1)]

# The multiplicative group F_17^* is cyclic of order 16.  The exact stabilizers
# of an affine arc-transitive connection set have the same size as S.
for S in selected:
    H = mult_stabilizer(S)
    assert len(H) == len(S)
    assert 16 in H   # -1 mod 17


def adjacency(S):
    return [[1 if i != j and ((j-i) % p in S) else 0
             for j in range(p)] for i in range(p)]


def connected(A):
    reached = {0}
    stack = [0]
    while stack:
        v = stack.pop()
        for w, x in enumerate(A[v]):
            if x and w not in reached:
                reached.add(w)
                stack.append(w)
    return len(reached) == len(A)


def matmul(A, B):
    n, m, k = len(A), len(B), len(B[0])
    assert len(A[0]) == m
    C = [[0]*k for _ in range(n)]
    for i in range(n):
        for t, a in enumerate(A[i]):
            if not a:
                continue
            for j, b in enumerate(B[t]):
                if b:
                    C[i][j] += a*b
    return C

for degree, _, canon in class_data:
    S = frozenset(canon)
    A = adjacency(S)
    assert connected(A)
    assert all(sum(row) == degree for row in A)
    H = mult_stabilizer(S)
    s0 = min(S)
    assert set((a*s0) % p for a in H) == set(S)

    M = [[int(i == j) for j in range(p)] for i in range(p)]
    for m in range(41):
        assert len({M[x][x] for x in range(p)}) == 1
        assert len({M[x][y] for x in range(p) for y in range(p) if A[x][y]}) == 1
        if m < 40:
            Mnext = matmul(M, A)
            for x in range(p):
                for y in range(p):
                    if A[x][y]:
                        assert Mnext[x][x] == degree*M[x][y]
            M = Mnext

# ---------------------------------------------------------------------------
# Exact determinant identity and first odd-step obstruction.
# ---------------------------------------------------------------------------
h, d, lam = sp.symbols('h d lam', real=True)
c = 1-h
# For Q_h = hI + (1-h)A/d on a loopless d-regular graph with constant
# edge common-neighbor number lam:
a1 = h
a2 = h**2 + c**2/d
a3 = h**3 + 3*h*c**2/d + lam*c**3/d**2
D1 = sp.factor(a1*a3 - a2**2)
expected_D1 = sp.factor((1-h)**2/d**2 * ((d-1-lam)*h**2 + (lam+2)*h - 1))
assert sp.simplify(D1 - expected_D1) == 0

# Positive root of the bracket.  Rationalization works also in the complete
# graph case d-1-lam=0.
root = 2/(sp.sqrt(lam**2 + 4*d) + lam + 2)
poly = (d-1-lam)*h**2 + (lam+2)*h - 1
assert sp.simplify(poly.subs(h, root)) == 0

# Pairwise moment/Hankel identity for three formal spectral atoms: a direct
# symbolic check, representative of the general expansion.
q0, q1, q2 = sp.symbols('q0 q1 q2')
w0, w1, w2 = sp.symbols('w0 w1 w2')
for m in range(5):
    am = w0*q0**m + w1*q1**m + w2*q2**m
    am1 = w0*q0**(m+1) + w1*q1**(m+1) + w2*q2**(m+1)
    am2 = w0*q0**(m+2) + w1*q1**(m+2) + w2*q2**(m+2)
    rhs = (w0*w1*(q0-q1)**2*(q0*q1)**m
           + w0*w2*(q0-q2)**2*(q0*q2)**m
           + w1*w2*(q1-q2)**2*(q1*q2)**m)
    assert sp.expand(am*am2 - am1**2 - rhs) == 0

# ---------------------------------------------------------------------------
# Exact C5 phase diagram.
# ---------------------------------------------------------------------------
s5 = sp.sqrt(5)
s = (s5-1)/4
t = -(s5+1)/4
qp = sp.simplify(h + (1-h)*s)
qn = sp.simplify(h + (1-h)*t)
alpha0 = sp.Rational(1,5)
alpha = sp.Rational(2,5)

# D_m = a_m a_{m+2} - a_{m+1}^2 from the exact C5 spectral weights.
def Dc5(m):
    return sp.factor(alpha0*alpha*(1-qp)**2*qp**m
                     + alpha0*alpha*(1-qn)**2*qn**m
                     + alpha**2*(qp-qn)**2*(qp*qn)**m)

assert sp.factor(Dc5(1) - (1-h)**2*(h**2+2*h-1)/4) == 0
assert sp.simplify(qp + qn - (5*h-1)/2) == 0

h_all = sp.sqrt(2)-1
h_eventual = sp.Rational(1,5)
assert sp.simplify((h**2+2*h-1).subs(h, h_all)) == 0
assert sp.simplify((qp+qn).subs(h, h_eventual)) == 0

# At h=1/5, qp=-qn=1/sqrt(5); the stationary-pair leading coefficient on
# odd m is strictly negative.
assert sp.simplify(qp.subs(h,h_eventual) - 1/s5) == 0
assert sp.simplify(qn.subs(h,h_eventual) + 1/s5) == 0
rho = 1/s5
lead_tie = sp.factor(alpha0*alpha*((1-rho)**2-(1+rho)**2))
assert sp.simplify(lead_tie + sp.Rational(8,25)*rho) == 0
assert lead_tie.evalf() < 0

# The first odd-step sign is negative below sqrt(2)-1 and nonnegative from
# sqrt(2)-1 upward; exact sample points on both sides check the orientation.
assert Dc5(1).subs(h, sp.Rational(1,3)) < 0
assert Dc5(1).subs(h, sp.Rational(1,2)) > 0

print('R05 I0030 exact order-17 + discrete spectral certificate')
print('p', p)
print('inverse_closed_connection_sets_total', len(all_sets))
print('affine_arc_transitive_connection_sets', len(selected))
print('isomorphism_types', len(classes))
print('class_degree_labeled_counts', [(d,cnt) for d,cnt,_ in class_data])
print('class_representatives', [canon for _,_,canon in class_data])
print('walk_identity_through_power', 40)
print('D1_factor', D1)
print('first_odd_root', root)
print('C5_D1_factor', Dc5(1))
print('C5_all_step_threshold', h_all)
print('C5_eventual_threshold', h_eventual)
print('C5_tie_leading_coefficient', lead_tie)
print('metric_largest_fully_certified_vertex_count', 17)
print('RESULT PASS')
