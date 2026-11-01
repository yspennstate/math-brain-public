from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json,time

R=Path(__file__).resolve().parents[1]
t0=time.perf_counter();checks=0
def ck(b):
 global checks
 checks+=1
 assert b,checks
 assert time.perf_counter()-t0<55,'runtime cap'
def fw(v):
 v=list(v);step=1
 while step<len(v):
  for start in range(0,len(v),2*step):
   for j in range(start,start+step):v[j],v[j+step]=v[j]+v[j+step],v[j]-v[j+step]
  step*=2
 return v
def conv(a,b):
 out=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def power(a,k):
 out=[Q(1)]
 for _ in range(k):out=conv(out,a)
 return out
lhs=[4*x-y for x,y in zip(power([3,0,1],3),power([9,3,3,1],2))]
rhs=[3*x for x in conv(power([1,-1],2),power([3,0,1],2))]
ck(lhs==rhs)
# Full grid, not reduced by symmetry. Square only nonnegative sides.
grid=[Q(0),Q(1,2),Q(1),Q(2)]
for vals in product(grid,repeat=6):
 xs=vals[:3];ys=vals[3:]
 left=8*xs[0]*xs[1]*xs[2]
 right=Q(1)
 for x,y in zip(xs,ys):right*=x+y
 left+=right
 right=Q(4)
 for x,y in zip(xs,ys):right*=3*x*x+y*y
 ck(left*left<=right)
v=[-1]+[1]*7
p=[Q(x*x,64) for x in fw(v)]
ck(p==[Q(9,16)]+[Q(1,16)]*7)
mu=Q(1,4)
for i in range(3):ck(sum(p[x] for x in range(8) if x>>i&1)==mu)
L=[sum((x>>i)&1 for i in range(3))-Q(3,4) for x in range(8)]
ck(sum(a*b for a,b in zip(p,L))==0)
var=sum(a*b*b for a,b in zip(p,L));ck(var==Q(15,16))
conditional=[]
for i in range(3):
 row=[]
 for bit in [0,1]:
  m=sum(p[x] for x in range(8) if x>>i&1==bit)
  m1=sum(p[x]*L[x] for x in range(8) if x>>i&1==bit)/m
  ck(m1==Q(5,3)*(bit-mu));row.append(m1)
 conditional.append(row)
margvar=sum((1-mu)*a[0]**2+mu*a[1]**2 for a in conditional)
ck(margvar==Q(25,16));ck(margvar/var==Q(5,3))
fixtures=[]
for r in [1,2]:
 truth=[(-1)**sum(((x>>(3*b))&7)==0 for b in range(r)) for x in range(1<<(3*r))]
 spectrum=[Q(x*x,len(truth)**2) for x in fw(truth)]
 expected=[Q(1) for _ in truth]
 for x in range(len(truth)):
  for b in range(r):expected[x]*=p[(x>>(3*b))&7]
 ck(spectrum==expected);ck(sum(spectrum)==1);ck(set(truth)=={-1,1})
 # Direct inverse Walsh integrality check.
 ck(fw(fw(truth))==[len(truth)*x for x in truth])
 fixtures.append({'blocks':r,'truth_table':truth,'Walsh_numerators':fw(truth),'spectrum':[str(x) for x in spectrum]})
ck(3**3<2**5);ck(3**9>2**14)
out={'PASS':True,'checks':checks,'seconds':time.perf_counter()-t0,'grid_cases':4**6,'scalar_coefficients':[str(x) for x in lhs],'dual_variances':[str(var),str(margvar)],'lower_contraction_limit':'5/3','actual_boolean_fixtures':fixtures}
(R/'out/validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='actual_boolean_fixtures'}))
