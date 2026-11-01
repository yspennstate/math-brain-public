from fractions import Fraction as F
from itertools import product
from pathlib import Path
from collections import defaultdict
from functools import lru_cache
import json,time
root=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def check(x):
 global checks
 assert x
 checks+=1
def spectrum(p):
 T={x:F(1 if sum(x)>=2 else -1) for x in product((0,1),repeat=3)}
 P={};W={};C={}
 for s in range(8):
  moment=F(0);den=F(1);w=F(1)
  for i in range(3):
   if s>>i&1:den*=2*p[i]*(1-p[i]);w*=4*p[i]*(1-p[i])
  for x,val in T.items():
   m=F(1)
   for i in range(3):
    m*=p[i] if x[i] else 1-p[i]
    if s>>i&1:m*=x[i]-p[i]
   moment+=m*val
  C[s]=moment/den;W[s]=w;P[s]=w*C[s]*C[s]
 check(sum(P.values())==1)
 return P,W,C
def closed(p):
 w=[4*x*(1-x) for x in p];C={}
 C[0]=2*(p[0]*p[1]+p[0]*p[2]+p[1]*p[2]-2*p[0]*p[1]*p[2])-1
 for i in range(3):
  j,k=[j for j in range(3) if j!=i]
  C[1<<i]=p[j]+p[k]-2*p[j]*p[k]
  C[7^(1<<i)]=(1-2*p[i])/2
 C[7]=F(-1,2)
 W={s:__import__('math').prod((w[i] for i in range(3) if s>>i&1),start=F(1)) for s in range(8)}
 return {s:W[s]*C[s]**2 for s in C},W,C
@lru_cache(None)
def ln(x,N=24):
 k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 def series(v):
  z=(v-1)/(v+1);lo=2*sum((z**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
  return lo,lo+2*z**(2*N+1)/(F(2*N+1)*(1-z*z))
 a,b=series(x);l,u=series(F(2))
 return (a+k*l,b+k*u) if k>=0 else (a+k*u,b+k*l)
def add(A,B):return A[0]+B[0],A[1]+B[1]
def scale(c,A):return (c*A[0],c*A[1]) if c>=0 else (c*A[1],c*A[0])
def entropy(P,W,sets):
 out=(F(0),F(0))
 for s in sets:
  if P[s]:out=add(out,scale(P[s],ln(W[s]/P[s])))
 return out
def div(A,B):
 corners=[a/b for a in A for b in B];return min(corners),max(corners)
def outward(A):
 z=10**10;return [str(F((A[0]*z).__floor__(),z)),str(F((A[1]*z).__ceil__(),z))]
ln2=ln(F(2));ln4=ln(F(4))
def inspect(p,direct=True):
 P,W,C=closed(p)
 if direct:
  PP,WW,CC=spectrum(p);check(PP==P);check(WW==W);check(CC==C)
 P2=sum(P[s] for s in (3,5,6));P3=P[7];D=P2+2*P3
 check(D>0)
 # Parseval on indicator-valued pivotal derivatives: exact high-degree credit.
 J=sum(W[1<<i]*C[1<<i]*(1-C[1<<i]) for i in range(3))
 check(J==2*P2+3*P3)
 E1=entropy(P,W,(1,2,4));Ehi=entropy(P,W,(3,5,6,7));E=add(E1,Ehi)
 check(E1[1] <= 2*J)
 hi_bound=add(scale(P2,ln4),scale(P3,add((F(3),F(3)),ln4)))
 check(Ehi[1]<=hi_bound[0])
 # E <= (4+ln4)D - (ln4-1)P3; all interval endpoints exact.
 target=add(scale(D,add((F(4),F(4)),ln4)),scale(-P3,add(ln4,(F(-1),F(-1)))))
 check(E[1]<=target[0])
 return P,W,C,D,E
grid=[F(1,64),F(1,8),F(1,4),F(1,3),F(1,2),F(2,3),F(3,4),F(7,8),F(63,64)]
for p in product(grid,repeat=3):inspect(p)
source=[]
for k in range(1,13):
 q=F(1,2**k);r=q**3
 P,W,C,D,E=inspect((1-r,q,q))
 check(P[1]==P[7]);check(P[2]==P[4]);check(P[3]==P[5])
 source.append({'k':k,'q':str(q),'ratio_bits':outward(div(E,scale(D,ln2)))})

exponents=[(1,1,1),(3,1,1),(1,3,3),(1,1,3),(3,2,1),(2,1,3),(1,4,2),(4,1,2)]
corners=[]
for k in range(3,11):
 t=F(1,2**k)
 for a,b,c in exponents:
  e,u,v=t**a,t**b,t**c;delta=max(e,u,v);S=e*u+e*v+u*v
  for kind,p in [('equal',(e,u,v)),('mixed',(1-e,u,v))]:
   P,W,C,D,E=inspect(p,False)
   check(abs(D-4*S)<=35*delta*S);check(D>=S)
   lmb=u*v/S
   if kind=='equal': leading=(F(2),F(2))
   else:leading=add((F(2),F(2)),div((2+2*lmb,2+2*lmb),ln2))
   ratio=div(E,scale(D,ln2));err=scale(400*delta,ln(1/delta))[0]
   check(ratio[1]-leading[0]<=err and leading[1]-ratio[0]<=err)
   if k==10:corners.append({'kind':kind,'exponents':[a,b,c],'ratio_bits':outward(ratio),'lambda_uv_over_S':str(lmb),'leading_bits':outward(leading)})

# Edges are checked at a finite perturbation; the limit itself is analytic.
edges=[]
for r in (F(1,4),F(1,2),F(3,4)):
 for kind in ('same','opposite'):
  t=F(1,4096);e=t;d=t*t
  p=(e,d,r) if kind=='same' else (1-e,d,r)
  P,W,C,D,E=inspect(p)
  def AA(x):return scale(x/(1-x),ln(1/x))
  if kind=='same':lead=add((F(2),F(2)),div(scale(2,AA(r)),ln2))
  else:
   z=add((F(1),F(1)),add(scale(e/(e+d),AA(r)),scale(d/(e+d),AA(1-r))))
   lead=add((F(2),F(2)),div(scale(2,z),ln2))
  edges.append({'kind':kind,'r':str(r),'ratio_bits':outward(div(E,scale(D,ln2))),'leading_bits':outward(lead)})

out={'helper_version':'A042-majority3-v1','assertions_passed':checks,'complete_grid_cases':729,'source_path_cases':12,'corner_cases':128,'edge_cases':6,'source_path':source,'unequal_rate_corner_records':corners,'edge_records':edges,'C_majority_bits':outward(add((F(2),F(2)),div((F(4),F(4)),ln2))),'runtime_seconds':time.monotonic()-start,'claim_scope':'continuum theorem proved analytically in REPORT.md; checks corroborate exact spectrum and each inequality'}
(root/'out/CHECK_OUTPUT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('source_path','unequal_rate_corner_records','edge_records')},indent=2))
