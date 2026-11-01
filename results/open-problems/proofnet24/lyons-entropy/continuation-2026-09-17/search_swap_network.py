"""Independent transposition coins; a stronger structural test than arbitrary shuffles."""
import json,time
from pathlib import Path
import numpy as np
from search_shuffle import data,curv

def network(n,swaps):
    bits=data(n);C=np.eye(2**n)
    for i,j,w in swaps:
        perm=np.arange(n);perm[i],perm[j]=perm[j],perm[i]
        to=(bits[:,perm]@(2**np.arange(n))).astype(int)
        C=(1-w)*C+w*C[to]
    return C

def main():
    rng=np.random.default_rng(260917);out=[];start=time.time()
    for n,count in [(4,3000),(5,3000),(6,1000),(8,100)]:
        bits=data(n);best=1e10;rec=None
        for k in range(count):
            m=int(rng.integers(2,3*n));swaps=[]
            for _ in range(m):
                i,j=rng.choice(n,2,replace=False);w=.5 if k%2==0 else rng.uniform(.01,.99)
                swaps.append((int(i),int(j),float(w)))
            C=network(n,swaps);p=1/(1+np.exp(rng.uniform(-6,6,n)))
            Q=curv(p,C,bits);ev,V=np.linalg.eigh(Q)
            if ev[0]<best:
                best=float(ev[0]);rec=dict(n=n,k=k,count_attempted=k+1,p=p.tolist(),swaps=swaps,min_curvature=best,direction=V[:,0].tolist())
            if best < -1e-6:break
        rec['count_attempted']=k+1;out.append(rec)
        Path('swap_network_search.json').write_text(json.dumps(dict(records=out,elapsed=time.time()-start),indent=2));print(json.dumps(rec),flush=True)

if __name__=='__main__':main()
