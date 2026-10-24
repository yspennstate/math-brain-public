import math
import numpy as np

alpha = 5.0/9.0
K_alpha = 2*math.sqrt(2)*(2*alpha+1)/(2*alpha)*2**((alpha-0.5)/(2*alpha+1))
H_const = 7*2**(5.0/9.0)
C_pair = K_alpha * H_const**(9.0/19.0)
C_tail = C_pair * 2**(5.0/76.0)
C_partner = (2**(4.0/3.0)+1)*math.sqrt(3)*2**(1.0/4.0)

print('K_alpha', K_alpha)
print('H_const', H_const)
print('C_pair', C_pair)
print('C_tail', C_tail)
print('C_partner', C_partner)
assert C_pair < 16.511
assert C_tail < 17.281
assert C_partner < 7.251

def dist_rank(M, k):
    s = np.linalg.svd(M, compute_uv=False)
    return math.sqrt(float(np.sum(s[k:]**2))) if len(s) > k else 0.0

def e2(M):
    s = np.linalg.svd(M, compute_uv=False)
    x = s*s
    return float(sum(x[i]*x[j] for i in range(len(x)) for j in range(i+1, len(x))))

rng = np.random.default_rng(20260923)
max_leak_violation = 0.0
max_e2_violation = 0.0
for _ in range(5000):
    m, n = rng.integers(4, 10, size=2)
    D = rng.normal(size=(m,n))
    U = rng.normal(size=(m,2))
    V = rng.normal(size=(n,2))
    K = U @ V.T
    M = D-K
    d3 = dist_rank(D, 3)
    d1 = dist_rank(M, 1)
    max_leak_violation = max(max_leak_violation, d3-d1)
    max_e2_violation = max(max_e2_violation, 0.5*d1**4-e2(M))

print('max_leak_violation', max_leak_violation)
print('max_e2_violation', max_e2_violation)
assert max_leak_violation < 1e-9
assert max_e2_violation < 1e-8
print('QFORM_B08_R36_CHECK_PASS')
