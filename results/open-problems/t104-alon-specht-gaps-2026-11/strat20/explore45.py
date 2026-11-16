import sympy as s
from transfer45 import construct,controls
from inherited19.inherited18.boundary44 import inspect
from inherited19.transfer35 import bernstein
from inherited19.inherited18.inherited17.lower_formula import x3
rr,M=construct('rank',1,6,2,s.Rational(22,15),s.Rational(3,10),3,s.Rational(1,100))
for i,A in enumerate(controls(rr,M)):
 n,bad=inspect(A);print('control',i,'bad',bad,flush=True)
k,t,d,z,v=s.symbols('k t d z v')
f=(4/k-s.Rational(4,7))*d+x3(k,(k-1-t)/2,s.Rational(31,20)-d)-x3(s.Integer(7),(7-t)/2,s.Rational(31,20)-d)
print('lower',s.factor(f))
for lo,hi in ((0,2),(2,4),(4,5)):
 for dd in (0,s.Rational(11,20)):
  p=s.cancel(k*k*(f-s.Rational(1,4))).subs({k:9+z,d:dd,t:lo+(hi-lo)*v}).expand()
  cs=bernstein(p,(v,),(2,))
  print(lo,hi,dd,[s.Poly(c,z).all_coeffs() for _,c in cs])
