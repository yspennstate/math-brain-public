from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict,Counter
from functools import lru_cache
import json,time,math
import kernel as k
ROOT=Path(__file__).resolve().parents[1];start=time.perf_counter();k.CAP=50
def chars(t):return [sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t)) for s in range(len(t))]
g=[k.bent(x&15,4) for x in range(32)];h=[g[x]*(-1 if (x&15)==0 and x&16 else 1) for x in range(32)]
cp=[];cm=[]
for y in range(4):
 p=(y.bit_count()%2)^(y==1);b=k.bent(y,2);cp.append(b if not p else 0);cm.append(b if p else 0)
ca,cb=chars(cp),chars(cm);gg,hh=chars(g),chars(h)
def spectrum(firstg,firsth):
 G,H=chars(firstg),chars(firsth);D=len(G)
 return [ca[s]*G[u]*gg[v]+cb[s]*H[u]*hh[v] for v in range(32) for u in range(D) for s in range(4)]
parent=spectrum(g,h);children=[spectrum(k.restrict(g,0,value),k.restrict(h,0,value)) for value in (0,1)]
assert sum(v*v for v in parent)==4096**2
assert all(sum(v*v for v in a)==2048**2 for a in children)
@lru_cache(None)
def factor(n):
 d=2;out={}
 while d*d<=n:
  while n%d==0:out[d]=out.get(d,0)+1;n//=d
  d+=1
 if n>1:out[n]=out.get(n,0)+1
 return out
def price_coeff(a,i):
 N=len(a);coef=defaultdict(Q);hist=Counter((a[s^(1<<i)]**2,a[s]**2+a[s^(1<<i)]**2) for s in range(N) if not s&(1<<i))
 for (b,r),count in hist.items():
  k.clock()
  if not b:continue
  for value,sgn in ((r,1),(b,-1)):
   for prime,exp in factor(value).items():coef[prime]+=Q(sgn*count*b*exp,N*N)
 return dict(coef)
c=price_coeff(parent,11);c0,c1=[price_coeff(a,10) for a in children]
drift={p:(c0.get(p,Q(0))+c1.get(p,Q(0)))/2-c.get(p,Q(0)) for p in c.keys()|c0.keys()|c1.keys()};drift={p:v for p,v in drift.items() if v}
scale=math.lcm(*(v.denominator for v in drift.values()));expo={p:int(v*scale) for p,v in drift.items()}
num=math.prod(p**v for p,v in expo.items() if v>0);den=math.prod(p**(-v) for p,v in expo.items() if v<0);assert num>den
outward=(Q(0),Q(0))
for p,v in drift.items():outward=k.add(outward,k.mul(k.logint(p),v))
assert outward[0]>0
physical=[]
for x in range(4096):
 y=x&3;a=(x>>2)&15;z=(x>>6)&1;b=(x>>7)&15;w=(x>>11)&1;p=(y.bit_count()%2)^(y==1)
 physical.append(k.bent(y,2)*k.bent(a,4)*k.bent(b,4)*(-1 if p*((a==0)*z+(b==0)*w)%2 else 1))
freqs=(0,4,2048,2052);sums={s:sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(physical)) for s in freqs}
assert all(sums[s]==parent[s] for s in freqs)
out=dict(helper_version='A035-positive-prime-repro-v1',runtime_seconds=time.perf_counter()-start,case_count=3,full_spectra_dimensions=[12,11,11],direct_complete_root_characters=sums,positive_drift=k.emit(outward),exact_integer_certificate=dict(scale=scale,prime_exponents=expo,numerator_bits=num.bit_length(),denominator_bits=den.bit_length(),comparison='numerator strictly greater than denominator; integers regenerated from prime_exponents'),status='PASS')
(ROOT/'out'/'positive_reproduction.json').write_text(json.dumps(out,indent=2),encoding='utf8');print(json.dumps(out,indent=2))
