"""Reproduce exploratory pointwise and cumulative normalized-resolvent tests.

The exact certified rational witnesses are in the separate verify_* scripts.
"""
import json
from pathlib import Path
import numpy as np
from search_hessian import basis,atoms

def run(cumulative):
    rng=np.random.default_rng(318917 if cumulative else 99817)
    count=2500 if cumulative else 2000
    for n in [3,4,5]:
        E=basis(n);E=E[np.any(abs(E.imag)>0,axis=(1,2))]
        worst=1e10;rec=None;bits=(np.arange(2**n)[:,None]>>np.arange(n))&1
        for k in range(count):
            U=np.linalg.qr(rng.normal(size=(n,n)))[0]
            w=rng.uniform(.002,.998,n) if cumulative else rng.uniform(.005,.995,n)
            K=(U*w)@U.T;p,B=atoms(K);R=np.linalg.inv(B)
            RE=np.einsum('sij,ajk->saik',R,E)
            G=np.einsum('saij,sbji->sab',RE,RE).real
            d=np.diag(K);q=np.prod(np.where(bits,d,1-d),axis=1);r=p/q
            grid=[.001,.1,1,10,100] if cumulative else [0,.01,.1,1,10,100,1000]
            for s in grid:
                weights=p*np.log1p(s/r) if cumulative else p/(r+s)
                M=np.einsum('s,sab->ab',weights,G)
                val=float(np.linalg.eigvalsh(M)[0])
                if val<worst:worst=val;rec=dict(n=n,k=k,s=s,value=val,K=K.tolist())
            if worst < -1e-6:break
        name=f'cumulative_resolvent_n{n}.json' if cumulative else f'normalized_resolvent_failure_n{n}.json'
        if cumulative or worst < -1e-6:Path(name).write_text(json.dumps(rec,indent=2))
        print(json.dumps(dict(cumulative=cumulative,**rec)),flush=True)

if __name__=='__main__':
    run(False)
    run(True)
