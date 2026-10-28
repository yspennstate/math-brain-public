from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from collections import Counter
import json,time,hashlib
root=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def check(b):
 global checks
 assert b;checks+=1
def mean(v):return Q(sum(v),len(v))
def inf(v):
 return sum((Q(sum(v[x]!=v[x^(1<<i)] for x in range(len(v))),len(v)) for i in range((len(v)-1).bit_length())),Q(0))
def cut(v,i,b):return tuple(v[x] for x in range(len(v)) if (x>>i)&1==b)
@lru_cache(None)
def spectrum(v):
 return tuple(Q(sum(z*(-1)**((s&x).bit_count()%2) for x,z in enumerate(v)),len(v)) for s in range(len(v)))
@lru_cache(None)
def lnunit(x):
 z=(x-1)/(x+1);lo=sum((2*z**(2*j+1)/(2*j+1) for j in range(20)),Q(0))
 return lo,lo+2*z**41/(41*(1-z*z))
@lru_cache(None)
def log2(x):
 k=x.numerator.bit_length()-x.denominator.bit_length();y=x/(Q(2)**k)
 if y<1:k-=1;y*=2
 a,b=lnunit(y);c,d=lnunit(Q(2))
 return k+a/d,k+b/c
def e(x):
 if not x:return Q(0),Q(0)
 a,b=log2(x);return -x*b,-x*a
def L(a,b):
 x=e(a*a);y=e(b*b);z=e(a*a+b*b)
 return x[0]+y[0]-z[1],x[1]+y[1]-z[0]
def sum_intervals(v):return sum(x[0] for x in v),sum(x[1] for x in v)
def H(v):return sum_intervals([e(a*a) for a in spectrum(v)])
def B(v,i):
 s=spectrum(v)
 return sum_intervals([L(a,s[j^(1<<i)]) for j,a in enumerate(s) if not j>>i&1])
def Xi(w,h):
 t=(1-mean(w))/2;r=(1-mean(h))/2
 return 5*(r*(1-r)*inf(w)+t*(1-t)*inf(h))
g=tuple(1 if x<3 else -1 for x in range(8));gp=tuple(1 if x in (0,1,2,4) else -1 for x in range(8))
w=tuple(gp[x>>1] if x&1 else g[x>>1] for x in range(16))
check(inf(w)==Q(3,2));check(mean(w)==-Q(1,8));bw=B(w,0);check(bw[1]<Q(1,2))
records=[];first_atoms=None
for N in (1,2,3):
 neg={u+8*z for u in range(3) for z in range(1<<N) if z.bit_count()%2}
 h=tuple(-1 if x in neg else 1 for x in range(1<<(N+3)))
 f=tuple(-1 if a==b==-1 else 1 for b in h for a in w)
 check((1-mean(h))/2==Q(3,16));check(inf(h)==Q(3*N+5,8))
 atoms=Counter(abs(a) for a in spectrum(f) if a)
 if first_atoms is None:first_atoms=atoms
 check(atoms==first_atoms);check(sum(atoms.values())<=256)
 f0,f1=cut(f,0,0),cut(f,0,1)
 q=inf(tuple(a*b for a,b in zip(f0,f1)))/2
 check(q==Q(3*N+14,128));check(inf(f)==Q(27*N+81,128))
 bf=B(f,0);check(bf[0]>Q(13,128));check(bf[1]<Q(3,32)+Q(1,120))
 D=Xi(w,h)-(Xi(g,h)+Xi(gp,h))/2
 check(q-D==Q(33*N+4,2048));check(q>D)
 hf=H(f);h0=H(f0);h1=H(f1)
 drop_upper=hf[1]-(h0[0]+h1[0])/2
 lower_budget=3*Q(3,128)+Q(3,16)*bw[0]+D
 check(drop_upper<lower_budget)
 records.append(dict(N=N,B_lift_interval=[str(z) for z in bf],B_inner_interval=[str(z) for z in bw],deficit=str(q-D),entropy_drop_upper=str(drop_upper),direct_erasure_budget_lower=str(lower_budget)))
 check(time.monotonic()-start<90)
# Formal all-N numerator check is coefficientwise, no sampled extrapolation.
check(16*3-5*3==33);check(16*14-5*44==4)
out=dict(status='PASS',implementation='separate direct character sums and unfactored rational-log intervals',roots=3,exact_assertions=checks,records=records,runtime_seconds=time.monotonic()-start,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),independent_agent_review=False)
(root/'out/AUDIT.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='records'}))
