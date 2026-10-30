import numpy as np, math

rng=np.random.default_rng(20260924)

def e2_gram(M):
    s=np.linalg.svd(M,compute_uv=False)
    return sum((s[i]*s[j])**2 for i in range(len(s)) for j in range(i+1,len(s)))

def xi_total(D,r,g):
    m=len(r); out=0.0
    for k in range(m):
        idx=[j for j in range(m) if j!=k]
        rr=r[idx]; d=D[k,idx]
        a=(d@rr)/(rr@rr)
        delta=np.linalg.norm(d-a*rr)
        Mk=np.vstack([g[0]*rr,g[1]*rr,d])
        lhs=e2_gram(Mk)
        rhs=(g@g)*(rr@rr)*delta**2
        if abs(lhs-rhs)>3e-12*max(1.0,abs(rhs)):
            raise AssertionError(("local identity",lhs,rhs))
        out += lhs
    return out

def dstar(D,r):
    m=len(r)
    num=den=0.0
    for i in range(m):
        for j in range(m):
            if i!=j:
                num += D[i,j]*r[i]*r[j]
                den += (r[i]*r[j])**2
    lam=num/den
    s=0.0
    for i in range(m):
        for j in range(m):
            if i!=j:
                s+=(D[i,j]-lam*r[i]*r[j])**2
    return math.sqrt(s),lam

def selected(D,r,g,S):
    T=[i for i in range(len(r)) if i not in S]
    z=0.0
    for k in S:
        for h in range(2):
            for aa in range(len(T)):
                for bb in range(aa+1,len(T)):
                    i,j=T[aa],T[bb]
                    d=g[h]*(r[i]*D[k,j]-r[j]*D[k,i])
                    z+=d*d
    return z

max_rel=0.0
min_comp=float("inf")
for trial in range(100):
    m=int(rng.integers(5,10))
    while True:
        r=rng.normal(size=m)
        R=np.linalg.norm(r)
        q=np.max(r*r)/(R*R)
        if q<0.85:
            break
    g=rng.normal(size=2)
    if np.linalg.norm(g)<0.2:
        g[0]+=1.0
    D=rng.normal(size=(m,m)); D=(D+D.T)/2
    Xi=0.0
    for k in range(m):
        idx=[j for j in range(m) if j!=k]
        rr=r[idx]; d=D[k,idx]
        a=(d@rr)/(rr@rr)
        delta=np.linalg.norm(d-a*rr)
        Mk=np.vstack([g[0]*rr,g[1]*rr,d])
        lhs=e2_gram(Mk)
        rhs=(g@g)*(rr@rr)*delta**2
        max_rel=max(max_rel,abs(lhs-rhs)/max(1.0,abs(rhs)))
        Xi+=lhs
    ds,_=dstar(D,r)
    lo=math.sqrt(Xi)/(np.linalg.norm(g)*R)
    hi=math.sqrt(2/(1-q))*lo
    if not (lo <= ds+1e-10 and ds <= hi+1e-10):
        raise AssertionError(("stability",lo,ds,hi,q))
    best=0.0
    for mask in range(1<<m):
        S=[k for k in range(m) if (mask>>k)&1]
        best=max(best,selected(D,r,g,S))
    if best+1e-10 < (4/27)*Xi:
        raise AssertionError(("compiler",best,(4/27)*Xi))
    min_comp=min(min_comp,best/Xi)

m=9
r=rng.normal(size=m); g=rng.normal(size=2)
D=1.7*np.outer(r,r)+np.diag(rng.normal(size=m))
aligned_Xi=xi_total(D,r,g)
aligned_ds,_=dstar(D,r)

A=np.zeros((6,6))
A[:2,:2]=np.array([[1.,1.],[1.,1.]])
g0=np.array([1.,-1.]); r0=np.ones(4)
A[:2,2:]=np.outer(g0,r0); A[2:,:2]=A[:2,2:].T
D0=np.zeros((4,4))
D0[0,2]=D0[2,0]=1.
D0[1,3]=D0[3,1]=1.
A[2:,2:]=D0
evals=np.linalg.eigvalsh(A)
K=A[np.ix_([0,2,3],[1,4,5])]
detK=np.linalg.det(K)
Xi0=xi_total(D0,r0,g0)
ds0,lam0=dstar(D0,r0)
partner=3*abs(detK)**(-1/3)

print("PASS")
print(f"100_random_max_local_identity_relative_error={max_rel:.3e}")
print(f"100_random_min_best_partition_over_Xi={min_comp:.12f}")
print(f"required_partition_ratio={4/27:.12f}")
print(f"aligned_Xi={aligned_Xi:.3e}")
print(f"aligned_dstar={aligned_ds:.3e}")
print("stress_eigenvalues="+np.array2string(evals,precision=12,separator=","))
print(f"stress_Xi={Xi0:.12f}")
print(f"stress_dstar={ds0:.12f}")
print(f"stress_lambda_opt={lam0:.12f}")
print(f"stress_detK={detK:.12f}")
print(f"partner_density_bound={partner:.12f}")
