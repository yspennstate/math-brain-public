"""Finite DPP entropy, full real Hessian, and high precision verification.

Every probability is enumerated; this is exact enumeration with floating point
arithmetic, not exact arithmetic. MP routines offer arbitrary precision checks.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[name]='1'
from pathlib import Path
import ctypes
import numpy as np
import mpmath as mp

ROOT=Path(__file__).resolve().parent
LIB=ctypes.CDLL(str(ROOT/'libdpp.dylib'))
LIB.dpp_stats.argtypes=[ctypes.c_int]+[ctypes.POINTER(ctypes.c_double)]*3
LIB.dpp_stats.restype=ctypes.c_int

def stats(q,a=None):
    q=np.ascontiguousarray(q,dtype=np.complex128)
    a=np.ascontiguousarray(np.zeros_like(q) if a is None else a,dtype=np.complex128)
    if not np.isfinite(q).all() or not np.isfinite(a).all():raise ArithmeticError('nonfinite input')
    if np.max(np.abs(q-q.conj().T))>1e-12 or np.max(np.abs(a-a.conj().T))>1e-12:
        raise ArithmeticError('non-Hermitian input')
    out=np.zeros(6)
    ptr=lambda x:x.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    code=LIB.dpp_stats(len(q),ptr(q),ptr(a),ptr(out))
    if code: raise ArithmeticError(f'dpp_stats status {code}')
    return out

def basis(n,complex_case=False):
    b=[]
    for i in range(n):
        e=np.zeros((n,n),complex);e[i,i]=1;b.append(e)
    for i in range(n):
        for j in range(i):
            e=np.zeros((n,n),complex);e[i,j]=e[j,i]=1/np.sqrt(2);b.append(e)
            if complex_case:
                e=np.zeros((n,n),complex);e[i,j]=1j/np.sqrt(2);e[j,i]=-1j/np.sqrt(2);b.append(e)
    return np.array(b)

def probabilities(q):
    n=len(q);bits=((np.arange(2**n)[:,None]>>np.arange(n))&1)
    mats=np.broadcast_to(q,(2**n,n,n)).copy().astype(complex)
    mats[:,np.arange(n),np.arange(n)]-=1-bits
    sign=(-1.)**(n-bits.sum(axis=1))
    p=(np.linalg.det(mats)*sign).real
    if p.min()<=0:raise ArithmeticError('nonpositive atom')
    return p,mats

def hessian(q,b):
    p,mats=probabilities(q)
    inv=np.linalg.inv(mats)
    c=np.einsum('sij,bjk->sbik',inv,b,optimize=True)
    r=np.trace(c,axis1=2,axis2=3).real
    h= -np.einsum('s,sb,sc->bc',p*(1+np.log(p)),r,r,optimize=True)
    h+=np.einsum('s,sbij,scji->bc',p*np.log(p),c,c,optimize=True).real
    return (h+h.T)/2

def random_unitary(rng,n,cx):
    z=rng.normal(size=(n,n))
    if cx:z=z+1j*rng.normal(size=(n,n))
    u,r=np.linalg.qr(z)
    return u

def spectral(u,lam):
    # Explicit contraction avoids spurious floating-point flag warnings from
    # this host's Accelerate complex GEMM. Symmetrize to exact binary Hermiticity.
    q=np.einsum('ik,jk,k->ij',u,u.conj(),lam,optimize=False)
    return (q+q.conj().T)/2

def random_kernel(rng,n,cx,kind):
    u=random_unitary(rng,n,cx)
    if kind=='uniform':lam=rng.uniform(.02,.98,n)
    elif kind=='extreme':
        eps=10**rng.uniform(-7,-1,n);lam=np.where(rng.random(n)<.5,eps,1-eps)
    elif kind=='projection':
        eps=10**rng.uniform(-6,-2);lam=np.r_[np.full(n//2,eps),np.full(n-n//2,1-eps)]
    else:raise ValueError(kind)
    return spectral(u,lam)

def mp_matrix(q):
    return mp.matrix([[mp.mpc(str(complex(z).real),str(complex(z).imag)) for z in row] for row in q])

def mp_stats(q,a=None,dps=80):
    with mp.workdps(dps):
        q=mp_matrix(q) if not isinstance(q,mp.matrix) else q
        a=mp.zeros(q.rows) if a is None else (mp_matrix(a) if not isinstance(a,mp.matrix) else a)
        n=q.rows;h=mp.mpf(0);h2=mp.mpf(0);mass=mp.mpf(0)
        for s in range(1<<n):
            b=q.copy()
            for i in range(n):
                if not ((s>>i)&1):b[i,i]-=1
            p=mp.re(mp.det(b))*(-1)**(n-s.bit_count())
            if p<0:raise ArithmeticError('negative MP atom')
            mass+=p
            if not p:continue
            h-=p*mp.log(p)
            c=b**-1*a;tr=sum(c[i,i] for i in range(n));tr2=sum(c[i,j]*c[j,i] for i in range(n) for j in range(n))
            h2-=mp.re(p*(tr**2+mp.log(p)*(tr**2-tr2)))
        return {'entropy':mp.nstr(h,dps-5),'second':mp.nstr(h2,dps-5),'mass':mp.nstr(mass,dps-5)}
