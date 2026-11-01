"""Exact rational-polynomial certificates; no search, 3 fixed identities, <10 MB, 60 s cap."""
from fractions import Fraction as F
from pathlib import Path
import json
class P:
 def __init__(self,v=0):self.c=v if isinstance(v,dict) else ({():F(v)} if v else {})
 def __add__(self,o):
  o=o if isinstance(o,P) else P(o);c=self.c.copy()
  for m,a in o.c.items():c[m]=c.get(m,F(0))+a
  return P({m:a for m,a in c.items() if a})
 __radd__=__add__
 def __neg__(self):return P({m:-a for m,a in self.c.items()})
 def __sub__(self,o):return self+-P(o) if not isinstance(o,P) else self+-o
 def __rsub__(self,o):return P(o)+-self
 def __mul__(self,o):
  o=o if isinstance(o,P) else P(o);c={}
  for m,a in self.c.items():
   for n,b in o.c.items():
    mn=tuple(sorted(m+n));c[mn]=c.get(mn,F(0))+a*b
  return P({m:a for m,a in c.items() if a})
 __rmul__=__mul__
 def __truediv__(self,k):return self*F(1,k)
def V(name):return P({(name,):F(1)})
r,t,Qw,Qh,J,Iw,Pw,Ph,e,q,d=map(V,['r','t','Qw','Qh','J','Iw','Pw','Ph','e','q','d'])
def phi(r,t,Qw,Qh,J,Iw,Pw,Ph):return r*Qw+t*Qh+(J*Pw+Iw*Ph-Pw*Ph)/2
parent=phi(r,t,Qw,Qh,J,Iw,Pw,Ph)
# Affine averages under one w query. The h-side factor in each product stays fixed.
child=phi(r,t,Qw-e*q,Qh,J,Iw-d,Pw-e*d,Ph)
rhs=e*(r*q+J*d/2)+(1-e)*Ph*d/2
cert1=(parent-child-rhs).c
r0,r1,J0,J1,Q,mass,d=map(V,['r0','r1','J0','J1','Q','P','d'])
r=(r0+r1)/2;J=(J0+J1)/2+d
cert2=(((r0*Q+J0*mass/2)+(r1*Q+J1*mass/2))/2-(r*Q+J*mass/2-d*mass/2)).c
# Union price equals full mixed price minus the complement/complement rebate.
A,B,X,Y=map(V,['A','B','X','Y'])
cert3=(A*Y+B*X-X*Y-(A*B-(A-X)*(B-Y))).c
assert not cert1 and not cert2 and not cert3
out={'status':'PASS','arithmetic':'rational polynomial coefficient normalization','certificates':{'potential_one_step':cert1,'frozen_first_core_mask':cert2,'union_overlap_rebate':cert3},'scope':'Universal polynomial identities only; does not formalize logarithm inequalities or Boolean hypotheses.'}
run=Path(__file__).resolve().parents[1]
(run/'out/POLYNOMIAL_CERTIFICATES.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print('PASS: three universal polynomial identities have zero coefficients exactly')
