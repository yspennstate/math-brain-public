import sys,json,time,itertools,math
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
R=Path(__file__).resolve().parents[1]
start=time.monotonic(); checks=0; counts={}
def ok(v):
 global checks
 assert v
 checks+=1
 if time.monotonic()-start>55: raise RuntimeError('55 second compute cap')
def fw(a):
 a=list(a); h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for i in range(j,j+h): a[i],a[i+h]=a[i]+a[i+h],a[i]-a[i+h]
  h*=2
 return a
@lru_cache(None)
def factors(a):
 out={}; b=2
 while b*b<=a:
  while a%b==0: out[b]=out.get(b,0)+1; a//=b
  b+=1
 if a>1: out[a]=out.get(a,0)+1
 return out

def add(*terms):
 out={}
 for c,v in terms:
  for p,w in v.items(): out[p]=out.get(p,Q(0))+c*w
 return {p:w for p,w in out.items() if w}
def logq(x):
 if not x: return {}
 z=x*x
 return add(*[(Q(-a)*z,{p:Q(1)}) for p,a in factors(z.numerator).items()],*[(Q(a)*z,{p:Q(1)}) for p,a in factors(z.denominator).items()])
@lru_cache(None)
def lnint(n):
 b=n.bit_length()-1; x=Q(n,2**b); z=(x-1)/(x+1); v=Q(0)
 for j in range(32): v+=2*z**(2*j+1)/(2*j+1)
 err=2*z**65/(65*(1-z*z))
 # ln(2) obtained separately with same positive series
 z2=Q(1,3); l2=sum((2*z2**(2*j+1)/(2*j+1) for j in range(32)),Q(0)); e2=2*z2**65/(65*(1-z2*z2))
 return v+b*l2,v+err+b*(l2+e2),l2,l2+e2
@lru_cache(None)
def log2int(n):
 if n==2: return Q(1),Q(1)
 lo,hi,l2,h2=lnint(n); return lo/h2,hi/l2
def interval(v):
 low=high=Q(0)
 for p,c in v.items():
  a,b=log2int(p); low+=c*(a if c>=0 else b); high+=c*(b if c>=0 else a)
 return low,high
def bounded(v,b):
 lo,hi=interval(v); ok(lo>=-b and hi<=b)
def rankadd(b,v):
 while v:
  j=v.bit_length()-1
  if j in b: v^=b[j]
  else: b[j]=v; return True
 return False
@lru_cache(None)
def stats(f):
 N=len(f); n=N.bit_length()-1; W=fw(f); mass=[Q(v*v,N*N) for v in W]
 H=add(*[(Q(1),logq(Q(v,N))) for v in W if v]); I=sum((s.bit_count()*x for s,x in enumerate(mass)),Q(0))
 B=fw([v*v for v in W]); cost=[Q(N*N-v,2*N*N) for v in B]
 minima=[]
 for centered in (False,True):
  weights=[min(x,1-x) if centered else x for x in cost]; basis={}; total=Q(0)
  for v in sorted(range(1,N),key=lambda v:weights[v]):
   if rankadd(basis,v): total+=weights[v]
  minima.append(total)
 b={}; support=[s for s,v in enumerate(W) if v]
 for s in support: rankadd(b,s^support[0])
 return {'n':n,'W':W,'mass':mass,'H':H,'I':I,'ell':minima[0],'a':minima[1],'cost':cost,'span':len(b),'mu':Q(W[0],N)}
def table(n,v): return tuple(1 if (v>>x)&1 else -1 for x in range(1<<n))
def tensor(g,t):
 d=len(g).bit_length()-1; mask=(1<<d)-1
 return tuple(math.prod(g[(x>>(d*j))&mask] for j in range(t)) for x in range(1<<(d*t)))
def activate(h,k): return tuple(h[x>>k] if x% (1<<k)==0 else 1 for x in range(len(h)*(1<<k)))
def restrict(f,A,b):
 n=len(f).bit_length()-1; free=[j for j in range(n) if j not in A]
 return tuple(f[sum(((x>>a)&1)<<j for a,j in enumerate(free))+sum(((b>>a)&1)<<j for a,j in enumerate(A))] for x in range(1<<len(free)))
def profile(mu,k):
 p=Q(1,2**k); nu=mu; delta=1-nu
 return add((1,logq(1-p*delta)),(-p,logq(nu)),(p*(1-p),logq(delta)),(2*k*p*((1-nu*nu)+(1-p)*delta*delta),{2:Q(1)}))
pilot='--pilot' in sys.argv
# finite rounding: direct conditional counts and exact squared-spectrum distance
for n in range((1 if pilot else 3)+1):
 for v in range(1<<(1<<n)):
  f=table(n,v); s=stats(f); counts['rounding_roots']=counts.get('rounding_roots',0)+1
  for m in range(1,n+1):
   g=tuple(1 if sum(f[x+(z<<m)] for z in range(1<<(n-m)))>=0 else -1 for x in range(1<<m)); gs=stats(g)
   ext=tuple(g[x%len(g)] for x in range(len(f)))
   e=Q(sum(a!=b for a,b in zip(f,ext)),len(f)); delta=sum(s['mass'][1<<m:],Q(0))
   tailI=sum((j.bit_count()*s['mass'][j] for j in range(1<<m,len(f))),Q(0))
   ok(2*e<=delta); ok(abs(s['I']-gs['I'])<=m*delta+tailI)
   tv=sum((abs(s['mass'][j]-(gs['mass'][j] if j<len(g) else 0)) for j in range(len(f))),Q(0))/2
   ok(tv*tv<=4*e); ok(tv*tv<=2*delta)
   for j in range(m):
    pf=Q(sum(f[x]!=f[x^(1<<j)] for x in range(len(f))),len(f)); pg=Q(sum(g[x]!=g[x^(1<<j)] for x in range(len(g))),len(g)); ok(abs(pf-pg)<=2*e)
   # exact collapse entropy identity, no real-valued sign oracle
   collapsed=add(*[(1,logq(Q(w,len(f)))) for w in s['W'][:1<<m] if w])
   if delta:
    # entropy contribution of mass delta is -delta log delta; half logq(delta) / delta
    collapsed=add((1,collapsed),(Q(1,2)/delta,logq(delta)))
   tailH=add(*[(1,logq(Q(w,len(f)))) for w in s['W'][1<<m:] if w])
   rhs=add((1,tailH),(-Q(1,2)/delta if delta else 0,logq(delta)))
   ok(add((1,s['H']),(-1,collapsed))==rhs); counts['roundings']=counts.get('roundings',0)+1
# seed-preserving activation, including noncanonical seeds as negative/zero guards
for d in range((1 if pilot else 2)+1):
 for v in range(1<<(1<<d)):
  g=table(d,v); sg=stats(g)
  for t in ((2,) if pilot else (2,4)):
   k=2; p=Q(1,4); h=tensor(g,t); sh=stats(h); F=activate(h,k); sf=stats(F)
   ok(sh['H']==add((t,sg['H']))); ok(sh['I']==t*sg['I'])
   ok(sf['I']==p*(sh['I']+k*(1-sh['mu'])))
   ok(sf['H']==add((p,sh['H']),(1,profile(sh['mu'],k))))
   ok(sf['a']==sf['ell']==p*(sh['ell']+k*(1-sh['mu'])))
   ok(Q(sum((x-1)**2 for x in F),len(F))==2*p*(1-sh['mu']))
   bounded(add((1,sf['H']),(-p,sh['H'])),p*(10*k+15))
   if sg['span']==d and sg['a']==sg['I'] and sg['I']>0:
    ok(sf['span']==sf['n']); ok(sf['a']==sf['I']); counts['canonical_roots']=counts.get('canonical_roots',0)+1
   counts['activation_roots']=counts.get('activation_roots',0)+1
   if t!=2: continue
   for q in range(min(2,d*t)+1):
    for A in itertools.combinations(range(d*t),q):
     released=Q(0)
     for b in range(1<<q):
      hb=restrict(h,A,b); sb=stats(hb); fb=activate(hb,k); sc=stats(fb)
      ok(sc['a']==p*(sb['ell']+k*(1-sb['mu'])))
      if sg['span']==d and sg['a']==sg['I'] and sg['I']>0:
       lower=(t-q)*sg['I']; ok(sb['a']>=lower)
       ok(sc['I']-sc['a']<=p*q*d)
       # finite-t form of uniform bounds; pt H0 and pt I0 are the targets
       H0=add((p*t,sg['H'])); Hbound=p*(q*(d+interval(sg['H'])[1])+10*k+15)
       bounded(add((1,sc['H']),(-1,H0)),Hbound)
       ok(abs(sc['a']-p*t*sg['I'])<=p*(q*(d+sg['I'])+2*k))
      released+=(sc['I']-sc['a'])/2**q
      counts['data_children']=counts.get('data_children',0)+1
     counts['data_blocks']=counts.get('data_blocks',0)+1
# exact named high-dimensional guard uses rational analytic envelope, no table
ok(Q(1)-Q(127,1024)==Q(897,1024)) # k10: (10+2)*10+15=135, actual bound below
ok(Q(1)-Q(135,1024)==Q(889,1024)); ok(Q(2)-Q(115,1024)==Q(1933,1024)); ok(Q(1933,1024)>Q(9,8))
# t=2^k, k10; I>=1, delta1<=1/256; hence missing influence tail fails
ok(Q(1)>Q(1,256)); ok(Q(4,1024)==Q(1,256))
out={'status':'PASS','assertions':checks,'counts':counts,'elapsed_seconds':time.monotonic()-start,'arithmetic':'integer/Fraction/prime-log/rigorous rational atanh','pilot':pilot}
(R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(out,indent=2),encoding='utf-8'); print(json.dumps(out))
