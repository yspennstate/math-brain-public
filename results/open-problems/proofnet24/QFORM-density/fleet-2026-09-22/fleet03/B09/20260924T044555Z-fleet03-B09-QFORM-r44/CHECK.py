import math
import random
import numpy as np

A_scalar = 2*math.sqrt(2)
B_star = 2**(5/4)*(math.sqrt(3)+1)
C_comb = math.sqrt(A_scalar*A_scalar + B_star*B_star)
C_pair = 4*math.sqrt(2*C_comb)
C_star_pair = 2**(25/8)*math.sqrt(math.sqrt(3)+1)

print('A_scalar', A_scalar)
print('B_star', B_star)
print('C_comb', C_comb)
print('C_pair', C_pair)
print('C_star_pair', C_star_pair)

# Check the deterministic near/far interval geometry used in Lemma 3.1.
random.seed(4409)
max_near_ratio = 0.0
max_far_ratio = 0.0
for _ in range(200000):
    delta = 10**random.uniform(-8, 3)
    K = min(1.0, 10**random.uniform(-8, 0))
    L = math.sqrt(delta/K)

    r = random.uniform(-delta, L*L + delta)
    if r + delta >= 0:
        radius = math.sqrt(r + delta)
        max_near_ratio = max(max_near_ratio, radius/(math.sqrt(3)*L))

    r2 = L*L + delta + 10**random.uniform(-8, 4)*L*L
    length = 2*(math.sqrt(r2 + delta) - math.sqrt(r2 - delta))
    max_far_ratio = max(max_far_ratio, length/(2*delta/L))

print('max_near_ratio', max_near_ratio)
print('max_far_ratio', max_far_ratio)
assert max_near_ratio <= 1 + 1e-12
assert max_far_ratio <= 1 + 1e-8

# Target-valid nonzero-Schur regression.  The scalar Schur coefficient passes
# continuously through zero while the whole physical Schur star is fixed.
C = np.array([[1.,0.],[0.,1.],[-1.,-1.]])
for eps in [0.0, 1e-8, 1e-4, 0.1, 1.0]:
    P = np.array([[0.,1.,0.],[1.,0.,1.],[0.,1.,eps]])
    B = P[:2,:2]
    p = P[:2,2]
    d = P[2,2]
    CH = C[:2,:]
    c = C[2,:]
    Binv = np.linalg.inv(B)
    s = d - p @ Binv @ p
    m = c - p @ Binv @ CH
    A = np.block([[P,C],[C.T,np.zeros((2,2))]])
    eig = np.linalg.eigvalsh(A)
    large = int(np.sum(np.abs(eig) >= 1-1e-12))
    print('eps', eps, 's', s, 'm', m.tolist(), 'normm', np.linalg.norm(m), 'large', large, 'spectrum', eig.tolist())
    assert abs(s-eps) < 1e-12
    assert np.linalg.norm(m - np.array([-2.,-1.])) < 1e-12
    assert large >= 3

print('star_only_regression_bound', C_star_pair*(math.sqrt(5))**(-1/4))
print('combined_regression_bound_eps_0p1', C_pair*(0.1+math.sqrt(5))**(-1/4))

# Designated fleet04/B09 theorem on K=I_3.
partner_bound = 3.0
print('partner_I3_bound', partner_bound)
assert abs(partner_bound - 3.0) < 1e-15
