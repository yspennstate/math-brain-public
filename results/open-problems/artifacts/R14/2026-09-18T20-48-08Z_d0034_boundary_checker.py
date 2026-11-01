from fractions import Fraction
import math
import sympy as sp

# Exact center-conditioned side-color matrix for the HL 1-dependent 4-coloring.
Q = sp.Matrix([
    [sp.Rational(1,12) if i == j else sp.Rational(1,8) for j in range(3)]
    for i in range(3)
])
detQ = sp.factor(Q.det())
K = 3 * Q
assert detQ == sp.Rational(1,1728)
assert all(sp.simplify(sum(K[i,j] for j in range(3)) - 1) == 0 for i in range(3))

v1 = sp.Matrix([1,-1,0])
v2 = sp.Matrix([1,1,-2])
assert K * v1 == -sp.Rational(1,8) * v1
assert K * v2 == -sp.Rational(1,8) * v2

# Explicit 3-component nonnegative product factorization of Q:
# Q[a,b] = (1/3) sum_h 1_{a=h} K[h,b].
for a in range(3):
    for b in range(3):
        rhs = sum(sp.Rational(1,3) * (1 if a == h else 0) * K[h,b] for h in range(3))
        assert sp.simplify(Q[a,b] - rhs) == 0

# Repeated one-site excursion probabilities under the Palm law at color 0.
# r repetitions of the excursion word (1) give an alternating word of length 2r+1;
# P(alternating proper word of length n) = 1 / [2 (n+1)!].
p = {r: sp.Rational(2, math.factorial(2*r + 2)) for r in (1,2,3)}
assert p[1] == sp.Rational(1,12)
assert p[2] == sp.Rational(1,360)
assert p[3] == sp.Rational(1,20160)
assert p[3] * p[1] != p[2] ** 2

# HHL k=1 tuning and bubble-endpoint density.
t = sp.symbols('t', positive=True)
q = (1+t)**2 / t
s = sp.simplify(t * (q - 2) / (q - 1 - t))
delta = sp.factor(1 - s)
assert sp.simplify(s - t * (t**2 + 1) / (t + 1)) == 0
assert sp.simplify(delta - (1 - t**3) / (1 + t)) == 0
assert sp.simplify((q - 4) - (1 - t)**2 / t) == 0
assert sp.simplify(delta.subs(t,1)) == 0

print('Q_det =', detQ)
print('K_nontrivial_eigenvalue = -1/8 (multiplicity 2 verified on basis)')
print('Q_nonnegative_rank = 3 (rank lower bound + explicit 3-component factorization)')
print('Palm repeated-one-site excursion: p1 =', p[1], 'p2 =', p[2], 'p3 =', p[3])
print('Markov_identity_lhs = p3*p1 =', p[3] * p[1])
print('Markov_identity_rhs = p2^2 =', p[2] ** 2)
print('MARKOV_ORDER1_TEST_FAILS =', p[3] * p[1] != p[2] ** 2)
print('HHL k=1: q(t) =', sp.factor(q))
print('HHL bubble nonendpoint probability s(t) =', sp.factor(s))
print('HHL bubble endpoint density delta(t) =', delta)
print('q(t)-4 =', sp.factor(q - 4))
print('delta(1) =', delta.subs(t,1))
print('ALL_EXACT_CHECKS_PASS')
