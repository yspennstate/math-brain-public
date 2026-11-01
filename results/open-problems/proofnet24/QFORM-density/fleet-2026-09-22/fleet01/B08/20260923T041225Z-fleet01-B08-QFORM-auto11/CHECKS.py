import math
import numpy as np

DELTA = 1/4
RHO = math.sqrt(3/5)
KAPPA_STAR = RHO - 3/128
BETA = (3/16)*RHO
EPS_STAR = BETA/8
C_STAR = (3/8)*KAPPA_STAR - 1/64
C3 = (9*math.sqrt(3)*math.e/2) * (16**(1/6))

print('rho', RHO)
print('kappa_star', KAPPA_STAR)
print('beta', BETA)
print('eps_star', EPS_STAR)
print('c_star', C_STAR)
print('paid_constant_over_L', C3/C_STAR)
print('V3_bicolop_coeff', C_STAR**6/48)
print('s1s2_coeff', 0.75*C_STAR**2)
print('E2_coeff', (0.75*C_STAR**2)**2)
print('s1_lower_coeff', 0.75*C_STAR**2/EPS_STAR)
print('anisotropy_ratio', (0.75*C_STAR**2/EPS_STAR)/EPS_STAR)

# theta=3/4 E2 fractional L3 receiver
th=3/4
K=th**(-th)*(1-th)**(-(1-th))
C_L3=(math.e*(3*th/(3*th-2))*K**(-1/(4*th)))**(2/3)
C_L3_c=C_L3*(9/16)**(-1/6)
print('L3_constant_over_c_2_3', C_L3_c)
print('L3_partner_constant', C_L3_c*C_STAR**(-2/3))
print('V2_bicolop_coeff', (3/16)*C_STAR**4)

# Deterministic-seed numerical sanity check of the main implication in the
# 4x4 compressed model. This is supplementary, not the proof.
def E3(M):
    s=np.linalg.svd(M,compute_uv=False)
    lam=s*s
    out=0.0
    for i in range(len(lam)):
        for j in range(i+1,len(lam)):
            for k in range(j+1,len(lam)):
                out += lam[i]*lam[j]*lam[k]
    return out

rng=np.random.default_rng(2026092304)
for trial in range(5000):
    X=rng.normal(size=(2,2)); UL,_,VR=np.linalg.svd(X)
    C=UL@np.diag(1+rng.random(2)*3)@VR
    X=rng.normal(size=(2,2)); UL,_,VR=np.linalg.svd(X)
    D=UL@np.diag(1+rng.random(2)*3)@VR

    # B rows I+,I- and columns J+,J-.  The recolored off-blocks use
    # B[I+,J-] and B[I-,J+]^T.
    B=rng.normal(size=(4,4))*3
    U0=B[:2,2:]
    V0=B[2:,:2].T
    M=np.block([[C,U0],[V0,D]])

    z=E3(M)
    sb=np.linalg.svd(B,compute_uv=False)
    # Here c>=1 by construction.
    if z < DELTA**2-1e-9:
        assert sb[0]*sb[1] >= 1-DELTA-1e-9

print('QFORM_B08_AUTO11_RECOLOR_E3_E2_CHECK_PASS')
