from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict,Counter
from functools import lru_cache
from math import comb
import time,json
ROOT=Path(__file__).resolve().parents[1];start=time.perf_counter();assertions=0
def ck(x):
 global assertions
 assert x
 assertions+=1
def clockguard():
 if time.perf_counter()-start>60:raise RuntimeError('frozen 60-second runtime exceeded')
def fw(a):
 a=a[:];step=1
 while step<len(a):
  for i in range(0,len(a),2*step):
   for j in range(step):
    x,y=a[i+j],a[i+j+step];a[i+j],a[i+j+step]=x+y,x-y
  step*=2
 return a
def prob(values):
 N=len(values);return [F(w*w,N*N) for w in fw(values)]
@lru_cache(None)
def factor(n):
 out=[];p=2
 while p*p<=n:
  k=0
  while n%p==0:n//=p;k+=1
  if k:out.append((p,k))
  p+=1
 if n>1:out.append((n,1))
 return tuple(out)
def atom(out,c,x):
 x=F(x)
 for p,k in factor(x.numerator):out[p]+=c*k
 for p,k in factor(x.denominator):out[p]-=c*k
def add(*terms):
 out=defaultdict(F)
 for scale,d in terms:
  for p,v in d.items():out[p]+=scale*v
 return {p:v for p,v in out.items() if v}
def equal(a,b):ck(not add((1,a),(-1,b)))
def entropy(p):
 out=defaultdict(F)
 for x,k in Counter(p).items():
  if x:atom(out,-k*x,x)
 return {p:v for p,v in out.items() if v}
def kl(p,q):
 out=defaultdict(F)
 for x,y in zip(p,q):
  if x:
   ck(y>0);atom(out,x,x/y)
 return {p:v for p,v in out.items() if v}
def marg(p,n):return [sum(x for s,x in enumerate(p) if s&(1<<i)) for i in range(n)]
def prod(d):
 return [__import__('functools').reduce(lambda a,b:a*b,(x if s&(1<<i) else 1-x for i,x in enumerate(d)),F(1)) for s in range(1<<len(d))]
def tc(p,n):return add((1,entropy(prod(marg(p,n)))),(-1,entropy(p)))
def expand(s,bits):return sum(((s>>j)&1)<<i for j,i in enumerate(bits))
def children(values,n,B):
 C=[i for i in range(n) if i not in B]
 return [[values[expand(t,C)|expand(y,B)] for t in range(1<<len(C))] for y in range(1<<len(B))]
def block(values,n,B):
 p=prob(values);C=[i for i in range(n) if i not in B];Nchild=1<<len(C)
 child=[prob(v) for v in children(values,n,B)];w=len(child)
 q=[];M=[];ch=[];level=defaultdict(F)
 for t in range(Nchild):
  row=[p[expand(t,C)|expand(u,B)] for u in range(1<<len(B))];mass=sum(row);q.append(mass)
  Mi=defaultdict(F);Ci=defaultdict(F)
  if mass:
   for x in row:
    if x:atom(Mi,x,mass/x)
   for py in child:
    if py[t]:atom(Ci,py[t]/w,py[t]/mass)
  M.append(dict(Mi));ch.append(dict(Ci))
 for u in range(1,1<<len(B)):
  x=p[expand(u,B)]
  if x:atom(level,-x,x)
 ck(all(sum(py)==1 for py in child));ck(sum(q)==1)
 equal(add((1,entropy(p[1:])),*[(F(-1,w),entropy(py[1:])) for py in child]),add(*[(1,x) for x in M[1:]],*[(1,x) for x in ch[1:]],(1,dict(level))))
 return p,child,q,M,ch,dict(level)
def reset(values,n,i,result):
 p,child,q,M,ch,level=result;d=marg(p,n);res=[j for j in range(n) if j!=i];dc=[marg(py,n-1) for py in child]
 G=add(*[(1,entropy([d[j],1-d[j]])) for j in res],*[(F(-1,2),entropy([dj,1-dj])) for dy in dc for dj in dy])
 B=add(*[(1,x) for x in M]);J=add(*[(1,x) for x in ch]);hi=entropy([d[i],1-d[i]])
 equal(tc(p,n),add((1,hi),(-1,B),(-1,J),(1,G),*[(F(1,2),tc(py,n-1)) for py in child]))
 R=prod([d[j] for j in res]);k=[[child[y][t]/(2*q[t]) if q[t] else F(1,2) for t in range(len(q))] for y in range(2)]
 QY=[sum(R[t]*k[y][t] for t in range(len(q))) for y in range(2)];ck(sum(QY)==1)
 Bayes=[[R[t]*k[y][t]/QY[y] for t in range(len(q))] for y in range(2)]
 Dout=kl([F(1,2)]*2,QY);QKL=[kl(py,Bayes[y]) for y,py in enumerate(child)]
 equal(kl(q,R),add((1,Dout),*[(F(1,2),z) for z in QKL]))
 delta=defaultdict(F)
 for y in range(2):
  Ry=prod(dc[y])
  for t,x in enumerate(child[y]):
   if x:atom(delta,x/2,Bayes[y][t]/Ry[t])
 equal(dict(delta),add((1,Dout),(1,J),(-1,G)))
 return G,J,dict(delta),Dout
# Rational natural logarithm intervals; exact range reduction and proved tail.
@lru_cache(None)
def ln(x):
 x=F(x);k=0
 while x<1:x*=2;k-=1
 while x>=2:x/=2;k+=1
 def core(a):
  z=(a-1)/(a+1);l=2*sum((z**(2*j+1)/F(2*j+1) for j in range(20)),F(0));h=l+2*z**41/(41*(1-z*z));return l,h
 l,h=core(x);l2,h2=core(F(2));return (l+k*l2,h+k*h2) if k>=0 else (l+k*h2,h+k*l2)
ln2=ln(F(2))
def interval(logmap,bits=False):
 l=h=F(0)
 for p,c in logmap.items():
  lo,hi=ln(F(p))
  l+=c*(lo if c>=0 else hi);h+=c*(hi if c>=0 else lo)
 if bits:return min(l/ln2[0],l/ln2[1]),max(h/ln2[0],h/ln2[1])
 return l,h
def lowerstr(x):
 y=F((x*10**12).__floor__(),10**12);return str(y)
tables=blocks=splits=0
for n in range(4):
 N=1<<n
 for truth in range(1<<N):
  v=[1-2*((truth>>x)&1) for x in range(N)];tables+=1
  p=prob(v);ck(sum(p)==1)
  for Bmask in range(1,1<<n):
   B=[i for i in range(n) if Bmask&(1<<i)];r=block(v,n,B);blocks+=1
   if len(B)==1:
    reset(v,n,B[0],r);splits+=1
  clockguard()
ck(tables==278);ck(blocks==1844);ck(splits==804)
padroots=prefixes=0;pad_min=None
Alower=1+6/ln2[1]
for m in range(1,4):
 for truth in range(1<<(1<<m)):
  g=[1-2*((truth>>x)&1) for x in range(1<<m)];s=g[0];pg=prob(g);Hg=entropy(pg);I_g=sum(marg(pg,m))
  F0=g[:];F0[0]=-F0[0]
  for r in range(1,4):
   v=[g[x&((1<<m)-1)] for x in range(1<<(m+r))];v[0]=-v[0];p=prob(v);H=entropy(p);d=F(1,1<<(m+r-1));ds=marg(p,m+r);Icore=sum(ds[:m]);padroots+=1
   ck(all(x==d for x in ds[m:]));ck(m*d<=Icore)
   oriented=[s*F(w,1<<m) for w in fw(g)];W=fw(v)
   for label in range(1<<(m+r)):
    expected=(oriented[label&((1<<m)-1)] if label>>m==0 else F(0))-d
    ck(s*F(W[label],1<<(m+r))==expected)
   for queried in range(1,r+1):
    left=r-queried;active=[g[x&((1<<m)-1)] for x in range(1<<(m+left))];active[0]=-active[0];pa=prob(active);weight=F(1,1<<queried)
    Q=add((1,H),(-(1-weight),Hg),(-weight,entropy(pa)));Ileaf=(1-weight)*I_g+weight*sum(marg(pa,m+left))
    ck(sum(ds)==queried*d+Ileaf)
    l,h=interval(Q,bits=True);margin=4*queried*d+Alower*Icore-h;ck(margin>=0)
    pad_min=margin if pad_min is None else min(pad_min,margin);prefixes+=1
   clockguard()
ck(padroots==828)
majority=[]
for n in [1,3,5,7]:
 v=[1 if x.bit_count()<n/2 else -1 for x in range(1<<n)];p=prob(v);alpha=F(comb(n-1,(n-1)//2),1<<(n-1))
 for i in range(n):
  _,child,q,M,C,level=block(v,n,[i]);equal(add(*[(1,x) for x in M]),{});equal(add(*[(1,x) for x in C]),{})
  ck(marg(p,n)[i]==alpha);target=entropy([alpha*alpha]);equal(level,target)
 majority.append({'n':n,'alpha':str(alpha),'full_erasure_and_channel':'0','positive_heat_drop':n>=3})
addresses=[]
for a,r in [(1,1),(1,2),(2,1),(2,2)]:
 k=a+(1<<a);D=k+r;delta=F(1,1<<D);A=F(1,1<<a);Mcount=1<<(2*a)
 v=[1-2*((x>>(a+(x&((1<<a)-1))))&1) for x in range(1<<D)];v[0]=-v[0];p=prob(v)
 ck(sum(marg(p,D))==1+F(a,2)+2*delta*(D-2))
 for b in range(1,r+1):
  B=list(range(k,k+b));_,child,q,Mc,Cc,lev=block(v,D,B);w=1<<b;s=4*delta*delta
  for t in range(1<<(D-b)):
   z=F(fw([1-2*((x>>(a+(x&((1<<a)-1))))&1) for x in range(1<<k)])[t],1<<k) if t<(1<<k) else F(0)
   xz=(z-2*delta)**2;qz=xz+(w-1)*s;cz=(z-2*w*delta)**2
   ck(q[t]==qz);ck(child[0][t]==cz);ck(all(py[t]==z*z for py in child[1:]))
   mm=defaultdict(F);cc=defaultdict(F)
   if xz:atom(mm,xz,qz/xz)
   atom(mm,(w-1)*s,qz/s)
   if cz:atom(cc,cz/w,cz/qz)
   if z:atom(cc,(1-F(1,w))*z*z,z*z/qz)
   equal(Mc[t],dict(mm));equal(Cc[t],dict(cc))
  equal(lev,{p:c*(w-1) for p,c in entropy([s]).items()})
 addresses.append({'a':a,'r':r,'block_sizes':list(range(1,r+1))})
# Exact block-tree budget counterexample: one complete block, point defect n128.
n=128
ln2lower=2*sum((F(1,3)**(2*j+1)/F(2*j+1) for j in range(3)),F(0));ck(ln2lower>F(693,1000))
# e>1+1+1/2+1/6=8/3 implies 2+2/e<11/4.
rate_lower=4*F(n-1,n)*(1-F(1,1<<n))*ln2lower
gap=rate_lower-F(11,4);ck(gap>0)
certificate={'Boolean_family':'f=1-2 indicator{x=all plus} on n128','tree':'one node revealing all128 coordinates; constant leaves','I':'256/2^128','channel_plus_level_rate_exact':'4*(127/128)*(1-2^-128)*ln(2)','claimed_rate':'2+2/e','ln2_lower':str(ln2lower),'e_lower':'8/3 strict','claimed_rate_upper':'11/4 strict','gap_lower_exact':str(gap),'gap_lower_rounded':lowerstr(gap)}
(ROOT/'out/A066_BLOCK_SCOPE_CERTIFICATE.json').write_text(json.dumps(certificate,indent=2),encoding='utf-8')
# Fixed real controls: normalized amplitudes, fair singleton children, and failed Boolean level price.
real=[F(1,2)]*4 # four singleton Fourier amplitudes, each square1/4
ck(sum(x*x for x in real)==1)
level_real=entropy([F(1,4)]);level_lower=interval(level_real)[0]/F(1,4)
ck(level_lower>F(3,4)) # 2/e<3/4, but level/d=ln4>3/4.
# Exact product-TC monotonic sign controls, independent Walsh of K4/triangle.
def quad(n):return [(-1)**sum(((x>>i)&1)*((x>>j)&1) for i in range(n) for j in range(i+1,n)) for x in range(1<<n)]
for n,sign in [(4,1),(3,-1)]:
 p,child,_,_,_,_=block(quad(n),n,[0]);change=add(*[(F(1,2),tc(py,n-1)) for py in child],(-1,tc(p,n)))
 equal(change,{2:F(sign)})
out={'status':'PASS','assertions':assertions,'runtime_seconds':time.perf_counter()-start,'small_tables':tables,'physical_blocks':blocks,'coherent_singleton_splits':splits,'padding_roots':padroots,'padding_prefixes':prefixes,'padding_reserve_min_margin_lower':lowerstr(pad_min),'majority':majority,'addressing':addresses,'block_scope_certificate':'A066_BLOCK_SCOPE_CERTIFICATE.json','nonBoolean_singleton_level_price':'fails; ln4>2/e','TC_monotonicity_controls':'K4 +1bit; triangle -1bit'}
(ROOT/'out/VALIDATION.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
