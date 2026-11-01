from fractions import Fraction as F
from itertools import combinations,product
from math import factorial,prod
from pathlib import Path
import json

def det(a):
 a=[list(r) for r in a]; val=F(1); n=len(a)
 for i in range(n):
  pivot=next((j for j in range(i,n) if a[j][i]),None)
  if pivot is None:return F(0)
  if pivot!=i:a[i],a[pivot]=a[pivot],a[i];val=-val
  z=a[i][i];val*=z
  for j in range(i+1,n):
   q=a[j][i]/z
   for k in range(i+1,n):a[j][k]-=q*a[i][k]
 return val
count=0;links=0;t=F(3,2)
for n in range(1,6):
 for ll in combinations(range(9),n):
  a=[[t**(z-i)/factorial(z-i) if z>=i else F(0) for z in ll] for i in range(n)]
  vv=prod(ll[j]-ll[i] for i in range(n) for j in range(i+1,n))
  rhs=t**(sum(ll)-n*(n-1)//2)*vv/prod(factorial(z) for z in ll)
  assert det(a)==rhs;count+=1
  if n>1:
   norm=F(0)
   for lower in product(*(range(ll[i]+1,ll[i+1]+1) for i in range(n-1))):
    v=prod(lower[j]-lower[i] for i in range(n-1) for j in range(i+1,n-1))
    norm+=F(factorial(n-1)*v,vv)
   assert norm==1;links+=1
facs=0;diffs=0
for a,b in product(range(51),repeat=2):
 r=(a+b)//2;s=(a+b+1)//2
 assert factorial(r)*factorial(s)<=factorial(a)*factorial(b);facs+=1
for x,y,z,w in product(range(-4,5),repeat=4):
 for c in range(4):
  a=x-y+c;b=z-w+c;r=(x+z)//2-(y+w)//2+c;s=(x+z+1)//2-(y+w+1)//2+c
  assert r+s==a+b and abs(r-s)<=1 and a*b<=r*s;diffs+=1
out={'determinants':count,'link_normalizations':links,'factorial_pairs':facs,'signed_difference_pairs_with_shifts':diffs,'result':'all exact checks passed'}
Path('identity_results.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(out)
