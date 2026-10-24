import itertools
import sympy as sp


def make_A(m):
    J = sp.ones(m, m) / sp.Integer(m)
    return sp.diag(sp.Matrix([[1]]), J, -J)


def schur(A, p):
    idx = [i for i in range(A.rows) if i != p]
    d = A[p, p]
    S = A.extract(idx, idx) - A.extract(idx, [p]) * A.extract([p], idx) / d
    return S, idx


def best_disjoint_2det(S):
    n = S.rows
    best = sp.Rational(0)
    for I in itertools.combinations(range(n), 2):
        remaining = [j for j in range(n) if j not in I]
        for J in itertools.combinations(remaining, 2):
            best = max(best, abs(S.extract(I, J).det()))
    return sp.simplify(best)


alpha = sp.symbols('alpha', positive=True)
f = alpha / ((1-alpha)*(2*alpha-1))
critical = sp.solve(sp.diff(f, alpha), alpha)
assert critical == [sp.sqrt(2)/2]
a0 = critical[0]
assert sp.simplify(f.subs(alpha, a0) - (1+sp.sqrt(2))**2) == 0
print('alpha_opt=', a0)
print('square_factor=', sp.simplify(f.subs(alpha, a0)))
print('density_constant=4(1+sqrt(2))')

A = sp.Matrix([
    [3,1,2,1,0,2],
    [1,4,0,2,1,0],
    [2,0,5,1,2,1],
    [1,2,1,6,0,1],
    [0,1,2,0,7,2],
    [2,0,1,1,2,8],
])
p = 0
I = [1,2]
J = [3,4]
S, idx = schur(A, p)
pos = {orig:k for k, orig in enumerate(idx)}
lhs = A.extract([p]+I, [p]+J).det()
rhs = A[p,p] * S.extract([pos[x] for x in I], [pos[x] for x in J]).det()
assert sp.simplify(lhs-rhs) == 0
print('mixed_minor_identity_sample=', lhs, rhs)

for m in range(2, 9):
    A = make_A(m)
    ev = A.eigenvals()
    assert ev.get(sp.Integer(1), 0) == 2
    assert ev.get(sp.Integer(-1), 0) == 1
    assert ev.get(sp.Integer(0), 0) == 2*m-2
    row = []
    for p in range(A.rows):
        if A[p,p] == 0:
            continue
        S, _ = schur(A, p)
        best = best_disjoint_2det(S)
        if p == 0:
            assert best == sp.Rational(1, m*m)
        else:
            assert best == 0
        row.append((p, str(A[p,p]), str(best)))
    print('m=', m, 'spectrum={1:2,-1:1,0:%d}' % (2*m-2), 'pivot_best=', row)

print('STATUS=PASS')
