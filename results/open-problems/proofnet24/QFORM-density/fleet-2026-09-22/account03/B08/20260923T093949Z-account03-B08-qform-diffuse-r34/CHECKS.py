import itertools
import math
import numpy as np

C_E2 = 12 * 2**(5/6) * math.exp(5/24)
C_L2 = 2**(1/3) * math.sqrt(6) * math.exp(5/24)
HALF = C_E2 * 135000**(1/8)
L2 = C_L2 * 135000**(1/8)
SMALL = math.sqrt(2) * L2
PARTNER = (2**(4/3) + 1) * math.sqrt(3) * 2**(1/4)

assert HALF < 116
assert L2 < 16.65
assert SMALL < 23.535
assert PARTNER < 7.251

def E2(B):
    total = 0.0
    for rr in itertools.combinations(range(B.shape[0]), 2):
        for cc in itertools.combinations(range(B.shape[1]), 2):
            total += np.linalg.det(B[np.ix_(rr, cc)])**2
    return total

rng = np.random.default_rng(20260923)
min_gap_a = float('inf')
min_gap_b = float('inf')
for _ in range(1000):
    B = rng.normal(size=(6, 7))
    a, b = B[0, 0], B[0, 1]
    c, d = B[1, 0], B[1, 1]
    delta = a*d - b*c
    W = np.array([[a*B[r,j] - B[r,0]*B[0,j]
                   for j in range(2, B.shape[1])]
                  for r in range(2, B.shape[0])])
    U = np.array([a*B[1,j] - c*B[0,j]
                  for j in range(2, B.shape[1])])
    V = np.array([a*B[r,1] - b*B[r,0]
                  for r in range(2, B.shape[0])])
    e2 = E2(B)
    gap_a = e2 - (delta**2 + np.sum(W**2))
    gap_b = e2 - (np.sum(U**2) + np.sum(V**2))
    min_gap_a = min(min_gap_a, gap_a)
    min_gap_b = min(min_gap_b, gap_b)
    assert gap_a > -1e-9
    assert gap_b > -1e-9

print(f'C_E2={C_E2:.15f}')
print(f'C_L2={C_L2:.15f}')
print(f'half_riesz_r34={HALF:.15f}')
print(f'L2_r34={L2:.15f}')
print(f'centered_small_ball={SMALL:.15f}')
print(f'partner_direct_sum={PARTNER:.15f}')
print(f'min_E2_gap_A={min_gap_a:.12g}')
print(f'min_E2_gap_B={min_gap_b:.12g}')
print('QFORM_B08_R34_CHECK_PASS')
