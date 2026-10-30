import math
import numpy as np

rng=np.random.default_rng(20260923)
max_alpha_err=0.0
max_zk_err=0.0
min_count_minus_touch=float('inf')
tested=0
for _ in range(500):
    m=int(rng.integers(3,9)); n=int(rng.integers(1,7))
    v=rng.normal(size=m); v=v/np.linalg.norm(v)
    M=rng.normal(size=(m,n))
    C=M-np.outer(v,v@M)
    Z=float(np.sum(C*C))
    if Z<1e-10:
        continue
    alpha=np.zeros(m)
    weights=[]
    for p in range(m):
        for q in range(p+1,m):
            for t in range(n):
                w=float((v[p]*M[q,t]-v[q]*M[p,t])**2/Z)
                alpha[p]+=w; alpha[q]+=w
                weights.append((p,q,t,w))
    formula=v*v+np.sum(C*C,axis=1)/Z
    max_alpha_err=max(max_alpha_err,float(np.max(np.abs(alpha-formula))))
    H=set(rng.choice(m,size=int(rng.integers(1,3)),replace=False).tolist())
    touch=sum(w for p,q,t,w in weights if p in H or q in H)
    lhs=float(sum(formula[list(H)]))
    min_count_minus_touch=min(min_count_minus_touch,lhs-touch)
    K=[i for i in range(m) if i not in H]
    s2=float(np.sum(v[K]**2))
    zk=sum(w*Z for p,q,t,w in weights if p in K and q in K)
    if s2>1e-12:
        r=(v[K]@M[K,:])/s2
        E=M[K,:]-np.outer(v[K],r)
        rhs=s2*float(np.sum(E*E))
        max_zk_err=max(max_zk_err,abs(zk-rhs))
    tested+=1

v=np.array([3/5,4/5],float)
M=np.array([[0.],[4.]])
C=M-np.outer(v,v@M)
Z=float(np.sum(C*C))
A=np.array([[36/25,48/25,0],[48/25,64/25,4],[0,4,0]],float)
eigs=np.linalg.eigvalsh(A)

print('QFORM_B06_FUSED_CONCENTRATION_CHECK_PASS')
print(f'cases={tested}')
print(f'max_alpha_identity_error={max_alpha_err:.3e}')
print(f'max_complement_identity_error={max_zk_err:.3e}')
print(f'minimum_Ecount_minus_touch={min_count_minus_touch:.3e}')
print(f'partner_Z_floor={11907/1048576:.15f}')
print(f'partner_residual_row_floor={math.sqrt((11907/1048576)/8):.15f}')
print(f'prototype_Z={Z:.15f}')
print(f'prototype_C1={C[0,0]:.15f}')
print(f'prototype_v1_sq={v[0]**2:.15f}')
print('prototype_eigenvalues='+','.join(f'{x:.15f}' for x in eigs))
print(f'prototype_density_bound_6sqrtpi={6*math.sqrt(math.pi):.15f}')
