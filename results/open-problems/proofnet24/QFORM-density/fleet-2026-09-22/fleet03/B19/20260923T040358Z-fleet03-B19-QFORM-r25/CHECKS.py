import math
import numpy as np

m0sq = 1023/4096
eta = 1/4
physical_diag_gate = 1/4
# dominant-star pair determinant in the B10 collar:
dom_D = (1-eta)*m0sq - (1/64)*physical_diag_gate
pair_bound = dom_D**(-0.5)*(9.2 + math.log(10000*math.sqrt(dom_D)))
C3 = 16*math.sqrt(30)*2**0.25
line7 = 2*C3*math.comb(7,3)**(1/3)
# stable-alignment aggregate branch when ||D_adjusted||_op <= 1/2
sum_delta_lb = eta*m0sq*(1-1/2)**2/8
cut_E2_lb = sum_delta_lb/8
q43_coeff = 9*math.sqrt(3)*math.e/2
volume_gate = q43_coeff*(3/(cut_E2_lb*(1/64)**2))**(1/6)

assert dom_D == 3005/16384
assert pair_bound < 42
assert line7 < 682
assert sum_delta_lb == m0sq/128
assert abs(cut_E2_lb - m0sq/1024) < 1e-18
assert volume_gate < 408

# Numerical regression for the stable-alignment inequality.
def stable_trial(seed, n=9):
    rng=np.random.default_rng(seed)
    while True:
        m=rng.normal(size=n)
        M2=float(m@m)
        if np.max(m*m) <= (1-eta)*M2:
            break
    H=rng.normal(size=(n,n)); H=(H+H.T)/2
    alpha=np.zeros(n); err=np.zeros((n,n)); deltas=np.zeros(n)
    for j in range(n):
        mask=np.arange(n)!=j
        mj=m[mask]; hj=H[j,mask]
        den=float(mj@mj)
        alpha[j]=float(hj@mj)/den
        e=hj-alpha[j]*mj
        err[j,mask]=e
        deltas[j]=den*float(hj@hj)-float(hj@mj)**2
    E0=float(np.sum(err**2))
    supp=np.abs(m)>1e-14
    w=m[supp]**2
    beta=alpha[supp]/m[supp]
    theta=float(np.sum(w*beta)/M2)
    R=H-theta*np.outer(m,m); np.fill_diagonal(R,0)
    lhs=float(np.sum(R**2))
    rhs=8/(eta*M2)*float(np.sum(deltas))
    assert lhs <= rhs*(1+1e-10)
    return lhs/rhs

mx=max(stable_trial(s) for s in range(200))
print('QFORM_B19_R25_STABLE_ALIGNMENT_CHECK_PASS')
print('dominant_pair_D_lower=', dom_D)
print('dominant_pair_density_bound=', pair_bound)
print('finite_line_K7_bound=', line7)
print('sum_Delta_sq_lower=', sum_delta_lb)
print('random_cut_E2_lower=', cut_E2_lb)
print('q43_volume_exit_bound_s3_ge_1over64=', volume_gate)
print('max_random_stable_ratio=', mx)
