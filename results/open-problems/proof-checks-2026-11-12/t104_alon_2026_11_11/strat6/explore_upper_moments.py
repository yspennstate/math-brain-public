"""PROVED: exact matrix coefficient tests for upper moment inequalities."""
import itertools
import json
from fractions import Fraction as F
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
rr,*g=ring('z0,z1,z2,z3,x0,x1,x2',QQ)
z,x=g[:4],g[4:]
U=[sum(((5-j) if i<j else -j)*z[j-1] for j in range(1,5)) for i in range(5)]
W=[sum((U[4]-U[j+1])*x[j] for j in range(3))]+[(U[0]-U[4])*x[j] for j in range(3)]+[sum((U[j+1]-U[0])*x[j] for j in range(3))]
t,n=sum(v*v for v in U),sum(v*v for v in W)
A,C=sum(v**4 for v in U),sum(a*a*b*b for a,b in zip(U,W))
def matrices(poly):
 out={}
 for mon,c in poly.terms():
  zz,xx=mon[:4],mon[4:]
  m=out.setdefault(zz,[[F(0)]*3 for i in range(3)])
  ids=[i for i in range(3) for _ in range(xx[i])];i,j=ids
  v=F(int(c.numerator),int(c.denominator))/(1 if i==j else 2)
  m[i][j]+=v
  if i!=j:m[j][i]+=v
 return out

def psd(m):
 a,b,c=m[0];_,d,e=m[1];_,_,f=m[2]
 return min(a,d,f,a*d-b*b,a*f-c*c,d*f-e*e,a*d*f+2*b*c*e-a*e*e-d*c*c-f*b*b)>=0
unit=matrices(t*t*n); aa=matrices(A*n);cc=matrices(t*C)
records=[]
for k in [F(3,2),F(2),F(3),F(4),F(5),F(8)]:
 low,high=int(1000*(k*F(13,20)+F(1,20))),int(1000*(k*F(13,20)+F(1,2)))
 winner=None
 while low+1<high:
  mid=(low+high)//2; bound=F(mid,1000)
  mats={zz:[[bound*unit[zz][i][j]-k*aa[zz][i][j]-cc.get(zz,[[F(0)]*3 for _ in range(3)])[i][j] for j in range(3)]for i in range(3)]for zz in unit}
  if all(psd(m) for m in mats.values()):high=mid;winner=bound
  else:low=mid
 if winner is not None:
  print('PROVED:',k,'A+C <=',winner,flush=True)
  records.append(dict(k=str(k),bound=str(winner)))
 else:print('NUMERICAL: no coefficient certificate at',k,flush=True)
with open('upper_moment_bounds.json','w') as fp:json.dump(records,fp,indent=2)
