from pathlib import Path
from itertools import permutations
from fractions import Fraction as Q
from collections import defaultdict,Counter
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(v):
 global checks
 checks+=1
 assert v,checks
def tablemask(fn):return sum((fn([1-2*((u>>i)&1) for i in range(4)])==1)<<u for u in range(16))
maj=tablemask(lambda x:1 if sum(x[:3])>0 else -1)
selector=tablemask(lambda x:x[2] if x[2]==x[3] else (x[0] if x[2]==1 else x[1]))
ck(selector==1343)
def orbit(mask):
 ans=set()
 for perm in permutations(range(4)):
  for neg in range(16):
   for out in range(2):
    new=0
    for u in range(16):
     old=sum((((u>>perm[i])&1)^((neg>>i)&1))<<i for i in range(4))
     new|=(((mask>>old)&1)^out)<<u
    ans.add(new)
 return ans
o1=orbit(maj);o2=orbit(selector);ck(len(o1)==32);ck(len(o2)==192);ck(not o1&o2)
eq=[];strict=0;dictators=0
for mask in range(1<<16):
 if mask.bit_count()!=8:continue
 vals=[1 if mask>>u&1 else -1 for u in range(16)]
 single=[sum(vals[u]*(-1 if u>>i&1 else 1) for u in range(16)) for i in range(4)]
 edges=sum(vals[u]!=vals[u^(1<<i)] for i in range(4) for u in range(16) if not u>>i&1)
 D=32*edges-256;ck(D>=0)
 # log2(N^(2 sum W_i^2) / product |W_i|^(2W_i^2)) <= 3D.
 lhs=2**(8*sum(w*w for w in single));rhs=2**(3*D)
 for w in single:
  if w:rhs*=abs(w)**(2*w*w)
 ck(lhs<=rhs)
 if not D:dictators+=1
 elif lhs==rhs:eq.append(mask)
 else:strict+=1
ck(set(eq)==o1|o2)
census=json.loads((R/'out/census.json').read_text());ck(set(eq)=={x['mask'] for x in census['extremizers'] if x['n']==4})
# Independently obtain consensus spectrum by direct character sums.
v=[1 if selector>>u&1 else -1 for u in range(16)]
W=[sum(v[u]*(-1 if (u&s).bit_count()%2 else 1) for u in range(16)) for s in range(16)]
ck(W==[0,4,4,0,8,4,-4,0,8,-4,4,0,0,-4,-4,0])
inf=[sum(Q(W[s]**2,256) for s in range(16) if s>>i&1) for i in range(4)]
ck(inf==[Q(1,4),Q(1,4),Q(1,2),Q(1,2)])
def factor(t):
 d=Counter();p=2
 while p*p<=t:
  while t%p==0:d[p]+=1;t//=p
  p+=1
 if t>1:d[t]+=1
 return d
def plus(*terms):
 d=defaultdict(Q)
 for c,t in terms:
  for p,e in t.items():d[p]+=c*e
 return {p:e for p,e in d.items() if e}
def log(v):
 d=factor(v.numerator);d.subtract(factor(v.denominator));return dict(d)
def entropy(v):return plus(*[(-p,log(p)) for p in v if p])
def packet(a,b):return plus((1,entropy([a,b])),(-1,entropy([a+b])))
def spectrum(v):
 return [Q(sum(v[u]*(-1 if (u&s).bit_count()%2 else 1) for u in range(len(v))),len(v)) for s in range(len(v))]
inn=[(1-2*(u&1))*(1 if u>>1<5 else -1) for u in range(16)]
inn_a=spectrum(inn);ck(inn_a[0]==0);ck(inn_a[1]==Q(1,4));ck(all(inn_a[s]==0 for s in range(16) if not s&1))
inn_H=entropy([a*a for a in inn_a]);inn_I=sum(s.bit_count()*a*a for s,a in enumerate(inn_a))
dyadic=[]
for m in [2,4]:
 N=1<<m;delta=Q(1,N);r=Q(1,1<<(m//2))
 bent=[(-1)**sum(((y>>j)&1)*((y>>(j+1))&1) for j in range(0,m,2)) for y in range(N)]
 vals=[1 if u>>4==0 else inn[u&15]*bent[u>>4] for u in range(16*N)]
 a=spectrum(vals);ps=[x*x for x in a]
 ck(sum(ps)==1);ck(a[0]==delta);ck(a[1]==(r-delta)/4)
 queryI=sum(ps[s] for s in range(len(ps)) if s&1);ck(queryI==1-delta)
 B=plus(*[(1,packet(ps[s],ps[s|1])) for s in range(len(ps)) if not s&1])
 counts=[(N+(1<<(m//2)))//2,(N-(1<<(m//2)))//2]
 L=plus((counts[0],packet(delta*delta,Q(1,16)*(r-delta)**2)),(counts[1],packet(delta*delta,Q(1,16)*(-r-delta)**2)))
 ck(B==L)
 ga=[delta]*N+[(v-delta) for v in spectrum(bent)]
 Hg=entropy([v*v for v in ga]);Ig=1-delta+m*(Q(1,2)+delta)
 ck(entropy(ps)==plus((1,Hg),(1-delta,inn_H)))
 ck(sum(s.bit_count()*ps[s] for s in range(len(ps)))==Ig+(1-delta)*(inn_I-1))
 dyadic.append({'m':m,'inner_singleton':'1/4','inner_query_influence':'1','query_influence':str(queryI),'root_singleton':str(a[1]),'root_B_equals_L':True})
out={'status':'PASS','assertions':checks,'runtime_seconds':time.perf_counter()-start,'balanced_n4_cases':12870,'strict':strict,'dictators':dictators,'equality_cases':len(eq),'Maj3_orbit':len(o1),'consensus_orbit':len(o2),'consensus_mask':selector,'actual_Maj3_seed_mask':maj,'consensus_W':W,'consensus_influences':[str(x) for x in inf],'dyadic_compositions':dyadic,'method':'direct character sums/direct edges/independent integer comparison, no FWHT'}
(R/'out/reproduction.json').write_text(json.dumps(out,indent=2));print(json.dumps(out))
