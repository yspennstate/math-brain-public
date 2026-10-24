from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from functools import lru_cache
import json,time,hashlib
R=Path(__file__).resolve().parents[1]
spec=json.loads((R/'out/FROZEN_SPEC.json').read_text())
start=time.perf_counter(); checks=0
counts={'ternary_product_pairs':0,'Boolean_semi_nodes':0,'monotone_separated_nodes':0,'delta_roots':0,'delta_prefix_nodes':0}
def check(condition):
 global checks
 assert condition
 checks+=1
 if time.perf_counter()-start>60:raise RuntimeError('frozen runtime exceeded')
@lru_cache(None)
def fourier(vals):
 v=list(vals);n=len(v).bit_length()-1
 for i in range(n):
  for x in range(len(v)):
   if not x&(1<<i):
    y=x|(1<<i);a,b=v[x],v[y];v[x]=a+b;v[y]=b-a
 return tuple(Q(x,len(v)) for x in v)
def energy(c):return sum((x*x for x in c),Q(0))
def logform(q):
 out={}
 for x,sign in [(q.numerator,1),(q.denominator,-1)]:
  p=2
  while p*p<=x:
   while x%p==0:out[p]=out.get(p,0)+sign;x//=p
   p+=1
  if x>1:out[x]=out.get(x,0)+sign
 return {p:Q(c) for p,c in out.items() if c}
def add(*terms):
 out={}
 for scale,d in terms:
  for p,c in d.items():out[p]=out.get(p,Q(0))+scale*c
 return {p:c for p,c in out.items() if c}
def ent(probs):return add(*[(-q,logform(q)) for q in probs if q])
def hb(q):return ent((q,1-q))
def Hp(c):return ent(tuple(x*x for x in c))
def influence(c):return sum((s.bit_count()*x*x for s,x in enumerate(c)),Q(0))
def node(a,b):
 check(len(a)==len(b) and energy(a)==1 and energy(b)==1)
 c=tuple((x+y)/2 for x,y in zip(a,b))+tuple((x-y)/2 for x,y in zip(a,b))
 d=sum(((x-y)**2 for x,y in zip(a,b)),Q(0));v=sum((abs(x*x-y*y) for x,y in zip(a,b)),Q(0))
 E={};refund={}
 for x,y in zip(a,b):
  z=x*x+y*y
  if z:
   E=add((1,E),(z/2,hb((x-y)**2/(2*z))))
   refund=add((1,refund),(z/2,add((1,{2:Q(1)}),(-1,hb(x*x/z)))))
 delta=add((1,Hp(c)),(Q(-1,2),Hp(a)),(Q(-1,2),Hp(b)))
 check(delta==add((1,E),(1,refund)))
 check(influence(c)==(influence(a)+influence(b))/2+d/4)
 return d/4,v,delta,c
for nq in (1,2):
 for pv,qv,rv in product(product((-1,0,1),repeat=2),product((-1,0,1),repeat=2**nq),product((-1,0,1),repeat=2)):
  n=1+nq+1
  plus=tuple(pv[x&1]*qv[(x>>1)&((1<<nq)-1)] for x in range(1<<n))
  minus=tuple(pv[x&1]*rv[x>>(1+nq)] for x in range(1<<n))
  a,b=fourier(plus),fourier(minus)
  D=sum(((x-y)**2 for x,y in zip(a,b)),Q(0));V=sum((abs(x*x-y*y) for x,y in zip(a,b)),Q(0))
  cp,cq,cr=map(fourier,(tuple(pv),tuple(qv),tuple(rv)))
  exactV=energy(cp)*(energy(cq)+energy(cr)-2*min(cq[0]**2,cr[0]**2))
  exactD=energy(cp)*(energy(cq)+energy(cr)-2*cq[0]*cr[0])
  check(V==exactV and D==exactD and V<=4*D)
  counts['ternary_product_pairs']+=1
for pv,qv,rv in product(product((-1,1),repeat=2),product((-1,1),repeat=4),product((-1,1),repeat=2)):
 a=fourier(tuple(pv[x&1]*qv[(x>>1)&3] for x in range(16)))
 b=fourier(tuple(pv[x&1]*rv[x>>3] for x in range(16)))
 I,V,_,_=node(a,b);check(V<=16*I)
 counts['Boolean_semi_nodes']+=1
monotone=[]
for v in product((-1,1),repeat=4):
 if all(v[x]<=v[x|(1<<i)] for x in range(4) for i in range(2) if not x&(1<<i)):monotone.append(v)
check(len(monotone)==6)
for h,k in product(monotone,repeat=2):
 a=fourier(tuple(max(h[x&3],k[x>>2]) for x in range(16)));b=fourier(tuple(h[x&3] for x in range(16)))
 I,V,_,_=node(a,b);check(V<=20*I)
 counts['monotone_separated_nodes']+=1
for widths,u in product(((),(1,),(2,),(3,),(1,1),(1,2),(2,1),(2,2)),(1,2,3)):
 m=sum(widths);H=[];G=[]
 for x in range(1<<(m+1)):
  offset=0;positive=False
  for w in widths:
   positive |= ((x>>offset)&((1<<w)-1))==((1<<w)-1);offset+=w
  H.append(1 if positive else -1);G.append(1 if x else -1)
 def kernel(r):
  return fourier(tuple(G[x&((1<<(m+1))-1)] if x>>(m+1)==(1<<r)-1 else H[x&((1<<(m+1))-1)] for x in range(1<<(m+1+r))))
 hc=fourier(tuple(H));gc=fourier(tuple(G));root=kernel(u)
 entropy_paid={};query_paid=Q(0)
 for depth in range(u):
  r=u-depth;a=kernel(r-1)
  # Inflate H with dummy coordinates to exactly the child's remaining cube.
  b=hc+tuple(Q(0) for _ in range(len(a)-len(hc)))
  I,V,delta,c=node(a,b)
  check(V<=38*I)
  if m==0:check(V==8*Q(1,2**r)*(1-Q(1,2**r)))
  entropy_paid=add((1,entropy_paid),(Q(1,2**depth),delta));query_paid+=Q(1,2**depth)*I
  counts['delta_prefix_nodes']+=1
 # Leaves H with weight 1-2^-u and G with weight 2^-u.
 terminalH=add((1-Q(1,2**u),Hp(hc)),(Q(1,2**u),Hp(gc)))
 terminalI=(1-Q(1,2**u))*influence(hc)+Q(1,2**u)*influence(gc)
 check(Hp(root)==add((1,entropy_paid),(1,terminalH)))
 check(influence(root)==query_paid+terminalI)
 counts['delta_roots']+=1
check(counts==spec['case_count'])
out={'status':'PASS','exact_assertions':checks,'counts':counts,'seconds':time.perf_counter()-start,
 'arithmetic':spec['arithmetic'],'source_class_bounds_checked':{'semi':16,'tribe_separated':20,'delta':38},
 'entropy_inequality_signs':'Analytic proof in DERIVATION.md; no numerical signs used',
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(R/'out/VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(out,indent=2))
