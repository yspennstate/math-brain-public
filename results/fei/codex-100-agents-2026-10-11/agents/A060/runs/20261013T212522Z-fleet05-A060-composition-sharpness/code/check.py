from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict,Counter
from itertools import combinations
import json,time,sys,hashlib
R=Path(__file__).resolve().parents[1];(R/'out').mkdir(exist_ok=True)
PILOT='--pilot' in sys.argv;start=time.perf_counter();assertions=0
def ck(c):
 global assertions
 assertions+=1
 assert c,assertions
def fac(n):
 d=Counter();j=2
 while j*j<=n:
  while n%j==0:d[j]+=1;n//=j
  j+=1
 if n>1:d[n]+=1
 return d
def logq(v):
 d=Counter(fac(v.numerator));d.subtract(fac(v.denominator));return {p:Q(k) for p,k in d.items() if k}
def add(*terms):
 d=defaultdict(Q)
 for c,v in terms:
  for p,e in v.items():d[p]+=c*e
 return {p:e for p,e in d.items() if e}
def ent(vs):return add(*[(-v,logq(v)) for v in vs if v])
def phi(a,b):return add((1,ent([a,b])),(-1,ent([a+b])))
def transform(vals):
 a=list(vals);N=len(a);h=1
 while h<N:
  for k in range(0,N,2*h):
   for j in range(k,k+h):u,v=a[j],a[j+h];a[j],a[j+h]=u+v,u-v
  h*=2
 return a
def prime_sign(d):
 # Clear rational denominators, then compare two positive integers exactly.
 from math import lcm
 den=1
 for v in d.values():den=lcm(den,v.denominator)
 ee={p:int(v*den) for p,v in d.items() if v}
 num=1;bot=1
 for p,e in ee.items():
  if e>0:num*=p**e
  else:bot*=p**(-e)
 return (num>bot)-(num<bot),ee,num.bit_length(),bot.bit_length()
sigcache={};stats=[];extremizers=[];failures=[]
def census(n,tables,kind):
 N=1<<n;counts=Counter();maxbits=0
 for index,vals in enumerate(tables):
  w=transform(vals);ck(w[0]==0);ck(sum(t*t for t in w)==N*N)
  S=tuple(sorted(abs(w[1<<i]) for i in range(n)))
  E=sum(vals[u]!=vals[u^(1<<i)] for i in range(n) for u in range(N) if not u>>i&1)
  D=2*N*E-N*N
  ck(D==sum(s.bit_count()*w[s]**2 for s in range(N))-N*N)
  ck(D>=0)
  key=(n,S,D)
  if key not in sigcache:
   exp=Counter({2:2*n*sum(t*t for t in S)-3*D})
   for t in S:
    if t:
     for p,e in fac(t).items():exp[p]-=2*t*t*e
   sign,ee,nb,db=prime_sign({p:Q(e) for p,e in exp.items() if e})
   sigcache[key]={'sign':sign,'exponents':ee,'numerator_bits':nb,'denominator_bits':db}
  cert=sigcache[key];maxbits=max(maxbits,cert['numerator_bits'],cert['denominator_bits'])
  if D==0:
   ck(cert['sign']==0);counts['dictators']+=1
  elif cert['sign']>0:
   counts['violations']+=1
   if len(failures)<10:failures.append({'n':n,'kind':kind,'mask':sum((v==1)<<u for u,v in enumerate(vals)),'singleton_W':S,'deficit_scaled':D,'certificate':cert})
  elif cert['sign']==0:
   counts['equalities']+=1
   occupied=[s for s,v in enumerate(w) if v]
   singles=[s for s in occupied if s.bit_count()==1]
   maj3=len(occupied)==4 and len(singles)==3
   if maj3:
    triple=singles[0]|singles[1]|singles[2]
    ck(triple in occupied and all(abs(w[s])==N//2 for s in occupied))
    ck(w[triple]==-Q(w[singles[0]]*w[singles[1]]*w[singles[2]],(N//2)**2))
   extremizers.append({'n':n,'kind':kind,'mask':sum((v==1)<<u for u,v in enumerate(vals)),'majority3_junta':maj3,'singleton_W':S,'deficit_scaled':D})
  else:counts['strict']+=1
  counts['cases']+=1
  if time.perf_counter()-start>(60 if PILOT else 180):raise RuntimeError('frozen watchdog')
 stats.append({'n':n,'kind':kind,**counts,'max_integer_certificate_bits':maxbits})
 # Save each completed census immediately, before the next phase.
 (R/'out'/('pilot_census.json' if PILOT else 'census.json')).write_text(json.dumps({'stats':stats,'extremizers':extremizers,'failures':failures},indent=2))
def balanced(n):
 N=1<<n
 for plus in combinations(range(N),N//2):
  vals=[-1]*N
  for u in plus:vals[u]=1
  yield vals
def odd5():
 for mask in range(512 if PILOT else 1<<16):
  v=[1 if mask>>u&1 else -1 for u in range(16)]
  yield v+[-v[31-u] for u in range(16,32)]
for n in range(1,4 if PILOT else 5):census(n,balanced(n),'balanced')
census(5,odd5(),'antipodally_odd')

caprecords=[]
def metrics(v):
 N=len(v);n=N.bit_length()-1;w=transform(v);p=[Q(a*a,N*N) for a in w]
 ck(sum(p)==1)
 inf=[sum(p[s] for s in range(N) if s>>i&1) for i in range(n)]
 bi=[add(*[(1,phi(p[s],p[s|(1<<i)])) for s in range(N) if not s>>i&1]) for i in range(n)]
 return w,p,inf,bi,ent(p)
for m in ([2,4] if PILOT else [2,4,6,8]):
 N=1<<m;delta=Q(1,N);r=Q(1,1<<(m//2))
 bent=[(-1)**sum(((y>>j)&1)*((y>>(j+1))&1) for j in range(0,m,2)) for y in range(N)]
 g=[bent[u>>1] if not u&1 else -bent[u>>1]+2*((u>>1)==0) for u in range(2*N)]
 w,ps,inf,bs,hg=metrics(g);ck(inf[0]==1-delta);ck(inf[1:]==[Q(1,2)+delta]*m);ck(Q(w[0],2*N)==delta)
 a=[Q(w[2*s],2*N) for s in range(N)];b=[Q(w[2*s+1],2*N) for s in range(N)]
 ck(a==[delta]*N);ck(sorted(Counter(b).values())==sorted([(N+(1<<(m//2)))//2,(N-(1<<(m//2)))//2]))
 B=bs[0]
 for x in [Q(1,4),Q(1,16),Q(9,16)]:
  L=add(*[(1,phi(a[s]**2,x*b[s]**2)) for s in range(N)])
  loss=add((1,B),(-1,L));upper=add((-delta,logq(x)))
  ck(prime_sign(loss)[0]>0);ck(prime_sign(add((1,upper),(-1,loss)))[0]>0)
  # At fixed x, a uniform positive gap factor cannot follow from |alpha|<1.
  caprecords.append({'m':m,'x':str(x),'B_prime_logs':{str(p):str(v) for p,v in B.items()},'L_prime_logs':{str(p):str(v) for p,v in L.items()},'loss_upper':str(delta)+'*log2(1/x)'})
 if m<=6:
  vals=[]
  for u in range(1<<(m+3)):
   signs=[1-2*((u>>j)&1) for j in range(3)];hh=1 if sum(signs)>0 else -1;y=u>>3
   vals.append(1 if y==0 else hh*bent[y])
  ww,pp,ii,bb,hf=metrics(vals)
  L=add(*[(1,phi(a[s]**2,Q(1,4)*b[s]**2)) for s in range(N)])
  for i in range(3):ck(bb[i]==L);ck(ii[i]==Q(1,2)*(1-delta));ck(Q(ww[1<<i],len(vals))==Q(1,2)*(r-delta))
  ck(hf==add((1,hg),(2*(1-delta),{2:Q(1)})))
  ck(sum(ii)==sum(inf)+Q(1,2)*(1-delta))
 # A spectator factor multiplies each a,b packet by its amplitudes;
 # check on a bent 2-bit spectator, whose four squared masses equal 1/4.
 x=Q(1,4);L=add(*[(1,phi(a[s]**2,x*b[s]**2)) for s in range(N)])
 ck(add(*[(1,phi(a[s]**2/4,x*b[s]**2/4)) for s in range(N) for _ in range(4)])==L)
 ck(add(*[(1,phi(a[s]**2/4,b[s]**2/4)) for s in range(N) for _ in range(4)])==B)
(R/'out'/('pilot_caps.json' if PILOT else 'caps.json')).write_text(json.dumps(caprecords,indent=2))
out={'status':'PASS' if not failures else 'COUNTEREXAMPLE','assertions':assertions,'runtime_seconds':time.perf_counter()-start,'censuses':stats,'unique_certificate_signatures':len(sigcache),'cap_examples':len(caprecords),'physical_Maj3_compositions':2 if PILOT else 3,'scope':'finite census only; all-dimensional cap asymptotic proved analytically'}
(R/'out'/('pilot.json' if PILOT else 'validation.json')).write_text(json.dumps(out,indent=2))
if not PILOT:(R/'out'/'integer_certificates.json').write_text(json.dumps([{'n':n,'singleton_W':ss,'deficit_scaled':d,**v} for (n,ss,d),v in sigcache.items()],indent=2))
print(json.dumps(out))
