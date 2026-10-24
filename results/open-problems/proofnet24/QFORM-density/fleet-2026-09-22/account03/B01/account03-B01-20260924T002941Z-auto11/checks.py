import math
import itertools
import numpy as np

THETA = 1.0/64.0
BETA = 1.0/32.0

C_BILIN = 4.0*math.sqrt(2.0/math.e)
C_INTERVAL = (C_BILIN**0.25) * (2.0/(1.0-THETA))**0.125
C_INTERVAL_2 = 2.0**0.75 * math.exp(-0.125) * (1.0-THETA)**(-0.125)
assert abs(C_INTERVAL-C_INTERVAL_2) < 1e-13
alpha = 1.0/8.0
C_FEJ_KERNEL = (2.0**alpha/(2.0*math.pi)
                + (2.0/math.pi)*2.0**(2.0*alpha)/(1.0-2.0**(-(2.0-alpha))))
C_FEJER = C_FEJ_KERNEL*C_INTERVAL

D_MIN = BETA**2-THETA**2
KAPPA_MIN = BETA-THETA
H_HALF = 2.0*math.sqrt(2.0/THETA)
PAIR_HALF = 4.0*math.sqrt(2.0*H_HALF)*(D_MIN*KAPPA_MIN)**(-0.25)
K_RADIUS = C_INTERVAL*2.0**0.125
A0 = 2.0*math.sqrt(2.0)
B0 = D_MIN**(-0.5) * 8.0*2.0**0.125*K_RADIUS*KAPPA_MIN**(-0.125)
r_star = (4.0*A0/B0)**0.8
PAIR_EIGHTH = A0/r_star + B0*r_star**0.25

print('C_BILIN =', C_BILIN)
print('C_INTERVAL(theta=1/64) =', C_INTERVAL)
print('C_FEJ_KERNEL(alpha=1/8) =', C_FEJ_KERNEL)
print('C_FEJER =', C_FEJER)
print('D_MIN =', D_MIN)
print('KAPPA_MIN =', KAPPA_MIN)
print('H_HALF =', H_HALF)
print('PAIR_HALF =', PAIR_HALF)
print('K_RADIUS =', K_RADIUS)
print('B0 =', B0)
print('r_star =', r_star)
print('PAIR_EIGHTH =', PAIR_EIGHTH)
assert C_INTERVAL < 1.488
assert C_FEJER < 1.806
assert PAIR_HALF < 463.0
assert PAIR_EIGHTH < 461.0

O = np.array([[0.0, 2.0, -1.0, 0.5],
              [2.0, 0.0, 0.75, -0.25],
              [-1.0, 0.75, 0.0, 1.5],
              [0.5, -0.25, 1.5, 0.0]])
normO = np.linalg.norm(O, 2)
vals=[]
Cs=[]
for eps in itertools.product([-1.0,1.0], repeat=4):
    e=np.array(eps)
    C=(O-(e[:,None]*O*e[None,:]))/2.0
    vals.append(np.linalg.norm(C,2))
    Cs.append(C)
Cavg=sum(Cs)/len(Cs)
assert np.linalg.norm(Cavg-O/2.0) < 1e-12
assert sum(vals)/len(vals) + 1e-12 >= normO/2.0
print('CUT_EXAMPLE normO =', normO)
print('CUT_EXAMPLE avg_norm/(normO) =', (sum(vals)/len(vals))/normO)
print('CUT_EXAMPLE best_norm/(normO) =', max(vals)/normO)

rng=np.random.default_rng(20260924)
min_slack=1e100
for n in range(5,9):
    for _ in range(100):
        G=rng.normal(size=(n,n))
        A=(G+G.T)/2.0
        B=A[:2,:2]
        if abs(np.linalg.det(B)) < 1e-5:
            continue
        U=A[:2,2:]
        C=A[2:,2:]
        S=C-U.T@np.linalg.inv(B)@U
        sA=np.linalg.svd(A,compute_uv=False)
        sS=np.linalg.svd(S,compute_uv=False)
        slack=sS[0]-sA[2]
        min_slack=min(min_slack,slack)
        assert slack > -1e-9
print('SCHUR_DIAGNOSTIC min(s1(S)-s3(A)) =', min_slack)

for nI,nJ in [(2,3),(4,2),(3,4)]:
    G=rng.normal(size=(nI+nJ,nI+nJ))
    A=(G+G.T)/2.0
    B=A[:nI,nI:]
    y=rng.normal(size=nI); yp=rng.normal(size=nI)
    z=rng.normal(size=nJ); zp=rng.normal(size=nJ)
    def q(y0,z0):
        x=np.concatenate([y0,z0])
        return float(x@A@x)
    lhs=(q(y,z)-q(yp,z))-(q(y,zp)-q(yp,zp))
    rhs=2.0*(y-yp)@B@(z-zp)
    assert abs(lhs-rhs) < 1e-10
print('DOUBLE_DIFFERENCE_IDENTITY = PASS')
print('STATUS=PASS')
