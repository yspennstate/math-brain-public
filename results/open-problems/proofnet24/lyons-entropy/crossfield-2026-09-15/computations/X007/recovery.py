"""Finite, reproducible checks of the Petz/compound/BKM identities.
No finite numerical sample certifies universal concavity.
"""
import itertools,json
from pathlib import Path
import numpy as np
from scipy.linalg import eigh


def subsets(n):
    return [tuple(i for i in range(n) if (s>>i)&1) for s in range(1<<n)]

def spectral(a, fun):
    v,u=eigh(a)
    return (u*fun(v))@u.conj().T

def gamma(a):
    ss=subsets(len(a)); out=np.zeros((len(ss),len(ss)),complex)
    for i,s in enumerate(ss):
        for j,t in enumerate(ss):
            if len(s)==len(t): out[i,j]=np.linalg.det(a[np.ix_(s,t)]) if s else 1
    return out

def compound(a,r):
    ss=list(itertools.combinations(range(len(a)),r))
    return np.array([[np.linalg.det(a[np.ix_(s,t)]) for t in ss] for s in ss])

def rho(k):
    eye=np.eye(len(k)); L=np.linalg.solve(eye-k,k)
    return np.linalg.det(eye-k).real*gamma(L)

def atoms(k):
    return np.diag(rho(k)).real

def frechet(a,e,fun,der):
    d,u=eigh(a); z=u.conj().T@e@u
    f=fun(d); dd=d[:,None]-d[None,:]
    out=np.empty_like(dd)
    mask=np.abs(dd)>1e-10
    out[mask]=((f[:,None]-f[None,:])[mask])/dd[mask]
    out[~mask]=np.broadcast_to(der(d)[:,None],dd.shape)[~mask]
    return u@(out*z)@u.conj().T

def dlogit(k,a):
    return frechet(k,a,lambda x:np.log(x/(1-x)),lambda x:1/x/(1-x))

def annihilators(n):
    out=[]
    for i in range(n):
        a=np.zeros((1<<n,1<<n),complex)
        for s in range(1<<n):
            if (s>>i)&1: a[s^(1<<i),s]=(-1)**((s&((1<<i)-1)).bit_count())
        out.append(a)
    return out

def onebody(h,aa):
    return sum(h[i,j]*aa[i].conj().T@aa[j] for i in range(len(h)) for j in range(len(h)))

def twobody(w,aa):
    pair=list(itertools.combinations(range(len(aa)),2)); out=np.zeros_like(aa[0])
    for a,(i,j) in enumerate(pair):
        for b,(k,l) in enumerate(pair):
            out+=w[a,b]*aa[i].conj().T@aa[j].conj().T@aa[l]@aa[k]
    return out

def covariance(tau,aa):
    return np.array([[np.trace(tau@aa[j].conj().T@aa[i]) for j in range(len(aa))] for i in range(len(aa))])

def rdm2(tau,aa):
    pair=list(itertools.combinations(range(len(aa)),2))
    return np.array([[np.trace(tau@aa[k].conj().T@aa[l].conj().T@aa[j]@aa[i]) for k,l in pair] for i,j in pair])

def metric(r,x):
    return np.trace(x@frechet(r,x,np.log,lambda x:1/x)).real

def omega(r,q):
    v,u=eigh(r); z=u.conj().T@q@u
    ld=np.log(v); den=ld[:,None]-ld[None,:]; nums=v[:,None]-v[None,:]
    factors=np.empty_like(den); mask=np.abs(den)>1e-10
    factors[mask]=nums[mask]/den[mask]
    factors[~mask]=np.broadcast_to(v[:,None],den.shape)[~mask]
    return u@(factors*z)@u.conj().T

def drho(k,v,aa,r):
    h=dlogit(k,v)
    q=onebody(h,aa)-np.trace(k@h)*np.eye(len(r))
    return omega(r,q)

def check(k,a):
    n=len(k); ss=subsets(n); aa=annihilators(n); r=rho(k); p=np.diag(r).real
    eye=np.eye(n); L=np.linalg.solve(eye-k,k); Lh=spectral(L,np.sqrt)
    Mh=spectral(k@(eye-k),lambda z:1/np.sqrt(z)); B=Mh@a@Mh
    pis=[]; gs=[]
    for s in ss:
        pi=Lh[:,s]@np.linalg.inv(L[np.ix_(s,s)])@Lh[s,:] if s else np.zeros_like(k)
        pis.append(pi); gs.append(np.linalg.inv(k-np.diag([i not in s for i in range(n)])))
    pis=np.array(pis); f=np.log(p)-p@np.log(p); sr=spectral(r,np.sqrt)
    tau=sr@np.diag(f)@sr; vf=np.einsum('s,sij->ij',p*f,pis); tangent=drho(k,vf,aa,r); eta=tau-tangent
    c2=sum(p[s]*f[s]*compound(pis[s]-k,2) for s in range(len(ss)))
    g=np.array([np.trace(z@a).real for z in gs]); h=np.array([g[s]**2-np.trace(gs[s]@a@gs[s]@a).real for s in range(len(ss))])
    FI=p@(g*g); acc=p@(h*np.log(p)); correction=2*np.trace(c2@compound(B,2)).real
    Q=2*twobody(compound(B,2),aa); Qc=Q-np.trace(r@Q)*np.eye(len(r))
    VQ=covariance(omega(r,Qc),aa); hQ=dlogit(k,VQ)
    Qp=Qc-onebody(hQ,aa)+np.trace(k@hQ)*np.eye(len(r))
    chi=np.trace(Qp@omega(r,Qp)).real
    wick_variance=4*np.trace(compound(k,2)@compound(B,2)@compound(eye-k,2)@compound(B,2)).real
    features=np.array([[1]+[int(i in s) for i in range(n)] for s in ss])
    beta=np.linalg.lstsq(features*np.sqrt(p)[:,None],np.log(p)*np.sqrt(p),rcond=None)[0]
    f_interaction=np.log(p)-features@beta
    interaction_variance=float(p@(f_interaction*f_interaction))
    eta_norm=metric(r,eta); eta_upper=p@(f*f)-np.trace(vf@dlogit(k,vf)).real
    chain=np.abs(sr)**2/p[None,:]
    chain_f=(chain@(p*f))/p
    chain_dirichlet=float(p@(f*(f-chain_f)))
    modular_remainder=float(p@(f*chain_f)-metric(r,tau))
    chain_bound=eta_upper-chain_dirichlet
    errs={
       'rho_trace':abs(np.trace(r)-1),
       'petz_recovery':np.linalg.norm(sr@np.diag(p/p)@sr-r),
       'projection':max(np.linalg.norm(pi@pi-pi) for pi in pis),
       'resolvent':max(np.linalg.norm(gs[s]-Mh@(pis[s]-k)@Mh) for s in range(len(ss))),
       'compound_moments':max(np.linalg.norm(sum(p[s]*compound(pis[s],j) for s in range(len(ss)))-compound(k,j)) for j in range(1,n+1)),
       'eta_covariance':np.linalg.norm(covariance(eta,aa)),
       'eta_rdm2':np.linalg.norm(rdm2(eta,aa)-c2),
       'acceleration_pairing':abs(acc-correction),
       'fock_pairing':abs(np.trace(eta@Q).real-correction),
       'bkm_orthogonality':abs(np.trace(eta@frechet(r,tangent,np.log,lambda x:1/x))),
       'observable_orthogonality':np.linalg.norm(covariance(omega(r,Qp),aa)),
       'bkm_pythagoras':abs(metric(r,tau)-metric(r,tangent)-eta_norm),
       'chain_stochastic':np.max(np.abs(chain.sum(axis=0)-1)),
       'chain_stationary':np.linalg.norm(chain@p-p),
       'chain_detailed_balance':np.linalg.norm(chain*p[None,:]-(chain*p[None,:]).T),
       'dirichlet_modular_identity':abs(eta_norm-(eta_upper-chain_dirichlet-modular_remainder)),
       'wick_variance':abs(np.trace(r@Qp@Qp).real-wick_variance),
    }
    result={'n':n,'eig_K':eigh(k,eigvals_only=True).tolist(),'eig_A':eigh(a,eigvals_only=True).tolist(),'errors':{x:float(y) for x,y in errs.items()},'FI':float(FI),'acceleration':float(acc),'minus_H_second':float(FI+acc),'eta_BKM_squared':float(eta_norm),'eta_BKM_upper':float(eta_upper),'eta_BKM_chain_upper':float(chain_bound),'two_body_dual_residual':float(chi),'recovery_certificate_exact':float(FI-np.sqrt(max(0,eta_norm*chi))),'recovery_certificate_upper':float(FI-np.sqrt(max(0,eta_upper*chi))),'recovery_certificate_chain':float(FI-np.sqrt(max(0,chain_bound*chi))),'C2_eigenvalues':eigh(c2,eigvals_only=True).tolist(),'recovery_metric_loss':float(p@(f*f)-metric(r,tau)),'chain_dirichlet_f':chain_dirichlet,'modular_remainder':modular_remainder}
    result.update(interaction_variance=interaction_variance,wick_variance=float(wick_variance),modular_wick_certificate=float(FI-np.sqrt(interaction_variance*wick_variance)))
    assert max(errs.values())<1e-8,errs
    assert eta_norm<=eta_upper+1e-8
    assert chain_dirichlet>=-1e-10 and modular_remainder>=-1e-10
    assert abs(correction)<=np.sqrt(max(0,eta_norm*chi))+1e-8
    assert eta_norm<=interaction_variance+1e-10
    return result


def main():
    k=np.array([[.31,.075,.024j,.017],[.075,.47,-.043,.028j],[-.024j,-.043,.58,.061],[.017,-.028j,.061,.71]],complex)
    a=np.array([[.21,.035j,.015,-.026],[-.035j,-.14,.02j,.01],[.015,-.02j,.17,-.023],[-.026,.01,-.023,-.11]],complex)
    b=np.array([[0,.035j,.015,-.026],[-.035j,0,.02j,.01],[.015,-.02j,0,-.023],[-.026,.01,-.023,0]],complex)
    checks={'full_rank_direction':check(k,a),'zero_diagonal_direction':check(k,b)}
    Path(__file__).with_name('results.json').write_text(json.dumps(checks,indent=2))
    print(json.dumps(checks,indent=2))

if __name__=='__main__': main()
