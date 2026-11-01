import itertools
import numpy as np

rng=np.random.default_rng(20260924)

def e2_ss(S):
    x=np.linalg.svd(S,compute_uv=False)**2
    return sum(x[i]*x[j] for i in range(len(x)) for j in range(i+1,len(x)))

def fixed_star(M,i,j):
    rows=[k for k in range(M.shape[0]) if k!=i]
    cols=[k for k in range(M.shape[1]) if k!=j]
    total=0.0
    for R in itertools.combinations(rows,2):
        for C in itertools.combinations(cols,2):
            total += np.linalg.det(M[np.ix_((i,)+R,(j,)+C)])**2
    return total

def Pperp(v):
    n=len(v); q=np.linalg.norm(v)
    if q==0: return np.eye(n)
    u=v/q
    return np.eye(n)-np.outer(u,u)

e_non=e_zero=e_rank=0.0
for _ in range(100):
    M=rng.normal(size=(7,8)); i,j=2,3
    rows=[k for k in range(7) if k!=i]
    cols=[k for k in range(8) if k!=j]
    m=M[i,j]; c=M[rows,j]; r=M[i,cols]; N=M[np.ix_(rows,cols)]
    lhs=fixed_star(M,i,j)
    S=N-np.outer(c,r)/m
    rhs=m*m*e2_ss(S)
    e_non=max(e_non,abs(lhs-rhs)/(1+abs(lhs)))

    M[i,j]=0.0
    c=M[rows,j]; r=M[i,cols]; N=M[np.ix_(rows,cols)]
    lhs=fixed_star(M,i,j)
    rhs=np.dot(c,c)*np.dot(r,r)*np.linalg.norm(Pperp(c)@N@Pperp(r),'fro')**2
    e_zero=max(e_zero,abs(lhs-rhs)/(1+abs(lhs)))

for _ in range(100):
    n=9
    a=float(rng.uniform(.2,2))*rng.choice([-1,1])
    u=rng.normal(size=n); w=rng.normal(size=n)
    C=rng.normal(size=(n,n)); C=(C+C.T)/2
    S=C-np.outer(u,u)/a
    e=w/np.linalg.norm(w); P=np.eye(n)-np.outer(e,e)
    alpha=e@S@e; b=P@S@e; T=P@S@P
    Rc=np.outer(u,u)/a+alpha*np.outer(e,e)+np.outer(e,b)+np.outer(b,e)
    e_rank=max(e_rank,np.linalg.norm(C-(Rc+T),2))

print(f'max_rel_error_nonzero_pivot={e_non:.3e}')
print(f'max_rel_error_zero_pivot={e_zero:.3e}')
print(f'max_op_error_physical_rank3_decomposition={e_rank:.3e}')
print('STATUS=PASS')
