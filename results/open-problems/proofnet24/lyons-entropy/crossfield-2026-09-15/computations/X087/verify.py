"""Finite consistency checks for X087; the uniform theorems are analytic."""
import json
from pathlib import Path
import numpy as np


def one_case(z, ell):
    n=len(z); z=np.array(z,complex); ell=np.array(ell,float)
    x=z.real
    L=2*np.sqrt(np.outer(ell*x,ell*x))/(z[:,None]+z.conj()[None,:])
    K=np.linalg.solve(np.eye(n)+L,L)
    C=np.zeros((n,n))
    for i in range(n):
        for j in range(i):
            C[i,j]=C[j,i]=np.log(abs(z[i]+z[j].conjugate())**2/abs(z[i]-z[j])**2)
    basis=[]
    for i in range(n):
        A=np.zeros((n,n),complex); A[i,i]=1; basis.append(A)
    for i in range(n):
        for j in range(i):
            A=np.zeros((n,n),complex); A[i,j]=A[j,i]=1; basis.append(A)
            A=np.zeros((n,n),complex); A[i,j]=1j; A[j,i]=-1j; basis.append(A)
    basis=np.array(basis)
    P=[]; Q=[]; invs=[]; signs=[]
    max_pair_log_error=0.0
    for mask in range(1<<n):
        sig=np.array([1 if mask>>i&1 else -1 for i in range(n)])
        inds=[i for i in range(n) if mask>>i&1]
        M=np.where(sig[None,:]>0,K,np.eye(n)-K)
        inv=np.linalg.inv(M)
        p=np.linalg.det(M).real
        q=p*np.array([np.trace(inv@(A*sig[None,:])).real for A in basis])
        log_weight=sum(np.log(ell[i]) for i in inds)-sum(C[i,j] for j in inds for i in inds if i<j)
        expected_log=log_weight-np.linalg.slogdet(np.eye(n)+L)[1]
        max_pair_log_error=max(max_pair_log_error,abs(np.log(p)-expected_log))
        P.append(p); Q.append(q); invs.append(inv); signs.append(sig)
    P=np.array(P); Q=np.array(Q)
    FI=Q.T@(Q/P[:,None])
    G=FI.copy(); G[:n,:n]-=C
    k=n
    for i in range(n):
        for j in range(i):
            G[k,k]+=2*C[i,j]; G[k+1,k+1]+=2*C[i,j]; k+=2
    chi=K.diagonal().real*(1-K.diagonal().real)
    w=abs(K)**2; np.fill_diagonal(w,0)
    D=chi+w.sum(axis=1)
    S=np.diag(chi)-w
    d=1-2*D
    errs=[]
    for t in range(4):
        coeff=np.array([np.sin((k+1)*(t+2))+.3*np.cos((k+2)*(t+1)) for k in range(n*n)])
        A=np.einsum('k,kij->ij',coeff,basis); v=A.diagonal().real
        q=Q@coeff; score=q/P
        features=np.array([[int(mask>>i&1)-K[i,i].real for i in range(n)] for mask in range(1<<n)])
        information=np.dot(q,q/P)
        right=np.dot(P,(score-2*features@v)**2)+2*np.dot(d,v*v)+4*sum(w[i,j]*(v[i]+v[j])**2 for i in range(n) for j in range(i))
        err1=abs(information-2*np.dot(v,v)-right)
        u=v/D
        right2=np.dot(P,(score-features@u)**2)+sum(w[i,j]*(u[i]+u[j])**2 for i in range(n) for j in range(i))
        err2=abs(information-np.dot(v,u)-right2)
        acceleration=0.0
        for p,inv,sig in zip(P,invs,signs):
            R=inv@(A*sig[None,:])
            pp=p*(np.trace(R)**2-np.trace(R@R)).real
            acceleration+=pp*np.log(p)
        direct=information+acceleration
        err3=abs(direct-coeff@G@coeff)
        errs.append([err1,err2,err3])
    return {
        'n':n,'min_probability':float(min(P)),
        'max_pair_log_error':max_pair_log_error,
        'maximum_identity_errors':np.max(errs,axis=0).tolist(),
        'max_interaction_row':float(max(C.sum(axis=1))),
        'interaction_spectral_radius':float(np.linalg.eigvalsh(C)[-1]),
        'weighted_interaction_top_eigenvalue':float(np.linalg.eigvalsh(np.sqrt(D[:,None]*D[None,:])*C)[-1]),
        'minimum_negative_entropy_hessian_eigenvalue':float(np.linalg.eigvalsh(G)[0]),
        'kernel_eigenvalues':np.linalg.eigvalsh(K).tolist(),
    }

cases={
    'vertical_unit_fields':one_case([1+3j*i for i in range(6)],[1]*6),
    'vertical_unequal_fields':one_case([1+2.5j*i for i in range(6)],[.1,.3,1,2,5,13]),
    'geometric_complex':one_case([6**i+1j*((i*i)%7) for i in range(6)],[.2,.5,1,2,5,10]),
}
for r in cases.values():
    assert r['max_pair_log_error']<1e-10
    assert max(r['maximum_identity_errors'])<1e-8
    assert r['minimum_negative_entropy_hessian_eigenvalue']>0
out=Path(__file__).with_name('verification.json')
out.write_text(json.dumps(cases,indent=2)+'\n')
print(json.dumps(cases,indent=2))
