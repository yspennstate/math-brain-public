from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json,sys,time

run=Path(__file__).resolve().parents[1]
start=time.perf_counter(); checks=0
pilot='--pilot' in sys.argv
def ck(v):
 global checks
 checks+=1
 assert v,checks
def table(n,k):return [2*((k>>x)&1)-1 for x in range(1<<n)]
def subsets(s):
 t=s
 while True:
  yield t
  if not t:break
  t=(t-1)&s
def vp(p,s):
 v=F(1)
 for i,q in enumerate(p):
  if s>>i&1:v*=4*q*(1-q)
 return v
def data(tab,p):
 n=len(p); active=sum(1<<i for i,q in enumerate(p) if 0<q<1)
 poly=list(map(F,tab))
 for i in range(n):
  for s in range(1<<n):
   if s>>i&1:poly[s]-=poly[s^(1<<i)]
 c={}
 for s in subsets(active):
  z=F(0)
  for a in range(1<<n):
   if a&s!=s:continue
   v=poly[a]
   for i,q in enumerate(p):
    if (a^s)>>i&1:v*=q
   z+=v
  c[s]=z/F(2**s.bit_count())
 P={s:vp(p,s)*v*v for s,v in c.items()};ck(sum(P.values())==1)
 # Independent centered-moment reconstruction, without polynomial coefficients.
 for s in c:
  z=F(0)
  for x,f in enumerate(tab):
   v=F(f)
   for i,q in enumerate(p):
    v*=q if x>>i&1 else 1-q
    if s>>i&1:v*=(F((x>>i)&1)-q)/(2*q*(1-q))
   z+=v
  ck(z==c[s])
 j={};W={}
 for s,z in c.items():
  if not s or not z:continue
  ck(abs(z)<=1); u=abs(z);jj=0
  while u<=F(1,2):u*=2;jj+=1
  j[s]=jj;W[s]=vp(p,s)/F(4**jj)
 V=1-P[0];Z=sum(W.values(),F(0));Q={s:F(0) for s in P};Q[0]=P[0]
 if V:
  for s in W:Q[s]=V*W[s]/Z
 ck(sum(Q.values())==1)
 I=sum(s.bit_count()*v for s,v in P.items())
 return dict(p=p,c=c,P=P,j=j,W=W,V=V,Z=Z,Q=Q,I=I,D=I-V,J=sum(P[s]*v for s,v in j.items()))

@lru_cache(None)
def factors(n):
 d={};p=2
 while p*p<=n:
  while n%p==0:d[p]=d.get(p,0)+1;n//=p
  p=3 if p==2 else p+2
 if n>1:d[n]=d.get(n,0)+1
 return tuple(d.items())
def logs(terms):
 d={}
 for w,q in terms:
  q=F(q)
  if not w:continue
  assert q>0
  for sign,n in [(1,q.numerator),(-1,q.denominator)]:
   for p,k in factors(n):d[p]=d.get(p,F(0))+sign*w*k
 return {p:v for p,v in d.items() if v}
def plus(a,b):
 d=a.copy()
 for p,v in b.items():d[p]=d.get(p,F(0))+v
 return {p:v for p,v in d.items() if v}
def times(w,a):return {p:w*v for p,v in a.items() if w*v}
def kl(d,q=None):
 q=d['Q'] if q is None else q
 return logs((z,z/q[s]) for s,z in d['P'].items() if z)
def ent(d):return logs((z,1/d['c'][s]**2) for s,z in d['P'].items() if s and z)
def bern(s,t):return logs([(s,s/t),(1-s,(1-s)/(1-t))])

laws=[(F(1,2),F(1,2)),(F(1,3),F(2,5)),(F(1,8),F(3,4)),(F(1),F(1,3))]
sels=[(F(1,2),),(F(1,4),),(F(1,2),F(1,4)),(F(1,4),F(1,4))]
cases=[(table(2,k),p,q) for k,p,q in product(range(16),laws,sels)]
cases +=[(table(3,k),(F(1,3),F(1,2),F(3,4)),(F(1,4),)) for k in range(256)]
ck(len(cases)==512)
if pilot:cases=[cases[17*k] for k in range(16)]
nonconstant=0; multi=0;worst=F(0);witness=None
for tab,p,qs in cases:
 n=len(p);m=len(qs);eps=F(1);ks=[]
 for q in qs:
  eps*=q;k=0;v=q
  while v<1:v*=2;k+=1
  ck(v==1);ks.append(k)
 g=data(tab,p);a=(1-g['c'][0])/2
 ft=[tab[x&((1<<n)-1)] if x>>n==(1<<m)-1 else 1 for x in range(1<<(n+m))]
 d=data(ft,p+qs)
 ot=[-1 if x&1==0 and x>>1==(1<<m)-1 else 1 for x in range(1<<(m+1))]
 o=data(ot,(1-a,)+qs)
 ck(d['D']==eps*g['D']+o['D'])
 ck(d['V']==4*a*eps*(1-a*eps))
 ck(d['I']==eps*g['I']+4*a*eps*sum(1-q for q in qs))
 ck(o['J']<=3*o['D'])
 if o['D'] and o['J']/o['D']>worst:
  worst=o['J']/o['D'];witness={'mean_event':str(a),'selectors':list(map(str,qs))}
 ck(d['J']==eps*g['J']+o['J'])
 if not g['V']:
  ck(g['J']==g['D']==0)
  continue
 nonconstant+=1;multi+=m>1
 ja=0;v=a
 while v<=F(1,2):v*=2;ja+=1
 b=F(1,4**ja);V=g['V'];K=sum(ks)
 Dsel=sum(q*k+1-q for q,k in zip(qs,ks))
 gate=eps*(4*a*Dsel+4*a*a*(ja-1)*(1-eps)-4*a*a*eps*K)
 ck(o['J']==gate)
 ck(d['D']==eps*g['D']+eps*(4*a*sum(1-q for q in qs)-4*a*a*(1-eps)))
 ck(d['Z']==eps*g['Z']+4*b*eps*(1-eps))
 ck(o['Z']==eps*V+4*b*eps*(1-eps))
 tree={s:F(0) for s in d['P']}
 for s,pp in d['P'].items():
  T=s&((1<<n)-1);U=s>>n;A=(U<<1)|bool(T)
  predicted=o['P'].get(A,F(0));q=o['Q'].get(A,F(0))
  if T:predicted*=g['P'].get(T,F(0))/V;q*=g['Q'].get(T,F(0))/V
  ck(predicted==pp);tree[s]=q
  if not pp:continue
  ratio=o['P'][A]/o['Q'][A]
  if T:ratio*=g['P'][T]/g['Q'][T]
  ck(ratio==pp/q)
  if T:
   shift=sum(1 if U>>i&1 else k for i,k in enumerate(ks))
   ck(d['j'][s]==g['j'][T]+shift)
  elif U:
   shift=sum(1 if U>>i&1 else k for i,k in enumerate(ks))-1
   ck(d['j'][s]==ja+shift)
 ck(sum(tree.values())==1)
 ck(kl(d,tree)==plus(kl(o),times(eps,kl(g))))
 w=d['V'];s=4*a*a*eps*(1-eps)/w;t=4*b*eps*(1-eps)/d['Z']
 ck(kl(d)==plus(times(eps,kl(g)),times(w,bern(s,t))))
 eg=ent(g);erhs=plus(times(eps,eg),logs([(eps*(4*a*Dsel-4*a*a*(1-eps)-4*a*a*eps*K),F(4)),(4*a*a*eps*(1-eps),1/(a*a))]))
 ck(ent(d)==erhs)
 # Exact signed complete-reference conversion. Empty/bias terms are identical.
 conv=logs([(w,d['Z']/o['Z']),(-eps*V,g['Z']/V)])
 ck(plus(kl(d),times(-1,kl(d,tree)))==conv)
 ck(0<=g['Z']-V)
 if m==1:
  B=V+4*a*a*ja;k=ks[0]
  ck(V<=B<=2*V)
  ck(o['J']==qs[0]*(1-qs[0])*B+qs[0]**2*k*V)
  ck(abs(d['J']/eps-g['J']-B)<=eps*(k+2)*V)

# Mandatory adversarial physical controls (outside the frozen enumeration).
# Reusing the SAME selector twice: X^2=X, not an independent product.
p=F(1,3);ck(p!=p*p)
actual=data([1,1,-1,1],(F(1,2),p))
fake=data([1,1,1,1,1,1,-1,1],(F(1,2),p,p))
ck(actual['c'][0]==1-p);ck(fake['c'][0]==1-p*p);ck(actual['P'][0]!=fake['P'][0])
# Spectral absence differs from physical X=0: fair AND spectrum conditional
# on X absent has two equal atoms, while physical zero restriction is constant.
and2=data([-1,-1,-1,1],(F(1,2),F(1,2)))
ck(and2['P'][0]/(and2['P'][0]+and2['P'][2])==F(1,2))
ck(data([-1,-1],(F(1,2),))['P'][0]==1)
# Deterministic selector contractions: epsilon=0 constant; epsilon=1 seed.
g=data([-1,1,1,1],(F(1,3),F(2,5)))
for q in [F(0),F(1)]:
 root=data([1,1,1,1,-1,1,1,1],(F(1,3),F(2,5),q))
 ck(root['D']==q*g['D']);ck(root['J']==q*g['J'])

elapsed=time.perf_counter()-start
result={'status':'PASS','pilot':pilot,'cases':len(cases),'nonconstant_seed_cases':nonconstant,'multiselector_nonconstant_cases':multi,'assertions':checks,'runtime_seconds':elapsed,'outer_max_J_over_Delta_in_ln4_units':str(worst),'sharp_witness':witness,'controls':['repeated physical selector','spectral absence versus physical restriction','deterministic zero selector','deterministic one selector'],'arithmetic':'Fraction Mobius polynomial plus independently centered moments; exact canonical prime-log dictionaries','no_universal_seed_bound':True}
(run/'out'/('PILOT.json' if pilot else 'CHECKS.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps(result));assert elapsed<55
