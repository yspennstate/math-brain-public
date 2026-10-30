from pathlib import Path
from fractions import Fraction as F
from math import comb
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(x):
 global checks
 checks+=1
 assert x,checks
def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
for n in range(2,33,2):
 a=[0]+[comb(n,l)+(2**n if l==n else 0) for l in range(1,n+1)]
 b=[i*v for i,v in enumerate(a)];d=[i*i*v for i,v in enumerate(a)]
 lhs=[x-y for x,y in zip(mul(d,a),mul(b,b))];rhs=[0]*(2*n+1)
 for i in range(n+1):
  for j in range(i+1,n+1):rhs[i+j]+=a[i]*a[j]*(i-j)**2
 ck(lhs==rhs);ck(all(x>=0 for x in rhs));ck(any(x>0 for x in rhs))
projection_cases=0
for n in (3,4,5,6):
 M=2**n;p0=F(1,M);c=F(M-1,2*M-1)
 q=[p0]+[c/M]*(M-2)+[c*(M+1)/M]
 ck(sum(q)==1)
 for x in (F(1,3),F(1,2),F(2,3)):
  z=sum(q[s]*x**s.bit_count() for s in range(1,M))
  u=[p0]+[(1-p0)*q[s]*x**s.bit_count()/z for s in range(1,M)]
  p=list(u);e=min(u[1],u[3],u[7])/4
  p[1]+=e;p[3]-=2*e;p[7]+=e
  ck(sum(p)==sum(u)==1);ck(p!=u);ck(min(p)>0);ck(p[0]==u[0]);ck(sum(F(s.bit_count())*(p[s]-u[s]) for s in range(M))==0)
  # Exact critical identity: one nontrivial three-cell perturbation preserves E log(u/q).
  ratio=[u[s]/q[s] for s in (1,3,7)]
  ck(ratio[0]*ratio[2]==ratio[1]**2)
  ck(all(p[s]==u[s] for s in range(M) if s not in (1,3,7)))
  # Independent atomwise count at rational tilts in the root's proved regime.
  if n>=4:
   ck(x>F(1,M+1));ratios=[M*v for v in u];rmin=min(ratios)
   zeros=[s for s,v in enumerate(ratios) if v==rmin]
   ck(len(zeros)==n);ck(all(s.bit_count()==n-1 for s in zeros))
   residual=[u[s]-rmin/M for s in range(M)]
   ck(min(residual)>=0);ck(sum(v>0 for v in residual)==M-n)
  projection_cases+=1
result={'status':'PASS','assertions':checks,'projection_cases':projection_cases,'variance_polynomials':16,'seconds':time.perf_counter()-start,'meaning':'Exact moment-cancellation ratio products, coefficientwise variance and atomwise representation counts. Rational tilts are audit fixtures, not claims that true root is rational.'}
(R/'out/AUDIT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
