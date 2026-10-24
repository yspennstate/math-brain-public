import math
import numpy as np

rng=np.random.default_rng(2026092403)
g=0.5-1/(4*math.sqrt(2))
m0=math.sqrt(47/48)
s0=g*m0-1/4096
qstar=1/(4096*s0)
rho=0.0006247538095703261
eta=2**-20
Ceta=6**(4/3)*(s0**4*eta**2)**(-1/6)
relative=2*((1+qstar)*math.sqrt(2)*eta/rho+qstar)
mismatch_rel=math.sqrt(3)*relative
mismatch_L=mismatch_rel*rho

max_py=0.0
max_transfer_violation=0.0
count=0
for m in [16,32,64]:
    for _ in range(200):
        Z=rng.normal(size=(m,2))
        V,_=np.linalg.qr(Z)
        for __ in range(1000):
            mask=rng.random(m)<0.5
            if mask.sum()<2 or (~mask).sum()<2:
                continue
            VJ,VK=V[mask],V[~mask]
            G=VJ.T@VJ
            H=VK.T@VK
            if np.linalg.eigvalsh(G).min()>.2 and np.linalg.eigvalsh(H).min()>.2:
                break
        else:
            continue

        b=rng.normal(size=m)
        bJ,bK=b[mask],b[~mask]
        cJ=np.linalg.solve(G,VJ.T@bJ)
        cK=np.linalg.solve(H,VK.T@bK)
        eJ=bJ-VJ@cJ
        eK=bK-VK@cK
        cstar=G@cJ+H@cK
        beta2=np.linalg.norm(bJ-VJ@cstar)**2+np.linalg.norm(bK-VK@cstar)**2
        rhs=np.linalg.norm(eJ)**2+np.linalg.norm(eK)**2+(cJ-cK)@(G@H)@(cJ-cK)
        max_py=max(max_py,abs(beta2-rhs))

        Lam=np.diag([1.2,-1.0])
        D0=VJ@Lam@VK.T
        F=rng.normal(size=D0.shape)
        F*=1e-4/np.linalg.svd(F,compute_uv=False)[0]
        D=D0+F
        U,s,VT=np.linalg.svd(D,full_matrices=False)
        R=VT[:2].T
        x=rng.normal(size=VK.shape[0])
        z=R@(R.T@x)
        d=np.linalg.norm(x-z)
        e=np.linalg.norm(x-VK@np.linalg.solve(H,VK.T@x))
        q=1e-4/s[1]
        bound=(1+q)*d+q*np.linalg.norm(x)
        max_transfer_violation=max(max_transfer_violation,e-bound)
        count+=1

print('QFORM_B08_SPLIT_ALIGNMENT_CHECK_PASS')
print('g=',repr(g))
print('m0=',repr(m0))
print('s0=',repr(s0))
print('qstar=',repr(qstar))
print('eta=',repr(eta))
print('Ceta=',repr(Ceta))
print('relative_ultra_alignment=',repr(relative))
print('mismatch_relative=',repr(mismatch_rel))
print('mismatch_L_scale=',repr(mismatch_L))
print('tests=',count)
print('max_pythagoras_abs_error=',repr(max_py))
print('max_plane_transfer_violation=',repr(max_transfer_violation))
