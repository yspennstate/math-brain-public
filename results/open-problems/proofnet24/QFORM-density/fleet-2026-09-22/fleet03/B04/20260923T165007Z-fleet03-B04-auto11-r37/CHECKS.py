from fractions import Fraction
from math import sqrt

L = 64
eps = Fraction(1, 64)

# Squared 2-row Gram determinants for C_(L,eps).
D = {
    (1,2): Fraction(L*L),
    (1,3): Fraction(L*L),
    (1,4): Fraction(L*L),
    (1,5): Fraction(L*L) * eps * eps,
    (2,3): Fraction(1),
    (2,4): Fraction(1),
    (2,5): eps * eps,
    (3,4): Fraction(4),
    (3,5): Fraction(2) * eps * eps,
    (4,5): Fraction(2) * eps * eps,
}
Z2 = sum(D.values(), Fraction(0))
num1 = sum(v for S, v in D.items() if 1 in S)
alpha1 = num1 / Z2

# Noncanonical law w_12=w_34=1/2.
alpha = {1: Fraction(1,2), 2: Fraction(1,2), 3: Fraction(1,2), 4: Fraction(1,2), 5: Fraction(0)}
Gamma = Fraction(8*L)

# B^T B is diagonal with entries below.
BtB_diag = [Fraction(1), Fraction(L*L+2), Fraction(3), eps*eps]
large_abs_eigs = [1.0, sqrt(L*L+2), sqrt(3)]

bound = 1.5 * 2**(2/3)

assert D[(1,2)] == 4096
assert D[(3,4)] == 4
assert Z2 == Fraction(50360325, 4096)
assert num1 == 12289
assert alpha1 > Fraction(1,2)
assert Gamma == 512
assert all(a <= Fraction(1,2) for a in alpha.values())
assert BtB_diag == [Fraction(1), Fraction(4098), Fraction(3), Fraction(1,4096)]
assert abs(bound - 2.381101577952299) < 1e-14

print({
    'Z2': str(Z2),
    'alpha1_canonical': float(alpha1),
    'Gamma_reweighted': str(Gamma),
    'BtB_diag': [str(x) for x in BtB_diag],
    'density_bound': bound,
    'six_large_eigenvalue_magnitudes': large_abs_eigs,
})
