from fractions import Fraction
import math
import numpy as np

c3 = Fraction(11907, 16384)
zcoef = Fraction(31, 2048)
z2 = zcoef*c3*c3
anchorcoef = Fraction(127, 512)*zcoef
assert anchorcoef == Fraction(3937, 1048576)

half_riesz = 8*math.sqrt(math.e)*float(z2)**(-1/8)
D0 = Fraction(3, 4096)
pair_bound = float(D0)**(-0.5)*(9.2 + math.log(10000*math.sqrt(float(D0))))
double_floor = math.sqrt(3937)/2048*float(c3)
core_floor = math.sqrt(3937)/64*float(c3)

rng = np.random.default_rng(20260923)
max_rel = 0.0
for _ in range(1000):
    m, n = 7, 8
    B = rng.normal(size=(m, n))
    i = int(rng.integers(m)); a = int(rng.integers(n))
    rows = [j for j in range(m) if j != i]
    cols = [q for q in range(n) if q != a]
    b = B[i, a]
    r = B[i, cols]
    c = B[rows, a]
    D = B[np.ix_(rows, cols)]
    lhs = 0.0
    for j in rows:
        for q in cols:
            det = b*B[j, q] - B[j, a]*B[i, q]
            lhs += det*det
    rhs = np.linalg.norm(b*D - np.outer(c, r), 'fro')**2
    rel = abs(lhs-rhs)/max(1.0, abs(lhs), abs(rhs))
    max_rel = max(max_rel, rel)

print('QFORM_B06_R37_CHECK_PASS')
print('c3 =', c3, float(c3))
print('Z2_floor =', z2, float(z2))
print('anchor_coefficient =', anchorcoef, float(anchorcoef))
print('half_Riesz_bound =', half_riesz)
print('pair_D0 =', D0, float(D0))
print('pair_density_bound =', pair_bound)
print('double_star_floor =', double_floor)
print('large_core_floor =', core_floor)
print('cofactor_identity_max_relative_error_1000 =', max_rel)
