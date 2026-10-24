"""C005: reproducible exterior and decomposable entropy-Hessian experiments."""
from pathlib import Path
import json
import itertools as it
import numpy as np
from scipy.optimize import minimize

OUT = Path(__file__).resolve().parent

def subsets(n):
    return [np.array([i for i in range(n) if m >> i & 1], dtype=int) for m in range(1 << n)]

def exterior2(A):
    ij = np.array(list(it.combinations(range(len(A)), 2)))
    a,b=ij.T
    return A[a[:,None],a[None,:]]*A[b[:,None],b[None,:]]-A[a[:,None],b[None,:]]*A[b[:,None],a[None,:]]

def wedge(u,v):
    return np.array([u[i]*v[j]-u[j]*v[i] for i,j in it.combinations(range(len(u)),2)])

def atom_data(K):
    n=len(K)
    ans=[]
    for S in subsets(n):
        present=np.zeros(n,dtype=bool);present[S]=True
        Q=K-np.diag(1-present.astype(int))
        sign,ld=np.linalg.slogdet(Q)
        p=float(np.real(sign*(-1)**(n-len(S))))*np.exp(ld)
        if p <= 0: raise ValueError('Nonpositive atom')
        ans.append((p,np.linalg.inv(Q)))
    return ans

def logdet_table(L):
    return np.array([0. if not len(S) else -np.linalg.slogdet(L[np.ix_(S,S)])[1] for S in subsets(len(L))])

def operator(K, f=None):
    data=atom_data(K)
    p=np.array([a[0] for a in data])
    if f is None:
        L=np.linalg.solve(np.eye(len(K))-K,K)
        f=logdet_table(L)
    # Center out a modular function to reduce cancellation.
    ff=f.copy()-f[0]
    for m in range(len(ff)):
        ff[m]-=sum(f[1<<i]-f[0] for i in range(len(K)) if m>>i&1)
    T=sum(p0*fi*exterior2(Qi) for (p0,Qi),fi in zip(data,ff))
    return (T+T.conj().T)/2, p

def random_unitary(rng,n,complex_=False):
    Z=rng.normal(size=(n,n))
    if complex_:Z=Z+1j*rng.normal(size=(n,n))
    return np.linalg.qr(Z)[0]

def random_K(rng,n,complex_=False):
    U=random_unitary(rng,n,complex_)
    lam=rng.beta(.4,.4,size=n)*.999+.0005
    return (U*lam)@U.conj().T

def rank2_min(T,n,rng,trials=8,complex_=False):
    def decode(z):
        if complex_: z=z[:2*n]+1j*z[2*n:]
        Z=z.reshape(n,2)
        return np.linalg.qr(Z)[0]
    def objective(z):
        Q=decode(z);w=wedge(Q[:,0],Q[:,1])
        return np.vdot(w,T@w).real
    best=None
    for _ in range(trials):
        z=rng.normal(size=(4 if complex_ else 2)*n)
        res=minimize(objective,z,method='BFGS',options={'maxiter':120,'gtol':1e-8})
        if best is None or res.fun < best.fun: best=res
    return float(best.fun),decode(best.x)

def json_complex(x):
    x=np.asarray(x)
    return {'real':x.real.tolist(),'imag':x.imag.tolist()}

def main():
    rng=np.random.default_rng(5005)
    rec=[]
    for complex_ in [False,True]:
        n=6
        worst=(float('inf'),None,None)
        negative_count=0
        for k in range(80):
            K=random_K(rng,n,complex_)
            T,p=operator(K)
            eig=np.linalg.eigvalsh(T)
            if eig[0]<-1e-9:
                negative_count+=1
                q,U=rank2_min(T,n,rng,trials=2,complex_=complex_)
                if q<worst[0]:worst=(q,K,U)
            rec.append({'complex':complex_,'trial':k,'mineig_T':float(eig[0]),'maxeig_T':float(eig[-1])})
        print('complex',complex_,'negative exterior count',negative_count,'best decomposable value',worst[0],flush=True)
        if worst[1] is not None:
            np.savez(OUT/f'worst_physical_{complex_}.npz',q=worst[0],K=worst[1],U=worst[2])
    (OUT/'exterior_search_results.json').write_text(json.dumps(rec,indent=2))

if __name__=='__main__':main()
