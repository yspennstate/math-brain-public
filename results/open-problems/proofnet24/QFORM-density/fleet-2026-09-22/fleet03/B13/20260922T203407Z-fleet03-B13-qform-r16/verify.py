from fractions import Fraction
import math, random

kappa = Fraction(7,800)
c0 = Fraction(3,10)
eps = Fraction(1,100)
delta = Fraction(1,100)

pi_cut = float(kappa*kappa)*math.sqrt(float(c0*eps))
C_cut = 3*math.e*pi_cut**(-1/3)
K0 = 4*math.sqrt(2)*math.sqrt(math.e/float(kappa))*float(c0)**(-1/2)
C_ray = K0*float(delta)**(-1/4)

assert 505.69 < C_cut < 505.70
assert 182.03 < K0 < 182.04
assert 575.64 < C_ray < 575.66

# Verify det(S)=det(G)*rho and the complementary determinant lower bound
# on random PSD block Grams S=[[tau,h^T],[h,G]].
import numpy as np
rng=np.random.default_rng(160313)
for _ in range(200):
    B=rng.normal(size=(8,3))
    S=B.T@B
    # rescale to keep S below a harmless norm; identity being checked is scale-free
    S=S/(10*np.linalg.norm(S,2)+1)
    tau=S[0,0]; h=S[0,1:]; G=S[1:,1:]
    if np.linalg.det(G) < 1e-14: continue
    rho=tau-h@np.linalg.solve(G,h)
    lhs=np.linalg.det(S)
    rhs=np.linalg.det(G)*rho
    assert abs(lhs-rhs) <= 1e-10*(1+abs(lhs)+abs(rhs))

# Verify the rectangular cross singular-product identity
# Pi_3(RI L RJ^T)^2 = det(L)^2 det(SI) det(SJ)
for _ in range(200):
    RI=rng.normal(size=(7,3)); RJ=rng.normal(size=(9,3))
    if np.linalg.matrix_rank(RI)<3 or np.linalg.matrix_rank(RJ)<3: continue
    Lam=np.diag(rng.choice([-1,1],3)*(1+rng.random(3)))
    C=RI@Lam@RJ.T
    sv=np.linalg.svd(C,compute_uv=False)[:3]
    lhs=float(np.prod(sv)**2)
    SI=RI.T@RI; SJ=RJ.T@RJ
    rhs=float(np.linalg.det(Lam)**2*np.linalg.det(SI)*np.linalg.det(SJ))
    assert abs(lhs-rhs) <= 2e-8*(1+abs(lhs)+abs(rhs))

print('kappa =', float(kappa))
print('Pi_cut_lower =', pi_cut)
print('C_cut_eps_0.01 =', C_cut)
print('K0 =', K0)
print('C_ray_delta_0.01 =', C_ray)
print('QFORM_B13_R16_CHECK_PASS')
