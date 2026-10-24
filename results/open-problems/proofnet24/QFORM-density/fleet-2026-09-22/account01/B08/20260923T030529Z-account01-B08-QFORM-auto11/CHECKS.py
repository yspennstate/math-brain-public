import math
import numpy as np

rho=math.sqrt(3/5)
beta=(3/16)*rho
c1=rho-3/128
c2=rho-1/640

assert abs((beta/8)/rho-3/128)<1e-15
assert abs((beta/120)/rho-1/640)<1e-15
assert c1>0.75
assert c2>0.773
assert abs(c1**2-0.5642400975355555)<1e-14
assert abs(c1**4-0.3183668876669332)<1e-14

# Numerical sanity check of Theorem 2.1 on deterministic-seed random
# symmetric matrices. This is not the proof; REPORT.md contains the proof.
rng=np.random.default_rng(20260923)
checked=0
worst_margin=float('inf')
for trial in range(500):
    n=12
    M=rng.normal(size=(n,n))
    A=(M+M.T)/2
    vals,vecs=np.linalg.eigh(A)
    idx=np.argsort(np.abs(vals))[-3:]
    R=vecs[:,idx]
    Lam=vals[idx]
    L=np.min(np.abs(Lam))

    perm=rng.permutation(n)
    I=np.sort(perm[:n//2])
    J=np.sort(perm[n//2:])
    GI=R[I].T@R[I]
    GJ=R[J].T@R[J]
    amin=min(np.linalg.eigvalsh(GI).min(),np.linalg.eigvalsh(GJ).min())
    if amin<=1e-6 or amin>0.5:
        continue
    alpha=0.999*amin
    rr=math.sqrt(alpha/(1-alpha))

    B=A[np.ix_(I,J)]
    sB=np.linalg.svd(B,compute_uv=False)
    sI=np.linalg.svd(A[np.ix_(I,I)],compute_uv=False)
    sJ=np.linalg.svd(A[np.ix_(J,J)],compute_uv=False)
    for r in (0,1,2):
        rhs=rr*L-(1/rr)*sB[r]
        lhs=min(sI[2-r],sJ[2-r])
        margin=lhs-rhs
        assert margin>-1e-8
        worst_margin=min(worst_margin,margin)
        checked+=1

print(f'rho={rho:.15f}')
print(f'beta/L={beta:.15f}')
print(f'c1={c1:.15f}')
print(f'c2={c2:.15f}')
print(f'c1^2={c1**2:.15f}')
print(f'c1^4={c1**4:.15f}')
print(f'randomized inequalities checked={checked}')
print(f'worst numerical margin={worst_margin:.15f}')
print('QFORM_B08_AUTO11_CHECK_PASS')
