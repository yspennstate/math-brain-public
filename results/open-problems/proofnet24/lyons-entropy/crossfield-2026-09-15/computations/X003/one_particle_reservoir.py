"""Self-checks the all-reservoir one-particle midpoint theorem and its gap."""
from pathlib import Path
import itertools
import json
import numpy as np
from check import atoms, entropy, splitter


def main():
    rng=np.random.default_rng(202609150032)
    rows=[]
    for n in [1,2,3,4,5]:
        u=rng.normal(size=n)+1j*rng.normal(size=n)
        u/=np.linalg.norm(u)
        P=np.outer(u,u.conj())
        Z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
        U,_=np.linalg.qr(Z)
        vals=rng.uniform(.1,.9,size=n)
        K=(U*vals)@U.conj().T
        p=atoms(K);a=abs(u)**2
        gamma=0.
        for mask,prob in enumerate(p):
            T=np.array([bool((mask>>i)&1) for i in range(n)])
            r=int(T.sum());at=float(a[T].sum())
            gamma+=prob*(at*(r-1)*np.log(2)+(1-at)*np.log(2.**(r+1)/(3*r+1)))
        gain=entropy(atoms(splitter(P,K)))-entropy(a)-entropy(p)
        midpoint=entropy(atoms((P+K)/2))-(entropy(a)+entropy(p))/2
        assert gain+1e-10>=gamma
        assert midpoint+1e-10>=gamma/2
        rows.append(dict(n=n,full_output_gain=gain,gamma_lower_bound=gamma,midpoint_gap=midpoint))
    sector_rows=[]
    for m in [1,2,3,4,5,6]:
        Z=rng.normal(size=(m,m))+1j*rng.normal(size=(m,m))
        R=Z@Z.conj().T;R/=np.trace(R)
        signs=np.array(list(itertools.product([-1.,1.],repeat=m)))
        F=np.einsum('ai,ij,aj->a',signs,R,signs).real
        q=F/2**m
        fourth_exact=1+4*sum(R[i,j].real**2 for i in range(m) for j in range(i+1,m))
        bound=m*np.log(2)-np.log(3-2/m)
        assert abs(np.mean(F**2)-fourth_exact)<1e-10
        assert entropy(q)+1e-10>=bound
        sector_rows.append(dict(m=m,output_entropy=entropy(q),proved_lower_bound=bound,
                                input_entropy=entropy(R.diagonal().real)))
    result=dict(reservoirs=rows,single_excitation_sectors=sector_rows)
    print(json.dumps(result,indent=2))
    Path(__file__).with_name('one-particle-reservoir-results.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':
    main()
