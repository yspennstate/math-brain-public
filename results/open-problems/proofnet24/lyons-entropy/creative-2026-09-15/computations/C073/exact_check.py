"""Exact atom and tangent identities underlying C073. No floating-point signs."""
from fractions import Fraction as Q
from itertools import permutations, product
import json

count=0
def check(a,b):
 global count
 assert a==b,(a,b)
 count+=1

def det2(M,A):
 """Coefficients through t^2 of det(M+t A), by the Leibniz formula."""
 n=len(M);out=[Q(0)]*3
 for p in permutations(range(n)):
  inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
  poly=[Q((-1)**inv),Q(0),Q(0)]
  for i,j in enumerate(p):
   poly=[poly[0]*M[i][j],poly[1]*M[i][j]+poly[0]*A[i][j],poly[2]*M[i][j]+poly[1]*A[i][j]]
  out=[a+b for a,b in zip(out,poly)]
 return out

def atoms(K,A):
 n=len(K);ans=[]
 for mask in range(1<<n):
  M=[[K[i][j] if (mask>>j)&1 else Q(int(i==j))-K[i][j] for j in range(n)]for i in range(n)]
  V=[[A[i][j] if (mask>>j)&1 else -A[i][j] for j in range(n)]for i in range(n)]
  p,d,c=det2(M,V);ans.append((p,d,2*c))
 return ans

for z in [[Q(3,8),Q(1,4),Q(1,8)],[Q(1,4),Q(1,5),Q(1,6),Q(1,7)]]:
 m=len(z);n=m+1;w=[4*x*x for x in z];assert sum(w)<1
 K=[[Q(int(i==j),2) for j in range(n)]for i in range(n)]
 D=[[Q(0) for j in range(n)]for i in range(n)];E=[[Q(0) for j in range(n)]for i in range(n)]
 a=[Q((-1)**i*(i+1)) for i in range(n)]
 for i in range(n):D[i][i]=a[i]
 for i in range(m):
  K[0][i+1]=K[i+1][0]=z[i]
  E[0][i+1]=E[i+1][0]=Q((-1)**i,i+7)
 A=[[D[i][j]+E[i][j] for j in range(n)]for i in range(n)]
 pd,pe,pa=atoms(K,D),atoms(K,E),atoms(K,A)
 p=[v[0] for v in pd];aa=Q(0);c=a[0]+sum(wi*ai for wi,ai in zip(w,a[1:]))
 for mask in range(1<<n):
  s=[2*((mask>>i)&1)-1 for i in range(n)];r=s[0];t=[-r*si for si in s[1:]]
  q=1+sum(wi*ti for wi,ti in zip(w,t));Z=sum(ai*ti for ai,ti in zip(a[1:],t))
  check(p[mask],q/(1<<n));check(pd[mask][1],2*r*(c-q*Z)/(1<<n));aa+=1/q/(1<<n)
  der2=sum(2*a[i]*a[j]*s[i]*s[j]*sum(p[mask^fl] for fl in [0,1<<i,1<<j,(1<<i)^(1<<j)]) for i in range(n) for j in range(i))
  check(pd[mask][2],der2)
  comp=((1<<n)-1)^mask
  check(pd[mask][1],-pd[comp][1]);check(pe[mask][1],pe[comp][1])
  mixed=pa[mask][2]-pd[mask][2]-pe[mask][2]
  mixedc=pa[comp][2]-pd[comp][2]-pe[comp][2]
  check(mixed,-mixedc)
 check(sum(v[1]*v[1]/v[0] for v in pd),4*(sum(x*x for x in a[1:])+aa*c*c))
 check(sum(p),Q(1))

result={'status':'PASS','exact_assertions':count,'arithmetic':'fractions.Fraction','checks':['star atoms against independent mixed-column determinants','diagonal first and second derivatives','closed Fisher quadratic form','particle-hole parity for diagonal, edge, and mixed second derivative']}
print(json.dumps(result,indent=2))
open('computations/C073/exact_check.json','w').write(json.dumps(result,indent=2)+'\n')
