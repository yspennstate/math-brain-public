"""Independent character-sum/edge audit. Never imports or executes source helpers."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from collections import Counter
import sys,time,json,hashlib
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[1]
NTEST=0
def check(x):
 global NTEST
 NTEST+=1
 assert x,NTEST
def add(*a):return (sum((z[0] for z in a),F()),sum((z[1] for z in a),F()))
def scale(a,c):return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
def sub(a,b):return add(a,scale(b,-1))
def avg(a,b):return scale(add(a,b),F(1,2))
def pos(a):return max(F(),a[0]),max(F(),a[1])
def val(a):return F(a),F(a)
GRID=1<<112
def roundout(a,b):return F((a*GRID).__floor__(),GRID),F((b*GRID).__ceil__(),GRID)
@lru_cache(None)
def lnunit(x):
 check(1<=x<=2)
 z=(x-1)/(x+1);p=z;s=F()
 for j in range(40):s+=p/(2*j+1);p*=z*z
 return roundout(2*s,2*s+2*p/(81*(1-z*z)))
LN2=lnunit(F(2))
@lru_cache(None)
def lg(x):
 x=F(x);check(x>0)
 e=x.numerator.bit_length()-x.denominator.bit_length()
 u=x/F(2)**e
 if u<1:u*=2;e-=1
 lo,hi=lnunit(u)
 return roundout(e+lo/LN2[1],e+hi/LN2[0])
def entropy(p):return add(*(scale(lg(x),-x) for x in p if x))
def bh(x):return entropy((x,1-x))
def restrict(t,i,b):
 return tuple(v for x,v in enumerate(t) if (x>>i)&1==b)
@lru_cache(None)
def walsh(t):
 # Direct character dot products, not a fast Walsh transform.
 return tuple(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t)) for s in range(len(t)))
@lru_cache(None)
def stats(t):
 n=len(t).bit_length()-1
 p=tuple(F(a*a,len(t)**2) for a in walsh(t));check(sum(p)==1)
 d=tuple(F(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)) for i in range(n))
 for i in range(n):check(d[i]==sum((v for s,v in enumerate(p) if (s>>i)&1),F()))
 h=entropy(p);k=sub(add(*(bh(x) for x in d)),h)
 return p,d,h,k
def product(d):
 a=[F(1)]
 for x in d:a=[v*(1-x) for v in a]+[v*x for v in a]
 check(sum(a)==1)
 return a
REFONLY=0
@lru_cache(None)
def query(t,i):
 global REFONLY
 p,d,h,k=stats(t);c=[restrict(t,i,b) for b in (0,1)];ss=[stats(v) for v in c]
 # Erasure positions are independently constructed from sorted full masks.
 buckets=[(s,s|(1<<i)) for s in range(len(t)) if not (s>>i)&1]
 q=[p[a]+p[b] for a,b in buckets]
 qe=product(d[:i]+d[i+1:]);r=[F(),F()];z=F()
 for s,m in enumerate(q):
  ks=[ss[b][0][s]/(2*m) if m else F(1,2) for b in (0,1)]
  check(sum(ks)==1)
  if not m:z+=qe[s]
  for b in (0,1):r[b]+=qe[s]*ks[b]
 check(sum(r)==1 and min(r)>0)
 REFONLY+=bool(z)
 o=scale(lg(4*r[0]*r[1]),-F(1,2));debit=sub(add(o,avg(ss[0][3],ss[1][3])),k)
 drop=sub(h,avg(ss[0][2],ss[1][2]))
 j=sub(entropy(q),avg(ss[0][2],ss[1][2]));b=sub(h,entropy(q))
 gap=sub(add(*(bh(x) for l,x in enumerate(d) if l!=i)),avg(add(*(bh(x) for x in ss[0][1])),add(*(bh(x) for x in ss[1][1]))))
 other=sub(sub(add(o,b,j),bh(d[i])),gap)
 check(max(debit[0],other[0])<=min(debit[1],other[1]))
 # Conditional physical influence conservation checked per untouched label.
 for l in range(len(d)):
  if l!=i:check(d[l]==(ss[0][1][l-(l>i)]+ss[1][1][l-(l>i)])/2)
 return c,debit,o,z
@lru_cache(None)
def tail(t):
 best=val(0)
 for i in range(len(t).bit_length()-1):
  c,d,o,z=query(t,i);v=add(pos(d),avg(tail(c[0]),tail(c[1])))
  best=max(best[0],v[0]),max(best[1],v[1])
 return best
def compose(v):
 return tuple(-1 if x&1==0 and x&2 else v[x>>3] if x&1 and x&4 else 1 for x in range(64))
def serial(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {k:serial(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [serial(v) for v in x]
 return x
def priority(pilot):
 global REFONLY
 start=time.perf_counter();src=Path('agents/A061/runs/20261014T085352Z-fleet05-A061-entropy-process/out/EXHAUSTIVE_CHECK.json')
 raw=src.read_bytes();check(hashlib.sha256(raw).hexdigest()=='6c48a94c44b030dfb851f33d99024e9fa91c7761dbfbd1bee400aa01862d2582')
 roots={}
 for r in json.loads(raw)['records']:
  v=tuple(F(x) for x in r['first_conversion_signed']);m=r['mask']
  if m in roots:check(roots[m]==v)
  roots[m]=v
 rows=[];states=queries=0
 for m in ([0,255,25,235] if pilot else range(256)):
  v=tuple(1 if (m>>s)&1 else -1 for s in range(8));t=compose(v);c=[restrict(t,1,b) for b in (0,1)]
  owner=avg(*(sub(val(4*sum(stats(v)[1],F())),stats(v)[2]) for v in c))
  w=add(pos(roots[m]),avg(*(tail(v) for v in c)))
  check(owner[0]>0);check(20*w[1]<owner[0])
  rows.append({'mask':m,'owner':owner,'booking':w,'ratio_upper':w[1]/owner[0]})
  states+=tail.cache_info().currsize;queries+=query.cache_info().currsize
  for f in [tail,query,stats,walsh]:f.cache_clear()
  check(time.perf_counter()-start<55)
 return {'domain':len(rows),'states':states,'queries':queries,'reference_only_queries':REFONLY,'max_ratio':max(r['ratio_upper'] for r in rows),'records':rows,'seconds':time.perf_counter()-start}
def bent(x,k):return -1 if sum(((x>>i)&1)*((x>>(i+1))&1) for i in range(0,k,2))%2 else 1
def profile(k,odd=False):
 out=[]
 for z in range(1<<(k+1+int(odd))):
  y=z&1 if odd else 0;x=(z>>1)&((1<<k)-1) if odd else z&((1<<k)-1);w=z>>(k+int(odd))
  out.append(bent(x,k)*(-1 if w and x==0 and y==0 else 1))
 return tuple(out)
def closed(k,odd=False):
 n=1<<k;r=1<<(k//2);a=(n+r)//2;b=(n-r)//2
 return ([(2*r-1,a),(2*r+1,b),(1,3*n)],2*n) if odd else ([(r-1,a),(r+1,b),(1,n)],n)
def closedh(items,den):
 check(sum(a*a*c for a,c in items)==den*den)
 return add(*(scale(lg(F(a*a,den*den)),-F(a*a*c,den*den)) for a,c in items if a and c))
@lru_cache(None)
def tree(t,C):
 if len(t)==1:return val(0)
 c=[restrict(t,0,b) for b in (0,1)]
 p,d,h,k=stats(t)
 return pos(add(sub(sub(h,avg(stats(c[0])[2],stats(c[1])[2])),val(C*d[0])),avg(tree(c[0],C),tree(c[1],C))))
def profiles(pilot):
 start=time.perf_counter();rows=[];qe={0:val(0)};C=F(6)
 for j in range(0,(4 if pilot else 12)+1,2):
  eo=closed(j);oo=closed(j,True);he=closedh(*eo);ho=closedh(*oo)
  do=sub(ho,avg(he,val(j)));qo=pos(add(sub(do,val(C/F(2*(1<<j)))),scale(qe[j],F(1,2))))
  if j>=2:check(do[1]<F(15,16));check(qo[1]<=F(15,16))
  if j+2<=(4 if pilot else 12):
   k=j+2;h=closedh(*closed(k));de=sub(h,avg(ho,val(j)))
   qe[k]=pos(add(sub(de,val(C*(F(1,2)+F(1,1<<k)))),scale(qo,F(1,2))))
   check(qe[k]==val(0))
  if j==0:continue
  for odd in [False,True]:
   t=profile(j,odd);items,den=closed(j,odd)
   # Independent direct character enumeration up to k6; higher widths use exact multiplicity norm and analytic proof.
   if j<=6:
    count=Counter(abs(x)*den//len(t) for x in walsh(t) if x)
    want=Counter()
    for a,c in items:
     if a and c:want[a]+=c
    check(count==want)
    dt=F(sum(t[z]!=t[z^1] for z in range(len(t))),len(t))
    check(dt==(F(1,2*(1<<j)) if odd else F(1,2)+F(1,1<<j)))
  if j<=6:check(tree(profile(j),C)==val(0))
  n=1<<j;r=1<<(j//2);np=(n+r)//2;nm=(n-r)//2
  hv=closedh([(r-2,np),(r+2,nm)],n);dw=sub(he,avg(val(j),hv))
  check((r-1)**2+1>F(n,4))
  eps=sub(add(dw,val(F(2,n))),val(F(32609,5000)*F(5,2*n)))
  check(eps[0]>F(1,n)*(j-F(32609,5000)*F(5,2)))
  if j==10:check(eps[0]>F(1,100000))
  if j==2:check(ho[0]>2)
  if j>=4:check(ho[0]>j-F(1,2))
  rows.append({'k':j,'E_reserve_at6':qe[j],'H_E':he,'H_O':ho,'tag_drop':dw,'epsilon_6_5218':eps})
  for f in [stats,walsh,tree]:f.cache_clear()
  check(time.perf_counter()-start<55)
 # Explicit rational side conditions for the all-width induction.
 check(F(303,128)-3+F(15,32)==-F(21,128))
 check(F(45,16)<3);check(81**2<2*64**2);check(3**5<2**8);check(5**3<2**7)
 return {'widths':len(rows),'records':rows,'seconds':time.perf_counter()-start}
if __name__=='__main__':
 mode=sys.argv[1];pilot='--pilot' in sys.argv
 result=priority(pilot) if mode=='priority' else profiles(pilot)
 result.update(status='PASS',exact_assertions=NTEST,helper='a087-independent-referee-v1',pilot=pilot)
 name=mode.upper()+('_PILOT' if pilot else '')+'.json'
 (ROOT/'out'/name).write_text(json.dumps(serial(result),indent=2)+'\n',encoding='utf-8')
 print(json.dumps(serial({k:v for k,v in result.items() if k!='records'})))
