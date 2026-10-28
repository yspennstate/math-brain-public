"""Exact affine-reset tree ledger; no floats enter a mathematical decision."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import itertools,json,time,sys
R=Path(__file__).resolve().parents[1];start=time.monotonic();pilot='--pilot' in sys.argv
cap_seconds=55 if pilot else 180;checks=0
def ok(x):
 global checks
 if not x: raise AssertionError('check '+str(checks))
 checks+=1
 if time.monotonic()-start>cap_seconds:raise TimeoutError('frozen wall-time cap')
def add(*terms):
 d={}
 for t in terms:
  for p,q in t:d[p]=d.get(p,F(0))+q
 return tuple(sorted((p,q) for p,q in d.items() if q))
def mul(t,q):return tuple((p,v*q) for p,v in t if v*q)
def rat(q):return () if not q else ((2,F(q)),)
@lru_cache(None)
def logint(n):
 d=[];p=2
 while p*p<=n:
  a=0
  while n%p==0:n//=p;a+=1
  if a:d.append((p,F(a)))
  p+=1
 if n>1:d.append((n,F(1)))
 return tuple(d)
def logq(q):return add(logint(q.numerator),mul(logint(q.denominator),-1))
@lru_cache(None)
def nonneg(t):
 lcm=1
 import math
 for p,q in t:lcm=math.lcm(lcm,q.denominator)
 pos=neg=1
 for p,q in t:
  z=int(q*lcm)
  if z>=0:pos*=p**z
  else:neg*=p**(-z)
 return pos>=neg
def entropy(ps):return add(*(mul(logq(p),-p) for p in ps if p))
def rank(vs):
 bs={}
 for v in vs:
  while v:
   j=v.bit_length()-1
   if j in bs:v^=bs[j]
   else:bs[j]=v;break
 return len(bs)
@lru_cache(None)
def info(f):
 n=(len(f)-1).bit_length();N=len(f)
 w=tuple(sum(f[x]*(-1)**((x&s).bit_count()%2) for x in range(N)) for s in range(N))
 p=tuple(F(v*v,N*N) for v in w);ok(sum(p)==1)
 costs=tuple(F(sum(f[x]!=f[x^v] for x in range(N)),N) for v in range(N))
 m=tuple(min(z,1-z) for z in costs);basis=[]
 for v in sorted(range(1,N),key=lambda v:(m[v],v)):
  if rank(basis+[v])>len(basis):basis.append(v)
 a=sum((m[v] for v in basis),F(0));physical=sum((costs[1<<i] for i in range(n)),F(0))
 # An independent exhaustive basis minimum guards the greedy calculation.
 brute=min((sum((m[v] for v in B),F(0)) for B in itertools.combinations(range(1,N),n) if rank(B)==n),default=F(0))
 ok(a==brute)
 I_fourier=sum((p[s]*s.bit_count() for s in range(N)),F(0));ok(physical==I_fourier)
 flip=sum(1<<i for i,v in enumerate(basis) if costs[v]>F(1,2))
 g=[]
 for y in range(N):
  x=0
  for i,v in enumerate(basis):
   if y>>i&1:x^=v
  g.append(f[x]*(-1)**((y&flip).bit_count()%2))
 return entropy(p),a,physical,p,tuple(g)
@lru_cache(None)
def canonical(f):
 g=info(f)[4];H,a,I,p,_=info(g)
 ok(a==I);ok(H==info(f)[0]);ok(a==info(f)[1]);return g
def restrict(f,i,b):
 n=(len(f)-1).bit_length()
 return tuple(f[(y&((1<<i)-1))|((y>>i)<<(i+1))|(b<<i)] for y in range(1<<(n-1)))
def deficit(f,K):H,a,*_=info(f);return add(H,rat(-K*a))
@lru_cache(None)
def node(f,i,K):
 H,a,I,p,_=info(f);n=(len(f)-1).bit_length();ok(a==I)
 raw=tuple(restrict(f,i,b) for b in (0,1));children=tuple(canonical(g) for g in raw)
 sigma=sum((p[s] for s in range(len(p)) if s>>i&1),F(0))
 outside=[F(0)]*(1<<(n-1));pairs=[[F(0),F(0)] for _ in outside]
 for s,mass in enumerate(p):
  t=(s&((1<<i)-1))|((s>>(i+1))<<i);outside[t]+=mass;pairs[t][s>>i&1]+=mass
 HC=add(H,mul(entropy(outside),-1))
 childH=mul(add(*(info(g)[0] for g in raw)),F(1,2))
 L=add(H,mul(childH,-1));J=add(L,mul(HC,-1));G=add(rat(3*sigma),mul(J,-1))
 Rchild=sum((info(g)[2]-info(g)[1] for g in raw),F(0))/2
 kappa=logq(1+F(2)**(3-K));W=add(kappa,rat((K-3)*sigma),mul(HC,-1))
 occ=()
 if sigma:
  occ=add(*(mul(logq(v/(sigma*outside[t])),v) for t,(u,v) in enumerate(pairs) if v))
 ok(nonneg(J));ok(nonneg(G));ok(nonneg(W));ok(nonneg(occ));ok(nonneg(add(W,mul(occ,-1))));ok(Rchild>=0)
 d=deficit(f,K);dc=mul(add(*(deficit(g,K) for g in children)),F(1,2))
 ok(add(d,mul(dc,-1),rat(K*Rchild),W,G)==kappa)
 return children,Rchild,W,G,sigma,occ
# profile = (expected queried bits, summed reset savings, summed W, summed G,
#            complete expected terminal deficit, occupation intensity, occupied divergence)
def mean(p,q):return ((p[0]+q[0])/2,(p[1]+q[1])/2,mul(add(p[2],q[2]),F(1,2)),mul(add(p[3],q[3]),F(1,2)),mul(add(p[4],q[4]),F(1,2)),(p[5]+q[5])/2,mul(add(p[6],q[6]),F(1,2)))
@lru_cache(None)
def profiles(f,K):
 n=(len(f)-1).bit_length();d=deficit(f,K);out=[(F(0),F(0),(),(),d,F(0),())]
 for i in range(n):
  children,Rc,W,G,v,occ=node(f,i,K)
  for p in profiles(children[0],K):
   for q in profiles(children[1],K):
    z=mean(p,q);out.append((z[0]+1,z[1]+Rc,add(z[2],W),add(z[3],G),z[4],z[5]+v,add(z[6],occ)))
 return tuple(out)
count=0;critical=0;negative=0;reset_guard=False;occ_guard=False
ns=range(3) if pilot else range(4)
Ks=(2,) if pilot else (2,4,8,16)
for n in ns:
 for mask in range(1<<(1<<n)):
  f=tuple(1-2*((mask>>x)&1) for x in range(1<<n));g=canonical(f)
  for K in Ks:
   d=deficit(g,K);kappa=logq(1+F(2)**(3-K))
   ps=profiles(g,K);ok(len(ps)==(1,2,9,244)[n])
   for q,Rc,W,G,dt,V,occ in ps:
    count+=1
    ok(add(d,mul(dt,-1),rat(K*Rc),W,G)==mul(kappa,q))
    # The stronger occupied ledger retains all of W-occ rather than renewing capacity.
    ok(add(occ,add(W,mul(occ,-1)),G,rat(K*Rc),mul(dt,-1),d)==mul(kappa,q))
    if q and nonneg(mul(dt,-1)):
     ok(nonneg(add(mul(kappa,q),mul(d,-1),mul(occ,-1))))
    if q and nonneg(dt) and dt:negative+=1
    if Rc:reset_guard=True
    if occ:occ_guard=True
   if n>=2 and nonneg(d) and d:
    children_ok=all(nonneg(mul(deficit(ch,K),-1)) for i in range(n) for ch in node(g,i,K)[0])
    if children_ok:
     critical+=1
     for i in range(n):
      ch,Rc,W,G,v,occ=node(g,i,K);S=mul(add(*(deficit(h,K) for h in ch)),F(-1,2))
      ok(nonneg(S));ok(nonneg(add(kappa,mul(d,-1),mul(W,-1),mul(G,-1),rat(-K*Rc),mul(S,-1))))
if not pilot:ok(reset_guard);ok(occ_guard);ok(critical>0);ok(negative>0)
result={'status':'PASS','mode':'pilot' if pilot else 'main','checks':checks,'root_policy_comparisons':count,'critical_root_K_cases':critical,'negative_expected_reserve_controls':negative,'nonzero_reset_guard':reset_guard,'nonzero_exterior_dependence_guard':occ_guard,'seconds':time.monotonic()-start,'arithmetic':'Fraction, integer Walsh, exact prime-log identities and integer-product signs','proof_scope':'finite validation only; analytic tree induction in PROOF.md'}
(R/('out/PILOT.json' if pilot else 'out/EXACT_TREE.json')).write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
