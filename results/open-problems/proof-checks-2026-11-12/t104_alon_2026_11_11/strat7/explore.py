"""NUMERICAL discovery only. Run with one BLAS thread; results are not proofs."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key] = '1'
import json
import numpy as np
from terms import terms

rng = np.random.default_rng(131107)

def simple(m):
    a = rng.exponential(size=(m,m))
    a = np.triu(a,1)
    # Include sparse connected supports; a positive spanning path is retained.
    a *= rng.random((m,m)) < rng.uniform(.15,1)
    for i in range(m-1): a[i,i+1] = max(a[i,i+1],rng.exponential())
    a += a.T
    L = np.diag(a.sum(1))-a
    ev = np.linalg.eigvalsh(L)
    if ev[-1]-ev[-2] < 1e-8: return simple(m)
    return a/ev[-1]

def double(m):
    # Top eigenvalue 1 twice, all other positive eigenvalues strictly below 1.
    z = rng.normal(size=(m,m-3)); z -= z.mean(axis=0)
    u = np.linalg.qr(z)[0]
    g = rng.uniform(.00001,.99999,size=m-3)
    if rng.random()<.5: g = 1-10**rng.uniform(-6,-.05,size=m-3)
    G = (u*g)@u.T if m>3 else np.zeros((m,m))
    a = np.ones((m,m))/m + G
    np.fill_diagonal(a,0)
    if np.min(a)<-1e-12: return None
    return a

def assemble(part, carriers, both):
    W = np.zeros((6,6)); offset=0
    for k,m in enumerate(part):
        if m>1:
            a = double(m) if both and k==carriers[0] else simple(m)
            if a is None: return None
            if k not in carriers: a *= rng.uniform(.00001,.99999)
            W[offset:offset+m,offset:offset+m]=a
        offset+=m
    return W/W[np.triu_indices(6,1)].sum()

def main(count=3000):
    parts=[(5,1),(4,2),(4,1,1),(3,3),(3,2,1),(3,1,1,1),(2,2,2),(2,2,1,1)]
    records=[]
    for part in parts:
        modes=[]
        for i,m in enumerate(part):
            if m>=3: modes.append(((i,),True))
        for i,m in enumerate(part):
            for j in range(i+1,len(part)):
                if part[j]>1: modes.append(((i,j),False))
        for carriers,both in modes:
            best=None; valid=0
            for trial in range(count):
                W=assemble(part,carriers,both)
                if W is None: continue
                D,x1,x2,x3,y=terms(W)
                if D!=2: continue
                den=x1+x2+x3
                if den<=1e-13: continue
                valid+=1; T=den-y; q=T/den
                if best is None or q<best['quotient']:
                    best=dict(quotient=q,T=T,terms=[x1,x2,x3,y],W=W.tolist())
                if T < -1e-9:
                    rec=dict(part=part,carriers=carriers,both=both,valid=valid,best=best)
                    records.append(rec)
                    with open('numerical.json','w') as f:json.dump(records,f,indent=2)
                    print('NUMERICAL NEGATIVE',rec,flush=True)
                    return
            rec=dict(part=part,carriers=carriers,both=both,valid=valid,best=best)
            records.append(rec)
            print('NUMERICAL',part,carriers,'both' if both else 'split',valid,None if best is None else best['quotient'],flush=True)
            with open('numerical.json','w') as f:json.dump(records,f,indent=2)
if __name__=='__main__':main()
