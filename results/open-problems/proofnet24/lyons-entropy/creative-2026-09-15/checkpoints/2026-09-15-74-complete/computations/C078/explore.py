"""Finite diagnostics only; exact statements are proved in agents/C078.md."""
import numpy as np
from math import comb


def herm_basis(n):
    out=[]
    for i in range(n):
        b=np.zeros((n,n),complex);b[i,i]=1;out.append(b)
    for i in range(n):
        for j in range(i+1,n):
            b=np.zeros((n,n),complex);b[i,j]=b[j,i]=1;out.append(b)
            b=np.zeros((n,n),complex);b[i,j]=1j;b[j,i]=-1j;out.append(b)
    return np.array(out)


def jets(k):
    n=len(k); basis=herm_basis(n); atoms=[]; first=[]; second=[]
    for s in range(1<<n):
        q=k-np.diag([not (s>>i&1) for i in range(n)])
        p=((-1)**(n-s.bit_count())*np.linalg.det(q)).real
        qa=np.array([np.linalg.solve(q,a) for a in basis])
        tr=np.trace(qa,axis1=1,axis2=2).real
        h=p*(np.outer(tr,tr)-np.einsum('aij,bji->ab',qa,qa).real)
        atoms.append(p);first.append(p*tr);second.append(h)
    return np.array(atoms),np.array(first),np.array(second)


def hessians(k):
    p,v,a=jets(k);n=len(k)
    h=-np.einsum('si,sj,s->ij',v,v,1/p)-np.einsum('sij,s->ij',a,np.log(p))
    sizes=np.array([s.bit_count() for s in range(1<<n)])
    f=np.array([p[sizes==j].sum() for j in range(n+1)])
    fv=np.array([v[sizes==j].sum(axis=0) for j in range(n+1)])
    fa=np.array([a[sizes==j].sum(axis=0) for j in range(n+1)])
    env=-np.einsum('si,sj,s->ij',fv,fv,1/f)-np.einsum('sij,s->ij',fa,np.log(f/np.array([comb(n,j) for j in range(n+1)])))
    return h,env,env-h


if __name__=='__main__':
    rng=np.random.default_rng(78)
    best=0
    for z in range(1000):
        d=rng.uniform(.03,.97)
        off=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
        off=off+off.conj().T;np.fill_diagonal(off,0)
        off*=min(d,1-d)*rng.uniform(.05,.99)/max(abs(np.linalg.eigvalsh(off)))
        k=d*np.eye(3)+off
        h,e,de=hessians(k)
        cur=np.linalg.eigvalsh(de)[0]
        if cur<best:
            best=cur;print(z,best,d,k.tolist(),np.linalg.eigvalsh(h)[-1],flush=True)
    print('Worst deficit eigenvalue',best)
