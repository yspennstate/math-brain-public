"""Exact checks for X005's integrated hyperbolic-barrier theorem.

Run with Python + SymPy. Numerical log evaluations only illustrate identities;
all normalization, positivity, and the stated rational bound are checked exactly.
"""
from itertools import combinations
import json
from pathlib import Path

import sympy as s


def subsets(n):
    return [t for k in range(n + 1) for t in combinations(range(n), k)]


def tr2(m):
    return s.simplify(s.trace(m * m))


def real(x):
    x = s.simplify(s.expand_complex(x))
    assert s.im(x) == 0
    return s.re(x)


def fmt(x):
    return str(s.factor(x))


n = 4
I = s.eye(n)
R = s.Matrix([
    [1, s.Rational(1, 3), s.I / 4, 0],
    [s.Rational(1, 3), 1, s.Rational(1, 5), s.I / 6],
    [-s.I / 4, s.Rational(1, 5), 1, s.Rational(1, 7)],
    [0, -s.I / 6, s.Rational(1, 7), 1],
])
scale = s.diag(s.Rational(1, 5), 2, 5, s.Rational(1, 3))
L = scale * R * scale
W = (I + L).inv()
K = I - W
u = s.Matrix([1, s.I, 2, -1])
A = I + u * u.conjugate().T
B = W.inv() * A * W.inv()
r = n

# R is Hermitian and strictly diagonally dominant, hence positive definite.
assert R == R.conjugate().T
row_sums = [sum(s.Abs(R[i, j]) for j in range(n) if i != j) for i in range(n)]
assert all(t < 1 for t in row_sums)
det_R = s.factor(R.det())
assert det_R > 0
assert A.det() > 0
assert K * A != A * K

data = []
for S in subsets(n):
    present = set(S)
    absent = [i for i in range(n) if i not in present]
    Q = K - s.diag(*[int(i in absent) for i in range(n)])
    Qi = Q.inv()
    atom = s.simplify((-1) ** len(absent) * Q.det())
    score = real(s.trace(Qi * A))
    energy = real(tr2(Qi * A))
    variance = s.simplify(energy - score * score / r)
    assert atom > 0 and energy >= 0 and variance >= 0

    RS = s.zeros(n)
    if S:
        inv = L.extract(S, S).inv()
        for a, i in enumerate(S):
            for b, j in enumerate(S):
                RS[i, j] = inv[a, b]
    assert s.simplify(s.trace((RS - W) * B) - score) == 0
    assert s.simplify(tr2((RS - W) * B) - energy) == 0
    det_RS = s.factor(R.extract(S, S).det()) if S else s.Integer(1)
    assert det_R <= det_RS <= 1
    data.append(dict(S=S, p=atom, score=score, q=energy, v=variance,
                     h=s.simplify(atom * (score * score - energy)),
                     det_correlation=det_RS))

FI = s.factor(sum(z['p'] * z['score'] ** 2 for z in data))
assert FI > 0
assert sum(z['p'] for z in data) == 1
assert s.simplify(sum(z['p'] * z['score'] for z in data)) == 0
assert s.simplify(sum(z['p'] * z['q'] for z in data) - FI) == 0
assert s.simplify(sum(z['p'] * z['v'] for z in data) - (1 - s.Rational(1, r)) * FI) == 0
assert s.simplify(sum(z['h'] for z in data)) == 0
for i in range(n):
    assert s.simplify(sum(z['h'] for z in data if i in z['S'])) == 0

nu_score = [s.factor(z['p'] * z['score'] ** 2 / FI) for z in data]
nu_variance = [s.factor(z['p'] * z['v'] / ((1 - s.Rational(1, r)) * FI)) for z in data]
assert s.simplify(sum(nu_score)) == 1
assert s.simplify(sum(nu_variance)) == 1
for i in range(n):
    assert s.simplify(sum(a - b for a, b, z in zip(nu_score, nu_variance, data)
                          if i in z['S'])) == 0

# Field-free surprise f(S)=-log det R_S can replace -log p_S because
# their difference is modular and both energy laws have identical marginals.
Qentropy = FI + sum(z['h'] * s.log(z['p']) for z in data)
transport = FI * (1 + (1 - s.Rational(1, r)) * sum(
    (v - a) * -s.log(z['det_correlation'])
    for a, v, z in zip(nu_score, nu_variance, data)))
assert abs(float((Qentropy - transport).evalf(50))) < 1e-40

# Entirely rational sufficient coefficient: -log det R < 1/det R - 1.
correlation_upper = s.factor(1 / det_R - 1)
coercivity = s.factor(1 - (1 - s.Rational(1, r)) * correlation_upper)
assert coercivity > 0
lower_bound = s.factor(coercivity * FI)
assert float((Qentropy - lower_bound).evalf(50)) > 0

# Independent exact likelihood-jet reconstruction in the unnormalized
# product-Walsh basis. This also verifies the integrated general-direction
# identity without square roots in the arithmetic.
d = [K[i, i] for i in range(n)]
E = K - s.diag(*d)
t = s.Symbol('t', real=True)
minor_jets = {}
for T in subsets(n):
    polynomial = (E + t * A).extract(T, T).det() if T else s.Integer(1)
    minor_jets[T] = [s.expand(polynomial).coeff(t, j) * s.factorial(j) for j in range(3)]
for z in data:
    S = set(z['S'])
    mu = s.prod(d[i] if i in S else 1 - d[i] for i in range(n))
    phi = [(int(i in S) - d[i]) / (d[i] * (1 - d[i])) for i in range(n)]
    reconstructed = [sum(minor_jets[T][j] * s.prod(phi[i] for i in T)
                         for T in subsets(n)) for j in range(3)]
    assert s.simplify(mu * reconstructed[0] - z['p']) == 0
    assert s.simplify(mu * reconstructed[1] - z['p'] * z['score']) == 0
    assert s.simplify(mu * reconstructed[2] - z['h']) == 0

pmin = min(z['p'] for z in data)
pmax = max(z['p'] for z in data)
out = {
    'status': 'all exact algebraic assertions passed',
    'n': n, 'rank_A': r,
    'R': [[fmt(R[i, j]) for j in range(n)] for i in range(n)],
    'scale': [fmt(scale[i, i]) for i in range(n)],
    'row_abs_sums': list(map(fmt, row_sums)),
    'det_R': fmt(det_R),
    'rational_correlation_upper': fmt(correlation_upper),
    'rational_coercivity': fmt(coercivity),
    'FI_exact': fmt(FI),
    'rational_lower_bound_exact': fmt(lower_bound),
    'FI_numeric': str(FI.evalf(30)),
    'negative_entropy_curvature_numeric': str(Qentropy.evalf(30)),
    'rational_lower_bound_numeric': str(lower_bound.evalf(30)),
    'gaussian_correlation_numeric': str((-s.log(det_R)).evalf(30)),
    'raw_log_atom_spread_numeric': str(s.log(pmax / pmin).evalf(30)),
    'atoms': [{k: (list(v) if k == 'S' else fmt(v)) for k, v in z.items()} for z in data],
}
path = Path(__file__).with_name('results.json')
path.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps({k: v for k, v in out.items() if k not in ['atoms', 'FI_exact', 'rational_lower_bound_exact']}, indent=2))
