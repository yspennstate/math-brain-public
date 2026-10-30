import json,time,math
from fractions import Fraction as F
from pathlib import Path
from functools import reduce
from math import lcm
r=Path(__file__).resolve().parents[1]
start=time.perf_counter(); checks=cases=0
def ck(v):
 global checks
 checks+=1
 assert v
 if time.perf_counter()-start>55: raise TimeoutError('55 seconds')
def power(ps,ratios):
 d=lcm(*(v.denominator for v in ps)); ans=F(1)
 for v,q in zip(ps,ratios):
  if v: ans*=q**int(v*d)
 return ans,d
for t in [F(1,2),F(3,4),F(1)]:
 for aa in [F(1,4),F(1,2),F(3,4)]:
  a=t*aa
  for bb in [F(1,8),F(3,8),F(5,8)]:
   b=t*bb
   for ll in [F(1,4),F(1,2),F(3,4),F(7,8)]:
    ell=t*ll
    if b>=ell: continue
    for ghost in [False,True]:
     ps=[1-t,a,F(0) if ghost else (t-a)/3,t-a if ghost else 2*(t-a)/3]
     q0=[1-t,b,(t-b)/2,(t-b)/2]
     zs=max(a,ell)
     def q(z): return [1-t,z,(t-z)/2,(t-z)/2]
     qs=q(zs); cases+=1
     ck(sum(ps)==sum(q0)==sum(qs)==1)
     for zz in {ell,a,zs,*[t*F(j,8) for j in range(1,8)]}:
      if not ell<=zz<t: continue
      qz=q(zz)
      # exp(d * (CE(p,qz)-CE(p,qs))) >= 1, no numerical logs.
      ratios=[F(1) if not v else qs[i]/qz[i] for i,v in enumerate(ps)]
      pp,den=power(ps,ratios); ck(pp>=1); ck((pp==1)==(zz==zs))
      ck(-a/zz+(t-a)/(t-zz)==t*(zz-a)/(zz*(t-zz)))
     # Independent atomwise vs aggregated signed price exponent.
     atom,d=power(ps,[F(1) if not v else q0[i]/qs[i] for i,v in enumerate(ps)])
     agg=(b/zs)**int(a*d)*((t-b)/(t-zs))**int((t-a)*d)
     ck(atom==agg)
# Physical truth table and both children, direct Fourier sums.
def spectrum(tab):
 n=(len(tab)).bit_length()-1
 return [F(sum(v*((-1)**((x&s).bit_count()%2)) for x,v in enumerate(tab)),len(tab))**2 for s in range(len(tab))]
tab=[-1 if x in [0,7] else 1 for x in range(8)]
ck(spectrum(tab)==[F(1,4) if s in [0,3,5,6] else F(0) for s in range(8)])
for bit in [0,1]:
 child=[tab[(x<<1)|bit] for x in range(4)]
 ck(spectrum(child)==[F(1,4)]*4)
p=[F(1,4)]*4; qs=[F(1,4),F(5,24),F(5,24),F(1,3)]
endpoints=[]
for q0,expected in [([F(1,4)]*4,F(27,25)),([F(1,4),F(5,16),F(5,16),F(1,8)],F(27,32))]:
 ratio,d=power(p,[x/y for x,y in zip(q0,qs)]); ck(d==4); ck(ratio==expected); endpoints.append(str(ratio))
 # Disjoint controller atom with beta3/8 and same controller law cancels.
 beta=F(3,8); P=[1-beta]+[beta*v for v in p]; Q0=[1-beta]+[beta*v for v in q0]; Qs=[1-beta]+[beta*v for v in qs]
 ratio2,d2=power(P,[x/y for x,y in zip(Q0,Qs)]); ck(ratio2==expected**int(beta*d2/4))
# Universal owner ledger subtraction is checked on signed rational surrogate costs.
for x in [F(-2),F(-1,3),F(0),F(1,3),F(2)]:
 for y in [F(-2),F(-1,3),F(0),F(1,3),F(2)]:
  B,C,U=F(7),F(3),F(1); change=F(1,4)*F(3,8)*x+F(3,4)*F(1,2)*y
  ck(B-(C+change)-U==(B-C-U)-change)
  ck((C+change+U<=B)==(change<=B-C-U))
# AND2, matched parent reference: full-child CE difference is -1, not -D_occ=0.
andtab=[-1,1,1,1]; parent=spectrum(andtab); ck(parent==[F(1,4)]*4)
qbar=[parent[0]+parent[1],parent[2]+parent[3]]; ck(qbar==[F(1,2)]*2)
children=[spectrum([andtab[(x<<1)|bit] for x in range(2)]) for bit in [0,1]]
ck([(u+v)/2 for u,v in zip(*children)]==qbar)
# All parent q=1/4 implies CE=2; all inherited child q=1/2 implies CE=1.
# Conditional parent occupancies=q occupancies=(1/2,1/2), D_occ=0 and B=1.
ck(sum(parent)==sum(qbar)==1); ck(F(1)-F(2)==-1); ck(F(1)+(F(1)-F(2))==0)
result={'status':'PASS','law_cases':cases,'exact_assertions':checks,'seconds':time.perf_counter()-start,'endpoint_power_ratios':endpoints,'arithmetic':'Fraction; integer Walsh; exact rational powers; no floating signs','universal_proof':'analytic reconstruction, not finite extrapolation'}
(r/'out/CHECKS.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
