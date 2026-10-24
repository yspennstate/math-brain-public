import itertools, math
import numpy as np

rng=np.random.default_rng(12345)

def c2(M):
    rows=list(itertools.combinations(range(M.shape[0]),2))
    cols=list(itertools.combinations(range(M.shape[1]),2))
    C=np.empty((len(rows),len(cols)))
    for a,(i,j) in enumerate(rows):
        for b,(p,q) in enumerate(cols):
            C[a,b]=M[i,p]*M[j,q]-M[i,q]*M[j,p]
    return C,rows,cols

def perp(v):
    return np.eye(len(v))-np.outer(v,v)/np.dot(v,v)

mx_norm=mx_marg=mx_tv_ratio=0.0
for trial in range(1000):
    m=int(rng.integers(3,8)); n=int(rng.integers(3,8))
    a=rng.normal(size=m); r=rng.normal(size=n); H=rng.normal(size=(m,n))
    K=np.outer(a,r)+H
    D,rows,cols=c2(K); U,_,_=c2(H); T=D-U
    Z=perp(a)@H@perp(r)
    lhs=np.sum(T*T); rhs=np.dot(a,a)*np.dot(r,r)*np.sum(Z*Z)
    mx_norm=max(mx_norm,abs(lhs-rhs)/(1+abs(rhs)))
    Om=np.sum(D*D); g=np.sum(U*U)
    if Om==0 or lhs==0: continue
    W=D.ravel()**2/Om; WT=T.ravel()**2/lhs
    tv=0.5*np.sum(np.abs(W-WT)); bd=2*math.sqrt(g/Om)
    if bd: mx_tv_ratio=max(mx_tv_ratio,tv/bd)
    pa=a*a/np.dot(a,a); qz=np.sum(Z*Z,axis=1)/np.sum(Z*Z)
    for i in range(m):
        inc=0.0
        for rr,rowpair in enumerate(rows):
            if i in rowpair:
                inc += np.sum(WT[rr*len(cols):(rr+1)*len(cols)])
        mx_marg=max(mx_marg,abs(inc-(pa[i]+qz[i])))

print('trials=1000')
print('max_relative_compound_norm_error=',mx_norm)
print('max_TV_over_proved_bound=',mx_tv_ratio)
print('max_row_marginal_identity_error=',mx_marg)
print('STATUS=PASS' if mx_norm<1e-12 and mx_tv_ratio<=1+1e-12 and mx_marg<1e-12 else 'STATUS=FAIL')
