from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,sys
import exact_utils as e
R=Path(__file__).resolve().parents[1];start=time.monotonic();count=0
pilot='--pilot' in sys.argv
def ck(b):
 global count
 count+=1
 assert b,count
 if count%512==0 and time.monotonic()-start>55:raise RuntimeError('frozen 55 second cap')
@lru_cache(None)
def lr(x):
 x=F(x);assert x>0
 return e.plus({p:F(v) for p,v in e.factor(x.numerator).items()},{p:F(-v) for p,v in e.factor(x.denominator).items()})
def kl(P,Q):
 return e.plus(*(e.scale(p,lr(p/Q[z])) for z,p in P.items() if p))
def hb(p):
 return e.plus(e.scale(-p,lr(p)) if p else {},e.scale(-(1-p),lr(1-p)) if p!=1 else {})
def nonneg(x):return e.nonneg(x)
roots=blocks=events=budgets=critical=bad_reserve=0
for n in range(4):
 for tab in range(1<<(1<<n)):
  if pilot and n==3 and tab%17:continue
  f=e.table(n,tab);s=e.stats(f);roots+=1
  for mask in range(1,(1<<n)-1):
   A=[i for i in range(n) if mask>>i&1];B=[i for i in range(n) if not mask>>i&1];r=len(A);b=e.block(f,A);blocks+=1
   def pack(z,ii):return sum(((z>>i)&1)<<j for j,i in enumerate(ii))
   P={(pack(z,A),pack(z,B)):F(v*v,s['N']**2) for z,v in enumerate(s['a']) if v}
   PB={}
   for (a,z),p in P.items():PB[z]=PB.get(z,F(0))+p
   G=e.sub(e.const(3*b['IA']),b['J']);ck(nonneg(G))
   delta=e.sub(e.plus(*(hb(s['p'][i]) for i in A)),b['B']);ck(nonneg(delta))
   for C in [2,3,4,8,16]:
    theta=F(1)/(1+F(2)**(C-3));qpat={a:theta**a.bit_count()*(1-theta)**(r-a.bit_count()) for a in range(1<<r)}
    Q={(a,z):q*PB[z] for a,q in qpat.items() for z in PB}
    W=kl(P,Q);cap=e.scale(r,lr(1+F(2)**(3-C)))
    D=e.sub(s['H'],e.const(C*s['I']));S=e.sub(e.const(C*b['avm']),b['avh'])
    ck(e.plus(D,S,e.const(C*b['rho']),W,G)==cap);budgets+=1
    ck(W==e.plus(delta,*(kl({0:1-s['p'][i],1:s['p'][i]},{0:1-theta,1:theta}) for i in A)))
    ck(nonneg(W));ck(nonneg(e.sub(cap,e.plus(D,S,e.const(C*b['rho'])))))
    if nonneg(S) and e.positive(D):
     critical+=1;ck(e.positive(e.sub(cap,W)));ck(e.positive(e.sub(cap,e.const(C*b['rho']))))
    if not nonneg(S):bad_reserve+=1
    if C!=4:continue
    for emask in range(1,(1<<(1<<r))-1):
     E={a for a in range(1<<r) if emask>>a&1};v=sum((p for (a,z),p in P.items() if a in E),F(0));q=sum((p for a,p in qpat.items() if a in E),F(0))
     d=kl({0:1-v,1:v},{0:1-q,1:q});parts=[d]
     for active,reach,qreach in [(True,v,q),(False,1-v,1-q)]:
      if not reach:continue
      PE={(a,z):p/reach for (a,z),p in P.items() if (a in E)==active}
      QE={(a,z):p/qreach for (a,z),p in Q.items() if (a in E)==active}
      Wi=kl(PE,QE);parts.append(e.scale(reach,Wi));ck(nonneg(Wi))
      # Exterior-reference correction, checked independently of identity (2).
      PBE={}
      for (a,z),p in PE.items():PBE[z]=PBE.get(z,F(0))+p
      altered={(a,z):qpat[a]/qreach*PBE[z] for a in qpat if (a in E)==active for z in PBE}
      ck(Wi==e.plus(kl(PE,altered),kl(PBE,PB)))
     ck(W==e.plus(*parts));events+=1
out={'status':'PASS','roots':roots,'proper_blocks':blocks,'budget_cases':budgets,'event_cases':events,'positive_D_nonnegative_S_cases':critical,'negative_S_cases':bad_reserve,'assertions':count,'helper_assertions':e.COUNT,'seconds':time.monotonic()-start,'pilot':pilot}
(R/'out'/('PILOT.json' if pilot else 'EXACT_CHECK.json')).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
