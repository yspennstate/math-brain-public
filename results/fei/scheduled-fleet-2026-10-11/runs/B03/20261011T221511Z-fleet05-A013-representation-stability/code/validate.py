from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import itertools,json,time
RUN=Path(__file__).resolve().parents[1]
start=time.perf_counter(); assertions=0
def check(b):
 global assertions
 assertions+=1
 if not b: raise AssertionError(assertions)
def tables(n):
 for t in range(1<<(1<<n)):
  yield [1 if t>>x&1 else -1 for x in range(1<<n)]
def walsh(t):
 a=list(t);h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for k in range(j,j+h):
    u,v=a[k],a[k+h];a[k]=u+v;a[k+h]=u-v
  h*=2
 return [F(v,len(a)) for v in a]
def influence(t):
 return [F(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t)) for j in range((len(t)-1).bit_length())]
def restrict(t,j,b):
 return [t[(x&((1<<j)-1)) | (b<<j) | ((x>>j)<<(j+1))] for x in range(len(t)//2)]
def ln_iv(z):
 u=(z-1)/(z+1)
 total=sum((2*u**(2*j+1)/F(2*j+1) for j in range(32)),F(0))
 return total,total+2*u**65/(65*(1-u*u))
LNLO,LNHI=ln_iv(F(2))
@lru_cache(None)
def log_iv(x):
 x=F(x);assert x>0;k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 a,b=ln_iv(x)
 return F(k)+a/LNHI,F(k)+b/LNLO
def entropy(p):
 lo=hi=F(0)
 for v in p:
  if v:
   a,b=log_iv(1/v);lo+=v*a;hi+=v*b
 return lo,hi
def cross(p,q):
 lo=hi=F(0)
 for v,w in zip(p,q):
  if v:
   check(w>0);a,b=log_iv(1/w);lo+=v*a;hi+=v*b
 return lo,hi
restrictions=0
for t in tables(3):
 gates=[x for x in range(8) if t[x]==1]
 for j,b in itertools.product(range(3),range(2)):
  child=restrict(t,j,b); kept=[x for x in gates if (x>>j&1)==b]
  pp=F(len(gates),8);pc=F(len(kept),4)
  check(pc<=2*pp);check(pc==F(child.count(1),4))
  for y in range(4):
   x=(y&((1<<j)-1))|(b<<j)|((y>>j)<<(j+1))
   check((x in kept)==(child[y]==1))
  for x in kept:
   lam=F(1,max(1,len(gates)));old=lam/8;new=lam/4
   check(new/(1+new)==2*old/(1+2*old))
  restrictions+=1
pairs=0
for g,h in itertools.product(list(tables(2)),repeat=2):
 ag,ah=walsh(g),walsh(h)
 product=[g[x&3]*h[x>>2] for x in range(16)];ap=walsh(product)
 for s in range(16):check(ap[s]==ag[s&3]*ah[s>>2])
 check(sum(influence(product))==sum(influence(g))+sum(influence(h)))
 check(product.count(1)==g.count(1)*h.count(1)+g.count(-1)*h.count(-1))
 mux=[(g if x&1 else h)[x>>1] for x in range(8)];am=walsh(mux)
 for t in range(4):
  check(am[2*t]==(ag[t]+ah[t])/2);check(am[2*t+1]==(ah[t]-ag[t])/2)
 check(influence(mux)[0]==F(sum(u!=v for u,v in zip(g,h)),4))
 check(sum(influence(mux)[1:])==(sum(influence(g))+sum(influence(h)))/2)
 reused=[(g if x&1 else h)[x] for x in range(4)]
 wg,wh=walsh(restrict(g,0,1)),walsh(restrict(h,0,0));ar=walsh(reused)
 for t in range(2):
  check(ar[2*t]==(wg[t]+wh[t])/2);check(ar[2*t+1]==(wh[t]-wg[t])/2)
 pairs+=1
activation_cases=0; min_gap=None; representatives=[]
for n in range(1,4):
 for g in tables(n):
  if sum(g):continue
  pg=[v*v for v in walsh(g)];ig=sum(influence(g))
  for r in range(1,5):
   p=F(1,1<<r);mask=(1<<r)-1
   ft=[g[x>>r] if x&mask==mask else 1 for x in range(1<<(n+r))]
   pf=[v*v for v in walsh(ft)];q=[F(0)]*len(pf)
   for u in range(1<<r):
    q[u]=sum((F(1,4**j) for j in range(max(1,u.bit_length()),r+1)),F(0))
    for t in range(1,1<<n):q[u+(t<<r)]=p*p*pg[t]
   direct=[F(0)]*len(q)
   for j in range(1,r+1):
    for u in range(1<<j):direct[u]+=F(1,4**j)
   for t in range(1,1<<n):
    for u in range(1<<r):direct[u+(t<<r)]+=p*p*pg[t]
   check(q==direct);check(sum(q)==1)
   for u in range(1<<r):
    check(pf[u]==((1-p)**2 if u==0 else p*p))
    for t in range(1,1<<n):check(pf[u+(t<<r)]==p*p*pg[t])
   check(sum(influence(ft))==p*(ig+r))
   v=2*p-p*p;qstar=sum(q[1:]);ref=[1-v]+[v*z/qstar for z in q[1:]]
   check(sum(ref)==1);check(qstar<=1)
   for u in range(1,1<<r):check(q[u]>=p*p)
   hg,hf,cf,hb=entropy(pg),entropy(pf),cross(pf,ref),entropy([v,1-v])
   check(ref==pf or cf[0]>hf[1]);check(cf[1]<hb[0]+2*r*v+p*hg[0])
   check(cf[1]<p*hg[0]+(6+2/LNHI)*p*r)
   gap=F(0) if ref==pf else cf[0]-hf[1]
   min_gap=gap if min_gap is None else min(min_gap,gap)
   if n==1:representatives.append({'r':r,'table':g,'I':str(p*(ig+r)),
    'raw_transcript_cost':str(4*(1-p)),'Q_empty':str(q[0]),'Q_nonempty':str(qstar),
    'cross_entropy_interval':[str(cf[0]),str(cf[1])]})
   activation_cases+=1
check([( [-1,1] if x&1 else [1,-1])[x] for x in range(2)]==[1,1])
check(F(3,2)<F(2,1))
result={'helper':'A013-exact-v1','status':'PASS','exact_assertions':assertions,
 'restriction_cases':restrictions,'two_bit_branch_pairs':pairs,'balanced_core_activation_cases':activation_cases,
 'failures':0,'arithmetic':'integer FWHT, Fraction identities, outward rational atanh log2 intervals (32 terms)',
 'max_dimension':7,'elapsed_seconds':time.perf_counter()-start,
 'minimum_cross_entropy_minus_entropy_lower_bound':str(min_gap),'literal_cases':representatives}
(RUN/'out'/'EXACT_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['literal_cases','minimum_cross_entropy_minus_entropy_lower_bound']},indent=2))
