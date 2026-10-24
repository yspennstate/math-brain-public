"""Finite self-checks of X043; the theorem is proved in agents/X043.md."""
from pathlib import Path
import itertools
import json
import numpy as np


def entropy(p):
    p=np.asarray(p,dtype=float)
    p=p[p>0]
    return float(-p@np.log(p))


def atoms(K):
    n=len(K);eye=np.eye(n);out=np.empty(1<<n)
    for mask in range(1<<n):
        keep=np.array([bool(mask>>i&1) for i in range(n)])
        value=np.linalg.det(np.where(keep[None,:],K,eye-K))
        assert abs(value.imag)<1e-11
        assert value.real>-1e-11
        out[mask]=max(0,value.real)
    assert abs(out.sum()-1)<1e-10
    return out


def splitter(P,K,t):
    C=np.sqrt(t*(1-t))*(K-P)
    return np.block([[(1-t)*P+t*K,C],[C,t*P+(1-t)*K]])


def main():
    rng=np.random.default_rng(202609150043)
    tmin=(1-np.sqrt(2/3))/2
    delta_star=np.log(128/125)/3
    sectors=[];max_identity_error=0.
    for m in [1,2,3,5,8]:
        Y=np.array(list(itertools.product([0.,1.],repeat=m)))
        Z=rng.normal(size=(m,m))+1j*rng.normal(size=(m,m))
        R=Z@Z.conj().T;R/=np.trace(R)
        a=R.diagonal().real
        for t in [tmin,.1,.25,.5,1-tmin]:
            v=t*(1-t);h=entropy([t,1-t]);kappa=1/v-3;c=kappa-3
            mu=t**Y.sum(axis=1)*(1-t)**(m-Y.sum(axis=1))
            z=(Y-t)/np.sqrt(v)
            F=np.einsum('ai,ij,aj->a',z,R,z).real
            q=mu*F
            exact4=1+(kappa-1)*(a@a)+4*sum(R[i,j].real**2 for i in range(m) for j in range(i+1,m))
            FlogF=np.where(F>0,F*np.log(np.maximum(F,1e-300)),0.)
            entropy_identity=(m-2)*h-np.log(v)-mu@FlogF
            max_identity_error=max(max_identity_error,abs(entropy(q)-entropy_identity),abs(mu@(F*F)-exact4))
            assert abs(q.sum()-1)<1e-12
            assert abs(q@Y.sum(axis=1)-(m*t+1-2*t))<1e-12
            assert abs(mu@(F*F)-exact4)<1e-11
            assert exact4<=3+c*(a@a)+1e-12
            assert entropy(a)+np.log(3+c*(a@a))<=np.log(3*m+c)+1e-12
            lower=h if m==1 else (m-2)*h-np.log1p(3*(m-2)*v)
            gain=entropy(q)-entropy(a)
            assert gain+1e-12>=lower
            assert h-np.log1p(3*v)>=delta_star-1e-12
            sectors.append(dict(m=m,t=t,input_entropy=entropy(a),output_entropy=entropy(q),gain=gain,lower=lower))
    reservoirs=[];max_chain_error=0.
    for n,t in [(2,.1),(3,tmin),(4,.25),(5,.8),(5,.5)]:
        u=rng.normal(size=n)+1j*rng.normal(size=n);u/=np.linalg.norm(u)
        P=np.outer(u,u.conj());a=abs(u)**2
        Z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
        U,_=np.linalg.qr(Z);K=(U*rng.uniform(.12,.87,n))@U.conj().T
        pk=atoms(K);full=atoms(splitter(P,K,t));v=t*(1-t);h=entropy([t,1-t]);delta=h-np.log1p(3*v)
        pt=atoms((1-t)*P+t*K);pr=atoms(t*P+(1-t)*K)
        ptable=full.reshape(1<<n,1<<n)
        margin_error=max(np.max(abs(ptable.sum(axis=0)-pt)),np.max(abs(ptable.sum(axis=1)-pr)))
        assert margin_error<1e-11
        gamma=pk[0]*h;count_excess=0.
        for mask,prob in enumerate(pk):
            T=[i for i in range(n) if mask>>i&1];r=len(T)
            if r>=2:
                gamma+=prob*((r-1)*h-(1-a[T].sum())*np.log1p(3*(r-1)*v))
                count_excess+=prob*(r-1)
        crude=pk[0]*h+delta*count_excess
        Hin=entropy(a)+entropy(pk);Hout=entropy(full)
        gain=Hout-Hin;I=entropy(pt)+entropy(pr)-Hout
        pair_gap=entropy(pt)+entropy(pr)-Hin
        assert gamma+1e-11>=crude
        assert gain+1e-11>=gamma
        assert pair_gap+1e-11>=gamma+I
        max_chain_error=max(max_chain_error,abs(pair_gap-gain-I))
        reservoirs.append(dict(n=n,t=t,commutator_norm=float(np.linalg.norm(P@K-K@P)),full_output_gain=gain,gamma=gamma,count_lower_bound=crude,mutual_information=I,symmetric_jensen_gap=pair_gap,marginal_error=margin_error))
    # The scalar auxiliary inequality is sharp in its c range for m=2.
    c=7.;epsilon=.001;a=np.array([.5+epsilon,.5-epsilon])
    auxiliary_violation=entropy(a)+np.log(3+c*(a@a))-np.log(6+c)
    assert auxiliary_violation>0
    result=dict(max_identity_error=max_identity_error,max_chain_error=max_chain_error,sector_checks=sectors,reservoir_checks=reservoirs,auxiliary_c7_violation=auxiliary_violation)
    Path(__file__).with_name('check-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['sector_checks','reservoir_checks']},indent=2))
    print('reservoir checks:',json.dumps(reservoirs,indent=2))

if __name__=='__main__':
    main()
