"""Independent direct Walsh verification; imports neither primary arithmetic nor checker."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from functools import lru_cache
import json,time,hashlib
R=Path(__file__).resolve().parents[1];O=R/'out'
spec={'version':1,'family':'eight explicit two-bit profiles, all ordered pairs and ternary Maj3 restrictions; original bent4 padding2 guard donor','cases':1728,'symmetry':'none','arithmetic':'direct character sums, Fraction prime-log vectors, outward 24-term atanh','memory_estimate_MB':40,'max_runtime_seconds':55,'imports_primary':False}
(O/'FROZEN_INDEPENDENT.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
start=time.monotonic();checks=0
def require(b):
 global checks
 checks+=1;assert b,checks
 assert time.monotonic()-start<55
def plus(*terms):
 z={}
 for c,d in terms:
  for p,v in d.items():z[p]=z.get(p,F(0))+c*v
 return {p:v for p,v in z.items() if v}
@lru_cache(None)
def prime(n):
 z={};p=2
 while p*p<=n:
  while n%p==0:z[p]=z.get(p,0)+1;n//=p
  p+=1
 if n>1:z[n]=z.get(n,0)+1
 return z
@lru_cache(None)
def gg(x):
 if not x:return {}
 q=x*x
 return plus(*[(-q*s,{p:F(v) for p,v in prime(n).items()}) for n,s in [(q.numerator,1),(q.denominator,-1)]])
@lru_cache(None)
def spectrum(v):
 return tuple(F(sum(y*(-1 if (i&s).bit_count()%2 else 1) for i,y in enumerate(v)),len(v)) for s in range(len(v)))
def entropy(v):return plus(*[(1,gg(a)) for a in spectrum(v)])
@lru_cache(None)
def lg(p):
 if p==2:return F(1),F(1)
 def ln(x):
  a=(x-1)/(x+1)
  lo=sum((2*a**(2*k+1)/F(2*k+1) for k in range(24)),F(0))
  return lo,lo+2*a**49/(49*(1-a*a))
 k=p.bit_length()-1;a,b=ln(F(p,2**k));c,d=ln(F(2))
 return F(k)+a/d,F(k)+b/c
def positive(x):
 lo=F(0)
 for p,c in x.items():
  a,b=lg(p);lo+=c*(a if c>=0 else b)
 return lo>=0
def child(v,i,b):return tuple(y for x,y in enumerate(v) if (x>>i)&1==b)
def influence(v,i):return F(sum(y!=v[x^(1<<i)] for x,y in enumerate(v)),len(v))
profiles=[(1,1,1,1),(-1,-1,-1,-1),(1,-1,1,-1),(1,1,-1,-1),(1,-1,-1,1),(-1,1,1,1),(1,-1,-1,-1),(1,1,1,-1)]
require(len(set(profiles))==8)
cases=identities=bothmeans=0;classes={}
for pat in product([-1,0,1],repeat=3):
 free=[i for i in range(3) if pat[i]==-1]
 original=[x for x in range(8) if all(pat[i]==-1 or pat[i]==(x>>i)&1 for i in range(3))]
 h=tuple(1 if x.bit_count()<=1 else -1 for x in original)
 ed={i:x for i,x in enumerate(original) if x in [0,1]};d=len(free);p=F(1,len(h))
 for v in profiles:
  for w in profiles:
   pr=[v,w]
   f=tuple(pr[ed[s]][z] if s in ed else h[s] for z in range(4) for s in range(len(h)))
   H=entropy(f)
   for i in range(d):
    cases+=1;children=[child(f,i,b) for b in [0,1]]
    delta=plus((1,H),(-F(1,2),entropy(children[0])),(-F(1,2),entropy(children[1])))
    j=influence(f,i);release=p*sum((1-F(sum(pr[t]),4)**2 for t in ed.values()),F(0))
    require(positive(plus((1,{2:release+10*j}),(-1,delta))))
    clean=[b for b in [0,1] if not any((s>>i)&1==b for s in ed)]
    character=[b for b in clean if sum(a!=0 for a in spectrum(child(h,i,b)))==1]
    if character:
     kind='character';identities+=1
     # Exact scalar identity after multiplying by an arbitrary signed character.
     rhs=plus((1,{2:4*j*(1-j)}),(1,gg(1-j)),(1,gg(j)),(-F(1,2),gg(1-2*j)))
     require(delta==rhs)
     require(positive(plus((1,{2:10*j}),(-1,delta))))
    elif len(h)==2 and len(ed)==2:
     kind='last_separator';require(positive(plus((1,{2:release+6*j}),(-1,delta))))
    else:
     kind='fixed_carrier_edge'
     floor=F(sum(s not in ed and (s^(1<<i)) not in ed and h[s]!=h[s^(1<<i)] for s in range(len(h))),len(h))
     require(floor>=F(1,4));require(j>=floor)
     require(positive(plus((1,{2:8*j}),(-1,delta))))
    classes[kind]=classes.get(kind,0)+1
    bothmeans+=int(len(ed)==2 and sum(v)!=0 and sum(w)!=0)
require(cases==1728)
# Full original Boolean donor: shared bits0..2, bent bits3..6, padding7..8, guard9.
truth=[]
for x in range(1024):
 s=x%8;z=(x>>3)%16;pad=(x>>7)%4;y=1-2*((x>>9)&1)
 b=(-1)**(((z&1)*((z>>1)&1))+(((z>>2)&1)*((z>>3)&1)))
 truth.append(y*b if s==0 else y*(1-2*(z==0 and pad==0)) if s==1 else 1 if s.bit_count()<=1 else -1)
truth=tuple(truth);infs=[influence(truth,i) for i in range(10)]
require(infs==[F(153,256),F(1,2),F(1,2)]+[F(17,256)]*4+[F(1,256)]*2+[F(1,4)])
require(sum(infs)==F(543,256))
result={'status':'PASS','exact_assertions':checks,'shared_queries':cases,'exact_character_identities':identities,'shared_classes':classes,'both_nonzero_means':bothmeans,'original_donor_coordinate_influences':[str(a) for a in infs],'original_donor_total_influence':str(sum(infs)),'runtime_seconds':time.monotonic()-start,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(O/'INDEPENDENT.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
