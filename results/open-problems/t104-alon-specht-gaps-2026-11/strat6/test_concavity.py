"""NUMERICAL/PROVED: exact coefficient test of normalized radial concavity."""
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
import sympy as s
rr,*g=ring('z0,z1,z2,z3,x0,x1,x2',QQ)
z,x=g[:4],g[4:]
U=[sum(((5-j) if i<j else -j)*z[j-1] for j in range(1,5)) for i in range(5)]
W=[sum((U[4]-U[j+1])*x[j] for j in range(3))]+[(U[0]-U[4])*x[j] for j in range(3)]+[sum((U[j+1]-U[0])*x[j] for j in range(3))]
t,n=sum(v*v for v in U),sum(v*v for v in W)
A,C=sum(v**4 for v in U),sum(a*a*b*b for a,b in zip(U,W))
d,e,f=sum(v**3 for v in U),sum(a*a*b for a,b in zip(U,W)),sum(a*b*b for a,b in zip(U,W))
poly=47*A*t*n+41*C*t*t-13*t**3*n-24*d*d*n-6*e*e*t-18*d*f*t
cs={}
for mon,c in poly.terms():
 zz,xx=mon[:4],mon[4:]
 cs.setdefault(zz,s.zeros(3))
 ids=[i for i in range(3) for _ in range(xx[i])]
 i,j=ids
 cs[zz][i,j]+=s.Rational(c.numerator,c.denominator)/(1 if i==j else 2)
 if i!=j:cs[zz][j,i]=cs[zz][i,j]
bad=[zz for zz,m in cs.items() if any(m.extract(ids,ids).det()<0 for k in range(1,4) for ids in __import__('itertools').combinations(range(3),k))]
print('PROVED: PSD coefficient matrices',len(cs)-len(bad),'NUMERICAL: unresolved',len(bad),bad[:10])
