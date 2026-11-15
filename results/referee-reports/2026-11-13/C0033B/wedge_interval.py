"""Validated negative exterior Rayleigh quotient at the order-five witness."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from fractions import Fraction
from itertools import combinations
import json,numpy as np,mpmath as mp
iv=mp.iv;iv.dps=80
n=5;z=np.load('data/wedge_n5.npz')
def complex_interval(t):
 return iv.mpc(str(complex(t).real),str(complex(t).imag))
def conj(t):return iv.mpc(t.real,-t.imag)
def positive(t):return t._mpi_[0][0]==0 and t._mpi_[0][1]>0
def bounds(t):
 def frac(v):
  sg,man,exponent,bc=v
  return Fraction((-1)**sg*man)*Fraction(2)**exponent
 scale=10**30;lo=frac(t._mpi_[0])*scale;hi=frac(t._mpi_[1])*scale
 return [str(lo.numerator//lo.denominator)+'/1000000000000000000000000000000',
         str(-((-hi.numerator)//hi.denominator))+'/1000000000000000000000000000000']
q=[[complex_interval(t) for t in row] for row in z['Q']]
w=[complex_interval(t) for t in z['v']];ix=list(combinations(range(n),2))
def ldl(m):
 l=[[iv.mpc(0) for j in range(n)] for i in range(n)];d=[]
 for i in range(n):
  di=(m[i][i]-sum(l[i][k]*conj(l[i][k])*d[k] for k in range(i))).real
  assert positive(di),(i,di);d.append(di);l[i][i]=iv.mpc(1)
  for j in range(i+1,n):
   l[j][i]=(m[j][i]-sum(l[j][k]*conj(l[i][k])*d[k] for k in range(i)))/di
 return [bounds(t) for t in d]
q_pivots=ldl(q)
complement=[[iv.mpc(int(i==j))-q[i][j] for j in range(n)] for i in range(n)]
iq_pivots=ldl(complement)
def determinant_inverse(m):
 m=[row.copy() for row in m];v=[[iv.mpc(int(i==j)) for j in range(n)] for i in range(n)];det=iv.mpc(1)
 # Every leading principal pattern determinant is nonzero for a strict DPP.
 for k in range(n):
  pivot=m[k][k];det*=pivot
  for j in range(n):m[k][j]/=pivot;v[k][j]/=pivot
  for i in range(n):
   if i==k:continue
   factor=m[i][k]
   for j in range(n):m[i][j]-=factor*m[k][j];v[i][j]-=factor*v[k][j]
 return det,v
value=iv.mpc(0);mass=iv.mpf(0);atoms=[]
for s in range(1<<n):
 b=[row.copy() for row in q]
 for i in range(n):
  if not s>>i&1:b[i][i]-=1
 det,bv=determinant_inverse(b);p=det.real*(-1)**(n-s.bit_count())
 assert positive(p),(s,p);atoms.append(bounds(p));mass+=p
 vv=iv.mpc(0)
 for k,(i,j) in enumerate(ix):
  for l,(a,bb) in enumerate(ix):
   vv+=conj(w[k])*(bv[i][a]*bv[j][bb]-bv[i][bb]*bv[j][a])*w[l]
 value-=p*iv.log(p)*vv
norm=sum((conj(t)*t).real for t in w)
result=value.real/norm
assert positive(-result),result
ww=dict(zip(ix,w))
plucker=ww[(0,1)]*ww[(2,3)]-ww[(0,2)]*ww[(1,3)]+ww[(0,3)]*ww[(1,2)]
plucker_squared=plucker.real**2+plucker.imag**2
assert positive(plucker_squared),plucker_squared
out=dict(n=n,precision_decimal=80,q_ldl_pivots=q_pivots,complement_ldl_pivots=iq_pivots,atoms=atoms,mass=bounds(mass),rayleigh=bounds(result),plucker_squared=bounds(plucker_squared),result='strict contraction and strictly negative exterior Rayleigh quotient certified by intervals')
Path('data/wedge_interval_n5.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('atoms','q_ldl_pivots','complement_ldl_pivots')},indent=2))
