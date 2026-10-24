import numpy as np,json,math
from scipy.linalg import eigh
from scipy.optimize import minimize
from pathlib import Path
out=Path(__file__).parent

def basis(n,complex_basis=True):
    E=[]
    for i in range(n):
        X=np.zeros((n,n),complex);X[i,i]=1;E.append(X)
    for i in range(n):
        for j in range(i):
            X=np.zeros((n,n),complex);X[i,j]=X[j,i]=1/np.sqrt(2);E.append(X)
            if complex_basis:
                X=np.zeros((n,n),complex);X[i,j]=1j/np.sqrt(2);X[j,i]=-1j/np.sqrt(2);E.append(X)
    return np.array(E)

def metric(K,B):
    n=len(K);d=len(B);g=np.zeros(d);G=np.zeros((d,d));H=0
    for mask in range(1<<n):
        b=np.array([(mask>>i)&1 for i in range(n)]);s=2*b-1
        M=K*s+np.diag(1-b);p=np.linalg.det(M).real
        if p<1e-15:return None
        R=np.linalg.solve(M,(B*s).transpose(1,0,2).reshape(n,-1)).reshape(n,d,n).transpose(1,0,2)
        v=np.einsum('aii->a',R).real
        T=np.einsum('aij,bji->ab',R,R).real
        logp=np.log(p);H-=p*logp;g-=p*v*logp
        G+=p*((1+logp)*np.outer(v,v)-logp*T)
    eig=eigh(G,eigvals_only=True)
    if eig[0]<=1e-12:return None
    A=np.linalg.solve(G,g);ratio=g@A
    return dict(ratio=ratio,H=H,least_curvature=eig[0],A=np.einsum('a,aij->ij',A,B))

rng=np.random.default_rng(3201);rows=[]
for n in [2,3,4,5]:
    B=basis(n);best=None
    for k in range(300 if n<4 else 70):
        U,_=np.linalg.qr(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))
        # wide range of occupancies and coherences
        lam=1/(1+np.exp(-rng.normal(size=n)*2.4))
        K=(U*lam)@U.conj().T
        r=metric(K,B)
        if r is not None and (best is None or r['ratio']>best['ratio']):best=dict(r,K=K,lam=lam)
    if best:
        np.savez(out/f'power_seed_{n}.npz',K=best['K'],A=best['A'])
        row={k:(float(v) if np.isscalar(v) else v.tolist()) for k,v in best.items() if k not in ['K','A']}
        row['n']=n;row['diagonal_cap']=n*.4392288398906452;rows.append(row);print(row,flush=True)
(out/'explore_power.json').write_text(json.dumps(rows,indent=2))
