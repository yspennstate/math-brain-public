"""Z2^3 flow enumeration and numerical smoothing test. No theorem claim."""
from collections import Counter
from pathlib import Path
import json
import numpy as np
from scipy.optimize import minimize


def flow_polynomial():
    edges=[(i,5+j) for i in range(5) for j in range(5) if (j-i)%5 in(0,1,4)]
    cycles=[]
    for mask in range(1<<15):
        degrees=[0]*10
        for i,(u,v) in enumerate(edges):
            if mask>>i&1:
                degrees[u]^=1; degrees[v]^=1
        if not any(degrees): cycles.append(mask)
    assert len(cycles)==64
    counts=Counter()
    for a in cycles:
        for b in cycles:
            for c in cycles:
                n=[0]*8
                for i in range(15): n[((a>>i)&1)+2*((b>>i)&1)+4*((c>>i)&1)]+=1
                counts[tuple(n)]+=1
    assert sum(counts.values())==64**3
    return edges,counts


def transfer_value_gradient(p):
    # Every derivative is with respect to p, with no normalization hidden.
    x,y=np.divmod(np.arange(64),8)
    k,l=x.copy(),y.copy()
    a=x[:,None]^y[:,None]
    b=x[:,None]^l[None,:]
    c=k[None,:]^y[:,None]
    T=p[a]*p[b]*p[c]
    T2=T@T; T4=T2@T2
    value=8**5*np.sum(T4.T*T)
    grad=np.zeros(8)
    for i in range(8):
        dT=(a==i)*p[b]*p[c]+(b==i)*p[a]*p[c]+(c==i)*p[a]*p[b]
        grad[i]=5*8**5*np.sum(T4.T*dT)
    return value,grad


def main():
    path=Path(__file__).with_suffix('.json')
    edges,F=flow_polynomial()
    print('flow terms',len(F),'flows',sum(F.values()),flush=True)
    out={'status':'exact flow polynomial; smoothing numerical only',
         'edges':edges,'flow_count':sum(F.values()),'Fourier_terms':len(F),
         'Fourier_polynomial':{','.join(map(str,a)):int(c) for a,c in sorted(F.items())}}
    path.write_text(json.dumps(out,indent=2))
    rng=np.random.default_rng(261003)
    perm=np.arange(8)^1
    def objective(z):
        zz=z-z.max(); p=np.exp(zz); p/=p.sum()
        q=(p+p[perm])/2
        v,g=transfer_value_gradient(p); w,h=transfer_value_gradient(q)
        raw=g-(h+h[perm])/2
        return v-w,p*(raw-p@raw)
    z=rng.normal(size=8)
    val,grad=objective(z)
    eps=1e-5
    fd=np.array([(objective(z+eps*np.eye(8)[i])[0]-objective(z-eps*np.eye(8)[i])[0])/(2*eps) for i in range(8)])
    out['finite_difference_gradient_max_error']=float(np.max(np.abs(fd-grad)))
    records=[]
    for i in range(80):
        z=rng.normal(size=8)*rng.choice([.2,1,3,8])
        result=minimize(objective,z,jac=True,method='L-BFGS-B',options={'maxiter':250,'ftol':1e-14,'gtol':1e-9})
        p=np.exp(result.x-result.x.max());p/=p.sum()
        records.append({'value':float(result.fun),'p':p.tolist(),'success':bool(result.success)})
        if i%10==0: print('trial',i,'best',min(t['value'] for t in records),flush=True)
        if result.fun < -1e-8: break
    out['smoothing_tests']=records
    out['minimum_smoothing_difference']=min(t['value'] for t in records)
    path.write_text(json.dumps(out,indent=2))
    print(json.dumps({k:v for k,v in out.items() if k not in ['edges','Fourier_polynomial','smoothing_tests']},indent=2))

if __name__=='__main__':main()
