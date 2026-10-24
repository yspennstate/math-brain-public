import math
import numpy as np

eta = 0.17
B = 99.0
pair_def = math.pi / eta
pair_indef = (9.2 + math.log(10000 * eta)) / eta
scalar_lift = 2 * math.sqrt(B / eta)
mu = 1/20
tau = 1/256
Lmu = 0.5 - mu - math.sqrt(2*mu)
ridge = 9 * math.sqrt(3*math.e) / (2 * (Lmu - tau))

assert pair_def < B
assert pair_indef < B
assert scalar_lift < B
assert ridge < B

rng = np.random.default_rng(20260923)
max_rel_err = 0.0
checked = 0
for _ in range(10000):
    M = rng.normal(size=(5,5))
    A = (M + M.T)/2
    i, j = rng.choice(5, size=2, replace=False)
    a = A[i,i]
    if abs(a) < 1e-10:
        continue
    s_jj = A[j,j] - A[j,i]**2/a
    lhs = np.linalg.det(A[np.ix_([i,j],[i,j])])
    rhs = a*s_jj
    max_rel_err = max(max_rel_err, abs(lhs-rhs)/(1+abs(lhs)))
    checked += 1

assert max_rel_err < 1e-11
print({
    'eta': eta,
    'pair_definite_constant': pair_def,
    'pair_indefinite_constant': pair_indef,
    'scalar_lift_constant': scalar_lift,
    'ridge_terminal_constant': ridge,
    'random_identity_checks': checked,
    'max_relative_error': max_rel_err,
    'status': 'PASS'
})
