"""Frozen exact finite checks; the all-k escape is analytic, not extrapolated."""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import sys,json,time,hashlib
import exact_utils as x
R=Path(__file__).resolve().parents[1]
START=time.monotonic(); PILOT='--pilot' in sys.argv; COUNT=0
def ck(b):
 global COUNT
 COUNT+=1
 assert b,COUNT
 if time.monotonic()-START>55:raise RuntimeError('55 second frozen cap')
def partial(ms,den):
 r=x.const(F(sum(ms),den)*(den.bit_length()-1))
 for z in ms:
  if z:r=x.plus(r,{p:-F(z*e,den) for p,e in x.factor(z).items()})
 return r
def measure(f):
 N=len(f);a=x.fwht(f);n=N.bit_length()-1
 ps=[F(sum(a[s]**2 for s in range(N) if s>>j&1),N*N) for j in range(n)]
 return a,ps,x.entropy([v*v for v in a],N*N)
def q(v):
 # All arguments here are dyadic; entropy contribution without normalization.
 return partial([v.numerator*v.numerator],v.denominator*v.denominator)
roots=[x.table(n,t) for n in range(3 if PILOT else 4) for t in range(1<<(1<<n))]
roundings=rankchecks=continuity=0
for f in roots:
 s=x.stats(f);n=s['n'];N=len(f);den=N*N
 # Independent threshold integral vs exhaustive actual parity bases, TWO E families.
 for E in [set(range(1,N)),set(1<<i for i in range(n))|({N-1} if n else set())]:
  cuts=sorted({F(0),F(1,2)}|{s['m'][v] for v in E})
  integ=sum(((b-a)*(n-(len(x.span(v for v in E if s['m'][v]<=a)).bit_length()-1)) for a,b in zip(cuts,cuts[1:])),F(0))
  admissible=[B for B in x.bases(n) if set(B)<=E]
  ck(integ==min(sum((s['m'][v] for v in B),F(0)) for B in admissible))
  chi=sum((max(F(0),2*p-1) for p in s['p']),F(0))
  gain=chi+sum(((b-a)*((len(x.span(v for v in E if s['m'][v]<=a)).bit_length()-1)-sum(s['m'][1<<j]<=a for j in range(n))) for a,b in zip(cuts,cuts[1:])),F(0))
  ck(gain==s['I']-integ);rankchecks+=1
 for m in range(n+1):
  means=[sum(f[y+(z<<m)] for z in range(1<<(n-m))) for y in range(1<<m)]
  g=tuple(1 if u>=0 else -1 for u in means)
  ga,gp,gh=measure(g);sg=x.stats(g)
  e=F(sum(f[y]!=g[y%len(g)] for y in range(N)),N)
  tail=[a*a for j,a in enumerate(s['a']) if j>=(1<<m)]
  delta=F(sum(tail),den);th=partial(tail,den)
  ti=F(sum(j.bit_count()*a*a for j,a in enumerate(s['a']) if j>=(1<<m)),den)
  ck(e<=delta/2)
  ck(abs(s['I']-sum(gp))<=m*delta+ti)
  ck(all(abs(s['p'][j]-gp[j])<=2*e for j in range(m)))
  probs=[F(a*a,den) for a in s['a']]
  gs=[F(a*a,len(g)**2) for a in ga]+[F(0)]*(N-len(g))
  tv=sum(abs(a-b) for a,b in zip(probs,gs))/2
  ck(tv*tv<=4*e<=2*delta)
  collapsed=x.entropy([a*a for a in s['a'][:1<<m]]+[sum(tail)],den)
  loss=x.sub(s['H'],collapsed)
  ck(x.nonneg(loss) and x.nonneg(x.sub(th,loss)))
  # Whole tail expression, including its delta log(delta) term.
  if delta:ck(loss==x.plus(th,{p:F(sum(tail)*ee,den) for p,ee in x.factor(sum(tail)).items()},x.const(-delta*(den.bit_length()-1))))
  else:ck(not loss)
  if m>=1 and delta<=F(1,8):
   B=1<<16;arg=2*delta*B*B;r=isqrt(arg.numerator//arg.denominator)
   if r*r<arg:r+=1
   eta=F(r,B);ck(eta*eta>=2*delta and eta<=F(1,2))
   budget=x.plus(th,x.entropy([r,B-r],B),x.const(m*eta))
   diff=x.sub(s['H'],gh)
   ck(x.nonneg(x.sub(budget,diff)) and x.nonneg(x.plus(budget,diff)))
   for K in [0,1,2,4]:
    d=x.sub(diff,x.const(K*(s['I']-sum(gp))))
    full=x.plus(budget,x.const(K*(ti+m*delta)))
    ck(x.nonneg(x.sub(full,d)) and x.nonneg(x.plus(full,d)))
    ck(x.nonneg(x.sub(x.sub(gh,x.const(K*sg['amin'])),x.sub(x.sub(s['H'],x.const(K*s['I'])),full))))
   continuity+=1
  roundings+=1

bent=tuple((-1)**(((z>>0)&1)*((z>>1)&1)) for z in range(4))
point=tuple(-1 if z==0 else 1 for z in range(8))
fixtures=[('bent',bent,1,2),('point3',point,1,2)]
if not PILOT:fixtures += [('bent',bent,2,2),('point3',point,2,2),('escape_bent_k2_t4',bent,4,2)]
records=[]
for name,g,t,k in fixtures:
 d=len(g).bit_length()-1;p=F(1,1<<k);mu=F(sum(g),len(g));nu=mu**t
 h=[]
 for z in range(1<<(d*t)):
  v=1
  for j in range(t):v*=g[(z>>(d*j))&((1<<d)-1)]
  h.append(v)
 f=tuple(h[z>>k] if z% (1<<k)==0 else 1 for z in range(1<<(k+d*t)))
 a,ps,H=measure(f);ha,hp,HH=measure(h);_,gpi,GH=measure(g)
 ck(HH==x.scale(t,GH));ck(sum(hp)==t*sum(gpi))
 ck(F(sum(f),len(f))==1-p*(1-nu));ck(sum(ps)==p*(t*sum(gpi)+k*(1-nu)))
 ck(F(sum((u-1)**2 for u in f),len(f))==2*p*(1-nu))
 formula=x.plus(x.scale(p*t,GH),q(1-p*(1-nu)),x.scale(-p,q(nu)),x.scale(p*(1-p),q(1-nu)),x.const(2*k*p*((1-nu*nu)+(1-p)*(1-nu)**2)))
 ck(H==formula)
 diff=x.sub(H,x.scale(p*t,GH));bd=x.const(p*(10*k+15))
 ck(x.nonneg(x.sub(bd,diff)) and x.nonneg(x.plus(bd,diff)))
 # Check EVERY activated directional cost using independent autocorrelation FWHT.
 N=len(f);ac=x.fwht([z*z for z in a]);hc=x.fwht([z*z for z in ha])
 for v in range(1,N):
  w=F(N*N-ac[v],2*N*N)
  want=p*(1-nu) if v% (1<<k) else p*F(len(h)**2-hc[v>>k],2*len(h)**2)
  ck(w==want)
  ck(min(w,1-w)>=max(ps[j] for j in range(k+d*t) if v>>j&1))
 support=[j for j,z in enumerate(a) if z]
 ck(len(x.span(j^support[0] for j in support))==N)
 records.append({'name':name,'n':k+d*t,'t':t,'k':k,'I':str(sum(ps)),'H':x.enc(H),'norm_error_squared':str(2*p*(1-nu))})

result={'status':'PASS','pilot':PILOT,'root_tables':len(roots),'roundings':roundings,'rank_family_checks':rankchecks,'small_tail_entropy_checks':continuity,'activation_fixtures':records,'assertions':COUNT+x.COUNT,'own_assertions':COUNT,'utility_assertions':x.COUNT,'runtime_seconds':time.monotonic()-START,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'utility_sha256':hashlib.sha256(Path(x.__file__).read_bytes()).hexdigest(),'arithmetic':'integer Walsh, physical errors, Fraction, prime-log identities and rational atanh intervals; no float sign decisions','limitations':'all-k escape and approximation bounds proved analytically; finite checks do not prove the universal pair selection'}
(R/'out'/('PILOT.json' if PILOT else 'CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='activation_fixtures'}))
