"""Separate direct-character/edge audit; no import of the main arithmetic/helper."""
from fractions import Fraction as Q
from pathlib import Path
from functools import lru_cache
import itertools,json,time,math
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def check(x):
 global checks
 assert x
 checks+=1
 if time.perf_counter()-start>55:raise RuntimeError('Frozen55s limit')
def walsh(t):return tuple(Q(sum(a*(-1 if (x&s).bit_count()%2 else 1) for x,a in enumerate(t)),len(t)) for s in range(len(t)))
@lru_cache(None)
def factors(n):
 out={};p=2
 while p*p<=n:
  while n%p==0:out[p]=out.get(p,0)+1;n//=p
  p=3 if p==2 else p+2
 if n>1:out[n]=out.get(n,0)+1
 return out
def add(*terms):
 out={}
 for d,w in terms:
  for p,c in d.items():out[p]=out.get(p,Q(0))+w*c
 return {p:c for p,c in out.items() if c}
def plog(x,w):
 if not x:return {}
 return add((factors(x.numerator),w),(factors(x.denominator),-w))
def entropy(c):return add(*[(plog(a*a,-a*a),Q(1)) for a in c if a])
def fiber(a,b):
 return add((plog(a,-a),Q(1)),(plog(b,-b),Q(1)),(plog(a+b,a+b),Q(1)))
def series_ln(x):
 z=(x-1)/(x+1);N=20
 lo=sum((2*z**(2*j+1)/Q(2*j+1) for j in range(N)),Q(0))
 return lo,lo+2*z**(2*N+1)/((2*N+1)*(1-z*z))
ln2=series_ln(Q(2))
@lru_cache(None)
def logbox(p):
 power=p.bit_length()-1;y=Q(p,1<<power);a,b=series_ln(y)
 return Q(power)+a/ln2[1],Q(power)+b/ln2[0]
def box(e):
 lo=hi=Q(0)
 for p,c in e.items():
  a,b=logbox(p);lo+=c*(a if c>0 else b);hi+=c*(b if c>0 else a)
 scale=1<<60
 return Q(math.floor(lo*scale),scale),Q(math.ceil(hi*scale),scale)
rows=[]
for fixed in itertools.product((-1,0,1),repeat=3):
 free=[i for i in range(3) if fixed[i]==-1];t=[];active=[]
 for x in range(1<<len(free)):
  s=sum(a<<i for i,a in enumerate(fixed) if a!=-1)+sum((x>>j&1)<<i for j,i in enumerate(free))
  active.append(s in (0,1));t.append(0 if active[-1] else 1 if s.bit_count()<=1 else -1)
 c=walsh(t);check(sum(a*a for a in c)==Q(sum(not a for a in active),len(t)))
 for j in range(len(free)):
  er=add(*[(fiber(c[s]**2,c[s|(1<<j)]**2),Q(1)) for s in range(len(t)) if not s>>j&1])
  low=sum((Q(0) if active[s] and active[s^(1<<j)] else Q(1,2) if active[s] or active[s^(1<<j)] else Q(t[s]!=t[s^(1<<j)]) for s in range(len(t))),Q(0))/len(t)
  margin=add(({2:2*low},Q(1)),(er,Q(-1)))
  if margin:check(box(margin)[0]>=0)
  else:check(True)
  rows.append({'fixed':list(fixed),'coordinate':free[j],'J':str(low),'erasure_prime_log':{str(p):str(a) for p,a in er.items()},'margin_interval':[str(a) for a in box(margin)]})

# Complete ORIGINAL source, before either old-debit collision branch is selected.
v=tuple((-1 if x>>6&1 else 1)*(-1 if ((x&1)*(x>>1&1)+(x>>2&1)*(x>>3&1))%2 else 1) for x in range(128))
w=tuple((-1 if x>>6&1 else 1)*(-1 if x%64==0 else 1) for x in range(128))
f=tuple(v[x] if s==0 else w[x] if s==1 else 1 if s.bit_count()<=1 else -1 for s in range(8) for x in range(128))
cf=walsh(f);cv=walsh(v);cw=walsh(w);p=Q(1,8)
physical=[Q(sum(f[x]!=f[x^(1<<j)] for x in range(len(f))),len(f)) for j in range(10)]
for j in range(10):check(physical[j]==sum((a*a for s,a in enumerate(cf) if s>>j&1),Q(0)))
check(sum(a*a for a in cf)==1);check(sum(physical)==Q(543,256))
check(physical==[Q(17,256)]*4+[Q(1,256)]*2+[Q(1,4),Q(153,256),Q(1,2),Q(1,2)])
collision=add(*[(add((entropy((a+b,)),Q(1,2)),(entropy((a-b,)),Q(1,2)),(entropy((a,)),Q(-1)),(entropy((b,)),Q(-1))),p) for a,b in zip(cv[1:],cw[1:])])
maskc=(Q(-1,4),Q(1,2),Q(1,4),Q(0),Q(1,4),Q(0),Q(-1,4),Q(-1,2))
check(not add((entropy(cf),Q(1)),(entropy(cv),-p),(entropy(cw),-p),(collision,Q(-1)),(entropy(maskc),Q(-1)),({2:Q(3,2)},Q(-1))))
check(entropy(cv)=={2:Q(4)})
iv=sum((s.bit_count()*a*a for s,a in enumerate(cv)),Q(0));check(iv==3)
check(5*p*iv==Q(4,8)+Q(11,8));check(Q(11,8)-Q(4,8)-Q(1,8)-Q(4,8)==Q(2,8))
out={'status':'PASS','implementation':'direct character sums, physical directed edges, prime-log basis; no main-helper imports','exact_assertions':checks,'carrier_queries':len(rows),'elapsed_seconds':time.perf_counter()-start,'carrier_certificate':rows,'original_source':{'coordinate_names':['z1','z2','z3','z4','x1','x2','y','s1','s2','s3'],'influences':[str(a) for a in physical],'total_influence':str(sum(physical)),'full_fourier_coefficients':[str(a) for a in cf],'H_interval':[str(a) for a in box(entropy(cf))],'retained_remainder':'1/4'}}
(R/'out'/'INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('carrier_certificate','original_source')}))
