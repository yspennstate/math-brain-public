"""Check Q directly, rather than only its derivative representation."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import json, signal, time
signal.alarm(280)
from fractions import Fraction as F
import numpy as np
from scipy.linalg import eigh_tridiagonal
from audit import polymer, gapq

start=time.monotonic()
def direct(n,b):
    k=np.arange(1,n+1,dtype=float)
    up=b*(n-k);down=k*(k-1)/n
    return float(eigh_tridiagonal(up+down,-np.sqrt(up[:-1]*down[1:]),select='i',select_range=(1,1))[0][0])

small=[]
for n in range(2,11):
    for b in (F(1,50),F(1,7),F(1),F(3)):
        q=np.full((n,n),F(0),dtype=object)
        for k in range(1,n+1):
            if k<n:q[k-1,k]=b*(n-k)
            if k>1:q[k-1,k-2]=F(k*(k-1),n)
            q[k-1,k-1]=-sum(q[k-1])
        derivative=np.full((n-1,n),F(0),dtype=object)
        A=np.full((n-1,n-1),F(0),dtype=object)
        for k in range(1,n):
            derivative[k-1,k-1]=-1;derivative[k-1,k]=1
            if k<n-1:A[k-1,k]=b*(n-k-1)
            if k>1:A[k-1,k-2]=F(k*(k-1),n)
            A[k-1,k-1]=-sum(A[k-1])-b-F(2*k,n)
        assert np.array_equal(derivative@q,A@derivative)
        states,qm,w=polymer(n,b)
        for i,m in enumerate(states):
            grouped=[sum(qm[i][j] for j,other in enumerate(states) if sum(other)==kk) for kk in range(1,n+1)]
            assert grouped==list(q[sum(m)-1])
        g=direct(n,float(b));err=abs(g-gapq(n,float(b)));assert err<1e-9
        small.append(dict(n=n,beta=str(b),gap_Q_direct=g,derivative_error=err))

large=[]
for n in (2,3,5,10,50,200,1000):
    for b in (1e-6,1e-4,1e-2,n**-2,1/n,1.,10.,1000.):
        g=direct(n,b);err=abs(g-gapq(n,b));assert err<1e-9
        large.append(dict(n=n,beta=b,gap_Q_direct=g,derivative_error=err))
result=dict(small=small,large=large,max_small_error=max(x['derivative_error'] for x in small),max_large_error=max(x['derivative_error'] for x in large),exact_intertwining_cases=len(small),exact_lumping_cases=len(small),elapsed_seconds=time.monotonic()-start)
with open('count_direct_checks.json','w') as f:json.dump(result,f,indent=2)
print({key:value for key,value in result.items() if key not in ('small','large')})
