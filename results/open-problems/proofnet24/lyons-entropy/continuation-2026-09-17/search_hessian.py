"""Full measured DPP entropy Hessian. Floating point exploration, never proof."""
import argparse, json, time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize

def basis(n):
    out=[]
    for i in range(n):
        a=np.zeros((n,n),complex); a[i,i]=1; out.append(a)
    for i in range(n):
        for j in range(i):
            a=np.zeros((n,n),complex); a[i,j]=a[j,i]=1/np.sqrt(2); out.append(a)
            a=np.zeros((n,n),complex); a[i,j]=1j/np.sqrt(2); a[j,i]=-1j/np.sqrt(2); out.append(a)
    return np.array(out)

def atoms(K):
    n=len(K); masks=np.arange(2**n)
    bits=(masks[:,None]>>np.arange(n))&1
    B=np.tile(K,(2**n,1,1)); B[:,np.arange(n),np.arange(n)]-=1-bits
    p=np.linalg.det(B).real*(-1.)**(n-bits.sum(1))
    return p,B

def curvature(K, E=None):
    if E is None: E=basis(len(K))
    p,B=atoms(K)
    if p.min()<=0: raise ValueError('nonpositive numerical atom')
    R=np.linalg.inv(B)
    RE=np.einsum('sij,ajk->saik',R,E,optimize=True)
    t=np.trace(RE,axis1=2,axis2=3).real
    tt=np.einsum('sa,sb->sab',t,t)
    tr=np.einsum('saij,sbji->sab',RE,RE,optimize=True).real
    Q=np.einsum('s,sab->ab',p,tt)+np.einsum('s,sab->ab',p*np.log(p),tt-tr)
    return (Q+Q.T)/2,p

def entropy(K):
    p,_=atoms(K)
    return -np.dot(p,np.log(p))

def sample(rng,n,mode):
    if mode in (0,1,2):
        Z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
        U=np.linalg.qr(Z)[0]
        if mode==0: w=rng.uniform(.03,.97,n)
        else:
            eps=10**rng.uniform(-6,-1,n)
            w=np.where(rng.random(n)<.5,eps,1-eps)
            if mode==2: w[rng.integers(n)]=rng.uniform(.05,.95)
        return (U*w)@U.conj().T
    Z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
    Z=(Z+Z.conj().T)/2; np.fill_diagonal(Z,0)
    if mode==3:
        keep=rng.random((n,n))<.4;keep=np.triu(keep,1);keep=keep|keep.T;Z*=keep
    if mode==4:
        keep=np.zeros((n,n));h=n//2;keep[:h,h:]=1;keep[h:,:h]=1;Z*=keep
    scale=max(abs(np.linalg.eigvalsh(Z)))
    if scale==0: return np.eye(n)/2
    return np.eye(n)/2+Z/scale*rng.uniform(.02,.4999)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--n',type=int,default=4);ap.add_argument('--count',type=int,default=2000);ap.add_argument('--seed',type=int,default=170926);ap.add_argument('--output',default='search.json');a=ap.parse_args()
    rng=np.random.default_rng(a.seed);E=basis(a.n);best=1e100;records=[];start=time.time();checked=0;rejected=0
    # Independent finite differences check the sign and full acceleration term.
    K=sample(rng,a.n,0);Q,p=curvature(K,E);v=rng.normal(size=a.n*a.n);v/=np.linalg.norm(v);A=np.einsum('a,aij->ij',v,E);h=1e-4
    fd=-(entropy(K+h*A)-2*entropy(K)+entropy(K-h*A))/h**2
    exact=float(v@Q@v);assert abs(fd-exact)<2e-5,(fd,exact)
    for k in range(a.count):
        mode=k%5;K=sample(rng,a.n,mode)
        try: Q,p=curvature(K,E)
        except (ValueError,np.linalg.LinAlgError):rejected+=1;continue
        checked+=1;w,V=np.linalg.eigh(Q);val=float(w[0])
        if val<best:
            best=val;vec=V[:,0];A=np.einsum('a,aij->ij',vec,E)
            rec=dict(k=k,mode=mode,min_curvature=val,atom_min=float(p.min()),kernel_eigenvalues=np.linalg.eigvalsh(K).tolist(),K_real=K.real.tolist(),K_imag=K.imag.tolist(),A_real=A.real.tolist(),A_imag=A.imag.tolist())
            records.append(rec)
            Path(a.output).write_text(json.dumps(dict(n=a.n,seed=a.seed,checked=checked,rejected=rejected,finite_difference=[fd,exact],records=records,elapsed=time.time()-start),indent=2))
        if k%250==0: print(json.dumps(dict(k=k,best=best,elapsed=time.time()-start)),flush=True)
    Path(a.output).write_text(json.dumps(dict(n=a.n,seed=a.seed,checked=checked,rejected=rejected,finite_difference=[fd,exact],records=records,elapsed=time.time()-start),indent=2))
    print(json.dumps(dict(n=a.n,checked=checked,rejected=rejected,best=best,elapsed=time.time()-start)),flush=True)

if __name__=='__main__': main()
