"""Independent Fourier/noise routines. Truth-table bit x=1 means f(x)=-1."""
import os
os.environ.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1',MKL_NUM_THREADS='1')
import numpy as np
US=np.array([0,.25,.5,.75,.875,1.])
def pc(n):return np.array([s.bit_count() for s in range(1<<n)])
def fwht(f):
    a=np.asarray(f,dtype=float).copy();N=a.shape[-1]
    for h in (1<<np.arange(N.bit_length()-1)):
        b=a.reshape(*a.shape[:-1],-1,2*h);p=b[...,:h].copy();q=b[...,h:].copy()
        b[...,:h]=p+q;b[...,h:]=p-q
    return a/N

def noise_polys(mu,u):
    a=mu.copy();N=a.shape[-1]
    for i in range(N.bit_length()-1):
        h=1<<i;b=a.reshape(*a.shape[:-1],-1,2*h);b[...,:h]+=u*b[...,h:]
    return a

def derivative(f,S):
    a=np.asarray(f,dtype=float).copy();N=a.shape[-1];n=N.bit_length()-1
    for i in range(n):
        if S>>i&1:
            h=1<<i;b=a.reshape(*a.shape[:-1],-1,2*h);p=b[...,:h].copy();q=b[...,h:].copy()
            b[...,:h]=(p+q)/2;b[...,h:]=(p-q)/2
    return a[...,np.array([x for x in range(N) if x&S==S])]

def data(f,details=False):
    f=np.atleast_2d(f);n=f.shape[-1].bit_length()-1;c=pc(n);hat=fwht(f);mu=hat**2
    F=np.stack([noise_polys(mu,u) for u in US],axis=1)
    phi=-(mu[:,None,:]*np.log2(np.maximum(F,1e-300))).sum(axis=-1)
    I=(mu*c).sum(axis=-1);var=1-mu[:,0];A=phi[:,-1];B=phi[:,0]-A
    d=dict(mu=mu,hat=hat,F=F,phi=phi,I=I,var=var,A=A,B=B,pc=c)
    if details:
        alpha=np.stack([np.abs(derivative(f,s)).mean(axis=-1) for s in range(1<<n)],axis=-1)
        gamma=(mu*np.log2(np.maximum(alpha,1e-300)/np.maximum(np.abs(hat),1e-300))).sum(axis=-1)
        d.update(alpha=alpha,gamma=gamma)
    return d

def from_tt(tt,n):return 1-2*((np.asarray(tt,dtype=np.uint64)[:,None]>>np.arange(1<<n,dtype=np.uint64))&1).astype(np.int8)
def tt_hex(f):return hex(sum((int(x)<0)<<j for j,x in enumerate(f)))
def sample(n,k,seed):
    rng=np.random.default_rng(seed);F=1-2*rng.integers(0,2,(k,1<<n),dtype=np.int8)
    q=rng.uniform(.01,.5,(k//2,1));F[:k//2]=1-2*(rng.random((k//2,1<<n))<q)
    return F

def coupling(d):
    mu,up=d['mu'],d['F'][:,-1];N=mu.shape[-1];Z=np.zeros_like(mu)
    w=np.divide(mu,up,out=np.zeros_like(mu),where=up>0)
    Z=w.copy()
    for i in range(N.bit_length()-1):
        h=1<<i;b=Z.reshape(*Z.shape[:-1],-1,2*h);b[...,h:]+=b[...,:h]
    kl=(mu*Z*np.log2(np.maximum(Z,1e-300))).sum(axis=-1)
    C=d['B']+kl
    return Z,kl,C
