import numpy as np
from math import sqrt

rng=np.random.default_rng(20260924)
max_disjoint=0.0
max_schur=0.0
min_sum_gap=float('inf')
min_star_ratio=float('inf')
checked=0
for _ in range(200):
    n=rng.normal(size=3); n/=np.linalg.norm(n)
    C=(np.eye(3)-np.outer(n,n))@rng.normal(size=(3,7))
    G=C@C.T
    lam,U=np.linalg.eigh(G)
    n0=U[:,0]
    if n0@n<0: n0=-n0
    n=n0
    sv=np.linalg.svd(C,compute_uv=False)
    s1,s2=sv[:2]; Delta=s1*s2

    P=rng.normal(size=(3,3)); P=(P+P.T)/2
    a=P@n
    D0=np.diag(np.diag(P))
    sum_z2=0.0
    for j in range(3):
        H=[q for q in range(3) if q!=j]
        M=np.column_stack([C[H,:],P[H,j]])
        z2=np.linalg.det(M@M.T)
        r=np.cross(np.eye(3)[j],P[:,j])
        rhs=Delta**2*n[j]**2+r@G@r
        max_disjoint=max(max_disjoint,abs(z2-rhs))
        sum_z2+=z2
    lower=Delta**2+s2**2*np.linalg.norm((P-D0)@n)**2
    min_sum_gap=min(min_sum_gap,sum_z2-lower)

    if abs(n[2])<1e-4:
        continue
    d1,d2=rng.normal(size=2); b=2+abs(rng.normal())
    B=np.array([[d1,b],[b,d2]])
    if np.linalg.det(B)>=0:
        B[1,1]=-abs(B[1,1])-3
    if np.linalg.det(B)>=0:
        continue
    p=rng.normal(size=2)
    d=float(p@np.linalg.inv(B)@p)
    Ps=np.block([[B,p[:,None]],[p[None,:],np.array([[d]])]])
    aa=Ps@n
    CH=C[:2,:]; c=C[2,:]
    m=c-p@np.linalg.inv(B)@CH
    sch=d-p@np.linalg.inv(B)@p
    ident=n[2]*m+CH.T@np.linalg.inv(B)@aa[:2]
    max_schur=max(max_schur,abs(sch),np.linalg.norm(ident))
    lb=s2*np.linalg.norm(aa[:2])/np.linalg.norm(B,2)
    if lb>1e-12:
        min_star_ratio=min(min_star_ratio,np.linalg.norm(m)/lb)
    checked+=1

P=np.array([[0.,1.,0.],[1.,0.,1.],[0.,1.,0.]])
C=np.array([[1.,0.],[0.,1.],[-1.,-1.]])
A=np.block([[P,C],[C.T,np.zeros((2,2))]])
eigs=np.linalg.eigvalsh(A)
B=P[:2,:2]; p=P[:2,2]
m=C[2,:]-p@np.linalg.inv(B)@C[:2,:]
bound=2**(27/8)*(abs(np.linalg.det(B))*np.linalg.svd(B,compute_uv=False)[-1]*np.linalg.norm(m))**(-1/4)
partner=3*4**(-1/3)

print('seeded_cases',checked)
print('max_disjoint_identity_error',max_disjoint)
print('max_schur_identity_error',max_schur)
print('minimum_summed_lower_bound_gap',min_sum_gap)
print('minimum_star_lower_bound_ratio',min_star_ratio)
print('regression_eigenvalues',eigs.tolist())
print('regression_m',m.tolist(),'norm',np.linalg.norm(m))
print('schur_null_density_constant',bound)
print('partner_constant',partner)
assert max_disjoint < 1e-9
assert max_schur < 1e-9
assert min_sum_gap >= -1e-9
assert min_star_ratio >= 1-1e-9
assert sum(abs(e)>=1-1e-10 for e in eigs)>=3
