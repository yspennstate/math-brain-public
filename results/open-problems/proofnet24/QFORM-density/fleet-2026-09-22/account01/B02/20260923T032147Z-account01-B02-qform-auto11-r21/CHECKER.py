import itertools
import numpy as np

rng=np.random.default_rng(0)

def e_k_singular_sq(M,k):
    s=np.linalg.svd(M,compute_uv=False)
    x=s*s
    return sum(np.prod([x[i] for i in C]) for C in itertools.combinations(range(len(x)),k))

def anchored(M,k):
    m,n=M.shape
    z=0.0
    for P in itertools.combinations(range(1,m),k):
        for T in itertools.combinations(range(1,n),k):
            rows=(0,)+P; cols=(0,)+T
            z += np.linalg.det(M[np.ix_(rows,cols)])**2
    return z

errs=[]
for _ in range(10):
    M=rng.normal(size=(7,8))
    a=M[0,0]; r=M[0,1:]; c=M[1:,0]; N=M[1:,1:]
    S=N-np.outer(c,r)/a
    for k in (1,2,3,4):
        lhs=anchored(M,k)
        rhs=a*a*e_k_singular_sq(S,k)
        errs.append(abs(lhs-rhs)/max(1.0,abs(lhs),abs(rhs)))

errs0=[]
for _ in range(10):
    M=rng.normal(size=(7,8)); M[0,0]=0.0
    r=M[0,1:]; c=M[1:,0]; N=M[1:,1:]
    Pc=np.eye(6)-np.outer(c,c)/np.dot(c,c)
    Pr=np.eye(7)-np.outer(r,r)/np.dot(r,r)
    K=Pc@N@Pr
    for k in (1,2,3,4):
        lhs=anchored(M,k)
        rhs=np.dot(c,c)*np.dot(r,r)*(1.0 if k==1 else e_k_singular_sq(K,k-1))
        errs0.append(abs(lhs-rhs)/max(1.0,abs(lhs),abs(rhs)))

print('NONZERO_EDGE_MAX_RELERR',max(errs))
print('ZERO_EDGE_MAX_RELERR',max(errs0))
assert max(errs)<1e-12
assert max(errs0)<1e-12
print('QFORM_B02_ANCHORED_COMPOUND_PASS')
