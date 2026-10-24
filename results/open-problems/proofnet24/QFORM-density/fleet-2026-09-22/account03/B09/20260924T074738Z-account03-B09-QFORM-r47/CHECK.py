import math
import numpy as np

rng=np.random.default_rng(20260924)

# 1. Endpoint rearrangement inequality used in the arcsine-maximal lemma.
m=np.linspace(1e-12,1.0,200001)
lhs=2*np.arccos(1-m)
rhs=math.pi*np.sqrt(m)
assert np.all(lhs <= rhs + 2e-14)
arc_ratio=float(np.max(lhs/np.sqrt(m)))

# 2. Polynomial-star algebra on seeded definite and negative-definite pairs.
max_alg=0.0
min_sign_delta=1e100
for k in range(2000):
    R=rng.normal(size=(2,2))
    eps=10**rng.uniform(-10,1)
    B=R.T@R+eps*np.eye(2)
    if k%2:
        B=-B
    a=float(B[0,0]); c=float(B[0,1])
    u=rng.normal(size=9); v=rng.normal(size=9)
    g=v-(c/a)*u
    H=a*v-c*u
    max_alg=max(max_alg,float(np.linalg.norm(H-a*g)/(1+np.linalg.norm(H))))
    delta=float(np.linalg.det(B)/a)
    min_sign_delta=min(min_sign_delta,math.copysign(1.0,a)*delta)
assert max_alg < 1e-12
assert min_sign_delta > 0

# 3. Target-valid punctured near-singular regression.
d=1/128
A=np.array([[1,0,0,0],
            [0,d,1,0],
            [0,1,1/d,0],
            [0,0,0,1]],dtype=float)
eigs=np.linalg.eigvalsh(A)
assert sum(abs(x)>=1-1e-12 for x in eigs)==3
assert np.allclose(eigs,[0,1,1,d+1/d],rtol=0,atol=1e-12)

# For pair (1,2): a=1,c=0,u=0,v=(1,0), so ||H||=1.
Hnorm=1.0

# 4. Constants.
C_one=2*math.pi*math.sqrt(6)
C_def=C_one/(2**0.25)  # 2^(5/4) pi sqrt(3)
assert abs(C_def-(2**1.25)*math.pi*math.sqrt(3))<1e-12
live=C_def/math.sqrt((4031/8192)*(1/8))
assert live < 52.184
partner=3*8**(-1/3)
assert abs(partner-1.5)<1e-12

print('QFORM_B09_R47_CHECK_PASS')
print('arcsine_max_ratio =',repr(arc_ratio))
print('pi =',repr(math.pi))
print('max_relative_H_minus_a_g =',repr(max_alg))
print('min_sign(a)*delta_over_random_definite_pairs =',repr(min_sign_delta))
print('near_singular_regression_delta =',repr(d))
print('near_singular_regression_eigenvalues =',[float(x) for x in eigs])
print('near_singular_large_eigenvalue_count =',sum(abs(x)>=1-1e-12 for x in eigs))
print('near_singular_polynomial_star_norm =',Hnorm)
print('one_sided_potential_constant_2pi_sqrt6 =',repr(C_one))
print('definite_pair_constant =',repr(C_def))
print('live_B08_punctured_branch_constant_over_L =',repr(live))
print('partner_diag_4_2_1_constant =',repr(partner))
