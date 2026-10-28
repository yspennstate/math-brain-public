"""Exact finite referee for affine tensor cost and adaptive untouched cores."""
import itertools, json, time
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
SPEC={'helper_version':'A055 untouched-core v1','family':'all labelled two-bit signs; all ordered two-seed products; adaptive physical restrictions of two identical seeds','domain':'n=0..4, K=1,2,4; all 81 partial restrictions; all 65 depth-at-most-two adaptive trees per seed','case_count':'256 ordered tensor pairs; 16*81 restrictions;16*65*3 tree/rate cases','symmetry':'none','arithmetic':'integer Walsh, independent physical edges, Fraction centered costs, exact prime-log vectors; no floating proof decisions','memory_estimate_MB':60,'maximum_runtime_seconds':55,'pilot':'single bounded certificate is pilot and final; no escalation'}
(BASE/'out'/'SPEC.json').write_text(json.dumps(SPEC,indent=2),encoding='utf-8')
start=time.perf_counter();checks=0
def ck(b):
 global checks
 assert b
 checks+=1
 assert time.perf_counter()-start<55
def fw(t):
 a=list(t);h=1
 while h<len(a):
  for i in range(0,len(a),2*h):
   for j in range(i,i+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return a
def add(a,b):
 z=dict(a)
 for p,v in b.items():z[p]=z.get(p,F(0))+v
 return {p:v for p,v in z.items() if v}
def scale(a,c):return {p:v*c for p,v in a.items() if v*c}
def fac(n):
 p=2;z={}
 while p*p<=n:
  while n%p==0:z[p]=z.get(p,0)+1;n//=p
  p+=1
 if n>1:z[n]=z.get(n,0)+1
 return z
@lru_cache(None)
def data(t):
 N=len(t);n=N.bit_length()-1;w=fw(t);H={2:F(2*n)}
 for v in w:
  if v:
   for p,e in fac(v*v).items():H[p]=H.get(p,F(0))-F(v*v*e,N*N)
 H={p:v for p,v in H.items() if v}
 costs=[F(min(sum(t[x]!=t[x^v] for x in range(N)),sum(t[x]==t[x^v] for x in range(N))),N) for v in range(N)]
 basis={};a=F(0)
 for v in sorted(range(1,N),key=lambda v:costs[v]):
  u=v
  while u:
   j=u.bit_length()-1
   if j in basis:u^=basis[j]
   else:basis[j]=u;a+=costs[v];break
 I=F(sum(sum(t[x]!=t[x^(1<<i)] for x in range(N)) for i in range(n)),N)
 ck(a<=I and a<=F(n,2))
 return H,a,I
def product(a,b):return tuple(x*y for y in b for x in a)
def restrict(t,assignment):
 n=len(t).bit_length()-1;free=[i for i in range(n) if i not in assignment];out=[]
 for x in range(1<<len(free)):
  z=sum(b<<i for i,b in assignment.items())+sum(((x>>j)&1)<<i for j,i in enumerate(free));out.append(t[z])
 return tuple(out)
def D(t,K):
 h,a,_=data(t);return add(h,{2:-K*a})
@lru_cache(None)
def lnunit(x):
 z=(x-1)/(x+1);s=sum((2*z**(2*j+1)/F(2*j+1) for j in range(24)),F(0));return s,s+2*z**49/(49*(1-z*z))
def bounds(z):
 l2,u2=lnunit(F(2));lo=hi=F(0)
 for p,c in z.items():
  k=p.bit_length()-1;l,u=lnunit(F(p,1<<k));l=k+l/u2;u=k+u/l2
  lo+=c*(l if c>=0 else u);hi+=c*(u if c>=0 else l)
 return lo,hi
signs=[tuple(1 if (v>>x)&1 else -1 for x in range(4)) for v in range(16)]
for a,b in itertools.product(signs,repeat=2):
 h,c,_=data(product(a,b));ha,ca,_=data(a);hb,cb,_=data(b)
 ck(h==add(ha,hb));ck(c==ca+cb)
leaf_rows=0;tree_rows=0;necessity=0
# All partial restrictions, including no query and complete exposure.
for h in signs:
 root=product(h,h)
 for pattern in itertools.product((-1,0,1),repeat=4):
  assignment={i:b for i,b in enumerate(pattern) if b>=0};T=len({i//2 for i in assignment});Q=len(assignment)
  child=restrict(root,assignment)
  for K in (F(1),F(2),F(4)):
   # Exact entropy-log inequality is nonnegative because each touched factor
   # has H>=0 and a<=(2-q_j)/2. Verify with certified logarithms.
   rhs=add(scale(D(h,K),2-T),{2:-K*T+K*Q/2})
   ck(bounds(add(D(child,K),scale(rhs,-1)))[0]>=0)
  leaf_rows+=1
def trees(free,depth):
 yield None
 if depth:
  for i in free:
   rest=tuple(j for j in free if j!=i)
   for a,b in itertools.product(tuple(trees(rest,depth-1)),repeat=2):yield i,a,b
alltrees=tuple(trees((0,1,2,3),2));ck(len(alltrees)==65)
def leaves(tree,assignment=None,weight=F(1)):
 assignment={} if assignment is None else assignment
 if tree is None:yield assignment,weight;return
 i,a,b=tree
 for bit,sub in enumerate((a,b)):yield from leaves(sub,dict(assignment,**{str(i):bit}) if False else {**assignment,i:bit},weight/2)
for h in signs:
 root=product(h,h)
 for tr in alltrees:
  L=list(leaves(tr));ck(sum(w for _,w in L)==1)
  ET=sum(w*len({i//2 for i in a}) for a,w in L);EQ=sum(w*len(a) for a,w in L)
  for K in (F(1),F(2),F(4)):
   actual={}
   for a,w in L:actual=add(actual,scale(D(restrict(root,a),K),w))
   rhs=add(scale(D(h,K),2-ET),{2:-K*ET+K*EQ/2})
   ck(bounds(add(actual,scale(rhs,-1)))[0]>=0)
   dl,du=bounds(D(h,K));al,au=bounds(actual)
   if dl>0:
    # Nonnegative average reserve means actual<=0. Interval detects only
    # certified cases; exact zero prime-log vector is included.
    if not actual or au<=0:ck(ET>=2*dl/(dl+K));necessity+=1
    if ET<2*dl/(dl+K):ck(al>0);necessity+=1
   tree_rows+=1
# Actual positive seed and exact threshold: AND2 has H=2,a=1,D_1=1.
h=(-1,1,1,1);ck(D(h,F(1))=={2:F(1)});ck(F(2,1+1)==1)
# The prior certified NAND32 gap >1/8 at K17/4 implies threshold >t/545.
ck(F(1,8)/(F(1,8)+F(17,4)*16)==F(1,545))
result={'status':'PASS','assertions':checks,'seconds':time.perf_counter()-start,'tensor_pairs':256,'partial_restrictions':leaf_rows,'tree_rate_cases':tree_rows,'eligibility_implications_checked':necessity,'NAND32_fraction_lower':'1/545','scope':'physical-query trees after activation/gadget resolved; no intermediate affine mixing or nonlinear phase reset'}
(BASE/'out'/'CHECK.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
