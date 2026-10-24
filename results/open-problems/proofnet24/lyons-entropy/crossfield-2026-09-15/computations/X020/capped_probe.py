"""Bounded spectral self-check of the capped Hall lemma at fixed two-planes.

This is not a universal proof. It enumerates the 2^20 triple families for a
fixed rationally specified U, evaluating the exact spectral reduction in X020.
"""
import itertools
import json
from pathlib import Path
import numpy as np

E=range(6)
PAIRS=list(itertools.combinations(E,2))
TRIPLES=list(itertools.combinations(E,3))
INC=np.array([[set(p)<=set(m) for p in PAIRS] for m in TRIPLES],dtype=int)

def reflector(v):
    v=np.array(v,dtype=float)
    return np.eye(6)-2*np.outer(v,v)/(v@v)

def frame():
    return reflector([1,2,3,4,5,6])@reflector([2,-1,3,-2,1,4])@reflector([3,1,-2,4,2,-1])

def probe(Q):
    U=Q[:,:2]; V=Q[:,2:]
    h=np.array([abs(np.linalg.det(U[list(p)]))**2 for p in PAIRS])
    T=np.array([[np.linalg.det(np.column_stack((U,V[:,s]))[list(m)]) for s in range(4)] for m in TRIPLES])
    effects=np.einsum('mi,mj->mij',T.conj(),T)
    worst={'gap':1.0}
    counts={}
    for start in range(0,1<<20,8192):
        masks=np.arange(start,min(start+8192,1<<20),dtype=np.uint32)
        bits=((masks[:,None]>>np.arange(20))&1).astype(float)
        B=np.einsum('bm,mij->bij',bits,effects)
        eig=np.linalg.eigvalsh(B)
        d=bits@INC
        cap=np.minimum(d,2)@h
        gap=cap-eig[:,2:].sum(axis=1)
        k=int(np.argmin(gap))
        if gap[k]<worst['gap']:
            mask=int(masks[k]); F=[TRIPLES[i] for i in range(20) if mask>>i&1]
            worst={'gap':float(gap[k]),'mask':mask,'family':F,'eigenvalues':eig[k].tolist(),'capacity':float(cap[k]),'degrees':d[k].astype(int).tolist()}
        counts['violations']=counts.get('violations',0)+int(np.sum(gap < -1e-9))
    return {'orthogonality_error':float(np.linalg.norm(Q.T@Q-np.eye(6))),'T_isometry_error':float(np.linalg.norm(T.conj().T@T-np.eye(4))),'pair_law':h.tolist(),'worst':worst,**counts}

if __name__=='__main__':
    out=probe(frame())
    print(json.dumps(out,indent=2))
    Path(__file__).with_name('capped_probe_output.json').write_text(json.dumps(out,indent=2)+'\n')
