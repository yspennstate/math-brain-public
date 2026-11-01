from pathlib import Path
from fractions import Fraction as F
import math,json,time
R=Path(__file__).resolve().parent;t0=time.monotonic()
def setup(coords,A):
 n=len(coords);idx={p:i for i,p in enumerate(coords)};adj=[0]*n;full=(1<<n)-1
 for (x,y),i in idx.items():
  for p in [(x+1,y),(x,y+1)]:
   if p in idx:j=idx[p];adj[i]|=1<<j;adj[j]|=1<<i
 z=[F(0)]*(1<<n);z[0]=F(1);cut=[0]*(1<<n)
 for S in range(1,1<<n):
  b=S&-S;v=b.bit_length()-1;T=S^b;cut[S]=cut[T]+4-2*(adj[v]&T).bit_count()
  bits=S;total=F(0)
  while bits:b=bits&-bits;bits^=b;total+=z[S^b]
  z[S]=total/cut[S]
 rates=[[] for _ in z]
 for S in range(1,1<<n):
  bits=S;total=F(0)
  while bits:
   b=bits&-bits;bits^=b;rate=z[S^b]/z[S];assert rate<=4
   rates[S].append((S^b,float(rate)/(4*n)));total+=rate
  assert total==cut[S]
 weights=[z[S]*z[full^S] if S&A==A else F(0) for S in range(1<<n)];Z=sum(weights,F(0))
 init=[float(w/Z) for w in weights]
 return n,full,z,cut,rates,init
def evolve(n,cut,rates,init,h):
 mu=4*n*h;weight=math.exp(-mu);cur=init[:];out=[weight*x for x in cur];k=0
 while True:
  if k>mu:
   tail=weight*mu/(k+1)/(1-mu/(k+2))
   if tail<1e-14:break
  nxt=[0.0]*len(cur)
  for S,p in enumerate(cur):
   if not p:continue
   nxt[S]+=p*(1-cut[S]/(4*n))
   for T,q in rates[S]:nxt[T]+=p*q
  cur=nxt;k+=1;weight*=mu/k
  for S,p in enumerate(cur):out[S]+=weight*p
  assert k<1000
 assert abs(sum(out)-1)<2e-12
 return out,tail,k
results=[]
# Independent analytical root CDF versus exact-generator uniformization.
coords=[(-1,0),(0,0),(1,0)];A=2
n,full,z,cut,rates,init=setup(coords,A)
for h in [.01,.1,.3,.6,1.0]:
 out,tail,k=evolve(n,cut,rates,init,h)
 actual=sum(p for S,p in enumerate(out) if S&A==0)
 expected=(F(9,64)*(1-math.exp(-4*h))-F(1,16)*(1-math.exp(-6*h))+F(1,128)*(1-math.exp(-8*h)))/F(11,128)
 assert abs(actual-expected)<2e-12
 assert actual<=1-math.exp(-4*h)+2e-12
 results.append({'case':'three_site_partial_wall_root','h':h,'generator_CDF':actual,'analytical_CDF':float(expected),'poisson_tail_bound':tail,'terms':k+1})
# All low-site count tails versus the negative-binomial r=3 comparator
# in a genuine 3x3 full-wall square, at four finite positive levels.
coords=[(x,y) for x in range(-1,2) for y in range(-1,2)];A=(1<<9)-1
n,full,z,cut,rates,init=setup(coords,A);r=cut[A]/4;assert r==3
for h in [.01,.1,.3,.6]:
 out,tail,k=evolve(n,cut,rates,init,h)
 mass=[0.0]*(n+1)
 for S,pS in enumerate(out):mass[n-S.bit_count()]+=pS
 p=math.exp(-4*h);nb=p**r;cdf=0.;worst=-1
 for m in range(1,n+1):
  cdf+=nb;bound=max(0.,1-cdf);actual=sum(mass[m:])
  assert actual<=bound+3e-12
  worst=max(worst,actual-bound)
  nb*=((m-1+r)/m)*(1-p)
 results.append({'case':'3x3_full_wall_count','h':h,'max_actual_tail_minus_NB_tail':worst,'poisson_tail_bound':tail,'terms':k+1})
(R/'death_count_checks.json').write_text(json.dumps({'results':results,'seconds':time.monotonic()-t0},indent=2),encoding='utf8')
print(json.dumps({'checks':len(results),'seconds':time.monotonic()-t0,'max_root_error':max(abs(x['generator_CDF']-x['analytical_CDF']) for x in results if 'generator_CDF' in x)}),flush=True)
