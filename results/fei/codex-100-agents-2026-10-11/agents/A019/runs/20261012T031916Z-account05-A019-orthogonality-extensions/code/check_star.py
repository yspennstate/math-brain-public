import json,time,hashlib,math,sys
from fractions import Fraction as Q
from pathlib import Path
from collections import defaultdict
from functools import lru_cache
R=Path(__file__).resolve().parents[1]
pilot='--pilot' in sys.argv
spec={'helper_version':'A019-star-v3-cached-signs','family':'F(x,z1,z2,y)=g(y+v1 1{x=s1}A1(z1)+v2 1{x=s2}A2(z2))','domain':'All 16 two-bit cores (pilot masks0,1); point modules sizes (1,1),(1,2),(2,2), all 16 ordered vectors, orientations (0,0),(0,1); all 16 ordered one-bit Boolean activation pairs with same cores/vectors/orientations; majority n=1,3,5, two block sizes, three vector pairs, both orientations','case_count':1252 if pilot else 9764,'symmetry':'fix s1=0 by shared-bit translation; include both s2; no core or vector quotient','arithmetic':'integer Walsh, Fraction, exact prime-log entropy identities and rational logarithm intervals; memoized identical exact signs','memory_estimate_MB':80,'maximum_runtime_seconds':60 if pilot else 300,'no_automatic_escalation':True}
(R/('out/PILOT_SPEC.json' if pilot else 'out/FROZEN_SPEC.json')).write_text(json.dumps(spec,indent=2))
t0=time.monotonic(); checks=0; cases=0
def ck(x):
 global checks
 checks+=1
 assert x
def fw(a):
 a=a[:];h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for i in range(j,j+h):a[i],a[i+h]=a[i]+a[i+h],a[i]-a[i+h]
  h*=2
 return [Q(x,len(a)) for x in a]
@lru_cache(None)
def fac(n):
 d={};p=2
 while p*p<=n:
  while n%p==0:d[p]=d.get(p,0)+1;n//=p
  p+=1
 if n>1:d[n]=d.get(n,0)+1
 return d
@lru_cache(None)
def ent(ps):
 d=defaultdict(Q)
 for x in ps:
  if x:
   for p,e in fac(x.denominator).items():d[p]+=x*e
   for p,e in fac(x.numerator).items():d[p]-=x*e
 return {p:v for p,v in d.items() if v}
def add(terms):
 d=defaultdict(Q)
 for w,e in terms:
  for p,v in e.items():d[p]+=w*v
 return {p:v for p,v in d.items() if v}
def ln1(x):
 z=(x-1)/(x+1);s=sum((2*z**(2*i+1)/Q(2*i+1) for i in range(48)),Q(0));e=2*z**97/(97*(1-z*z))
 return s,s+e
L2,U2=ln1(Q(2))
@lru_cache(None)
def lg(p):
 k=p.bit_length()-1;l,u=ln1(Q(p,2**k));return k+l/U2,k+u/L2
def interval(e):
 lo=hi=Q(0)
 for p,w in e.items():
  l,u=lg(p)
  lo+=w*(l if w>=0 else u);hi+=w*(u if w>=0 else l)
 return lo,hi
def nonnegative(e):
 return cached_sign(tuple(sorted(e.items())))
@lru_cache(None)
def cached_sign(items):
 if not items:return True
 return interval(dict(items))[0]>=0
def phi(a,b):
 if not a+b:return {}
 return add([(Q(1),ent((a,b))),(-Q(1),ent((a+b,)))])
def spectrum(a):return tuple(x*x for x in fw(a))
def row_phase(h1,h2,s2,bits):
 out=[]
 for z2 in range(len(h2)):
  for z1 in range(len(h1)):
   for x in (0,1):out.append((h1[z1] if bits[0] and x==0 else 1)*(h2[z2] if bits[1] and x==s2 else 1))
 return out
def test(g,act,ks,vs,s2):
 global cases
 cases+=1;n=(len(g)).bit_length()-1;a=1+sum(ks);N=2**a
 if time.monotonic()-t0>spec['maximum_runtime_seconds']:raise TimeoutError('frozen deadline exceeded')
 c=fw(g);p=tuple(x*x for x in c);h=[[1-2*x for x in aa] for aa in act]
 hp=[spectrum(u) for u in h];H=[ent(u) for u in hp];means=[sum(u,Q(0))/len(u) for u in h]
 private=[sum(Q(t.bit_count())*prob for t,prob in enumerate(pp)) for pp in hp]
 rho=[sum(p[T] for T in range(len(p)) if (T&v).bit_count()%2) for v in vs]
 table=[]
 for y in range(len(g)):
  for w in range(N):
   x=w&1;z1=(w>>1)&(len(act[0])-1);z2=w>>(1+ks[0]);v=0
   if x==0 and act[0][z1]:v^=vs[0]
   if x==s2 and act[1][z2]:v^=vs[1]
   table.append(g[y^v])
 ff=fw(table);pp=tuple(u*u for u in ff)
 prediction=[(Q(1),ent(p))];Bpred=[];Bxpred=[];Ixp=Q(0)
 for T in range(len(p)):
  bits=tuple((T&v).bit_count()%2 for v in vs)
  phase=row_phase(h[0],h[1],s2,bits);sp=spectrum(phase)
  rowH=ent(sp);prediction.append((p[T],rowH));Bpred.append((p[T],rowH))
  alpha=Q(1);beta=Q(1)
  for j in range(2):
   if bits[j]:
    if (0,s2)[j]==0:alpha*=means[j]
    else:beta*=means[j]
  aa=(alpha+beta)**2/4;bb=(alpha-beta)**2/4
  bxrow=add([(Q(1),phi(aa,bb)),(1-(alpha*alpha+beta*beta)/2,{2:Q(1)})])
  Bxpred.append((p[T],bxrow));dt=(1-alpha*beta)/2;Ixp+=p[T]*dt
  ck(nonnegative(add([(3*dt,{2:Q(1)}),(-Q(1),bxrow)])))
  # Exact entropy correction at the only colliding private frequency (empty).
  kappa=add([(Q(1),ent((aa,bb))),(Q(-1,2),ent((alpha*alpha,beta*beta))),(2-alpha*alpha-beta*beta,{2:Q(1)})])
  expected=add([(Q(bits[0],2),H[0]),(Q(bits[1],2),H[1]),(Q(1),kappa)])
  ck(rowH==expected)
  ck(sum(sp)==1)
  for A in range(N):ck(pp[(T<<a)+A]==p[T]*sp[A])
 ck(ent(pp)==add(prediction));ck(sum(pp)==1)
 Ix=sum(pp[z] for z in range(len(pp)) if z&1);ck(Ix==Ixp)
 ck(Ix==Q(sum(table[z]!=table[z^1] for z in range(len(table))),len(table)))
 Bx=add([(Q(1),phi(pp[z],pp[z+1])) for z in range(0,len(pp),2)])
 ck(Bx==add(Bxpred))
 for i in range(a):
  edge=Q(sum(table[z]!=table[z^(1<<i)] for z in range(len(table))),len(table))
  ck(edge==sum(pp[z] for z in range(len(pp)) if (z>>i)&1))
 ck(sum(Q((z>>a).bit_count())*pp[z] for z in range(len(pp)))==sum(Q(z.bit_count())*p[z] for z in range(len(p))))
 ck(sum(Q((z&(N-1)).bit_count())*pp[z] for z in range(len(pp)))==Ix+sum(rho[j]*private[j]/2 for j in range(2)))
 if all(sum(aa)==1 for aa in act):
  Isel=Ix+sum(rho[j]*private[j]/2 for j in range(2))
  ck(nonnegative(add([(5*Isel,{2:Q(1)}),(-Q(1),add(Bpred))])))
for mask in range(2 if pilot else 16):
 g=[1-2*((mask>>y)&1) for y in range(4)]
 for ks in ((1,1),(1,2),(2,2)):
  act=[[int(z==0) for z in range(2**k)] for k in ks]
  for s in (0,1):
   for v in range(4):
    for u in range(4):test(g,act,ks,(v,u),s)
 for b in range(4):
  for c in range(4):
   act=[[(b>>z)&1 for z in range(2)],[(c>>z)&1 for z in range(2)]]
   for s in (0,1):
    for v in range(4):
     for u in range(4):test(g,act,(1,1),(v,u),s)
 (R/'out/LIVE_CHECKPOINT.json').write_text(json.dumps({'status':'PARTIAL_EXACT_CHECKS','core_mask_completed':mask,'cases':cases,'assertions':checks,'runtime_seconds':time.monotonic()-t0}))
for n in (1,3,5):
 g=[1 if 2*y.bit_count()<n else -1 for y in range(2**n)]
 for ks in ((1,1),(2,2)):
  act=[[int(z==0) for z in range(2**k)] for k in ks]
  for vs in ((1,1),(1,2**(n-1)),(1,2**n-1)):
   for s in (0,1):test(g,act,ks,vs,s)
 for t in range(n+1):
  v=2**t-1
  direct=Q(sum(g[y]!=g[y^v] for y in range(2**n)),2**n)
  formula=Q(sum(math.comb(t,i)*math.comb(n-t,j) for i in range(t+1) for j in range(n-t+1) if abs(t-2*i)>abs(n-t-2*j)),2**n)
  ck(direct==formula)
# All-k singleton point-module bound: B/I <= 2 + 2^-k(4k-8+2/ln2) <=3.
ck(L2>Q(1,2))
for k in range(2,101):ck(k-1<=2**(k-2));ck(2+Q(1,2**k)*(4*k-8+2/L2)<3)
out={'status':'PASS','cases':cases,'assertions':checks,'runtime_seconds':time.monotonic()-t0,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'shared_bit_erasure_bound':'B_x<=3 Inf_x; rational certificates all cases','star_collision_bound':'B_W<=5 I_W for point private modules; checked finite cases, analytic proof supplies all dimensions'}
(R/('out/PILOT.json' if pilot else 'out/CHECK.json')).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
