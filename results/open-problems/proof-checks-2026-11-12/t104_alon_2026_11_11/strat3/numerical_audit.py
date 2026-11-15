"""Independent numerical checks using original eigenbasis pair definitions.
Run: OMP_NUM_THREADS=1 python3 numerical_audit.py
All observations printed by this script are NUMERICAL.
"""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS']:
    os.environ[key]='1'
import time
import numpy as np

rng=np.random.default_rng(20261113)
start=time.monotonic()
max_error=0.; min_rankone=float('inf'); min_equitable=float('inf'); count=0

def original_terms(W,Pi,lam):
    n=len(W); c=2*n/(n-2); beta=(1-lam)/(n-2)
    L=np.diag(W.sum(axis=1))-W
    H=np.eye(n)-np.ones((n,n))/n
    G=lam*H-L
    ev,V=np.linalg.eigh(G)
    ep,U=np.linalg.eigh(Pi); U=U[:,ep>.5]
    vals=np.zeros(4)
    for idx,g in enumerate(ev):
        if g<1e-11: continue
        v=V[:,idx]; mu=lam-g
        for u in U.T:
            p=u*v
            A2=1-c*np.dot(p,p)
            vals[0]+=g*mu
            vals[1]+=g*c*(lam*np.dot(p,p)-p@L@p)
            vals[2]+=g*beta*A2
            for i in range(n):
                for j in range(i):
                    vals[3]+=2*g*W[i,j]*((u[i]-u[j])*(v[i]-v[j]))**2
    M=Pi*G; D=round(np.trace(Pi)); tr=np.trace
    tracevals=np.array([D*np.sum(L*G.T),c*np.sum(G*M.T),beta*(D*tr(G)-c*tr(M)),
        2*sum(W[i,j]*(Pi[i,i]+Pi[j,j]-2*Pi[i,j])*(G[i,i]+G[j,j]-2*G[i,j])
              for i in range(n) for j in range(i))])
    assert np.isfinite(vals).all() and np.isfinite(tracevals).all()
    global max_error
    max_error=max(max_error,np.max(np.abs(vals-tracevals)))
    return vals

for it in range(240):
    v=rng.normal(size=5); v-=v.mean(); v/=np.linalg.norm(v)
    p=max(-v[i]*v[j] for i in range(5) for j in range(i))
    gcap=min(2/3,2/(20*p-1)); g=gcap*(1 if it%3==0 else rng.uniform(.01,1))
    lam=(2+g)/4; H=np.eye(5)-np.ones((5,5))/5
    W=lam/5+g*np.outer(v,v); np.fill_diagonal(W,0)
    assert W.min()>-1e-13
    vals=original_terms(W,H-np.outer(v,v),lam)
    T=vals[:3].sum()-vals[3]
    B=7+16*g+(70-200*g)*sum(v**4)+120*g*sum(v**3)**2
    max_error=max(max_error,abs(T-g*B/45))
    assert T>=g/9-1e-11
    min_rankone=min(min_rankone,B)
print('NUMERICAL: 240 feasible rank-one examples; minimum bracket %.12g'%min_rankone)

# Check both kinds of feasible endpoint at g=2/3.
for k in [1,2]:
    v=np.array([np.sqrt((5-k)/(5*k))]*k+[-np.sqrt(k/(5*(5-k)))]*(5-k))
    g=2/3; lam=2/3; W=lam/5+g*np.outer(v,v); np.fill_diagonal(W,0)
    vals=original_terms(W,np.eye(5)-np.ones((5,5))/5-np.outer(v,v),lam)
    T=vals[:3].sum()-vals[3]
    print('NUMERICAL: endpoint split %d+%d, bracket %.12g, T %.12g'%(k,5-k,45*T/g,T))

# Construct G directly on the internal block spaces. This avoids inferring
# multiplicity from nearly repeated floating-point eigenvalues.
for q in [3,4]:
    for it in range(80):
        sizes=([1,2,2] if q==3 and it%4==0 else
               [1,1,3] if q==3 and it%4==1 else
               [int(x) for x in rng.integers(1,5,size=q)])
        n=sum(sizes)
        if n<5: continue
        off=np.cumsum([0]+sizes)
        blocks=[slice(off[i],off[i+1]) for i in range(q)]
        Hs=[np.eye(a)-np.ones((a,a))/a for a in sizes]
        G0=np.zeros((n,n)); E=np.zeros((n,n)); Pblock=np.zeros((n,n)); R=np.zeros((n,n))
        for i,(a,sl,H) in enumerate(zip(sizes,blocks,Hs)):
            Pblock[sl,sl]=np.ones((a,a))/a; R[sl,sl]=H
            raw=rng.uniform(0,1,size=(a,a)); raw=np.triu(raw,1); raw+=raw.T
            Li=np.diag(raw.sum(1))-raw
            if a>1: Li*=rng.uniform(0,.8)*(a/n)/max(np.linalg.eigvalsh(Li)[-1],1e-12)
            G0[sl,sl]=(a/n)*H-Li
        for i in range(q):
            for j in range(i):
                B=Hs[i]@rng.normal(size=(sizes[i],sizes[j]))@Hs[j]
                E[blocks[i],blocks[j]]=B; E[blocks[j],blocks[i]]=B.T
        scale=1.
        for shrink in range(100):
            G=G0+scale*E
            W=G+np.ones((n,n))/n; np.fill_diagonal(W,0)
            # Add identity on the kernel to test positivity just on U.
            if W.min()>-1e-12 and np.linalg.eigvalsh(G+Pblock)[0]>1e-7: break
            scale*=.7
        else: raise AssertionError('No feasible shrink')
        lam=2/((n-1)-np.trace(G)); G*=lam; W*=lam
        Pi=Pblock-np.ones((n,n))/n
        vals=original_terms(W,Pi,lam)
        T=vals[:3].sum()-vals[3]; assert T>-1e-10
        min_equitable=min(min_equitable,T); count+=1
        # Independently check the block expression for 2S5.
        ss=[np.trace(G[sl,sl]) for sl in blocks]
        Y=2*lam/n*sum((q-2+n/a)*sv for a,sv in zip(sizes,ss))
        Y-=4*sum((1/sizes[i]+1/sizes[j])*np.sum(G[blocks[i],blocks[j]]**2)
                 for i in range(q) for j in range(i))
        max_error=max(max_error,abs(Y-vals[3]))
print('NUMERICAL: %d equitable examples; minimum T %.12g'%(count,min_equitable))
print('NUMERICAL: maximum discrepancy, original pair definitions vs trace/block/bracket formulas: %.3g'%max_error)
print('NUMERICAL: elapsed seconds %.3f'%(time.monotonic()-start))
assert time.monotonic()-start<1200
