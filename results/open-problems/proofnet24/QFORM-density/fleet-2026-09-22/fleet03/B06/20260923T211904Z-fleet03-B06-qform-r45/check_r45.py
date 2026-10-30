from fractions import Fraction
import math
import numpy as np

TAU = Fraction(109, 200)
M = Fraction(11, 20)
upper = TAU**3 + 2*M**3 + 3*TAU*M**2
assert upper == Fraction(7913729, 8000000)
assert upper < 1

# Case-A constant: compare fourth powers exactly.
case_a_4 = Fraction(16**4 * 30**2 * 200, 109)
assert case_a_4 < 102**4
case_a = 16*math.sqrt(30)*(200/109)**0.25
assert case_a < 102

# Case-B pair-log constant from kappa > 1/200.
case_b = 8*2**0.25*200**0.25
assert case_b < 36

# Designated-partner anchored-diagonal payment.
partner_diag = 102*256**(1/3)
assert partner_diag < 647.660
wmax = (61/1728)**(1/3)
assert wmax > 0.328
assert 0.25*wmax > 0.082

# Finite sanity check only: normalize random symmetric matrices to |det|=1.
rng = np.random.default_rng(20260923)
bad = 0
case_b_count = 0
min_kappa = float('inf')
for _ in range(200000):
    A = rng.normal(size=(3,3))
    A = (A + A.T)/2
    det = np.linalg.det(A)
    if abs(det) < 1e-8:
        continue
    A = A / abs(det)**(1/3)
    if np.max(np.abs(np.diag(A))) < float(TAU):
        case_b_count += 1
        pairs = [(0,1),(0,2),(1,2)]
        i,j = max(pairs, key=lambda ij: abs(A[ij]))
        if abs(A[i,j]) <= float(M):
            bad += 1
        B = A[np.ix_([i,j],[i,j])]
        kappa = np.min(np.abs(np.linalg.eigvalsh(B)))
        min_kappa = min(min_kappa, kappa)
        if not kappa > 1/200 - 1e-10:
            bad += 1

assert bad == 0
print('QFORM_B06_R45_CHECK_PASS')
print('determinant_upper', float(upper))
print('case_A_constant', case_a)
print('case_B_constant', case_b)
print('partner_diagonal_constant', partner_diag)
print('case_B_random_count', case_b_count)
print('minimum_observed_kappa', min_kappa)
