"""Rational arithmetic checks of identities, independent of the floating sampler."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json,os
assert os.getpriority(os.PRIO_PROCESS,0)>=10

def d(n): return F(comb(2*n,n),4**n)
def h(n): return 2*n*d(n) if n>0 else F(0)
def neg(m,K): return d(m-1)*F(K-1,2*m*(m+K-1))
cases=0
for p in range(1,17):
 for K in range(2,10):
  assert h(p+K-1)/h(K)+sum(neg(m,K)*h(p-m) for m in range(1,p))==h(p)
  assert d(p+K-1)/h(K)+sum(neg(m,K)*d(p-m) for m in range(1,p+1))==d(p)
  cases+=1
r={2:F(1,3),4:F(2,3)}
mu={k:v/k for k,v in r.items()}
mu0=1-sum(mu.values());Z=1/mu0
q={k:v/(Z**(k-1)*comb(2*k-1,k-1)) for k,v in mu.items()}
f=sum(q[k]*comb(2*k-1,k-1)*Z**(k-1) for k in q)
fp=sum(q[k]*comb(2*k-1,k-1)*(k-1)*Z**(k-2) for k in q)
assert f==1-1/Z and Z*Z*fp==1
out=dict(exact_pure_component_cases=cases,two_harmonic_identities_per_case=True,
 criticality_exact=True,Z=str(Z),q={str(k):str(v) for k,v in q.items()})
Path('data/exact_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(out)
