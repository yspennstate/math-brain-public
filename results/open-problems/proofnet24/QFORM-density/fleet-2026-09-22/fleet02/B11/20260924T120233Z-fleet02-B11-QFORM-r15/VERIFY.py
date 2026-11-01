import math
import numpy as np

rng=np.random.default_rng(20260924)
viol=0
min_ratio=float('inf')
for _ in range(50000):
    Q,_=np.linalg.qr(rng.normal(size=(3,3)))
    signs=np.array([1,1,-1]) if rng.random()<0.5 else np.array([1,-1,-1])
    mags=1+rng.random(3)*4
    vals=signs*mags
    M=Q@np.diag(vals)@Q.T
    s=np.min(np.abs(vals))

    U,_=np.linalg.qr(rng.normal(size=(3,3)))
    t=rng.random(3)*0.8
    T=U@np.diag(t)@U.T
    eps=np.max(t)
    S=np.eye(3)-T
    ev,EV=np.linalg.eigh(S)
    sqrtS=EV@np.diag(np.sqrt(ev))@EV.T
    O,_=np.linalg.qr(rng.normal(size=(3,3)))
    W=sqrtS@O
    B=W.T@M@W
    sb=np.min(np.abs(np.linalg.eigvalsh(B)))
    lower=s*(1-eps)
    ratio=sb/lower
    min_ratio=min(min_ratio,ratio)
    if sb+1e-10 < lower:
        viol += 1

print('frame_deficit_violations',viol)
print('minimum_sigma_ratio',repr(min_ratio))

for m in [1,2,3,5,10,100,1000]:
    C=np.array([[0,m**-0.5,m**-0.5],
                [m**-0.5,0,m**-1],
                [m**-0.5,m**-1,0.0]])
    smin=np.min(np.abs(np.linalg.eigvalsh(C)))
    print('m',m,'literal_smin',repr(smin),'m_times_smin',repr(m*smin))

Cprime=np.array([[0,1/math.sqrt(2),1/math.sqrt(2)],
                 [1/math.sqrt(2),0,0.5],
                 [1/math.sqrt(2),0.5,0]])
print('Cprime_eigenvalues',np.linalg.eigvalsh(Cprime))
print('Cprime_det',np.linalg.det(Cprime))
print('exact_moving_log_constant',8*2**(5/8))
print('zerodiagonal_generic_constant',16*6**0.25)
print('general_frame_deficit_constant',2*(4*22**0.75*3**0.25))
assert viol==0
assert abs(np.linalg.det(Cprime)-0.5)<1e-12
assert abs(np.min(np.abs(np.linalg.eigvalsh(Cprime)))-0.5)<1e-12
print('QFORM_B11_R15_FRAME_DEFICIT_CHECK_PASS')
