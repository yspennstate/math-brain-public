"""Exact, one-sided membership certificates for integer superharmonic matrices.

All arithmetic deciding certificates uses Python integers/Fraction. The search uses
int64 (bounded inputs); an independent verifier never trusts its floating output.
A failed fixed-period/affine-phase search is NOT nonmembership in Gamma.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
from fractions import Fraction as F
from itertools import product
from math import lcm
import numpy as np


def matrix(A):
    A=[[F(v) for v in row] for row in A]
    d=len(A)
    assert all(len(row)==d for row in A)
    assert all(A[i][j]==A[j][i] for i in range(d) for j in range(d))
    return A


def setup(A,N=None,phase=None):
    A=matrix(A); d=len(A)
    D=lcm(*(v.denominator for row in A for v in row))
    M=np.array([[int(v*D) for v in row] for row in A],dtype=np.int64)
    if N is None:
        N=D if all(((D-1)*int(M[i,i]))%2==0 for i in range(d)) else 2*D
    phase=tuple(phase or [0]*d)
    b=[-A[i][i]/2+F(phase[i],N) for i in range(d)]
    assert all((N*A[i][j]).denominator==1 for i in range(d) for j in range(d))
    assert all((N*N*A[i][i]/2+N*b[i]).denominator==1 for i in range(d))
    # One arithmetic denominator for q+b.x.
    K=lcm(2*D,*(v.denominator for v in b))
    coords=np.indices((N,)*d,dtype=np.int64)
    def base(coords):
        value=np.zeros((N,)*d,dtype=np.int64)
        for i in range(d):
            value+=int(K*A[i][i]/2)*coords[i]*coords[i]+int(K*b[i])*coords[i]
            for j in range(i): value+=int(K*A[i][j])*coords[i]*coords[j]
        return -np.floor_divide(-value,K)
    f0=base(coords)
    lap=-2*d*f0
    for i in range(d):
        for sign in (-1,1):
            c=coords.copy(); c[i]+=sign; lap+=base(c)
    return A,N,b,lap


def search(A,N=None,phase=None,max_rounds=20000,save=True,max_sites=300000):
    A=matrix(A);d=len(A)
    if sum(A[i][i] for i in range(d))>1:
        return {'status':'trace_excluded','trace':str(sum(A[i][i] for i in range(d)))}
    # Check size before allocating arrays.
    D=lcm(*(v.denominator for row in A for v in row))
    if N is None:
        N=D if all(((D-1)*int(A[i][i]*D))%2==0 for i in range(d)) else 2*D
    if N**d>max_sites: return {'status':'size_limit','N':N,'sites':N**d}
    A,N,b,lap=setup(A,N,phase)
    u=np.zeros(lap.shape,dtype=np.int64)
    for step in range(max_rounds+1):
        if int(lap.max())<=1:
            u-=int(u.min())
            cert={'A':[[str(v) for v in row] for row in A], 'N':N,
                  'b':[str(v) for v in b], 'u':u.ravel().tolist()}
            out={'status':'member','N':N,'sites':N**d,'rounds':step,
                 'lap_min':int(lap.min()),'lap_max':int(lap.max()),
                 'mean_lap':str(sum(A[i][i] for i in range(d)))}
            if save: out['certificate']=cert
            return out
        if int(u.min())>0:
            return {'status':'phase_period_excluded','N':N,'rounds':step,
                    'reason':'all vertices legally toppled; least action forbids a periodic stabilizer in this phase'}
        if step==max_rounds:break
        k=np.maximum((lap-1+2*d-1)//(2*d),0)
        u+=k
        lap-=2*d*k
        for i in range(d):lap+=np.roll(k,1,axis=i)+np.roll(k,-1,axis=i)
        assert int(u.max())<10**12
    return {'status':'inconclusive','N':N,'rounds':max_rounds}


def verify(cert,extra_translates=False):
    """Independent exact rational check, including quasi-periodic integrality."""
    A=matrix(cert['A']); d=len(A);N=int(cert['N']);b=list(map(F,cert['b']))
    assert N>=1 and len(cert['u'])==N**d and len(b)==d
    assert all(type(v) is int for v in cert['u'])
    assert all((N*A[i][j]).denominator==1 for i in range(d) for j in range(d))
    assert all((N*N*A[i][i]/2+N*b[i]).denominator==1 for i in range(d))
    def value(x):
        q=sum(A[i][j]*x[i]*x[j] for i in range(d) for j in range(d))/2+sum(b[i]*x[i] for i in range(d))
        r=[v%N for v in x];index=0
        for v in r:index=index*N+v
        return -((-q.numerator)//q.denominator)+cert['u'][index]
    lo=10**30;hi=-10**30;total=0
    for x in product(range(N),repeat=d):
        lap=-2*d*value(x)
        for i in range(d):
            for sign in (-1,1):
                y=list(x);y[i]+=sign;lap+=value(y)
        assert lap<=1,(x,lap)
        lo=min(lo,lap);hi=max(hi,lap);total+=lap
    assert F(total,N**d)==sum(A[i][i] for i in range(d))
    if extra_translates:
        for x in product((-N-1,-1,0,1,N+1),repeat=d):
            lap=-2*d*value(x)
            for i in range(d):
                for sign in (-1,1):
                    y=list(x);y[i]+=sign;lap+=value(y)
            assert lap<=1
    return {'valid':True,'sites':N**d,'lap_min':lo,'lap_max':hi,'trace':str(F(total,N**d))}


def phase_representatives(A,N):
    """Exhaust affine slopes modulo integer slopes and integer translations.

    Translating x by t changes phase by N*A*t modulo N. HNF of the
    integer lattice generated by columns of [N*A | N*I] gives coset reps.
    """
    from sympy import Matrix
    from sympy.matrices.normalforms import hermite_normal_form
    A=matrix(A);d=len(A)
    generators=Matrix(d,2*d,lambda i,j: int(N*A[i][j]) if j<d else (N if i==j-d else 0))
    H=hermite_normal_form(generators)
    return product(*(range(int(H[i,i])) for i in range(d)))


def search_phases(A,N=None,max_phases=4096,**kwargs):
    A=matrix(A);d=len(A)
    first=search(A,N=N,**kwargs)
    if first['status'] in ('member','trace_excluded','size_limit'):first['phases_tried']=1;return first
    N=first['N'];tried=1;unfinished=first['status']=='inconclusive'
    for phase in phase_representatives(A,N):
        if not any(phase):continue
        if tried>=max_phases:
            return {'status':'phase_limit','N':N,'phases_tried':tried}
        r=search(A,N,phase,**kwargs);tried+=1
        if r['status']=='member':r['phases_tried']=tried;return r
        unfinished|=r['status']=='inconclusive'
    return {'status':'inconclusive' if unfinished else 'period_excluded', 'N':N,'phases_tried':tried,
            'reason':'does not exclude nonperiodic representatives or larger periods'}
