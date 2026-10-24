"""Checks the exact Rademacher formula for a rank-one/corank-one collision."""
from pathlib import Path
import itertools
import json
import numpy as np
from check import atoms, entropy, splitter


def xlogx(x):
    x=np.asarray(x)
    return np.where(x>0,x*np.log(np.maximum(x,1e-300)),0)


def run():
    rng=np.random.default_rng(202609150031)
    rows=[]
    for n in [2,3,4,5]:
        u=rng.normal(size=n)+1j*rng.normal(size=n)
        v=rng.normal(size=n)+1j*rng.normal(size=n)
        u/=np.linalg.norm(u)
        v/=np.linalg.norm(v)
        K0=np.outer(u,u.conj())
        K1=np.eye(n)-np.outer(v,v.conj())
        a=abs(u)**2;b=abs(v)**2;c=a*b
        signs=np.array(list(itertools.product([-1.,1.],repeat=n)))
        zz=abs(signs@(u*v.conj()))**2
        predicted=(n-2)*np.log(2)+np.sum(xlogx(4*c))/4-np.mean(xlogx(zz))
        # (4*c)*log(4*c)/4 equals c*log(4*c).
        actual=entropy(atoms(splitter(K0,K1)))-entropy(a)-entropy(b)
        midpoint=entropy(atoms((K0+K1)/2))-(entropy(a)+entropy(b))/2
        segment_errors=[]
        biased_entropy_errors=[]
        for t in [.17,.5,.83]:
            probs=atoms((1-t)*K0+t*K1)
            expected=[]
            for mask in range(1<<n):
                S=np.array([bool((mask>>i)&1) for i in range(n)])
                AS=a[S].sum();BS=b[S].sum()
                WS=(u*v.conj())[S].sum();W=np.sum(u*v.conj())
                mu=t**S.sum()*(1-t)**(n-S.sum())
                expected.append(mu*(AS*(1-BS)+abs(WS-t*W)**2)/(t*(1-t)))
            segment_errors.append(float(np.max(abs(probs-np.array(expected)))))
            bits=(signs+1)/2
            mu=t**bits.sum(axis=1)*(1-t)**(n-bits.sum(axis=1))
            yy=abs((bits-t)@(u*v.conj()))**2/(t*(1-t))
            ht=-t*np.log(t)-(1-t)*np.log(1-t)
            biased=(n-2)*ht+np.sum(xlogx(c))-c.sum()*np.log(t*(1-t))-np.sum(mu*xlogx(yy))
            actual_biased=entropy(atoms(splitter(K0,K1,t)))-entropy(a)-entropy(b)
            biased_entropy_errors.append(abs(float(biased)-actual_biased))
        rows.append(dict(n=n,predicted_full_gain=float(predicted),actual_full_gain=actual,
                         absolute_error=abs(actual-predicted),midpoint_gap=midpoint,
                         segment_atom_formula_max_error=max(segment_errors),
                         biased_entropy_formula_max_error=max(biased_entropy_errors),
                         proved_full_gain_lower_bound=float((n-2)*np.log(2)-n/(4*np.e))))
        assert abs(actual-predicted)<1e-10
    print(json.dumps(rows,indent=2))
    Path(__file__).with_name('rank-one-corank-one-results.json').write_text(json.dumps(rows,indent=2)+'\n')


if __name__=='__main__':
    run()
