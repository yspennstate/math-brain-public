import math
import numpy as np

C_density = 3*2**(2/3)
common = 128*math.sqrt(15)
tau = (C_density/common)**6
u2_floor = 0.994673971719684
u4_floor = u2_floor**2
tau_wdelta = tau/u4_floor
C_collision = (24/5)*2**(1/3)*math.sqrt(math.pi)

assert abs(C_density-4.762203155904598) < 1e-14
assert abs(common-495.7418683145494) < 1e-12
assert abs(tau-7.858034223318098e-13) < 1e-25
assert abs(u4_floor-0.9893763100166106) < 1e-14
assert abs(tau_wdelta-7.942411945547968e-13) < 1e-25
assert abs(C_collision-10.719129200270824) < 1e-13

rng=np.random.default_rng(260923)
max_abs=0.0
max_rel=0.0
for n in [4,5,8,15]:
    for _ in range(50):
        Q,_=np.linalg.qr(rng.normal(size=(n,2)))
        v,q=Q[:,0],Q[:,1]
        beta=float(rng.normal())
        m=10**float(rng.uniform(-1,1))
        h=beta*v+m*q
        rows=np.c_[h,v]
        w={(i,j):(q[i]*v[j]-q[j]*v[i])**2 for i in range(n) for j in range(i+1,n)}
        for i in range(n):
            for j in range(i+1,n):
                delta=sum(val for (k,l),val in w.items() if i not in (k,l) and j not in (k,l))
                G=sum((np.outer(rows[k],rows[k]) for k in range(n) if k not in (i,j)),np.zeros((2,2)))
                target=m*m*delta
                err=abs(np.linalg.det(G)-target)
                max_abs=max(max_abs,err)
                if abs(target)>1e-12:
                    max_rel=max(max_rel,err/abs(target))
        r=0
        ids=[k for k in range(n) if k!=r]
        G=sum((np.outer(rows[k],rows[k]) for k in ids),np.zeros((2,2)))
        if np.linalg.det(G)>1e-9:
            zeta=1-(v[r]**2+q[r]**2)
            inv=np.linalg.inv(G)
            for j in ids:
                lev=float(rows[j]@inv@rows[j])
                G2=G-np.outer(rows[j],rows[j])
                target=m*m*zeta*(1-lev)
                err=abs(np.linalg.det(G2)-target)
                max_abs=max(max_abs,err)
                if abs(target)>1e-12:
                    max_rel=max(max_rel,err/abs(target))

print('QFORM_B03_TWO_RIGHTROW_Q2_PASS')
print(f'C_density={C_density:.15f}')
print(f'common_envelope={common:.15f}')
print(f'threshold_u4_wdelta={tau:.18e}')
print(f'left_concentrated_u4_floor={u4_floor:.15f}')
print(f'left_concentrated_wdelta_threshold={tau_wdelta:.18e}')
print(f'C_collision={C_collision:.15f}')
print(f'max_random_absolute_identity_error={max_abs:.3e}')
print(f'max_random_relative_identity_error={max_rel:.3e}')
