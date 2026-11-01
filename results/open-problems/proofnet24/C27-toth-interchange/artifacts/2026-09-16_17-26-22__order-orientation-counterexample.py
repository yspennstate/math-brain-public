from itertools import permutations
import sympy as sp

# Exact continuous-time interchange on the path 0--1--2 at t=log(2).
# A state p is represented by p[i] = current position of initial label i.
states = list(permutations(range(3)))
idx = {p: i for i, p in enumerate(states)}
Q = sp.zeros(6)
edges = [(0, 1), (1, 2)]
for i, p in enumerate(states):
    for a, b in edges:
        q = tuple(b if x == a else a if x == b else x for x in p)
        Q[i, idx[q]] += 1
    Q[i, i] -= len(edges)

x = sp.symbols('x')
cp = sp.factor(Q.charpoly(x).as_expr())
expected_cp = x * (x + 1)**2 * (x + 3)**2 * (x + 4)
assert sp.expand(cp - expected_cp) == 0
assert Q == Q.T  # therefore diagonalizable over R

# On the spectrum {0,-1,-3,-4}, lambda -> 2^lambda is represented by
# (3 lambda^3 + 32 lambda^2 + 125 lambda + 192)/192.
I = sp.eye(6)
P = (3 * Q**3 + 32 * Q**2 + 125 * Q + 192 * I) / 192
assert all(v >= 0 for v in P)
for i in range(6):
    assert sp.simplify(sum(P[i, j] for j in range(6)) - 1) == 0

id_idx = idx[(0, 1, 2)]
row = [sp.Rational(P[id_idx, j]) for j in range(6)]
expected = {
    (0, 1, 2): sp.Rational(37, 96),
    (0, 2, 1): sp.Rational(7, 32),
    (1, 0, 2): sp.Rational(7, 32),
    (1, 2, 0): sp.Rational(7, 96),
    (2, 0, 1): sp.Rational(7, 96),
    (2, 1, 0): sp.Rational(1, 32),
}
for p, w in zip(states, row):
    assert w == expected[p]

# Total order 1 < 0 < 2.  The nontrivial upward-arrow indicators are
# A={label 0 ends at 2}; B={label 1 ends at 0 or 2}.
def prob(pred):
    return sp.simplify(sum(w for p, w in zip(states, row) if pred(p)))

pA = prob(lambda p: p[0] == 2)
pB = prob(lambda p: p[1] in (0, 2))
pAB = prob(lambda p: p[0] == 2 and p[1] in (0, 2))
cov = sp.factor(pAB - pA * pB)
assert pA == sp.Rational(5, 48)
assert pB == sp.Rational(7, 12)
assert pAB == sp.Rational(7, 96)
assert cov == sp.Rational(7, 576) and cov > 0

# At z=2 the product-mgf inequality fails by exactly the covariance.
mgf_joint = sp.simplify(1 + pA + pB + pAB)
mgf_product = sp.simplify((1 + pA) * (1 + pB))
assert sp.factor(mgf_joint - mgf_product) == sp.Rational(7, 576)

print('C27 ORDER-ORIENTATION COUNTEREXAMPLE')
print('charpoly(Q)=', cp)
print('transition row at t=log(2):')
for p, w in zip(states, row):
    print(p, w)
print('order: 1 < 0 < 2')
print('P(A)=', pA)
print('P(B)=', pB)
print('P(A and B)=', pAB)
print('covariance=', cov)
print('E[2^(IA+IB)] - E[2^IA]E[2^IB]=', mgf_joint - mgf_product)
print('PAIRWISE_NEGATIVE_ASSOCIATION_FAILS_EXACTLY')
print('ALL_EXACT_CHECKS_PASS')
