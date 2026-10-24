"""Finite checks of a candidate conditional Lorentz cone cover."""
import numpy as np
from explore import data,BASIS
from conditional_geometry import matrices
from pathlib import Path
import json

def adj(A):
    return A@A-np.trace(A)*A+0.5*(np.trace(A)**2-np.trace(A@A))*np.eye(3)

def run():
    rng=np.random.default_rng(661006)
    worst=(-1,None)
    positives=0
    for case in range(40):
        while True:
            xyz=1/(1+np.exp(-rng.normal(size=3)*2))
            x,y,z=xyz
            cc=(x*y+x*z+y*z-x*y*z)/(2*np.sqrt(x*y*z))
            if cc<1:break
        a,b,c=np.sqrt(xyz);ell=np.exp(rng.normal(size=3)*2)
        R=np.array([[1,a,c*np.exp(-1j*np.arccos(cc))],[a,1,b],[c*np.exp(1j*np.arccos(cc)),b,1]])
        L=np.sqrt(ell[:,None]*ell[None,:])*R
        K=np.linalg.solve(np.eye(3)+L,L);d=data(K);Ns,_=matrices(K,d)
        for _ in range(800):
            v=rng.normal(size=9);A=sum(q*B for q,B in zip(v,BASIS));Ad=adj(A)
            q=np.trace(d['M']@Ad).real
            if q<=0:continue
            positives+=1
            qs=[np.trace(N@Ad).real for N in Ns]
            denom=sum(max(r,0) for r in qs)
            rat=q/denom if denom>0 else np.inf
            if rat>worst[0]:worst=(rat,dict(K=str(K),A=str(A),q=q,qs=qs,c=d['c'].tolist(),tau=d['tau']))
    out={'positive_directions':positives,'worst_ratio':float(worst[0]) if np.isfinite(worst[0]) else None,'zero_denominator_with_positive_numerator':bool(np.isinf(worst[0])),'witness':worst[1]}
    Path(__file__).with_name('cone_cover_results.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))

if __name__=='__main__':run()
