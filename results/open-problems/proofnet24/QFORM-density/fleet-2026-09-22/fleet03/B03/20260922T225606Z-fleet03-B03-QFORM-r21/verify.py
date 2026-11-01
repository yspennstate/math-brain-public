import itertools
import math
import numpy as np
import mpmath as mp

mp.mp.dps = 50

def beta(a, b):
    return mp.beta(mp.mpf(a), mp.mpf(b))

# Exact constants from the report.
k = 3
C3 = mp.sqrt(mp.e)/(2*k) * beta(mp.mpf(1)/(4*k), mp.mpf(k-2)/(8*k))
L2sq3 = mp.e/(4*k) * beta(mp.mpf(1)/(2*k), mp.mpf(k-2)/(4*k))
collision3 = 2 * L2sq3
assert abs(C3 - mp.mpf('9.8406558649220185')) < mp.mpf('1e-15')
assert abs(L2sq3 - mp.mpf('3.9992289169513335')) < mp.mpf('1e-15')
assert abs(collision3 - mp.mpf('7.998457833902667')) < mp.mpf('2e-15')

# k=2 is the logarithmic endpoint: second beta parameter vanishes.
assert mp.mpf(1)/8 - mp.mpf(1)/(4*2) == 0
assert mp.mpf(1)/4 - mp.mpf(1)/(2*2) == 0

# Cauchy-Binet check for E_k(B)=sum_{I,J} det(B[I,J])^2=e_k(BB^T).
def ek_from_eigs(B, k):
    vals = np.linalg.eigvalsh(B @ B.T)
    ans = 0.0
    for inds in itertools.combinations(range(len(vals)), k):
        prod = 1.0
        for i in inds:
            prod *= vals[i]
        ans += prod
    return ans

def ek_from_minors(B, k):
    m, n = B.shape
    ans = 0.0
    for I in itertools.combinations(range(m), k):
        for J in itertools.combinations(range(n), k):
            M = B[np.ix_(I, J)]
            ans += float(np.linalg.det(M))**2
    return ans

B = np.array([
    [1.0, 2.0, -1.0, 3.0],
    [0.5, -2.0, 4.0, 1.0],
    [3.0, 1.0, 2.0, -1.0],
    [-2.0, 0.25, 1.5, 2.0],
])
for kk in (3, 4):
    lhs = ek_from_eigs(B, kk)
    rhs = ek_from_minors(B, kk)
    assert math.isclose(lhs, rhs, rel_tol=2e-12, abs_tol=2e-12), (kk, lhs, rhs)

# Homogeneity: d -> rho*d, E_k -> rho^(2k) E_k gives density factor |rho|^-1.
for rho in (0.2, 3.0, 11.0):
    factor = rho**(-0.5) * (rho**(2*k))**(-1/(4*k))
    assert math.isclose(factor, rho**(-1), rel_tol=1e-14, abs_tol=1e-14)

print(f'C3={float(C3):.16f}')
print(f'L2sq3={float(L2sq3):.16f}')
print(f'collision3={float(collision3):.16f}')
print('k2_endpoint=diverges')
print('cauchy_binet=PASS')
print('homogeneity=PASS')
print('QFORM_B03_R21_CHECK_PASS')
